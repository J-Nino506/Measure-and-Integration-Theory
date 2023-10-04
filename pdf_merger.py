import os
from PyPDF2 import PdfMerger

print("Running pdf_merge.py...")

# Set the path to the "lectures" folder
root_dir = os.getcwd()
lecture_dir = os.path.join(root_dir, "lectures")

# Create a PdfFileMerger object
merger = PdfMerger()

# Loop through each subfolder and add its PDF files to the merger
for week_folder in sorted(os.listdir(lecture_dir)):
    week_path = os.path.join(lecture_dir, week_folder)
    if os.path.isdir(week_path):
        for file in sorted(os.listdir(week_path)):
            if file.endswith(".pdf"):
                pdf_path = os.path.join(week_path, file)
                merger.append(open(pdf_path, "rb"))

# Save the merged PDF file to a new file
merged_path = os.path.join(lecture_dir, "lecture-notes-merged.pdf")
with open(merged_path, "wb") as merged_file:
    merger.write(merged_file)

# Set the path to the "homeworks" folder
homework_dir = os.path.join(root_dir, "homeworks")

# Create a PdfFileMerger object
merger = PdfMerger()

# Loop through each subfolder and add its PDF files to the merger
for week_folder in sorted(os.listdir(homework_dir)):
    week_path = os.path.join(homework_dir, week_folder)
    if os.path.isdir(week_path):
        for pdf_file in sorted(os.listdir(week_path)):
            if pdf_file.endswith(".pdf") and pdf_file.startswith("homework"):
                pdf_path = os.path.join(week_path, pdf_file)
                merger.append(open(pdf_path, "rb"))

# Save the merged PDF file to a new file
merged_path = os.path.join(homework_dir, "homework-problems-merged.pdf")
with open(merged_path, "wb") as merged_file:
    merger.write(merged_file)

