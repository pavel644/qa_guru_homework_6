from zipfile import ZipFile
import os
import csv

resources_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
temp_files_dir = os.path.join(resources_dir, 'sample_files')

with ZipFile(os.path.join(resources_dir, "sample.zip"), "w") as myzip:
    for file in os.listdir(temp_files_dir):
        myzip.write(os.path.join(temp_files_dir, file), file)

def test_csv_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_csv.csv' in myzip.namelist()

def test_csv_file_valid():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        with open(myzip.extract('sample_csv.csv')) as csv_file:
            csv_file = csv.reader('sample_csv.csv')
            assert 'laura@example.com' in str(list(csv_file)[1])
    os.remove('sample_csv.csv')


def test_xlsx_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_xlsx.xlsx' in myzip.namelist()


def test_xlsx_file_valid():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        with open(myzip.extract('sample_xlsx.xlsx')) as xlsx_file:



def test_pdf_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_pdf.pdf' in myzip.namelist()
