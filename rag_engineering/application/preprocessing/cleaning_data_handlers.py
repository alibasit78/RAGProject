from abc import ABC, abstractmethod
from rag_engineering.domain.cleaned_documents import CleanedArticleDocument
from .operations import clean_text


class CleaningDataHandler(ABC):
    @abstractmethod
    def clean(self, data_model):
        pass

class ArticleCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(valid_data)), platform=data_model.platform, author_full_name=data_model.author_full_name, author_id=data_model.author_id, link=data_model.link)

class PostCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(valid_data)), platform=data_model.platform, author_full_name=data_model.author_full_name, author_id=data_model.author_id, link=data_model.link)

class RepositoryCleaningHandler(CleaningDataHandler):
    def clean(self, data_model):
        valid_data = [content for content in data_model.content.values() if content]
        return CleanedArticleDocument(id=data_model.id, content=clean_text(" #### ".join(valid_data)), platform=data_model.platform, author_full_name=data_model.author_full_name, author_id=data_model.author_id, link=data_model.link)

    