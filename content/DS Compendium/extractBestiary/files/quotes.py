import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    in_block = False
    block_indent = None
    block_start = None

    for i, line in enumerate(lines):
        stripped_line = line.lstrip()
        indent_level = len(line) - len(stripped_line)

        if stripped_line.startswith('"') and not in_block:
            in_block = True
            block_indent = indent_level
            block_start = i

        if in_block and (indent_level < block_indent or i == len(lines) - 1):
            if not lines[block_start].rstrip().endswith('"'):
                lines[block_start] = lines[block_start].rstrip() + '"\n'
            in_block = False
            block_indent = None
            block_start = None

    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith('.md'):
            process_file(file_path)

# Directory containing the files
directory = '/mnt/c/Obsidian/DS Compendium/extractBestiary/'

# Process the files
process_files(directory)