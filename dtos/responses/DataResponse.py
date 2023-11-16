class DataResponse(dict):
    def __init__(self, status: int, data: dict):
        super().__init__(
            status=status,
            data=data
        )

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value
