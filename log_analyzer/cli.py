import argparse
from pathlib import Path
from .core import analyze_lines

def main():
    parser = argparse.ArgumentParser(description="Analyze a text log file")
    parser.add_argument("logfile", type=Path)
    parser.add_argument("--threshold", type=int, default=5)
    args = parser.parse_args()
    with args.logfile.open(encoding="utf-8", errors="replace") as file:
        result = analyze_lines(file, args.threshold)
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
