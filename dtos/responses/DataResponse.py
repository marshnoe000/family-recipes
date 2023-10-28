class DataResponse(dict):
    def __init__(self, status: int, data: dict):
        super().__init__(
            status=status,
            data=data
        )
