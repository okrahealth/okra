""" Custom errors we can expect. 

References:
  https://docs.python.org/3/tutorial/errors.html
"""

class Error(Exception):
    """ Base class for exceptions in okra """
    pass

class NetworkError(Error):
    """ Exception raised for errors related to network requests

    :param expression: input expression in which the error occurred
    :param message: explanation of error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class MissingEnvironmentVariableError(Error):
    """ Exception raised when mandatory enviroment variable is missing.

    :param expression: input expression in which error occurred
    :param message: explanation of error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class DirectoryNotCreatedError(Error):
    """ Exception raised when directory unable to be created.

    :param expression: input expression in which error occurred
    :param message: explanation of error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


    
