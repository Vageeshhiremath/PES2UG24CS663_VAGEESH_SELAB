# Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running it. It identifies defects,
security risks, maintainability problems, and style violations early, which makes
issues cheaper to fix and helps teams apply consistent quality standards.

## 2. What did each tool contribute?

Pylint found code-quality problems such as missing documentation, inconsistent
naming, the mutable default argument, and opportunities to simplify the code.
Flake8 focused on precise PEP 8 violations such as whitespace, blank lines, and
line length. Bandit identified security risks including shell command execution,
unsafe temporary-file creation, hardcoded credentials, and weak randomness.

## 3. Which issue was most important, and how was it fixed?

The shell command injection warning was the most important because untrusted server
input was concatenated into a command executed by a shell. The helper was unused
by the application, so it was removed rather than preserving a dangerous feature.
The other security findings were also addressed by removing the unused password,
using a secure temporary-file API, and using `SystemRandom` for the coin toss.

## 4. How did static analysis improve the program?

The final program retains the original scoreboard output while being easier to read,
better documented, and safer. Pylint improved from 4.75/10 to 10.00/10, Bandit
reports no issues, and Flake8 reports no violations. Static analysis provided an
objective way to verify that the changes addressed the detected problems.
