import os

# Get the current working directory
folder_path = os.getcwd()

# Get a list of all PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

# Sort the files to ensure they are renamed in order
pdf_files.sort()

# Rename each PDF file
for index, pdf_file in enumerate(pdf_files, start=1):
    new_filename = f'file{index:02d}.pdf'
    old_file_path = os.path.join(folder_path, pdf_file)
    new_file_path = os.path.join(folder_path, new_filename)
    os.rename(old_file_path, new_file_path)
    print(f'Renamed {pdf_file} to {new_filename}')
