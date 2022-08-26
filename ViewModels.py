from ObservableObjects import *
from DataModels import *
from varname import *


class ViewModel(ObservableObject):
    """
    Class for storing various data models and preparing data, which comes from them, for the visualization.
    Visualization data is exposed via class properties - kind of python feature similar to C#.
    Class inherits from 'ObservableObject' to be able to trigger events about its attributes' values changes.
    """
    def __init__(self):
        # For larger applications, data models can be stored e.g. in lists or dictionaries to switch between them
        # during application execution
        self.data_models = []
        # For presentation purposes there will be only one data model object stored
        self.current_model: DataModel = DataModel()

        # Register property that needs to be in sync with particular PyQt5 GUI objects - to allow these objects
        # to subscribe to this property. Registration is done by 'Utilities.PropertyChangedEventHandler' static class.
        # Property itself is defined below - along with getter and setter method.
        self.registerProperty(nameof(self.presented_data))

    # Define property to interact with 'x' property from current selected data model object (getter and setter
    # functions, docs string etc...)
    def get_model_x(self):
        if self.current_model:
            return self.current_model.x
        else:
            return ''

    def set_model_x(self, value):
        self.current_model.x = value
        # Since the 'presented_data' property (defined below) consists of i.e. this property and has to be in sync
        # with PyQt5 GUI object, trigger property changed event for 'presented_data' every time this setter is used.
        self.publishPropertyChanges(nameof(self.presented_data))

    model_x = property(get_model_x, set_model_x, None, 'Variable to interact with datamodel values')

    # Define another property to interact with 'y' property of current selected data model object
    def get_model_y(self):
        if self.current_model:
            return self.current_model.y
        else:
            return ''

    def set_model_y(self, value):
        self.current_model.y = value
        # Since the 'presented_data' property (defined below) consists of i.e. this property and has to be in sync
        # with PyQt5 GUI object, trigger property changed event for 'presented_data' every time this setter is used.
        self.publishPropertyChanges(nameof(self.presented_data))

    model_y = property(get_model_y, set_model_y, None, 'Variable to interact with datamodel values')

    # Define a property to provide data to visualization objects - in this case it consists of data from another
    # two properties. Notice that this is the same property as the one registered to the PropertyChangedEventHandler in
    # the class constructor.
    def get_presented_data(self):
        return self.model_x + ' ' + self.model_y

    def set_presented_data(self, value):
        raise Exception('Variable _presented_data cannot be set. It is read only!')

    presented_data = property(get_presented_data, set_presented_data, None, 'Data to be presented on the screen')

