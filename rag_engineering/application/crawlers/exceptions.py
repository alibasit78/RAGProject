class NotValidUrlException(Exception):
    def __init__(self, message="The URL provided is not valid"):
        self.message = message
        super().__init__(self.message)