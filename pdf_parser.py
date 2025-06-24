def parse_document(upload_file):
    import PyPDF2
    from io import BytesIO
    reader = PyPDF2.PdfReader(BytesIO(upload_file.file.read()))
    text = "\n".join(page.extract_text() for page in reader.pages)
    return text
