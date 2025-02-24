from abc import ABC, abstractmethod
from rag_engineering.domain.base import NoSQLBaseDocument

class BaseCrawler(ABC):
    model: type[NoSQLBaseDocument]
    @abstractmethod
    def extract(self, link: str, **kwargs):
        pass

class BaseSeleniumCrawler(BaseCrawler):
    def __init__(self, scroll_limit: int = 5):
        self.scroll_limit = scroll_limit
        
    def scroll_page(self) -> None:
        print("scrolling page")
    
    def login(self):
        pass
        