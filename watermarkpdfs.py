import PyPDF2
import time
from tqdm import tqdm

template = PyPDF2.PdfFileReader(open('dummypdf.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('png2pdf.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

    # Initial call to print 0% progress
    for i in tqdm(range(100)):
        time.sleep(0.005)
print("All PDF's are watermarked")
