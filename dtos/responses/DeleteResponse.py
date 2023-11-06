class DeleteResponse(dict):
    def __init__(self, status: int, rowsAffected: int):
        super().__init__(
            status=status,
            rowsAffected=rowsAffected
        )
