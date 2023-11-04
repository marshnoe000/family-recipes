class DatabaseError(Exception):
    def __init__(self, msg: str):
        # TODO hmm dont like this
        # might just keep the full error msgs
        if "UNIQUE constraint failed" in msg:
            msg = msg[msg.find("UNIQUE"):].lower()

        super().__init__(msg)
