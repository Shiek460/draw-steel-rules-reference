import os

def split_markdown(file_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, 'r') as file:
        content = file.readlines()

    current_file = None
    current_file_name = None

    for line in content:
        if line.startswith('#'):
            # Close the current file if it's open
            if current_file:
                current_file.close()

            # Extract the name after the `#` symbol
            current_file_name = line[1:].strip().replace(" ", "_") + ".md"
            current_file_path = os.path.join(output_dir, current_file_name)

            # Open a new file for writing
            current_file = open(current_file_path, 'w')

        # Write the line to the current file
        if current_file:
            current_file.write(line)

    # Close the last file if it's open
    if current_file:
        current_file.close()

# Path to the input file
input_file_path = '/mnt/c/Obsidian/DS Compendium/extractBestiary/files/MonstersRawText1.md'

# Directory to save the output files
output_directory = '/mnt/c/Obsidian/DS Compendium/extractBestiary'

# Split the markdown file
split_markdown(input_file_path, output_directory)