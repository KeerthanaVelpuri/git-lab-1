import os
import shutil

reports_folder = "reports"

if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print(f"Created folder: {reports_folder}")
else:
    print(f"Folder already exists: {reports_folder}")


txt_files = [file for file in os.listdir() if file.endswith(".txt") and os.path.isfile(file)]


for file in txt_files:
    print(f"Moving file: {file}")
    shutil.move(file, os.path.join(reports_folder, file))

print("All .txt files moved to 'reports' folder.")