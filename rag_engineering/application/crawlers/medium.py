from rag_engineering.domain.documents import ArticleDocument, UserDocument
from .base import BaseSeleniumCrawler
from loguru import logger
from data.sample_data import sample_dataset1, sample_dataset2

class MediumCrawler(BaseSeleniumCrawler):
    model = ArticleDocument
    def extract(self, link, **kwargs) -> None:
        logger.info(f"Extracting content from {link}")
        topic = link.split("/")[-1].replace("-", " ")
        content = ""
        for sample_dataset in [sample_dataset1, sample_dataset2]:
            if topic in sample_dataset['Medium']:
                content = sample_dataset['Medium'][topic]
                break
        # print("topic: ", topic)
        # print("content: ", content)
        self.scroll_page()
        user = kwargs["user"]
        instance = self.model(
            content={"content": content},
            name=topic,
            link=link,
            platform="medium",
            author_id=user.id,
            author_full_name=user.full_name,
        )
        self.model.save(instance)
        self.scroll_page()        
        logger.info(f"Completed scrolling medium page!")
        
if __name__ == "__main__":
    medium_crawler = MediumCrawler()
    user_document = UserDocument(first_name="author", last_name = "1")
    medium_crawler.extract(link=r"https://medium.com/Understanding-Large-Language-Models", user = user_document)
    print(medium_crawler)