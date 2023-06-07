class Document:
    def convertToPlainText(self):
        raise NotImplementedError("Method convertToPlainText() must be implemented.")

class PDFDocument(Document):
    def convertToPlainText(self):
        # Conversion logic for PDF document
        return "Plain text representation of PDF document"

class DOCXDocument(Document):
    def convertToPlainText(self):
        # Conversion logic for DOCX document
        return "Plain text representation of DOCX document"

class TXTDocument(Document):
    def convertToPlainText(self):
        # Conversion logic for TXT document
        return "Plain text representation of TXT document"

class DocumentFactory:
    def createDocument(self, filePath):
        # Perform format detection based on file extension or other logic
        if filePath.endswith(".pdf"):
            return PDFDocument()
        elif filePath.endswith(".docx"):
            return DOCXDocument()
        elif filePath.endswith(".txt"):
            return TXTDocument()
        else:
            raise ValueError("Unsupported file format")

filePath = "example.pdf"

factory = DocumentFactory()
document = factory.createDocument(filePath)

plainText = document.convertToPlainText()
print(plainText)

'''
In Python, we don't have the concept of explicit interfaces like in Java. Instead, we define the base class `Document` 
with a `convertToPlainText()` method that raises a `NotImplementedError`. This acts as a placeholder that must be 
implemented by the subclasses. (This is similar to JavaScript as well)

The subclasses `PDFDocument`, `DOCXDocument`, and `TXTDocument` inherit from the `Document` base class and provide 
their own implementations of the `convertToPlainText()` method.

The `DocumentFactory` class remains the same, creating the appropriate document object based on the file extension. 
We then use this object to call the `convertToPlainText()` method and print the result.

Note that in Python, there's no need to explicitly declare the variable types or handle access modifiers like 
`public`.
'''
