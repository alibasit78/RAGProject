from typing_extensions import Annotated
from rag_engineering.application.preprocessing import CleaningDispatcher

def clean_documents(documents: Annotated[list, "raw_documents"]) -> Annotated[list, "cleaned_documents"]:
    cleaned_documents = []
    for document in documents:
        cleaned_document = CleaningDispatcher.dispatch(document)
        cleaned_documents.append(cleaned_document)
    return cleaned_document
    