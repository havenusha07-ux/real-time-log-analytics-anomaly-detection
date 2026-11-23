# Real-Time Log Analytics & Anomaly Detection (Starter)

A command-line tool that summarizes log files and flags unusually frequent error messages.

## Tech stack
- Python 3.11+
- Standard library (collections, argparse, datetime)
- pytest

## Setup
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python -m log_analyzer.cli sample.log
```

## Sample log format
One event per line. The tool counts lines containing `ERROR`, reports the most common error messages, and warns if errors exceed a configurable threshold.

## Development status
Starter implementation. Future improvements include JSON log parsing, time-windowed metrics, streaming input, dashboards, and statistical anomaly detection.
