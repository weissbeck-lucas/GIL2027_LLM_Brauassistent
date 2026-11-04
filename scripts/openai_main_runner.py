"""Validate and execute the eight frozen OpenAI main runs one at a time."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "prompts" / "Main_Run_Manifest_v1.2.json"
OUTPUT_DIR = ROOT / "outputs" / "main"
API_TIMEOUT_SECONDS = 1800
EXPECTED_MODEL = "gpt-5.6-sol"
EXPECTED_ENDPOINT = "https://api.openai.com/v1/responses"
EXPECTED_PARAMETERS = {
    "reasoning": {"effort": "max"},
    "text": {"verbosity": "low"},
    "max_output_tokens": 128000,
    "store": False,
}
EXPECTED_RUNS = (
    (1, "C01", "RUN-S01-P01-M02-R01", "O-S01-P01-M02-R01", "S01", "P01", "R01"),
    (2, "C01", "RUN-S01-P01-M02-R02", "O-S01-P01-M02-R02", "S01", "P01", "R02"),
    (3, "C02", "RUN-S01-P02-M02-R01", "O-S01-P02-M02-R01", "S01", "P02", "R01"),
    (4, "C02", "RUN-S01-P02-M02-R02", "O-S01-P02-M02-R02", "S01", "P02", "R02"),
    (5, "C03", "RUN-S02-P01-M02-R01", "O-S02-P01-M02-R01", "S02", "P01", "R01"),
    (6, "C03", "RUN-S02-P01-M02-R02", "O-S02-P01-M02-R02", "S02", "P01", "R02"),
    (7, "C04", "RUN-S02-P02-M02-R01", "O-S02-P02-M02-R01", "S02", "P02", "R01"),
    (8, "C04", "RUN-S02-P02-M02-R02", "O-S02-P02-M02-R02", "S02", "P02", "R02"),
)
PLACEHOLDER_PATTERN = re.compile(r"\{[A-Za-z_][A-Za-z0-9_]*\}")


class RunnerError(RuntimeError):
    """Raised for a controlled validation or execution failure."""


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    if not isinstance(manifest, dict):
        raise RunnerError("Manifest root must be a JSON object.")
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    expected_header = {
        "manifest_version": "v1.2",
        "freeze_protocol": "public_replication_package_v1.0",
        "endpoint": EXPECTED_ENDPOINT,
        "model": EXPECTED_MODEL,
        "expected_returned_model": EXPECTED_MODEL,
    }
    for field, expected in expected_header.items():
        if manifest.get(field) != expected:
            raise RunnerError(f"Unexpected manifest value for {field!r}.")
    if manifest.get("parameters") != EXPECTED_PARAMETERS:
        raise RunnerError("Manifest parameters differ from freeze v1.2.")

    runs = manifest.get("runs")
    if not isinstance(runs, list) or len(runs) != len(EXPECTED_RUNS):
        raise RunnerError("Manifest must contain exactly eight main runs.")

    for run, expected in zip(runs, EXPECTED_RUNS, strict=True):
        if not isinstance(run, dict):
            raise RunnerError("Every run must be a JSON object.")
        fields = (
            "sequence",
            "condition_id",
            "run_id",
            "output_id",
            "scenario_id",
            "prompt_id",
            "replicate_id",
        )
        actual = tuple(run.get(field) for field in fields)
        if actual != expected:
            raise RunnerError(
                f"Run definition at sequence {expected[0]} differs from freeze v1.2."
            )
        prompt = run.get("input")
        if not isinstance(prompt, str) or not prompt.strip():
            raise RunnerError(f"Missing prompt at sequence {expected[0]}.")
        if PLACEHOLDER_PATTERN.search(prompt):
            raise RunnerError(f"Open placeholder at sequence {expected[0]}.")
        if "sk-" in prompt:
            raise RunnerError(f"Possible API key fragment at sequence {expected[0]}.")

    if len({run["run_id"] for run in runs}) != 8:
        raise RunnerError("Run IDs must be unique.")
    if len({run["output_id"] for run in runs}) != 8:
        raise RunnerError("Output IDs must be unique.")
    return runs


def request_body(manifest: dict[str, Any], prompt: str, max_tokens: int | None = None) -> dict[str, Any]:
    parameters = dict(manifest["parameters"])
    if max_tokens is not None:
        parameters["max_output_tokens"] = max_tokens
    return {"model": manifest["model"], "input": prompt, **parameters}


def json_bytes(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")


def require_api_key() -> str:
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RunnerError(
            "OPENAI_API_KEY is not available. Use the PowerShell wrapper for secure input."
        )
    return api_key


def call_api(endpoint: str, api_key: str, body: dict[str, Any]) -> bytes:
    request = urllib.request.Request(
        endpoint,
        data=json_bytes(body),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=API_TIMEOUT_SECONDS) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace")
        raise RunnerError(f"API returned HTTP {exc.code}: {message}") from exc
    except urllib.error.URLError as exc:
        raise RunnerError(f"API connection failed: {exc.reason}") from exc


def parse_response(raw_response: bytes) -> dict[str, Any]:
    try:
        response = json.loads(raw_response)
    except json.JSONDecodeError as exc:
        raise RunnerError("API response is not valid JSON.") from exc
    if not isinstance(response, dict):
        raise RunnerError("API response root is not a JSON object.")
    return response


def validate_response(response: dict[str, Any]) -> None:
    if response.get("model") != EXPECTED_MODEL:
        raise RunnerError(
            f"Backend model changed: expected {EXPECTED_MODEL!r}, "
            f"received {response.get('model')!r}."
        )
    if response.get("status") != "completed":
        raise RunnerError(
            f"API response is not completed: status={response.get('status')!r}, "
            f"incomplete_details={response.get('incomplete_details')!r}."
        )


def extract_output_text(response: dict[str, Any]) -> str:
    texts: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if (
                isinstance(content, dict)
                and content.get("type") == "output_text"
                and isinstance(content.get("text"), str)
            ):
                texts.append(content["text"])
    text = "\n".join(texts)
    if not text:
        raise RunnerError("API response contains no output_text.")
    return text


def output_paths(run: dict[str, Any]) -> tuple[Path, Path, Path]:
    output_id = run["output_id"]
    return (
        OUTPUT_DIR / f"{output_id}_request.json",
        OUTPUT_DIR / f"{output_id}_response.json",
        OUTPUT_DIR / f"{output_id}.md",
    )


def output_state(run: dict[str, Any]) -> str:
    paths = output_paths(run)
    present = [path.exists() for path in paths]
    if all(present):
        try:
            with paths[1].open("r", encoding="utf-8") as handle:
                response = json.load(handle)
            validate_response(response)
            extract_output_text(response)
        except (OSError, json.JSONDecodeError, RunnerError) as exc:
            raise RunnerError(f"Invalid completed files for {run['output_id']}: {exc}") from exc
        return "completed"
    if present == [True, False, True]:
        # The public package intentionally omits raw API response JSON files.
        if not paths[2].read_text(encoding="utf-8").strip():
            raise RunnerError(f"Empty public output for {run['output_id']}.")
        return "completed"
    if any(present):
        names = ", ".join(path.name for path, exists in zip(paths, present) if exists)
        raise RunnerError(
            f"Partial files exist for {run['output_id']}: {names}. "
            "Do not retry silently; document and assign a new retry ID."
        )
    return "pending"


def next_run(runs: list[dict[str, Any]]) -> dict[str, Any] | None:
    found_pending = False
    candidate: dict[str, Any] | None = None
    for run in runs:
        state = output_state(run)
        if state == "pending" and not found_pending:
            found_pending = True
            candidate = run
        elif state == "completed" and found_pending:
            raise RunnerError("A later main run exists before an earlier pending run.")
    return candidate


def print_status(runs: list[dict[str, Any]]) -> None:
    completed = sum(output_state(run) == "completed" for run in runs)
    candidate = next_run(runs)
    print("MAIN_STATUS_OK")
    print(f"completed={completed}")
    print(f"pending={len(runs) - completed}")
    if candidate is None:
        print("next=none")
    else:
        print(f"next_sequence={candidate['sequence']}")
        print(f"next_output_id={candidate['output_id']}")
    print("api_called=false")


def print_dry_run(manifest: dict[str, Any], runs: list[dict[str, Any]]) -> None:
    print("DRY_RUN_OK")
    print(f"model={manifest['model']}")
    print(f"endpoint={manifest['endpoint']}")
    for run in runs:
        digest = hashlib.sha256(run["input"].encode("utf-8")).hexdigest()
        paths = ", ".join(str(path.relative_to(ROOT)) for path in output_paths(run))
        print(
            f"{run['sequence']}: {run['condition_id']} {run['run_id']} "
            f"prompt_sha256={digest} files=[{paths}]"
        )
    print("api_called=false")


def check_access(manifest: dict[str, Any]) -> None:
    api_key = require_api_key()
    body = request_body(
        manifest,
        "Gib ausschliesslich den Text API_OK aus.",
        max_tokens=1000,
    )
    response = parse_response(call_api(manifest["endpoint"], api_key, body))
    validate_response(response)
    summary = {
        "access_check": "completed",
        "response_id": response.get("id"),
        "requested_model": manifest["model"],
        "returned_model": response.get("model"),
        "status": response.get("status"),
        "usage": response.get("usage"),
        "output_text": extract_output_text(response),
        "files_written": False,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


def run_next(manifest: dict[str, Any], runs: list[dict[str, Any]]) -> None:
    run = next_run(runs)
    if run is None:
        print("MAIN_RUNS_COMPLETE")
        return

    api_key = require_api_key()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    request_path, response_path, text_path = output_paths(run)
    body = request_body(manifest, run["input"])
    request_bytes = json_bytes(body)
    raw_response = call_api(manifest["endpoint"], api_key, body)
    response = parse_response(raw_response)
    try:
        validate_response(response)
        output_text = extract_output_text(response)
    except RunnerError as exc:
        with request_path.open("xb") as handle:
            handle.write(request_bytes)
        with response_path.open("xb") as handle:
            handle.write(raw_response)
        raise RunnerError(
            f"{exc} Request and response saved for {run['output_id']}."
        ) from exc

    with request_path.open("xb") as handle:
        handle.write(request_bytes)
    with response_path.open("xb") as handle:
        handle.write(raw_response)
    with text_path.open("x", encoding="utf-8", newline="\n") as handle:
        handle.write(output_text)
        if not output_text.endswith("\n"):
            handle.write("\n")

    print(
        json.dumps(
            {
                "sequence": run["sequence"],
                "condition_id": run["condition_id"],
                "run_id": run["run_id"],
                "output_id": run["output_id"],
                "response_id": response.get("id"),
                "requested_model": manifest["model"],
                "returned_model": response.get("model"),
                "status": response.get("status"),
                "usage": response.get("usage") or {},
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=("dry-run", "status", "check-access", "run-next"),
    )
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = load_manifest(args.manifest.resolve())
    runs = validate_manifest(manifest)
    if args.mode == "dry-run":
        print_dry_run(manifest, runs)
    elif args.mode == "status":
        print_status(runs)
    elif args.mode == "check-access":
        check_access(manifest)
    else:
        run_next(manifest, runs)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RunnerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
