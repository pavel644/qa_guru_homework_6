import openpyxl, csv, os
from zipfile import ZipFile
from PyPDF2 import PdfReader

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
            csv_file = csv.reader(csv_file)
            assert 'laura@example.com' in list(csv_file)[1][0]
    os.remove('sample_csv.csv')


def test_xlsx_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_xlsx.xlsx' in myzip.namelist()


def test_xlsx_file_valid():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        myzip.extract('sample_xlsx.xlsx')
        workbook = openpyxl.load_workbook('sample_xlsx.xlsx')
        sheet = workbook.active
        assert sheet.cell(row=4, column=6).value == 'JVF78YQU6HH'
        os.remove('sample_xlsx.xlsx')


def test_pdf_file_exist_in_archive():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        assert 'sample_pdf.pdf' in myzip.namelist()


def test_pdf_file_valid():
    with ZipFile(os.path.join(resources_dir, "sample.zip"), "r") as myzip:
        myzip.extract('sample_pdf.pdf')
        reader = PdfReader('sample_pdf.pdf')
        page_text = reader.pages[0].extract_text()
        assert 'ТестёжзфЩ' in page_text
        os.remove('sample_pdf.pdf')

os.remove('archive_test.py')