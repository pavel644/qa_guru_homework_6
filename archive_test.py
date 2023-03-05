from zipfile import ZipFile
import os

resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
temp_files_dir = os.path.join(resources_dir, 'sample_files')

with ZipFile(os.path.join(resources_dir, "sample.zip"), "w") as myzip:
    for file in os.listdir(temp_files_dir):
        myzip.write(os.path.join(temp_files_dir, file), file)

def test_csv_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_csv.csv' in myzip.namelist()


def test_pdf_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_xlsx.xlsx' in myzip.namelist()

def test_pdf_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_pdf.pdf' in myzip.namelist()
