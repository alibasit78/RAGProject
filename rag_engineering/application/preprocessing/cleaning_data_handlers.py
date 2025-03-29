from abc import ABC, abstractmethod
from rag_engineering.domain.cleaned_documents import CleanedArticleDocument
from .operations.cleaning import clean_text
# from rag_engineering.application.preprocessing.operations import clean_text


class CleaningDataHandler(ABC):
    @abstractmethod
    def clean(self, data_model):
        pass

class ArticleCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(valid_data)), platform=data_model.platform, author_full_name=data_model.author_full_name, link=data_model.link)

class PostCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(valid_data)), platform=data_model.platform, author_full_name=data_model.author_full_name, link=data_model.link)

class RepositoryCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        new_content = []
        for content in valid_data:
            if isinstance(content, dict):
                new_content.extend(list(content.values()))
            else:
                new_content.append(content)
        # print(f"valid_data: {new_content}")
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(new_content)), platform=data_model.platform, author_full_name=data_model.author_full_name, link=data_model.link)

    