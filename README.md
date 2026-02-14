# summer_school_DSA
A mini project assignment for the DSA 2026 Summer School Admittance Check at Makerere University.

This project tests proficiency in three key areas: **Data Analysis & Engineering (E)**, **Machine Learning & Visualization (M)**, and **Natural Language Processing (N)**.

---

## Project Overview

**Target Audience:** Prospective attendees of DSA 2026 at Makerere University  
**Delivery:** Jupyter Notebook (`DSA_2026_Entry.ipynb`)  
**Grading:** Automated via Otter grader with 12 test cases (e1–e5, m1–m4, n1–n3)

---

## Data Overview

This workspace includes two real-world datasets:

### 1. data-2class.npz
**Location:** `summerschool/data/data-2class.npz`

NumPy archive containing synthetic 2D classification data:
- **`d`**: Feature matrix, shape (1000, 2) — two continuous features (floats)
- **`l`**: Label array, shape (1000, 1) — binary labels {0, 1}

**Purpose:** Machine learning exercises on classification, visualization, and statistical fitting.

### 2. uganda-consumer-price-index-trends-2020-2023.xlsx
**Location:** `summerschool/data/uganda-consumer-price-index-trends-2020-2023.xlsx`

Real economic dataset from Uganda, with 158 CPI indicators across 28 months (Dec 2020–Jan 2023):
- **Columns:** `indicator_code`, `description`, + monthly data columns
- **Indicators:** Overall CPI, Core CPI, Food CPI, Energy/Fuel/Utilities (EFU), and historical variants
- **Purpose:** Data wrangling, reshape operations, missing value handling, and time series basics

---

## Expected Solutions Summary

### Part E: Data Engineering (5 questions)

| Q | Task | Expected Output | Key Skills |
|---|------|-----------------|-----------|
| **E1** | Load Uganda CPI dataset | `df` as pandas DataFrame (158 rows × 28 cols) | File I/O, pandas basics |
| **E2** | Reshape wide → long format | `df_long` with columns: indicator_code, description, date, value | `pd.melt()`, data reshaping |
| **E3** | Parse date column | `df_long['date']` as datetime64 | Date parsing (e.g., 'dec-20' → '2020-12-01') |
| **E4** | Filter by indicator type | `df_cpi`, `df_all_items`, `df_core`, `df_food`, `df_efu` | String filtering, `.str.startswith()` |
| **E5** | Handle missing values | Replace NaN in 'value' column with indicator-specific median | `.fillna()`, `.groupby()`, `.transform()` |

**Key Concepts:** Pandas (load, melt, filter, fillna), datetime handling, missing value imputation.

---

### Part M: Machine Learning & Visualization (4 questions)

| Q | Task | Expected Output | Key Skills |
|---|------|-----------------|-----------|
| **M1** | Load & visualize 2D data | Scatterplot with red (class 0) and blue (class 1) points | `np.load()`, matplotlib scatter |
| **M2** | Draw separating line | Scatterplot + linear decision boundary | Line drawing (`plt.axline()` or `plt.plot()`) |
| **M3** | Fit Gaussians to each class | Mean vectors and 2×2 covariance matrices for both classes | Filtering, `np.mean()`, `np.cov()` |
| **M4** | Plot probability heatmap | Contour plot of Gaussian PDFs overlaid with data points | `scipy.stats.multivariate_normal`, `plt.contourf()` |

**Key Concepts:** NumPy (filtering, mean/cov), matplotlib (scatter/contour), scipy multivariate distributions, statistical fitting.

---

### Part N: Natural Language Processing (3 questions)

| Q | Task | Expected Output | Key Skills |
|---|------|-----------------|-----------|
| **N1** | Word frequency counter | Function returns dict with lowercase words as keys, counts as values; ignore punctuation | String manipulation, `.lower()`, `.split()`, dict aggregation |
| **N2** | Entity extraction | Function returns list of sentences containing any keyword from input list | Sentence split (e.g., split on `.`), keyword matching |
| **N3** | Text similarity (Jaccard) | Function returns float [0, 1]; J(A,B) = \|A ∩ B\| / \|A ∪ B\| | Set operations, word tokenization |

**Key Concepts:** String processing, basic NLP (tokenization, keyword search), set operations, similarity metrics.

---

## Test Organization

Tests reside in [summerschool/tests/](summerschool/tests/):
- **e1.py–e5.py**: Verify data structure, types, shapes, non-empty checks
- **m1.py–m4.py**: Verify array types, dimensions, statistical properties (symmetric covariance, etc.)
- **n1.py–n3.py**: Verify function callability, return types, basic output validation

Tests use Otter grader's auto-checking framework.

---

## How to Use This Notebook

1. **Open** `DSA_2026_Entry.ipynb` in Jupyter Lab/Notebook
2. **Complete** each `...` placeholder with your solution
3. **Run** each `grader.check()` cell to validate
4. **Review** any failing tests and debug
5. **Export** the completed notebook using `grader.export()` at the end
6. **Submit** the generated `.zip` file to the DSA application portal

---

## Key Libraries Required

```python
pandas              # Data wrangling, reshaping
numpy               # Array operations, statistics
matplotlib.pyplot   # Visualization
scipy.stats         # Multivariate normal distributions
otter-grader        # Auto-grading framework
```

---

## Important Notes

- ✅ All work **must be your own**; plagiarism results in non-admittance
- ✅ Do **not modify test files** or grader initialization
- ✅ Save your notebook before exporting
- ✅ All 12 tests should pass before submission
