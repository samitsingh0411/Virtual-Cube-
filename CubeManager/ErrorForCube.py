class InvalidMove(Exception):
    """
    This error is raised when we enter a move that is not valid.
    """
    pass

class UnrecoganizedName(Exception):
    """
    The alg name that you entered isn't recoganized. We support all PLLs using their common names and and OLLs
    using their common names and numbers. 
    """
    pass  

class InvalidInput(Exception):
    """
    This error is raised whenever you enter inputs to a function that you are not supposed to.
    """
    pass


class PathNotFound(Exception):
    """
    This error is raised when the path to the load file or the custom path for the save file is not found. 
    """
