# DEV_LOG – Summer School DSA Project Exploration

**Date:** Feb 14, 2026  
**Status:** Initial exploration and documentation completed  
**Scope:** Full repository review with focus on datasets, test specifications, and expected solutions

---

## 1. Repository Structure Overview

```
summer_school_DSA/
├── LICENSE
├── README.md                          [UPDATED with full guide]
├── DEV_LOG.md                         [THIS FILE]
├── .git/                              [Git repository]
├── .gitignore
├── .venv/                             [Virtual environment with pandas, numpy]
└── summerschool/
    ├── DSA_2026_Entry.ipynb          [Main assignment notebook – 12 questions]
    ├── .ipynb_checkpoints/
    ├── .OTTER_LOG                    [Grader logs]
    ├── data/
    │   ├── data-2class.npz           [1000×2 synthetic 2-class dataset]
    │   └── uganda-consumer-price-index-trends-2020-2023.xlsx  [158 CPI series, 28 months]
    └── tests/
        ├── e1.py through e5.py       [Data Engineering tests]
        ├── m1.py through m4.py       [Machine Learning & Viz tests]
        └── n1.py through n3.py       [NLP tests]
```

---

## 2. Datasets Analyzed

### Dataset A: data-2class.npz
- **Format:** NumPy archive
- **Contents:**
  - `d`: (1000, 2) float64 array — 1000 points in 2D space
  - `l`: (1000, 1) float64 array — binary labels (0 or 1)
- **Sample d values:** `[[1.138, 1.746], [0.664, -0.112], [0.417, 0.377], ...]`
- **Sample l values:** `[[0], [0], [0], ...]`
- **Use:**
  - Classification visualization (M1: scatterplot)
  - Separating line (M2: decision boundary)
  - Gaussian fitting (M3: mean, covariance per class)
  - Heatmap with PDF overlay (M4: contour + scatter)

### Dataset B: uganda-consumer-price-index-trends-2020-2023.xlsx
- **Sheet:** "Sheet1"
- **Dimensions:** 158 rows × 28 columns
- **Structure:**
  - Col 1: `indicator_code` (e.g., CPI_16, CPI_CORE_16, CPI_FOOD_16, CPI_EFU_16, CPI_09, etc.)
  - Col 2: `description` (human-readable labels for each CPI series)
  - Cols 3–28: monthly data columns (dec-20, jan-21, feb-21, ..., jan-23)
- **Value Range:** Float values representing CPI indices; some zero values (missing/inactive series)
- **Use:**
  - Load and inspect (E1)
  - Reshape wide→long (E2)
  - Date parsing (E3)
  - Filtering by prefix (E4)
  - Missing value handling (E5)

---

## 3. Notebook Structure & Questions

### Part E: Data Engineering (Pandas + Date Handling)

**E1: Load Dataset**
- Load `data/uganda-consumer-price-index-trends-2020-2023.xlsx`
- Expected: `df` as pandas DataFrame
- Validate: 158 rows, columns include 'indicator_code' and 'description'
- **Solution Hint:** `pd.read_excel(path)`

**E2: Reshape Wide → Long**
- Transform from: `[indicator_code, description, dec-20, jan-21, ..., jan-23]`
- Transform to: `[indicator_code, description, date, value]`
- Expected: `df_long` with shape (4404, 4) or similar [158 indicators × 28 months = 4424 rows]
- **Solution Hint:** `pd.melt(df, id_vars=['indicator_code', 'description'], var_name='date', value_name='value')`

**E3: Parse Dates**
- Convert date column from strings like 'dec-20', 'jan-21' to datetime64 format
- Expected: 'dec-20' → '2020-12-01', 'jan-21' → '2021-01-01', etc.
- **Solution Hint:** `pd.to_datetime(df_long['date'], format='%b-%y' or custom parsing)`

**E4: Filter by Indicator Type**
- Create separate dataframes for CPI categories:
  - `df_cpi`: All rows where indicator_code starts with 'CPI_'
  - `df_all_items`: Filter for 'CPI_16' or 'CPI_09' (all-items CPI)
  - `df_core`: Filter for 'CPI_CORE_16' or 'CPI_CORE_09'
  - `df_food`: Filter for 'CPI_FOOD_16' or 'CPI_FOOD_09'
  - `df_efu`: Filter for 'CPI_EFU_16' or 'CPI_EFU_09'
- Expected: Each filtered dataframe contains relevant rows only
- **Solution Hint:** `df[df['indicator_code'].str.startswith('CPI_')]`, boolean indexing

**E5: Handle Missing Values**
- Check for NaN in 'value' column
- Replace each NaN with the median value for that specific indicator_code
- Expected: All missing values replaced; missing_after count = 0
- **Solution Hint:** `df_long.groupby('indicator_code')['value'].transform('median')` for per-group median, then `.fillna()`

---

### Part M: Machine Learning & Visualization (NumPy + Matplotlib + SciPy)

**M1: Load & Scatterplot**
- Load `data/data-2class.npz` using `np.load()`
- Create 2D scatterplot with:
  - Red points for label = 0
  - Blue points for label = 1
- Expected: Visual separation visible; ~500 points per class
- **Solution Hint:**
  ```python
  data = np.load('path/data-2class.npz')
  d, l = data['d'], data['l']
  plt.scatter(d[l.ravel() == 0, 0], d[l.ravel() == 0, 1], color='red')
  plt.scatter(d[l.ravel() == 1, 0], d[l.ravel() == 1, 1], color='blue')
  ```

**M2: Separating Line**
- Draw a straight line on the scatterplot that separates the two classes
- Expected: Line visually divides red and blue regions
- **Solution Hint:** `plt.axline((x0, y0), slope=m)` or `plt.plot([x1, x2], [y1, y2])`

**M3: Gaussian Fitting**
- For each class (0 and 1), compute:
  - Mean vector (centroid) → shape (2,)
  - Covariance matrix → shape (2, 2)
- Expected:
  - `mean_class_0`, `mean_class_1`: shape (2,)
  - `cov_class_0`, `cov_class_1`: shape (2, 2), symmetric, positive semi-definite
- Test checks: Symmetric, det ≥ 0, correct shapes
- **Solution Hint:**
  ```python
  points_class_0 = d[l.ravel() == 0, :]
  mean_class_0 = np.mean(points_class_0, axis=0)
  cov_class_0 = np.cov(points_class_0.T)
  ```

**M4: Gaussian PDF Heatmap**
- Create multivariate normal distributions using fitted means & covariances
- Generate 100×100 meshgrid over data space
- Compute PDF values for both classes
- Overlay as contour/heatmap with original scatterplot
- Expected:
  - `gaussian_class_0`, `gaussian_class_1`: multivariate_normal objects
  - `pdf_class_0`, `pdf_class_1`: shape (100, 100), non-negative values
- **Solution Hint:**
  ```python
  from scipy.stats import multivariate_normal
  gaussian_class_0 = multivariate_normal(mean_class_0, cov_class_0)
  pos = np.dstack((xx, yy))
  pdf_class_0 = gaussian_class_0.pdf(pos)
  plt.contourf(xx, yy, pdf_class_0, alpha=0.6)
  plt.scatter(...)
  ```

---

### Part N: Natural Language Processing (String + Set Operations)

**N1: Word Frequency Counter**
- Function `count_words(text: str) → dict`
- Count unique words (lowercase) and their frequencies
- Ignore punctuation; split on whitespace
- Example: `"Hello world hello"` → `{'hello': 2, 'world': 1}`
- **Solution Hint:**
  ```python
  def count_words(text):
      import string
      words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
      return {word: words.count(word) for word in set(words)}
  ```

**N2: Entity Extraction**
- Function `extract_entities(text: str, keywords: list) → list`
- Find and return all sentences containing any keyword
- Assumes sentences split on periods (.)
- Example:
  - Input: "Makerere is in Kampala. Kampala is capital.", keywords: ["Kampala"]
  - Output: ["Makerere is in Kampala.", "Kampala is capital."]
- **Solution Hint:**
  ```python
  def extract_entities(text, keywords):
      sentences = [s.strip() for s in text.split('.') if s.strip()]
      return [s for s in sentences if any(kw in s for kw in keywords)]
  ```

**N3: Jaccard Similarity**
- Function `calculate_similarity(text1: str, text2: str) → float`
- Compute Jaccard index: J(A, B) = |A ∩ B| / |A ∪ B|
- Words are tokenized (lowercase, whitespace-split)
- Expected: float in [0, 1]
- Example: "data science africa" vs "data science kampala" → 2 common / 3 unique = 0.667
- **Solution Hint:**
  ```python
  def calculate_similarity(text1, text2):
      words1 = set(text1.lower().split())
      words2 = set(text2.lower().split())
      intersection = len(words1 & words2)
      union = len(words1 | words2)
      return intersection / union if union > 0 else 0
  ```

---

## 4. Test Coverage Summary

| Category | Tests | Coverage |
|----------|-------|----------|
| **Data Engineering (E)** | e1, e2, e3, e4, e5 | Loading, reshaping, parsing, filtering, imputation |
| **Machine Learning (M)** | m1, m2, m3, m4 | Visualization, fitting, PDF computation |
| **NLP (N)** | n1, n2, n3 | Word counting, entity extraction, similarity |
| **Total** | **12** | ComprehensivePython proficiency assessment |

**Test Framework:** Otter Grader  
**Execution:** `grader.check("question_name")` in notebook cells

---

## 5. Key Concepts & Skills Validated

### Data Engineering
- Pandas I/O (Excel, CSV)
- DataFrame reshaping (wide ↔ long)
- DateTime parsing & formatting
- String filtering & regex (`.str.startswith()`)
- Missing value imputation (median, groupby, transform)

### Machine Learning & Visualization
- NumPy array operations (loading, filtering, slicing)
- NumPy statistics (mean, covariance)
- Matplotlib visualization (scatter, plot, contour, contourf, legend)
- SciPy multivariate distributions (PDF computation)
- Linear algebra (covariance matrices, symmetry checks)

### NLP
- String manipulation (`.lower()`, `.split()`, punctuation removal)
- Set operations (intersection, union)
- List comprehensions & filtering
- Basic tokenization
- Similarity metrics (Jaccard index)

---

## 6. Development Notes

### Strengths of This Project
✅ Covers three essential DSA domains (data, ML, NLP)  
✅ Uses real-world CPI data (practical relevance)  
✅ Synthetic 2D data perfect for visualization teaching  
✅ Clear, testable specifications via Otter grader  
✅ Progressively complex (load → reshape → parse → filter → impute)  

### Observations
- CPI dataset has ~158 indicators but only ~24 unique CPI series (prefixes: CPI_, CPI_CORE_, CPI_FOOD_, CPI_EFU_)
- Some indicators have zero values (inactive/future series); candidates should handle gracefully
- M questions build on M1 (reuse d, l); suggests sequential execution
- N questions are independent; can be done in any order
- All tests use `try/except NameError` for format validation—robust approach

---

## 7. Next Steps for Candidates

1. ✅ Read all 12 question descriptions in notebook
2. ✅ Understand data structure (verify with `df.shape`, `df.head()`, `df.dtypes`)
3. ✅ Implement solutions incrementally; **run tests after each section**
4. ✅ Verify all outputs match expected shapes/types
5. ✅ Use `grader.export()` to generate submission `.zip`
6. ✅ Submit via DSA application portal

---

## 8. Resources & Libraries

- **pandas:** `df.read_excel()`, `df.melt()`, `df.fillna()`, `df.groupby().transform()`
- **numpy:** `np.load()`, `np.mean()`, `np.cov()`, array indexing
- **matplotlib.pyplot:** `plt.scatter()`, `plt.plot()`, `plt.contourf()`, `plt.legend()`
- **scipy.stats:** `multivariate_normal(mean, cov)`, `.pdf()`
- **string:** `string.punctuation` for removing punctuation

---

**End of DEV_LOG**  
Generated: Feb 14, 2026
