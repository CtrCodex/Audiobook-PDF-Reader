import pyttsx3
import PyPDF2

book = open('your_sample.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()  
