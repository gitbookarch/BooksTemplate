#pip install pdf2image
#pip install  unidecode
import os
import tempfile
from pdf2image import convert_from_path
from unidecode import unidecode

def remove_accents(accented_string):
    unaccented_string = unidecode(accented_string)
    return unaccented_string

def pdf_to_png(pdf_name):
    with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(pdf_path=f'books/{pdf_name}',
            output_folder='covers',
            fmt="png",
            size=(337, None),
            output_file=remove_accents(pdf_name[:-4]),
            single_file=True,
            poppler_path=poppler_path)
            #if you are running on windows add this parameter.
            #poppler_path = r"C:\path\to\poppler-xx\bin"
            #Poppler download:
            #https://github.com/oschwartz10612/poppler-windows/releases/

#unzip poppler
import zipfile
with zipfile.ZipFile('scripts/poppler.zip', 'r') as zip_ref:
    zip_ref.extractall('scripts')
poppler_path = r'' + os.getcwd()+'/scripts/poppler-20.11.0/bin'

#mkdir covers folder
os.makedirs('covers', exist_ok=True)

#make png 
for filename in os.listdir('books'):
    if filename.endswith(".pdf"):
        pdf_to_png(filename)

#remove popple folder
import shutil
shutil.rmtree('scripts/poppler-20.11.0')

output_msg='''
#######################################
####### Successfully completed! #######
#######################################
'''
print(output_msg)