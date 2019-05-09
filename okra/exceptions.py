""" Custom exceptions for Okra. """

class OkraError(Exception):
    """ Base class for exceptions in Okra """
    pass

class UrlJoinError(OkraError):
    """ Exception raised for error in 'urllib.parse.urljoin'

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

