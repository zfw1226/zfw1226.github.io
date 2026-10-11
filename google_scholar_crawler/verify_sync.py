"""Fail closed unless the citation files were fetched by the current workflow run."""
import argparse
import json
import os
from pathlib import Path


def verify_sync(data, badge, expected_run_id, expected_attempt="1"):
    if not expected_run_id or data.get("sync_run_id") != expected_run_id:
        raise ValueError("No successful Google Scholar fetch was published by this workflow run")
    if data.get("sync_run_attempt") != expected_attempt:
        raise ValueError("Google Scholar data belongs to an earlier execution of this workflow run")
    count = data.get("citedby")
    if type(count) is not int or count < 0:
        raise ValueError("Invalid Google Scholar citation count")
    if badge.get("message") != str(count):
        raise ValueError("Citation JSON and badge disagree")
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    data = json.loads((args.directory / "gs_data.json").read_text())
    badge = json.loads((args.directory / "gs_data_shieldsio.json").read_text())
    count = verify_sync(
        data, badge, os.environ["GITHUB_RUN_ID"], os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    )
    print(f"Verified this workflow's fresh Google Scholar data: {count} citations")


if __name__ == "__main__":
    main()
