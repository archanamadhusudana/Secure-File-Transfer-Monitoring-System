from datetime import datetime

def generate_report():
    try:
        with open("file_monitor.log", "r") as log:
            entries = log.readlines()

        with open("audit_report.txt", "w") as report:
            report.write("=" * 50 + "\n")
            report.write("   SECURE FILE TRANSFER AUDIT REPORT\n")
            report.write("=" * 50 + "\n")
            report.write(f"Generated: {datetime.now()}\n\n")
            report.write(f"Total Events: {len(entries)}\n\n")
            report.write("--- EVENT LOG ---\n")
            for entry in entries:
                report.write(entry)

        print("Audit report saved as audit_report.txt ✅")

    except FileNotFoundError:
        print("No log file found. Run monitor.py first!")

generate_report()