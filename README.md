# Playwright + Pytest Reference Automation Framework

This repository demonstrates a production-grade test automation framework
built with Playwright and Pytest. It showcases UI automation, end-to-end
testing, backend network assertions, and clean REST API automation practices.

NOTE
Amazon heavily protects its frontend with anti-automation mechanisms including bot detection, region-specific consent flows, iframe-based cookie banners and dynamic DOM variations.
These mechanisms intentionally make external UI automation unreliable.
For this reason, the test framework prioritizes stability and determinism by using defensive waits and conditional skips when the environment blocks automated interaction.

--------------------------------------------------
TECH STACK
--------------------------------------------------

- Python 3.13
- Pytest
- Playwright (sync API)
- Requests
- Pydantic
- Black & Ruff

--------------------------------------------------
PROJECT STRUCTURE
--------------------------------------------------

- src/
  - core/          Framework configuration, logging, artifacts
  - pages/         Page Object Model and UI components
  - api/           UI-triggered network helpers
  - api_demo/      Standalone REST API automation demo
  - utils/         Shared helpers
- tests/
  - ui/            Smoke, regression, edge, checks, and E2E tests
  - amazon_network Network-level assertions triggered by UI flows
  - api_demo       REST API smoke, regression, and edge tests
- docs/
  - TEST_COVERAGE.txt
  - RUNBOOK_README.txt

--------------------------------------------------
SETUP
--------------------------------------------------

1. Create virtual environment
   python -m venv .venv

2. Activate environment
   .venv\Scripts\activate    (Windows)
   source .venv/bin/activate (Linux/Mac)

3. Install dependencies
   pip install -r requirements.txt

4. Install Playwright browsers
   playwright install

5. Configure environment
   Copy .env.example to .env

--------------------------------------------------
RUNNING TESTS
--------------------------------------------------

Examples:

Run all tests:
   pytest

Run smoke tests:
   pytest -m smoke

Run regression tests:
   pytest -m regression

Run edge tests:
   pytest -m edge

Run E2E tests:
   pytest -m e2e

Run Amazon network tests:
   pytest -m amazon_network

Run demo API tests:
   pytest -m api_demo

--------------------------------------------------
DESIGN PRINCIPLES
--------------------------------------------------

- Page Object Model with component composition
- Clear separation of test logic and implementation
- Marker-based test categorization
- Stable waits, no hard-coded sleeps
- Failure-based artifact collection
- CI-ready execution

--------------------------------------------------
DISCLAIMER
--------------------------------------------------

This project is intended as a reference implementation to demonstrate
automation best practices and architectural patterns. It is not affiliated
with or endorsed by Amazon.


Jenkis scheduled cron jobs screenshots.
![alt text](image.png)
![alt text](image-1.png)

ENV script:
set PYTHON=C:\Users\Levi\AppData\Local\Programs\Python\Python313\python.exe
set PLAYWRIGHT_BROWSERS_PATH=%WORKSPACE%\pw-browsers

%PYTHON% -m venv .venv

call .venv\Scripts\activate

.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\pip.exe install -r requirements.txt
.venv\Scripts\pip.exe install pytest-html

.venv\Scripts\python.exe -m playwright install chromium

copy .env.example .env

.venv\Scripts\pytest.exe -m regression ^
  --junitxml=test-results/junit.xml ^
  --html=test-results/report.html ^
  --self-contained-html
