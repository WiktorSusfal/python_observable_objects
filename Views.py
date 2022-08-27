from PyQt5 import QtWidgets as qtw
from ViewModels import *
import Utilities


class MainView(qtw.QWidget, ObserverObject):
    """
    Class representing main view of simple PyQt5 GUI application. Stores GUI objects like QLineEdits and QLabels.
    The main purpose of this class is to present the solution to in-background values propagation from plain variables
    to PyQt5 objects (e.g. QLabels), every time the plain variable changes.
    View consists of two QLineEdits that update 'model_x' and 'model_y' properties of assigned 'ViewModel' object -
    in real-time (using PyQt5 signal slots).
    Every time each of the above properties changes, the QLabel widget is automatically updated with 'presented_data'
    property of 'ViewModel' object - with the use of event-driven callbacks mechanism.
    Every time the setter method of 'model_x' or 'model_y' property is called, there is a property changed event
    triggered for 'presented_data' property. There is a subscription to 'presented_data' property made for QLabel object
    - in the constructor of 'MainView' class, so the value can be synchronized automatically
    """

    def __init__(self, v_model: ViewModel):
        qtw.QWidget.__init__(self)

        # Assign view model to the view
        self.view_model = v_model

        # Build the main layout of the view class - add QLineEdits and QLabel
        self.main_layout = qtw.QHBoxLayout()

        self.left_pane_layout = qtw.QVBoxLayout()
        self.input_1 = qtw.QLineEdit()
        self.input_1.setFixedWidth(200)
        self.input_2 = qtw.QLineEdit()
        self.input_2.setFixedWidth(200)
        self.left_pane_layout.addWidget(self.input_1)
        self.left_pane_layout.addWidget(self.input_2)

        self.right_pane_layout = qtw.QVBoxLayout()
        self.label = qtw.QLabel()
        self.label.setFixedWidth(300)
        self.right_pane_layout.addWidget(self.label)

        self.main_layout.addLayout(self.left_pane_layout)
        self.main_layout.addLayout(self.right_pane_layout)
        # Set the layout of the Main View class as the one created above
        self.setLayout(self.main_layout)

        self.createSubscriptionToVariables()
        self.createBindingsToVariables()

    def createSubscriptionToVariables(self):
        """
        Function to group all the statements aimed to create subscriptions to particular attributes.
        :return: None
        """

        # Create subscription to 'view_model.presented_data' property from the QLabel object.
        # The setter method for assigning received values to QLabel ('setText') is a property of the QLabel itself,
        # so need to pass both: dst_property_name and setter_method_name.
        # Source object is 'view_model', source property - 'presented_data', and getter method is default - 'getattr'.
        self.subscribeToVariable(dst_property_name=nameof(self.label), setter_method_name=nameof(self.label.setText),
                                 src_obj=self.view_model, src_property_name=nameof(self.view_model.presented_data),
                                 getter_method_name=None)

    def createBindingsToVariables(self):
        """
        Function to group all the statements aimed to create bindings FROM PyQt5 GUI elements TO plain variables -
        using signal slots. Thanks to inheriting from 'ObserverObject', there can be one consistent method used to
        propagate new values to destinations ('updateObjectFromAttribute').
        :return: None
        """

        # Destination object - view_model
        # dst_property_name - 'model_x'
        # setter_method_name = None, so the default 'setattr' function is used to set the value for destination property
        # Name of this class' property that is a source - 'input_1' (QLineEdit object)
        # Value getter method (from source) - 'text'
        self.input_1.textChanged.connect(lambda:
                                         self.updateObjectFromAttribute(
                                             dst_obj=self.view_model,
                                             dst_property_name=nameof(self.view_model.model_x),
                                             setter_method_name=None,
                                             src_property_name=nameof(self.input_1),
                                             getter_method_name=nameof(self.input_1.text)
                                         )
                                         )

        # Do exactly the same for 'input_2' QLineEdit and 'model_y' property of 'view_model'
        self.input_2.textChanged.connect(lambda:
                                         self.updateObjectFromAttribute(
                                             dst_obj=self.view_model,
                                             dst_property_name=nameof(self.view_model.model_y),
                                             src_property_name=nameof(self.input_2),
                                             getter_method_name=nameof(self.input_2.text)
                                         )
                                         )


class MainWindow(qtw.QMainWindow):
    """
    Class representing main window - for presentation purposes
    """
    def __init__(self):
        super().__init__()

        # Assign the main widget of the window - created 'ViewModel' class instance
        self.main_widget = MainView(ViewModel())

        self.setWindowTitle('In-Background Values Synchronization Tests')
        self.setCentralWidget(self.main_widget)
        self.setFixedSize(500, 150)

        # If you want to have all subscriptions updated BEFORE application starts, you need to invoke following method
        # on the PropertyChangedEventHandler static class.
        Utilities.PropertyChangedEventHandler.updateAllBindings()

        self.show()


if __name__ == '__main__':
    # invoke the application
    app = qtw.QApplication([])
    app_main_gui = MainWindow()
    app.exec_()
