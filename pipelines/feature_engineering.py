from steps import feature_engineering as fe_steps
def feature_engineering(author_full_names: list[str]):
    """
    _description: 
    step0: get the author full names,
    step1: query_datawarehouse, 
    step2: clean_data,
    step3: store cleaned data to vector database,
    step4: chunk and embedd the cleaned data,
    step5: store the embedded data to vector database,
    Args:
        author_full_names (list[str]): _description_
    """
    documents = fe_steps.query_data_warehouse(author_full_names)
    
    
if __name__ == "__main__":
    feature_engineering(author_full_names=['author 1', 'author 2'])