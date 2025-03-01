from steps.etl import crawl_links, get_or_create_user   

def data_etl(user_full_name: str, links: list[str]) -> str:
    user = get_or_create_user(user_full_name)
    print(user)
    last_step = crawl_links(user=user, links = links)
    # return last_step  

if __name__ == "__main__":
    links = ["https://linkedin.com/AI-Trends-2025", "https://medium.com/Understanding-Large-Language-Models", "https://github.com/Financial-Market-Analysis-Tool"]
    data_etl(user_full_name='vivek kumar gupta', links = links)