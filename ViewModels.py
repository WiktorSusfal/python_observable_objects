from ObservableObjects import *
from DataModels import *
from varname import *


class ViewModel(ObservableObject):
    def __init__(self):
        self.data_models = []
        self.current_model: DataModel = DataModel()

        self.registerProperty(nameof(self.presented_data))

    def get_presented_data(self):
        return self.model_x + ' ' + self.model_y

    def set_presented_data(self, value):
        raise Exception('Variable _presented_data cannot be set. It is read only!')

    presented_data = property(get_presented_data, set_presented_data, None, 'Data to be presented on the screen')

    def get_model_x(self):
        if self.current_model:
            return self.current_model.x
        else:
            return ''

    def set_model_x(self, value):
        self.current_model.x = value
        self.publishPropertyChanges(nameof(self.presented_data))

    model_x = property(get_model_x, set_model_x, None, 'Variable to interact with datamodel values')

    def get_model_y(self):
        if self.current_model:
            return self.current_model.y
        else:
            return ''

    def set_model_y(self, value):
        self.current_model.y = value
        self.publishPropertyChanges(nameof(self.presented_data))

    model_y = property(get_model_y, set_model_y, None, 'Variable to interact with datamodel values')

