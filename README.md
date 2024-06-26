# pre-commit-check-inline-styles
This hook checks for inline styles in HTML files.

## Using pre-commit-hooks with pre-commit
Add this to your .pre-commit-config.yaml

```
repos:
  - repo: https://github.com/architrixs/pre-commit-check-inline-styles
    rev: 1.1.0  # Use the appropriate tag
    hooks:
      - id: check-inline-styles
        args: [--warn-only]
        verbose: true

```

### Usage:
To check for inline styles in HTML files:

```bash
check-inline-styles [--warn-only] [file_or_directory ...]
--warn-only: Only warn about inline styles without modifying files and exit with a success status.
```