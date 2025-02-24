from rag_engineering.domain.documents import ArticleDocument


if __name__ == '__main__':
    dir_name = r'C:\Users\DELL\Downloads\projects\MyAssistant\MLProject\data\domain'
    # article_document = ArticleDocument(id = 1, author_id = 1, content = {"content":"content 123"}, platform = "medium", author_full_name = "author 1", link = r"https:\\medium.com\1")
    # article_document = ArticleDocument(content = {"content":"content 123"}, platform = "medium", author_full_name = "author 1", link = r"https:\\medium.com\1")
    # article_document.save(dir_name=dir_name)
    
    #####################################333
    article_document = ArticleDocument.get_object_(id_ = "d987a85f-b768-45a8-95f2-327b915e78c2", dir_name = dir_name, platform = "medium")
    print(article_document, type(article_document))