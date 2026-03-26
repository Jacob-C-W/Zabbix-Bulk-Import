
#CSV imports
import csv
import os
from typing import Dict

#Function imports
from zabbix_login import zabbix_login
from zabbix_utils import ZabbixAPI
from zabbix_hostcreate import zabbix_hostcreate

# CSV file and config
CSV_FILENAME = "bulk_import.csv"  # Fixed name, same directory
MAX_CREATE = 100  # Only create 2 for testing

def main() -> None:
    print("[BOOT] Bulk prompt import started.", flush=True)

    # Build full path to CSV in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, CSV_FILENAME)

    # Simple prompts
    print(f"[INFO] CSV file: {csv_path}", flush=True)
    print(f"[INFO] Will create up to {MAX_CREATE} host(s) for this test.", flush=True)
    go = input("Type YES to proceed: ").strip().upper()

    if go != "YES":
        print("[EXIT] Cancelled by user.", flush=True)
        return

    # login to the API
    api = zabbix_login()

    created = 0
    skipped = 0

   # Read CSV and create hosts
    with open(csv_path, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        # Minimal validation: ensure required headers exist
        if not reader.fieldnames:
            print("[FAIL] CSV has no headers.", flush=True)
            return

        # Normalize headers to lowercase so Hostname/hostname both work
        fieldnames_lower = [h.strip().lower() for h in reader.fieldnames]
        if "hostname" not in fieldnames_lower or "ip" not in fieldnames_lower:
            print("[FAIL] CSV must contain headers: hostname, ip", flush=True)
            print(f"[DEBUG] Found headers: {reader.fieldnames}", flush=True)
            return

    # Map normalized header -> actual header name
        header_map = {h.strip().lower(): h for h in reader.fieldnames}

        for row_num, row in enumerate(reader, start=2):  # row 1 = header
            if created >= MAX_CREATE:
                print("[STOP] Reached MAX_CREATE limit for this test run.", flush=True)
                break

            hostname = (row.get(header_map["hostname"]) or "").strip()
            host_ip = (row.get(header_map["ip"]) or "").strip()

            # Skip blank/invalid lines
            if not hostname or not host_ip:
                skipped += 1
                print(f"[SKIP] line={row_num} missing hostname or ip", flush=True)
                continue

            print(f"[DOING] Creating host #{created+1}: {hostname} ({host_ip})", flush=True)

            # Call YOUR existing hostcreate function
            # This should raise on failure, and return a result dict on success.
            result = zabbix_hostcreate(api, hostname, host_ip)

            created += 1
            print(f"[CREATED] {hostname} result={result}", flush=True)

    print("\n[SUMMARY]", flush=True)
    print(f"Created: {created}", flush=True)
    print(f"Skipped: {skipped}", flush=True)
    print("[DONE]", flush=True)


if __name__ == "__main__":
    main()
