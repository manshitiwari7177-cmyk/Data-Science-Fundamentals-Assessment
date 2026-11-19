# Data-Science-Fundamentals-Assessment
A Python-based assessment covering data science fundamentals, including Python basics, data types, statistics, data cleaning, exploratory data analysis (EDA), correlation, and coding best practices with practical examples and tests.
Data Science Fundamentals Assessment
A beginner-friendly, runnable Python assessment covering core data science fundamentals.

Objectives
Practice Python variables, operators, conditionals, loops, and functions.
Work with common data types and collections (list, set, dict, str).
Understand descriptive statistics: mean, median, mode, range, variance, and standard deviation.
Calculate z-scores and identify potential outliers using the IQR method.
Practice data cleaning and validation.
Perform a small exploratory data analysis (EDA) on a sample dataset.
Calculate Pearson correlation and understand its limitations.
Apply coding best practices and basic tests.
Files
data_science_fundamentals.py — code, sample dataset, assessment functions, and self-tests.
README.md — instructions and topic overview.
Requirements
Python 3.8+ recommended.
No third-party libraries required.
Run the assessment
Open a terminal in this folder and run:

python data_science_fundamentals.py
The program prints example outputs and runs assertions at the end. If all assertions pass, it prints:

All self-tests passed.
Assessment completed successfully.
Assessment sections
1. Python basics
classify_score(score): maps a score to a letter grade.
is_even(number): checks evenness.
factorial(n): computes factorial iteratively.
2. Data types and collections
summarize_collection(items): count, unique values, min, and max.
word_frequency(sentence): case-insensitive word counts.
3. Statistics
statistical_summary(values): descriptive statistics.
calculate_z_scores(values): standardizes values.
detect_outliers_iqr(values): identifies IQR-based outliers.
4. Data cleaning
clean_numeric_values(values): converts valid numeric values and skips invalid/missing entries.
normalize_categories(categories): trims whitespace and normalizes capitalization.
5. Exploratory data analysis
eda_report(records): summaries from the built-in student sample.
correlation_coefficient(x, y): Pearson correlation.
6. Best practices
Functions have docstrings.
Inputs are validated and errors are explicit.
The script uses a main() entry point.
Assertions verify expected behavior.
Suggested extensions
Add a function to calculate a percentage or weighted average.
Implement a linear search and binary search, then compare their use cases.
Add missing-value counts to eda_report.
Explain in your own words why correlation does not imply causation.
Replace the sample data with a CSV dataset and extend the EDA.
Notes
This is a learning assessment example, not a production data pipeline. Real projects should additionally consider privacy, reproducibility, version control, logging, robust schema validation, and testing frameworks such as pytest.

