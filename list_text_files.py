import os


print("Text files in the current directory:")

txt_files = [file for file in os.listdir() if file.endswith('.txt') and os.path.isfile(file)]

for file in txt_files:
    print(file)