# 5. Mini Exploratory Data Analysis (EDA) using a sample dataset
# ---------------------------------------------------------------------------

SAMPLE_STUDENTS = [
    {"name": "Aarav", "department": "Data Science", "hours_studied": 5, "score": 82},
    {"name": "Diya", "department": "Computer Science", "hours_studied": 7, "score": 91},
    {"name": "Kabir", "department": "Data Science", "hours_studied": 3, "score": 68},
    {"name": "Meera", "department": "Computer Science", "hours_studied": 8, "score": 95},
    {"name": "Rohan", "department": "Data Science", "hours_studied": 6, "score": 87},
    {"name": "Sana", "department": "Mathematics", "hours_studied": 2, "score": 58},
    {"name": "Ishaan", "department": "Mathematics", "hours_studied": 4, "score": 73},
    {"name": "Tara", "department": "Computer Science", "hours_studied": 6, "score": 84},
]


def eda_report(records):
    """Generate a compact report from a list of student dictionaries."""
    if not records:
        return {"row_count": 0, "departments": {}, "score_summary": None}

    scores = [record["score"] for record in records]
    study_hours = [record["hours_studied"] for record in records]
    departments = Counter(record["department"] for record in records)

    return {
        "row_count": len(records),
        "department_counts": dict(departments),
        "average_score": mean(scores),
        "median_score": median(scores),
        "average_study_hours": mean(study_hours),
        "highest_score_student": max(records, key=lambda record: record["score"])["name"],
        "lowest_score_student": min(records, key=lambda record: record["score"])["name"],
    }


def correlation_coefficient(x, y):
    """Calculate Pearson correlation; returns None for undefined cases."""
    if len(x) != len(y) or len(x) < 2:
        raise ValueError("x and y must have equal length and at least 2 values")
    x_mean, y_mean = mean(x), mean(y)
    x_dev = [a - x_mean for a in x]
    y_dev = [b - y_mean for b in y]
    denominator = math.sqrt(sum(a * a for a in x_dev) * sum(b * b for b in y_dev))
    if denominator == 0:
        return None
    return sum(a * b for a, b in zip(x_dev, y_dev)) / denominator


# ---------------------------------------------------------------------------
# 6. Best Practices: tests, validation, readable output
# ---------------------------------------------------------------------------

def run_self_tests():
    """Lightweight assertions for key functions."""
    assert classify_score(95) == "A"
    assert classify_score(80) == "B"
    assert is_even(4) is True
    assert is_even(5) is False
    assert factorial(5) == 120
    assert summarize_collection([1, 1, 2, 3])["unique_count"] == 3
    assert word_frequency("Data science, data!") == {"data": 2, "science": 1}
    assert statistical_summary([1, 2, 3])["mean"] == 2
    assert calculate_z_scores([10, 10, 10]) == [0.0, 0.0, 0.0]
    assert clean_numeric_values(["1", "2.5", None, "bad"]) == [1.0, 2.5]
    assert normalize_categories([" data science ", "PYTHON", None]) == [
        "Data Science", "Python", None
    ]
    assert round(correlation_coefficient([1, 2, 3], [2, 4, 6]), 6) == 1.0
    print("All self-tests passed.")


def main():
    print("=" * 60)
    print("DATA SCIENCE FUNDAMENTALS ASSESSMENT")
    print("=" * 60)

    print("\n1) Python Basics")
    print(f"Score 86 -> Grade {classify_score(86)}")
    print(f"Is 14 even? {is_even(14)}")
    print(f"Factorial of 6: {factorial(6)}")

    print("\n2) Data Types & Collections")
    print(summarize_collection([2, 4, 4, 6, 8]))
    print(word_frequency("Python is useful. Python is popular!"))

    print("\n3) Statistical Summary")
    scores = [72, 80, 85, 85, 90, 96, 100]
    for key, value in statistical_summary(scores).items():
        print(f"{key}: {value}")
    print(f"Z-scores: {[round(z, 2) for z in calculate_z_scores(scores)]}")
    print(f"IQR outliers: {detect_outliers_iqr(scores)}")

    print("\n4) Data Cleaning")
    print(f"Clean numeric values: {clean_numeric_values(['12', '3.5', None, 'N/A', ''])}")
    print(f"Normalized categories: {normalize_categories([' science ', 'PYTHON', None])}")

    print("\n5) Mini EDA")
    report = eda_report(SAMPLE_STUDENTS)
    for key, value in report.items():
        print(f"{key}: {value}")
    hours = [student["hours_studied"] for student in SAMPLE_STUDENTS]
    marks = [student["score"] for student in SAMPLE_STUDENTS]
    print(f"Correlation (study hours vs score): {correlation_coefficient(hours, marks):.3f}")

    print("\n6) Best Practices")
    run_self_tests()
    print("\nAssessment completed successfully.")


if __name__ == "__main__":
    main()

