import re
import sys

# Regular expression to match inline styles
inline_style_pattern = re.compile(r'style\s*=\s*["\'][^"\']*["\']')

def find_inline_styles(file_path):
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            match = inline_style_pattern.search(line)
            if match:
                matches.append((line_number, match.group(0)))
    return matches

def main():
    files_with_inline_styles = []
    for file_path in sys.argv[1:]:
        if file_path.endswith('.html'):
            matches = find_inline_styles(file_path)
            if matches:
                files_with_inline_styles.append((file_path, matches))
    
    if files_with_inline_styles:
        print("Inline styles found in the following files:")
        for file_path, matches in files_with_inline_styles:
            for line_number, match in matches:
                # Output in format recognized by VS Code: file_path:line_number:column_number
                print(f"{file_path}:{line_number}:0: {match}")
        sys.exit(1)
    else:
        print("No inline styles found.")
        sys.exit(0)

if __name__ == '__main__':
    main()