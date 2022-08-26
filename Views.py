from PyQt5 import QtWidgets as qtw

import Utilities
from ViewModels import *


class MainView(qtw.QWidget, ObserverObject):

    def __init__(self, v_model: ViewModel):
        qtw.QWidget.__init__(self)

        self.view_model = v_model

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
        self.label.setFixedWidth(200)
        self.right_pane_layout.addWidget(self.label)

        self.main_layout.addLayout(self.left_pane_layout)
        self.main_layout.addLayout(self.right_pane_layout)

        self.setLayout(self.main_layout)

        self.subscribeToVariable(nameof(self.label), nameof(self.label.setText), self.view_model,
                                 nameof(self.view_model.presented_data))

        self.input_1.textChanged.connect(lambda:
                                         self.updateObjectFromAttribute(
                                             dst_obj=self.view_model,
                                             dst_property_name=nameof(self.view_model.model_x),
                                             src_property_name=nameof(self.input_1),
                                             getter_method_name=nameof(self.input_1.text)
                                         )
                                         )
        self.input_2.textChanged.connect(lambda:
                                         self.updateObjectFromAttribute(
                                             dst_obj=self.view_model,
                                             dst_property_name=nameof(self.view_model.model_y),
                                             src_property_name=nameof(self.input_2),
                                             getter_method_name=nameof(self.input_2.text)
                                         )
                                         )


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_widget = MainView(ViewModel())

        self.setWindowTitle('Dynamic GUI List Tests')
        self.setCentralWidget(self.main_widget)
        self.setFixedSize(600, 480)

        Utilities.PropertyChangedEventHandler.updateAllBindings()

        self.show()


if __name__ == '__main__':
    # invoke the application
    app = qtw.QApplication([])
    app_main_gui = MainWindow()
    app.exec_()
