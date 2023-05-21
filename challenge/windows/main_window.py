from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow

from challenge.windows.review import ReviewWindow
from challenge.windows.text import TextWindow
from challenge.windows.videos import VideosWindow
from .base_ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.url = "http://localhost:3000"
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.textCreateButton.clicked.connect(self.__open_text_window)
        self.ui.textEditButton.clicked.connect(self.__open_text_update_window)
        self.ui.textDeleteButton.clicked.connect(self.__open_text_delete_window)

        self.ui.videoCreateButton.clicked.connect(self.__open_video_window)
        self.ui.videoEditButton.clicked.connect(self.__open_video_update_window)
        self.ui.videoDeleteButton.clicked.connect(self.__open_video_delete_window)

        self.ui.reviewCreateButton.clicked.connect(self.__open_review_window)
        self.ui.reviewEditButton.clicked.connect(self.__open_review_update_window)
        self.ui.reviewDeleteButton.clicked.connect(self.__open_review_delete_window)

        self.__text_window = TextWindow(self.url, endpoint="/texts", parent=self)
        self.__video_window = VideosWindow(self.url, endpoint="/videos", parent=self)
        self.__review_window = ReviewWindow(self.url, endpoint="/reviews", parent=self)

    @Slot()
    def __open_text_window(self):
        self.__text_window.open_create_window()

    @Slot()
    def __open_text_update_window(self):
        self.__text_window.open_select_window()

    @Slot()
    def __open_text_delete_window(self):
        self.__text_window.open_select_window(delete_obj=True)

    @Slot()
    def __open_video_window(self):
        self.__video_window.open_create_window()

    @Slot()
    def __open_video_update_window(self):
        self.__video_window.open_select_window()

    @Slot()
    def __open_video_delete_window(self):
        self.__video_window.open_select_window(delete_obj=True)

    @Slot()
    def __open_review_window(self):
        self.__review_window.open_create_window()

    @Slot()
    def __open_review_update_window(self):
        self.__review_window.open_select_window()

    @Slot()
    def __open_review_delete_window(self):
        self.__review_window.open_select_window(delete_obj=True)
