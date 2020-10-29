import pyttsx3
import PyPDF2
book = open("mongodb.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
totalPages = pdfReader.numPages
print(totalPages)
speaker = pyttsx3.init()
for page in range(0,totalPages):
    requiredPage = pdfReader.getPage(page)
    text = requiredPage.extractText()
    speaker.say(text)
    speaker.runAndWait()