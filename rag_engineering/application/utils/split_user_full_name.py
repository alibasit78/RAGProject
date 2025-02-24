from rag_engineering.domain.exceptions import IncorrectConfigured

def split_user_full_name(user_full_name: str):
    if user_full_name is None:
        raise IncorrectConfigured("User full name is empty")
    tokens = user_full_name.split(" ")
    if len(tokens) == 1:
        first_name, last_name = tokens[0], tokens[0]
    elif len(tokens) == 0:
        raise IncorrectConfigured("User name is empty")
    else:
        first_name, last_name = " ".join(tokens[:-1]), tokens[-1]
    return first_name, last_name