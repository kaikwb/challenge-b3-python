import sys

from PySide6.QtWidgets import QApplication
from challenge.windows.main_window import MainWindow

from challenge.api.mock.mock_server import start_mock_server

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    mock_thread = start_mock_server()
    app_exit_code = app.exec()
    mock_thread.join(0.1)
    sys.exit(app_exit_code)
