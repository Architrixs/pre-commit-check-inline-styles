import argparse
import os
import re
import sys
from termcolor import colored

# Regular expression to match inline styles
inline_style_pattern = re.compile(r'style\s*=\s*["\'][^"\']*["\']')
separator = colored("=" * 50, 'white')
def find_inline_styles(file_path):
    matches = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            match = inline_style_pattern.search(line)
            if match:
                matches.append((line_number, match.group(0)))
    return matches

def colored_text(text, color, no_color):
        if no_color:
            return text
        else:
            return colored(text, color)

def main():
    parser = argparse.ArgumentParser(description='Check for inline styles in HTML files.')
    parser.add_argument('--warn-only', action='store_true', help='Warn about inline styles without modifying files and exit with 0.')
    parser.add_argument('--no-color', action='store_true', help='Disable color output.')
    parser.add_argument('files', nargs='*', help='HTML files to check.')
    args = parser.parse_args()

    html_files = args.files
    if not html_files:
        for root, _, files in os.walk('.'):
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))

    files_with_inline_styles = []
    for file_path in html_files:
        matches = find_inline_styles(file_path)
        if matches:
            files_with_inline_styles.append((file_path, matches))   
    
    if files_with_inline_styles:
        print(colored_text("Warning: Inline styles found in the following files:", 'yellow', args.no_color))
        for file_path, matches in files_with_inline_styles:
            print(separator)
            print(colored_text(f"File: {file_path}", 'white', args.no_color))
            for line_number, match in matches:
                # Output in format recognized by VS Code: file_path:line_number:column_number
                print(f"{colored_text(file_path, 'cyan', args.no_color)}:{colored_text(str(line_number), 'cyan', args.no_color)}:0: {colored_text(match, 'red', args.no_color)}")
            print(separator)
        if args.warn_only:
            sys.exit(0)
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    main()