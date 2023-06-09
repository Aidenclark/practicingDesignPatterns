
/* Let's consider a real-life example of a document converter application. This application needs to convert documents 
from various formats (such as PDF, DOCX, and TXT) into a common format, such as plain text.

To implement this functionality using the Factory Method pattern, we can define an abstract class or interface called 
`Document` that represents the common interface for all documents. This class can have a method like `convertToPlainText()` 
that converts the document into plain text.

Next, we create concrete classes that implement the `Document` interface for each document format. For example, we can have 
classes like `PDFDocument`, `DOCXDocument`, and `TXTDocument`. Each of these classes would override the `convertToPlainText()` 
method to implement the specific conversion logic for that document format.

Finally, we create a `DocumentFactory` class that acts as the factory responsible for creating the appropriate `Document` objects. 
This class can have a method like `createDocument(String filePath)` that takes a file path as input and returns the corresponding 
`Document` object based on the file's format. Inside this method, we can check the file extension or perform some other format 
detection logic to determine the appropriate document type to instantiate.

Here's an example code snippet to illustrate this:
*/


// In Java, an interface is a blueprint of a class that defines a set of methods that must be implemented by any class that claims 
// to implement that interface. It establishes a contract or an agreement for classes to adhere to.
interface Document {
    String convertToPlainText();
}

// Implements is a Java keyowrd that inidcates that a class is going to implement an interface
class PDFDocument implements Document {
    public String convertToPlainText() {
        // Conversion logic for PDF document
        return "Plain text representation of PDF document";
    }
}

class DOCXDocument implements Document {
    public String convertToPlainText() {
        // Conversion logic for DOCX document
        return "Plain text representation of DOCX document";
    }
}

class TXTDocument implements Document {
    public String convertToPlainText() {
        // Conversion logic for TXT document
        return "Plain text representation of TXT document";
    }
}

class DocumentFactory {
    public Document createDocument(String filePath) {
        // Perform format detection based on file extension or other logic
        if (filePath.endsWith(".pdf")) {
            return new PDFDocument();
        } else if (filePath.endsWith(".docx")) {
            return new DOCXDocument();
        } else if (filePath.endsWith(".txt")) {
            return new TXTDocument();
        } else {
            throw new IllegalArgumentException("Unsupported file format");
        }
    }
}


///////////////////If calling in Main///////////////////

public class Main {
    public static void main(String[] args) {
        String filePath = "example.pdf"; // actual path to file you want to convert
        
        DocumentFactory factory = new DocumentFactory();
        Document document = factory.createDocument(filePath);
        
        String plainText = document.convertToPlainText();
        System.out.println(plainText);
    }
}



/*

In the above example, the `DocumentFactory` acts as the factory for creating different `Document` objects based on the file format. 
The client code can use the `DocumentFactory` to create a specific `Document` object without worrying about the details of how each 
document type is created or converted to plain text.

This way, you can easily add support for new document formats in the future by creating a new concrete class that implements the `Document` 
interface and adding the corresponding logic in the `DocumentFactory`. The client code remains unchanged, as it interacts with the `Document` 
objects through the common interface.


*/
