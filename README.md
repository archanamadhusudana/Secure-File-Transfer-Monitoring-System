*Secure File Transfer Monitoring System*

A Python-based cybersecurity tool that monitors, detects, and logs all file activities within a designated secure folder in real time. Built as part of a structured enterprise cybersecurity learning project.

---

*About*

This system watches a specified directory for any file system events including file creation, modification, movement, and deletion. When a sensitive file is detected, it automatically generates a SHA-256 cryptographic hash to verify file integrity and logs the event with a timestamp for audit purposes.

---

*Features*

- Real-time file system monitoring using the watchdog library
- SHA-256 hash generation for file integrity verification
- Automatic event logging with timestamps
- Alert generation for sensitive file movements
- Audit report generation summarizing all monitored activity
- Supports sensitive file types: .pdf, .docx, .xlsx, .txt

---

*Tools & Technologies*

- Python 3.12
- watchdog — filesystem event monitoring
- hashlib — SHA-256 cryptographic hashing
- logging — event log management
- psutil — optional process tracking

---

*Project Structure*

SecureFileMonitor/
├── monitor.py         # Main monitoring script
├── audit_report.py    # Generates audit report
├── file_monitor.log   # Auto-generated event log
└── audit_report.txt   # Final audit report output


---

*How to Run*
bash
pip install watchdog psutil
python monitor.py


---

*Learning Outcomes*

This project demonstrates practical skills in filesystem security monitoring, cryptographic hashing, security event logging, and audit trail generation — core concepts in enterprise cybersecurity and network security monitoring.
