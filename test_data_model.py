from rag_engineering.domain.documents import ArticleDocument, PostDocument


if __name__ == '__main__':
    # dir_name = r'C:\Users\DELL\Downloads\projects\MyAssistant\RAGProject\data\domain'
    # article_document = ArticleDocument(id = 1, author_id = 1, content = {"content":"content 123"}, platform = "medium", author_full_name = "author 1", link = r"https:\\medium.com\1")
    # article_document = ArticleDocument(content = {"content":"content 123"}, platform = "medium", author_full_name = "author 1", link = r"https:\\medium.com\1")
    # article_document.save(dir_name=dir_name)
    
    #####################################333
    # article_document = ArticleDocument.get_object_(id_ = "d987a85f-b768-45a8-95f2-327b915e78c2", platform = "medium")
    # print(article_document, type(article_document))
    # user_document = ArticleDocument.get_object_(id_ = "7aef6759-6c5d-4cd6-b663-43a00b57bee9", platform = "user")
    # print(user_document, type(user_document))
    ##########################
    post_document = PostDocument.get_object_(id_ = "58e29c13-0399-4584-bc32-be5dee89b68e", platform = "linkedin")
    print(post_document, type(post_document))
    # user_document = ArticleDocument.get_object_(id_ = "7aef6759-6c5d-4cd6-b663-43a00b57bee9", platform = "user")
    # print(user_document, type(user_document))