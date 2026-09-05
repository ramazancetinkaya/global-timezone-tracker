"""
Global Timezone & GMT Offset Tracker
Developed by Ramazan Çetinkaya (https://github.com/ramazancetinkaya)

Copyright (c) 2026 Ramazan Çetinkaya. All rights reserved.
Licensed under the MIT License.
"""

import datetime
import json
import os
import sys
from pathlib import Path
import pytz

DATA_FILE = Path("timezones.json")
README_FILE = Path("README.md")
STATUS_FILE = Path("last_run.json")


def update_last_run(status: str, error_message: str = None) -> None:
    """Records execution timestamp, status, and error details if any."""
    now = datetime.datetime.now(datetime.timezone.utc)
    payload = {
        "last_run_utc": now.isoformat(),
        "timestamp_epoch": int(now.timestamp()),
        "status": status,
        "error_message": error_message,
    }
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def get_current_offset_data(tz_name: str, now_utc: datetime.datetime) -> dict:
    """Calculates active GMT offset and Daylight Saving Time (DST) status for a zone."""
    tz = pytz.timezone(tz_name)
    localized_time = now_utc.astimezone(tz)

    offset = localized_time.utcoffset()
    total_seconds = int(offset.total_seconds()) if offset else 0

    abs_seconds = abs(total_seconds)
    hours = abs_seconds // 3600
    minutes = (abs_seconds % 3600) // 60
    sign = "+" if total_seconds >= 0 else "-"
    formatted_offset = f"UTC{sign}{hours:02d}:{minutes:02d}"

    dst_offset = localized_time.dst()
    is_dst_active = bool(dst_offset and dst_offset.total_seconds() != 0)

    return {
        "timezone": tz_name,
        "gmt_offset": formatted_offset,
        "offset_seconds": total_seconds,
        "is_dst": is_dst_active,
    }


def collect_world_timezones() -> list:
    """Iterates over ISO country codes and resolves current timezone information."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    dataset = []

    for code, country_name in pytz.country_names.items():
        zone_names = pytz.country_timezones.get(code, [])
        if not zone_names:
            continue

        resolved_zones = []
        for zone in zone_names:
            try:
                tz_data = get_current_offset_data(zone, now_utc)
                resolved_zones.append(tz_data)
            except Exception:
                continue

        if resolved_zones:
            dataset.append(
                {
                    "country_code": code,
                    "country_name": country_name,
                    "zones": resolved_zones,
                }
            )

    dataset.sort(key=lambda item: item["country_name"])
    return dataset


def generate_markdown(dataset: list, execution_time: str) -> str:
    """Builds a scannable, modern Markdown table."""
    total_countries = len(dataset)
    total_zones = sum(len(c["zones"]) for c in dataset)

    md = [
        "# Global Country Timezone & GMT Offsets",
        "",
        "> Automated weekly tracker capturing real-time UTC/GMT offsets and active Daylight Saving Time (DST) changes.",
        "",
        f"- **Last Updated:** `{execution_time} (UTC)`",
        f"- **Tracked Countries:** `{total_countries}`",
        f"- **Total Timezones:** `{total_zones}`",
        "- **Data Export:** [`timezones.json`](./timezones.json) | **Run Telemetry:** [`last_run.json`](./last_run.json)",
        "",
        "| Country | Alpha-2 | Timezone Identifier | Current Offset | DST Active |",
        "| :--- | :---: | :--- | :---: | :---: |",
    ]

    for country in dataset:
        c_name = country["country_name"]
        c_code = country["country_code"]
        for idx, z in enumerate(country["zones"]):
            dst_flag = "Yes" if z["is_dst"] else "No"
            country_display = c_name if idx == 0 else ""
            code_display = f"`{c_code}`" if idx == 0 else ""
            md.append(
                f"| {country_display} | {code_display} | `{z['timezone']}` | `{z['gmt_offset']}` | {dst_flag} |"
            )

    md.append("")
    return "\n".join(md)


def main():
    try:
        data = collect_world_timezones()

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        now_str = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        readme_content = generate_markdown(data, now_str)

        with open(README_FILE, "w", encoding="utf-8") as f:
            f.write(readme_content)

        update_last_run(status="success")
        print("Timezone sync completed successfully.")

    except Exception as exc:
        update_last_run(status="failed", error_message=str(exc))
        print(f"Error during execution: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
