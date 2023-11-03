class ErrorResponse(dict):
    def __init__(self, err: Exception):
        error = type(err).__name__
        status = None
        match error:
            case "DatabaseError":
                status = 500
            case "BadRequestError":
                status = 400
            case _:
                status = 500

        super().__init__(
            status=status,
            error=error,
            message=err.__str__()
        )
