using System;

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
