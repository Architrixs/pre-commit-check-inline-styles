# check_inline_styles.py
import re
import sys

# Regular expression to match inline styles
inline_style_pattern = re.compile(r'style\s*=\s*["\'][^"\']*["\']')

def find_inline_styles(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = inline_style_pattern.findall(content)
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
            print(f"{file_path}:")
            for match in matches:
                print(f"  {match}")
        sys.exit(1)
    else:
        print("No inline styles found.")
        sys.exit(0)

if __name__ == '__main__':
    main()
