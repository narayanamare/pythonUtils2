from pdf2image import convert_from_path

pdf_path = r"C:\poppler\poppler-25.07.0\Global_Risks_Report.pdf"
poppler_path = r"C:\poppler\poppler-25.07.0\Library\bin"

pages = convert_from_path(pdf_path, dpi=300, poppler_path=poppler_path)

for i, page in enumerate(pages):
    image_path = f"page_{i+1}.jpg"
    page.save(image_path, "JPEG")
    print(f"Saved: {image_path}")
