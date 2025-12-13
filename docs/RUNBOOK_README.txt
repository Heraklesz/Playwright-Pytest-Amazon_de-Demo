TEST EXECUTION RUNBOOK
=====================

This document describes how to set up, execute, and analyze test runs
for the Playwright + Pytest automation framework.

--------------------------------------------------
PREREQUISITES
--------------------------------------------------

- Python 3.13
- pip
- Git
- Internet connection (for Amazon and demo API access)

--------------------------------------------------
INITIAL SETUP
--------------------------------------------------

1. Clone the repository
   git clone <repository-url>
   cd playwright-pytest-amazon-de

2. Create and activate a virtual environment
   python -m venv .venv
   .venv\Scripts\activate    (Windows)
   source .venv/bin/activate (Linux/Mac)

3. Install dependencies
   pip install -r requirements.txt

4. Install Playwright browsers
   playwright install

5. Create environment configuration
   Copy .env.example to .env and adjust values if needed

--------------------------------------------------
RUNNING TESTS
--------------------------------------------------

Run all tests:
   pytest

Run UI smoke tests:
   pytest -m smoke

Run UI regression tests:
   pytest -m regression

Run edge tests:
   pytest -m edge

Run checks:
   pytest -m checks

Run E2E tests:
   pytest -m e2e

Run Amazon network tests:
   pytest -m amazon_network

Run demo API tests:
   pytest -m api_demo

--------------------------------------------------
ARTIFACTS AND LOGS
--------------------------------------------------

On test failure, the framework automatically captures:
- Screenshots
- Playwright traces
- (Optional) Videos

Artifacts are stored under:
- test-results/screenshots/
- test-results/traces/
- test-results/videos/
- test-results/logs/test_run.log

--------------------------------------------------
ANALYZING FAILURES
--------------------------------------------------

1. Check console output for assertion failures
2. Review logs in test-results/logs/
3. Open Playwright trace files using:
   playwright show-trace <trace-file>

--------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------

- Import errors:
  Ensure the correct Python interpreter and virtual environment are active.

- Browser launch failures:
  Re-run 'playwright install'

- Network-related test failures:
  Verify internet connectivity and retry execution.

--------------------------------------------------
CI NOTES
--------------------------------------------------

This framework is CI-ready and can be executed in headless mode
using environment variables defined in .env.
