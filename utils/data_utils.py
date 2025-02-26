import os
from data.sample_data import authors
import pickle

def save_pickle(model, file_path: str):
    with open(file_path, "wb") as fw:
        pickle.dump(model, fw)

def load_pickle(file_path):
    with open(file_path, "rb") as fr:
        return pickle.load(fr)

def get_links(sample_dataset):
    links = []
    for domain in sample_dataset:
        for dataset_topic in sample_dataset[domain]:
            links.append(("-".join(dataset_topic.split(" ")), domain))
    link_str = ""
    for link, domain in links:
        link_str += f"    - https://{domain.lower()}.com/"+link +"\n"
    return link_str

def create_yaml_file(filepath, user_filename, sample_dataset):
    with open(filepath, "w") as f:
        links = get_links(sample_dataset)
        f.write("parameters:\n")
        f.write(f"  user_file_name: {user_filename}\n".format(user_filename=user_filename))
        f.write(f"  links:\n")
        f.write(f"""{links}""".format(links=links, user_filename = user_filename))

if __name__ == "__main__":
    output_dir = r"configs"
    output_fn = "data_etl.yaml"
    for i, author in enumerate(authors):
        author_output_fn =  output_fn.replace(".yaml", "_"+author+"_"+str(i+1)+".yaml")
        create_yaml_file(os.path.join(output_dir, author_output_fn), author, authors[author])
    