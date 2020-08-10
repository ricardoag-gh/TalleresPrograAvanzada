
class Player: # model of a player
    def __init__(self):
        self._username = ""
        self._password = ""
        self._email = ""
        self._icon = ""


    def create(self,data):
        self._username=data[0]
        self._password=data[1]

# puede apoyarse en este template o generar el propio.
