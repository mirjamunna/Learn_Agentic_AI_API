# Conditionals
def check_document_type(filename):
    if filename.endswith('.pdf'):
        return "PDF Document"
    elif filename.endswith('.docx'):
        return "Word Document"
    elif filename.endswith('.xlsx'):
        return "Excel Document"
    elif filename.endswith('.txt'):
        return "Text Document"
    else:
        return "Unknown Document Type"
    
# Loops
documents = ["report.pdf", "presentation.pptx", "invoice.xlsx", "notes.txt", "data.docx"]

for doc in documents:
    processor = check_document_type(doc)
    print(f"Processing {doc}: {processor}")

# List comprehensions
pdf_files = [doc for doc in documents if doc.endswith('.pdf')]
print("PDF Files:", pdf_files)

# While loops
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    filename = input("Enter a document filename: ")
    if check_document_type(filename) != "Unknown Document Type":
        print(f"Processing {filename}...")
        break
    else:
        print("Invalid document type. Please try again.")
        attempts += 1

