from .base import BaseSeleniumCrawler
from loguru import logger
from data.sample_data import sample_dataset1, sample_dataset2
from rag_engineering.domain.documents import PostDocument, UserDocument

class LinkedinCrawler(BaseSeleniumCrawler):
    model = PostDocument
    def extract(self, link, **kwargs) -> None:
        logger.info(f"Extracting content from {link}")
        topic = link.split("/")[-1].replace("-", " ")
        content = ""
        for sample_dataset in [sample_dataset1, sample_dataset2]:
            if topic in sample_dataset['LinkedIn']:
                content = sample_dataset['LinkedIn'][topic]
                break
        print("topic: ", topic)
        print("content: ", content)
        self.scroll_page()
        user = kwargs["user"]
        instance = self.model(
            content={"content": content},
            name=topic,
            link=link,
            platform="linkedin",
            author_id=user.id,
            author_full_name=user.full_name,
        )
        self.model.save(instance)
        logger.info(f"Completed the linkedin crawler!")


if __name__ == "__main__":
    linkedin_crawler = LinkedinCrawler()
    user_document = UserDocument(first_name="author", last_name = "1")
    linkedin_crawler.extract(link=r"https://linkedin.com/Remote-Work-Productivity", user = user_document)
    print(linkedin_crawler)