class Error(Exception):
    """Base Class for other exceptions"""
    pass

class InvalidLogin(Error):
    """Raised when there is an invalid login attempt"""
    pass

class TooManyBadAttempts(Error):
    """Raised when there have been too many bad login attempts"""
    pass

class ServerError(Error):
    """"Raised when ServerError is returned"""
    pass
