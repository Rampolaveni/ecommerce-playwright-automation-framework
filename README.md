# Ecommerce Playwright Automation Framework

A **Python + Playwright + Pytest** automation framework designed for **UI test automation** with **CI/CD (Jenkins)**. This project follows clean structure, reproducible installs, and industry best practices.

---

## 📌 Tech Stack

* **Language:** Python 3.11.x
* **Test Runner:** Pytest
* **Automation Tool:** Playwright (sync API)
* **Reporting:** pytest-html (optional Allure support)
* **CI/CD:** Jenkins

---

## 📂 Project Structure

```text
ecommerce-playwright-automation-framework/
│
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
├── conftest.py              # Global fixtures
├── README.md
├── .gitignore
│
└── src/
    ├── commonUtility/       # Reusable utilities
    ├── core/                # Base classes / driver setup
    ├── dao/                 # Data access objects
    ├── objectRepository/    # Page locators
    ├── scenario/            # Business flows
    ├── test/                # Test cases (pytest discovery)
    └── testData/            # Test data files
```

---

## ✅ Prerequisites

* **Python 3.11.x** (required)
* **pip** (comes with Python)
* Internet access (for Playwright browser download)

> ⚠️ Python 3.12+ or 3.14 is **not recommended** for CI stability.

---

## ⚙️ Environment Setup (Local)

### 1️⃣ Verify Python version

```bash
python --version
```

Expected:

```text
Python 3.11.x
```

---

### 2️⃣ (Recommended) Create virtual environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install Playwright browsers

```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests

```bash
python -m pytest -v
```

### Run a specific test file

```bash
python -m pytest src/test/test_login.py -v
```

### Run with live logs

```bash
python -m pytest -v -s
```

---

## 🧪 Pytest Configuration

**pytest.ini**

```ini
[pytest]
testpaths = src/test
python_files = test_*.py
addopts = -v
```

---

## 📊 HTML Test Report (Optional)

Run tests with HTML reporting:

```bash
python -m pytest -v --html=reports/report.html --self-contained-html
```

---

## 🤖 Jenkins CI Integration

### Jenkins Build Steps (Windows Agent)

```bat
py -3.11 -m pip install --upgrade pip
py -3.11 -m pip install -r requirements.txt
py -3.11 -m playwright install
py -3.11 -m pytest -v
```

### Key CI Notes

* Jenkins must **clone the Git repository** (not local path)
* Python 3.11 must be installed on the Jenkins agent
* Workspace must not be empty before execution

---

## 🚫 What is Ignored (.gitignore)

* `__pycache__/`
* `.pytest_cache/`
* `playwright-report/`
* `test-results/`
* `.venv/`
* IDE folders (`.idea`, `.vscode`)

Generated files are **never committed**.

---

## 🧠 Best Practices Followed

* Pinned dependencies via `requirements.txt`
* Clean separation of test logic and locators
* CI-safe Python version
* Explicit Playwright browser install
* Reproducible local & CI runs

---

## 📌 Future Enhancements

* Allure reporting integration
* Dockerized execution
* Parallel execution with pytest-xdist
* Environment-based configs (QA / UAT)

---

✅ **Framework is CI-ready and production-aligned.**
