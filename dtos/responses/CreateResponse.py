class CreateResponse(dict):
    def __init__(self, status: int, id: int = None):
        if id is None:
            super().__init__(
                status=status,
            )
        else:
            super().__init__(
                status=status,
                id=id
            )

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value
