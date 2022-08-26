class DataModel:
    def __init__(self):
        super().__init__()
        self._x = 'x'
        self._y = 'y'

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    x = property(getx, setx, None, "I'm the 'x' property.")

    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    y = property(gety, sety, None, "I'm the 'y' property.")
