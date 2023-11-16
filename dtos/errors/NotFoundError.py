class NotFoundError(Exception):
    def __init__(self):
        super().__init__("Unable to find the requested resource")
