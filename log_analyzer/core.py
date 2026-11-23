from collections import Counter

def analyze_lines(lines, threshold=5):
    total = 0
    errors = []
    for line in lines:
        total += 1
        if "ERROR" in line.upper():
            errors.append(line.strip())
    counts = Counter(errors)
    return {
        "total_lines": total,
        "error_count": len(errors),
        "unique_errors": len(counts),
        "top_errors": counts.most_common(5),
        "threshold_exceeded": len(errors) > threshold,
    }
