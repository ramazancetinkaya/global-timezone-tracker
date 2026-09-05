import json
import os
import sys
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import pytz

README_FILE = "README.md"
JSON_OUTPUT_FILE = "timezones.json"
LAST_RUN_FILE = "last_run.json"

START_MARKER = "<!-- TIMEZONE_TABLE_START -->"
END_MARKER = "<!-- TIMEZONE_TABLE_END -->"


def record_run_status(status: str, error_msg: str = None, total_entries: int = 0) -> None:
    """Records the execution status and timestamp to last_run.json."""
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "epoch": int(datetime.now(timezone.utc).timestamp()),
        "status": status,
        "records_processed": total_entries,
        "error_message": error_msg
    }
    with open(LAST_RUN_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def format_gmt_offset(total_seconds: float) -> str:
    """Converts offset in seconds to standard GMT representation (e.g. GMT+03:00)."""
    sign = "+" if total_seconds >= 0 else "-"
    abs_seconds = int(abs(total_seconds))
    hours, remainder = divmod(abs_seconds, 3600)
    minutes = remainder // 60
    return f"GMT{sign}{hours:02d}:{minutes:02d}"


def fetch_country_timezones():
    """Extracts current GMT offsets and DST states for all countries."""
    now_utc = datetime.now(timezone.utc)
    results = []

    # Sort countries alphabetically by name
    sorted_country_items = sorted(
        pytz.country_names.items(), key=lambda x: x[1]
    )

    for country_code, country_name in sorted_country_items:
        tz_list = pytz.country_timezones.get(country_code, [])
        if not tz_list:
            continue

        zone_details = []
        for tz_name in tz_list:
            try:
                tz = ZoneInfo(tz_name)
                localized_time = now_utc.astimezone(tz)
                offset = localized_time.utcoffset()
                dst_offset = localized_time.dst()

                total_seconds = offset.total_seconds() if offset else 0
                is_dst = bool(dst_offset and dst_offset.total_seconds() != 0)

                zone_details.append({
                    "timezone": tz_name,
                    "gmt_offset": format_gmt_offset(total_seconds),
                    "raw_offset_seconds": int(total_seconds),
                    "is_dst": is_dst,
                    "abbreviation": localized_time.strftime("%Z"),
                    "current_local_time": localized_time.strftime("%Y-%m-%d %H:%M:%S")
                })
            except Exception as e:
                print(f"Warning: Failed to parse timezone {tz_name} ({country_name}): {e}")
                continue

        if zone_details:
            results.append({
                "country_name": country_name,
                "country_code": country_code,
                "zones": zone_details
            })

    return results


def update_readme(data) -> None:
    """Generates a clean Markdown table and replaces markers in README.md."""
    lines = [
        "| Country | ISO | Primary / Available Timezones | Current Offset | DST Active | Local Time |",
        "| :--- | :---: | :--- | :---: | :---: | :--- |"
    ]

    for item in data:
        country = item["country_name"]
        code = item["country_code"]
        for idx, zone in enumerate(item["zones"]):
            # Display country name only on the first row if country has multiple timezones
            display_country = country if idx == 0 else ""
            display_code = f"`{code}`" if idx == 0 else ""
            dst_badge = "Yes" if zone["is_dst"] else "No"

            lines.append(
                f"| {display_country} | {display_code} | `{zone['timezone']}` | **{zone['gmt_offset']}** | {dst_badge} | `{zone['current_local_time']}` |"
            )

    table_markdown = "\n".join(lines)
    replacement_content = f"{START_MARKER}\n\n{table_markdown}\n\n{END_MARKER}"

    if not os.path.exists(README_FILE):
        content = f"# Global Timezones & Live GMT Registry\n\n{replacement_content}\n"
    else:
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        if START_MARKER in content and END_MARKER in content:
            parts = content.split(START_MARKER)
            post_part = parts[1].split(END_MARKER)[1]
            content = parts[0] + replacement_content + post_part
        else:
            content += f"\n\n## Current Global Offsets\n\n{replacement_content}\n"

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    try:
        print("Fetching worldwide timezones and calculating DST offsets...")
        data = fetch_country_timezones()

        # 1. Write timezones.json
        with open(JSON_OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "metadata": {
                    "updated_at_utc": datetime.now(timezone.utc).isoformat(),
                    "total_countries": len(data)
                },
                "countries": data
            }, f, indent=2, ensure_ascii=False)
        print(f"Successfully generated {JSON_OUTPUT_FILE}")

        # 2. Update README.md
        update_readme(data)
        print(f"Successfully updated {README_FILE}")

        # 3. Write success record to last_run.json
        record_run_status(status="success", total_entries=len(data))
        print("Execution finished successfully.")

    except Exception as exc:
        error_str = str(exc)
        print(f"Fatal error occurred: {error_str}", file=sys.stderr)
        record_run_status(status="failed", error_msg=error_str)
        sys.exit(1)


if __name__ == "__main__":
    main()
