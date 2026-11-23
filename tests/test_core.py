from log_analyzer.core import analyze_lines

def test_counts_errors():
    result = analyze_lines(["INFO ok", "ERROR failure", "ERROR failure"], threshold=1)
    assert result["total_lines"] == 3
    assert result["error_count"] == 2
    assert result["threshold_exceeded"] is True

def test_no_errors():
    result = analyze_lines(["INFO ok"], threshold=0)
    assert result["error_count"] == 0
    assert result["threshold_exceeded"] is False
