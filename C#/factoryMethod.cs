using System;

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


// to implement that interface. It establishes a contract or an agreement for classes to adhere to.

interface Document
{
    string ConvertToPlainText();
}

class PDFDocument : Document
{
    public string ConvertToPlainText()
    {
        // Conversion logic for PDF document
        return "Plain text representation of PDF document";
    }
}

class DOCXDocument : Document
{
    public string ConvertToPlainText()
    {
        // Conversion logic for DOCX document
        return "Plain text representation of DOCX document";
    }
}

class TXTDocument : Document
{
    public string ConvertToPlainText()
    {
        // Conversion logic for TXT document
        return "Plain text representation of TXT document";
    }
}

class DocumentFactory
{
    public Document CreateDocument(string filePath)
    {
        // Perform format detection based on file extension or other logic
        if (filePath.EndsWith(".pdf"))
        {
            return new PDFDocument();
        }
        else if (filePath.EndsWith(".docx"))
        {
            return new DOCXDocument();
        }
        else if (filePath.EndsWith(".txt"))
        {
            return new TXTDocument();
        }
        else
        {
            throw new ArgumentException("Unsupported file format");
        }
    }
}

public class MainClass
{
    public static void Main(string[] args)
    {
        string filePath = "example.pdf";

        DocumentFactory factory = new DocumentFactory();
        Document document = factory.CreateDocument(filePath);

        string plainText = document.ConvertToPlainText();
        Console.WriteLine(plainText);
    }
}


/* 
In C#, we use the interface keyword to define an interface, and the class keyword to define classes. 
The methods in the interface and classes are defined using the public access modifier by default.

The DocumentFactory class remains the same, creating the appropriate document object based on the file 
extension.

In the MainClass, we create an instance of DocumentFactory, use it to create a Document object based 
on the file path, and then call the ConvertToPlainText() method on that object to obtain the plain 
text representation of the document. Finally, we use Console.WriteLine() to print the plain text 
representation to the console.

Note that in C#, we use string instead of String, and Console.WriteLine() instead of System.out.println().

*/
