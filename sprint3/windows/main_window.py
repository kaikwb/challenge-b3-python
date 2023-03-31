from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from sprint3.windows.text_window import TextWindow
from .base_ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.textCreateButton.clicked.connect(self.__open_text_window)
        self.ui.textEditButton.clicked.connect(self.__open_text_update_window)
        self.ui.textDeleteButton.clicked.connect(self.__open_text_delete_window)

        self.__text_window = TextWindow("http://localhost:3000", endpoint="/texts", parent=self)

    @Slot()
    def __open_text_window(self):
        self.__text_window.open_create_window()

    @Slot()
    def __open_text_update_window(self):
        self.__text_window.open_select_window()

    @Slot()
    def __open_text_delete_window(self):
        self.__text_window.open_select_window(delete_obj=True)
