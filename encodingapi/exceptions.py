class RateLimitException(BaseException):
    pass


class ResponseErrorException(Exception):
    def __init__(self, message):
        super().__init__(message)
