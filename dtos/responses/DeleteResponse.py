class DeleteResponse(dict):
    def __init__(self, status: int, rowsAffected: int):
        super().__init__(
            status=status,
            rowsAffected=rowsAffected
        )

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value
