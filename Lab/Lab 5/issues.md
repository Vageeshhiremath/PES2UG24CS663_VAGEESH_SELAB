# Static Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command injection risk (B605) | Security, high | 70-71 before fix | `os.system()` built a shell command by concatenating the server argument. | Removed the unused publishing helper instead of retaining an unsafe feature. |
| Insecure temporary file creation (B306) | Security, medium | 66 before fix | `tempfile.mktemp()` returned a path without safely creating the file. | Replaced it with `NamedTemporaryFile(..., delete=False)` in a context manager. |
| Hardcoded password (B105) | Security, low | 6 before fix | A referee password was stored in source code and was not used by the program. | Removed the unused credential. |
| Non-cryptographic randomness (B311) | Security, low | 61 before fix | The standard `random` generator was used for the coin toss. | Used `random.SystemRandom()` for stronger randomness. |
| Mutable default argument (W0102) | Bug risk | 11 before fix | `players=[]` could be shared between calls and cause unexpected state changes. | Changed the default to `None` and created a list per call. |
| Missing documentation and naming violations | Quality/style | Throughout | Functions lacked docstrings and used camelCase names. | Added documentation and renamed functions and arguments to snake_case. |
| Formatting violations (E203, E231, E261, E302, E501) | Style | 5, 60, 79, 87 | Whitespace, blank-line, and line-length rules were violated. | Reformatted the code to comply with Flake8. |
