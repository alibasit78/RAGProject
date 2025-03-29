from typing_extensions import Annotated
from rag_engineering.application.preprocessing import CleaningDispatcher

def clean_documents(documents: Annotated[list, "raw_documents"]) -> Annotated[list, "cleaned_documents"]:
    cleaned_documents = []
    for document in documents:
        cleaned_document = CleaningDispatcher.dispatch(document)
        cleaned_documents.append(cleaned_document)
    return cleaned_document

if __name__ == "__main__":
    # Example usage
    documents = [
        {
            "id": 1,
            "content": {
                "title": "Sample Title",
                "body": "Sample body content",
                "footer": None
            },
            "platform": "example_platform",
            "author_full_name": "John Doe",
            "author_id": 123,
            "link": "http://example.com"
        }
    ]
    cleaned_documents = clean_documents(documents)
    print(cleaned_documents)
    