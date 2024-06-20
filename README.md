# pre-commit-check-inline-styles
This hook checks for inline styles in HTML files.

## Using pre-commit-hooks with pre-commit
Add this to your .pre-commit-config.yaml

```
repos:
  - repo: https://github.com/architrixs/pre-commit-check-inline-styles
    rev: main  # Use the appropriate branch or tag
    hooks:
      - id: check-inline-styles

```