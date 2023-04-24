import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(filename):
    with open(filename, 'r') as f:
        text = f.read()

    matches = tool.check(text)
    return len(matches)

# Check the grammar of all .md files in the repository
if __name__ == '__main__':
    import os
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith('.md'):
                num_errors = check_grammar(os.path.join(root, filename))
                if num_errors > 0:
                    print(f"Grammar check failed for file: {filename}")
                    exit(1)
