import os

def process_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            # Find the first empty line
            for i, line in enumerate(lines):
                if line.strip() == '':
                    lines[i] = '```statblock\n'
                    break
            
            # Ensure the last line is ```
            if lines[-1].strip() != '```':
                lines.append('```\n')
            else:
                lines[-1] = '```\n'
            
            # Write the changes back to the file
            with open(file_path, 'w') as file:
                file.writelines(lines)

# Directory containing the files
directory = '/mnt/c/Obsidian/DS Compendium/extractBestiary'

# Process the files
process_files(directory)