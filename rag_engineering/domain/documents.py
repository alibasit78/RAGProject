from abc import ABC
from rag_engineering.domain.base import NoSQLBaseDocument
from typing import Optional
from pydantic import Field, UUID4
import uuid

class UserDocument(NoSQLBaseDocument):
    first_name: str
    last_name: str
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Document(NoSQLBaseDocument, ABC):
    content: dict
    platform: str
    # author_id: UUID4 = Field(alias="author_id", default_factory=uuid.uuid4)
    author_full_name: str

class ArticleDocument(Document):
    link: str
    
class PostDocument(Document):
    link: str | None = None
    image: Optional[str] = None

class RepositoryDocument(Document):
    link: str | None = None
    name: str