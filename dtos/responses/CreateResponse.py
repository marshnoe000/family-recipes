class CreateResponse(dict):
    def __init__(self, status: int, id: int):
        super().__init__(
            status=status,
            id=id
        )

    def __getattr__(self, attr: str):
        return self[attr]
