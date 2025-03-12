import os
import re

def extract_tags(lines):
    ancestry_tags = []
    roles_tags = []
    in_ancestry = False
    in_roles = False

    for line in lines:
        if line.strip().startswith('ancestry:'):
            in_ancestry = True
            in_roles = False
        elif line.strip().startswith('roles:'):
            in_roles = True
            in_ancestry = False
        elif line.strip().startswith('- '):
            if in_ancestry:
                ancestry_tags.append(line.strip()[2:].strip('"'))
            elif in_roles:
                roles_tags.append(line.strip()[2:].strip('"'))
        elif line.strip() == '':
            in_ancestry = False
            in_roles = False

    return ancestry_tags, roles_tags

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    ancestry_tags, roles_tags = extract_tags(lines)
    tags = set(ancestry_tags + roles_tags)
    tag_lines = [f'#{tag}\n' for tag in tags]

    with open(file_path, 'w') as file:
        file.writelines(tag_lines + ['\n'] + lines)

def process_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and file_path.endswith('.md'):
            process_file(file_path)

# Directory containing the files
directory = '/mnt/c/Obsidian/DS Compendium/extractBestiary'

# Process the files
process_files(directory)