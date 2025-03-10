from rag_engineering.domain.base import VectorBaseDocument
from abc import ABC
from pydantic import UUID4
from rag_engineering.domain.types import DataCategory
from typing import Optional
class CleanedDocument(VectorBaseDocument, ABC):
    content: str
    platform: str
    author_full_name: str
    author_id: UUID4

class CleanedArticleDocument(CleanedDocument):
    link: str
    class Config:
        name = "cleaned_articles"
        category = DataCategory.ARTICLES
        use_vector_index = False

class CleanedPostDocument(CleanedDocument):
    link: str
    image: Optional[str]
    class Config:
        name = "cleaned_posts"
        category = DataCategory.POSTS
        use_vector_index = False

class CleanedRepositoryDocument(CleanedDocument):
    link: str
    name: str
    class Config:
        name = "cleaned_repositories"
        category = DataCategory.REPOSITORIES
        use_vector_index = False