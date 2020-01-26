class InvalidInput(Exception):

    def __init__(self):
        message = "Input is not valid"
        super().__init__(message)

class InvalidPlaylists(Exception):

    def __init__(self):
        message = "Playlists is not valid"
        super().__init__(message)