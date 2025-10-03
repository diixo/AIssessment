
import PyPDF2

# Открываем PDF
with open("datasets/PMBoK-v6.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

print(text)

