class ErrorResponse(dict):
    def __init__(self, err):
        if isinstance(err, Exception):
            error = type(err).__name__
            status = None
            message = err.__str__()
            match error:
                case "DatabaseError":
                    status = 500
                case "BadRequestError":
                    status = 400
                case "InvalidLoginError":
                    status = 401
                case "NotFoundError":
                    status = 404
                case _:
                    status = 500
        # flask builtin errors, dont really want to deal with them more than this -deparr
        else:
            status = err.code
            error = err.name
            message = err.description

        super().__init__(
            status=status,
            error=error,
            message=message
        )

    def __getattr__(self, attr: str):
        return self[attr]

    def __setattr__(self, attr: str, value: any):
        self[attr] = value
