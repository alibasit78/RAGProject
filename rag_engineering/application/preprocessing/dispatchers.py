from rag_engineering.domain.base import NoSQLBaseDocument
from rag_engineering.domain.types import DataCategory
from loguru import logger
from rag_engineering.application.preprocessing.cleaning_data_handlers import ArticleCleaningHandler, PostCleaningHandler, RepositoryCleaningHandler
# from rag_engineering.application.preprocessing import ArticleCleaningHandler, PostCleaningHandler, RepositoryCleaningHandler
class CleaningHandlerFactory:
    @staticmethod
    def create_cleaning_handler(data_category: str):
        if data_category == DataCategory.ARTICLES:
            return ArticleCleaningHandler()
        elif data_category == DataCategory.POSTS:
            return PostCleaningHandler()
        elif data_category == DataCategory.REPOSITORIES:
            return RepositoryCleaningHandler()
        else:
            raise ValueError(f"Invalid data category: {data_category}")
    

class CleaningDispatcher:
    factory = CleaningHandlerFactory()
    @classmethod
    def dispatch(cls, data_model: NoSQLBaseDocument):
        data_category = DataCategory(data_model.get_collection_name())
        handler = cls.factory.create_cleaning_handler(data_category)
        cleaned_data = handler.clean(data_model)
        logger.info(f"Cleaned data: {cleaned_data}", data_category=data_category, cleaned_content_len = len(cleaned_data.content))
        return cleaned_data