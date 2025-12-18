from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    """
    Loads a PDF file and converts it into LangChain documents.
    """
    loader = PyPDFLoader(pdf_path)
    return loader.load()

