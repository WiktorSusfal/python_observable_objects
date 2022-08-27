class DataModel:
    """
    Class containing raw data unprepared for visualization
    """

    @property
    def x(self):
        return self._x

    def __init__(self):
        super().__init__()
        # Portions of data - "private" attributes
        self._x = 'X - Waiting for data  '
        self._y = 'Y - Waiting for data'

    # Define a property (similar to C# feature) for interacting with '_x' "private" attribute. Define getter and setter
    # method (to provide value outside and accepts values from outside) and declare property.
    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    x = property(getx, setx, None, "I'm the 'x' property - providing raw data")

    # Define a property for another "private" attribute in exact the same way
    def gety(self):
        return self._y

    def sety(self, value):
        self._y = value

    y = property(gety, sety, None, "I'm the 'y' property - providing raw data")

    # There can be also another methods for e.g. accessing and loading data into private attributes, validating data...
    # In case there will be need to keep track of this class' attributes' changes, this class must also inherit from
    # 'ObservableObjects.ObservableObject' class and trigger property changed events every time the attribute's
    # value changes
