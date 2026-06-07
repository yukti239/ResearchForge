from pypdf import PdfReader


def extract_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def get_page_count(pdf_file):

    reader = PdfReader(pdf_file)

    return len(reader.pages)


def get_word_count(text):

    return len(text.split())