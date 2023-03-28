from PySide6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PySide6.QtCore import Slot, Qt

from .base_ui import text_ui, select_ui

from typing import Any

from sprint3.api.api import API
from sprint3.api.exceptions import APICreateError

from collections import OrderedDict


def _fill_select_header(table_widget, ca_map: dict) -> None:
    columns = list(ca_map.keys())
    table_widget.setColumnCount(len(columns))
    table_widget.setHorizontalHeaderLabels(ca_map.keys())
    # table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)


class TextWindow(QDialog):
    def __init__(self, url_base: str, endpoint: str = "", parent: Any | None = None):
        super().__init__(parent)

        self.__delete_obj = False
        self.__url_base = url_base
        self.__endpoint = endpoint
        self.__is_update = False
        self.__obj: dict | None = None

        self.ui = text_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.accepted.connect(self.__accepted)
        self.finished.connect(self.__finished)
        self.rejected.connect(self.__rejected)

        self.__select_window = QDialog(self)
        self.__select_ui = select_ui.Ui_Dialog()
        self.__select_ui.setupUi(self.__select_window)

        self.__api = API(url_base)

    def _fill_fields(self) -> None:
        if self.__is_update:
            title = self.__obj.get("title", "")
            author = self.__obj.get("author", "")
            source = self.__obj.get("source", "")
            link = self.__obj.get("link", "")
            content = self.__obj.get("content", "")
        else:
            title = ""
            author = ""
            source = ""
            link = ""
            content = ""

        self.ui.titleEdit.setText(title)
        self.ui.authorEdit.setText(author)
        self.ui.sourceEdit.setText(source)
        self.ui.linkEdit.setText(link)
        self.ui.contentEdit.setText(content)

    def _get_object(self) -> dict:
        obj = dict()

        obj["title"] = self.ui.titleEdit.text()
        obj["author"] = self.ui.authorEdit.text()
        obj["source"] = self.ui.sourceEdit.text()
        obj["link"] = self.ui.sourceEdit.text()
        obj["content"] = self.ui.contentEdit.toPlainText()

        return obj

    def _get_column_attr_map(self) -> dict:
        ca_map = OrderedDict()
        ca_map["Título"] = "title"
        ca_map["Autor"] = "author"
        ca_map["Fonte"] = "source"
        ca_map["Link"] = "link"
        ca_map["Conteúdo"] = "content"

        return ca_map

    @Slot()
    def __accepted(self):
        if self.__is_update:
            pass
        else:
            self.__create_entity()

    @Slot()
    def __finished(self):
        print("Finished")

    @Slot()
    def __rejected(self):
        self.__show_cancel_message()

    def __create_entity(self):
        try:
            self.__api.create(self._get_object(), self.__endpoint)
            self.__show_success_message()
        except APICreateError:
            self.__show_failed_message()

    def __show_success_message(self):
        mbox = QMessageBox(self)
        mbox.setIcon(QMessageBox.Icon.Information)
        mbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.__delete_obj:
            mbox.setWindowTitle("Excluir registro")
            mbox.setText("Registro excluido com sucesso.")
        elif self.__is_update:
            mbox.setWindowTitle("Atualizar registro")
            mbox.setText("Registro atualizado com sucesso.")
        else:
            mbox.setWindowTitle("Criar registro")
            mbox.setText("Registro criado com sucesso.")

        mbox.exec_()

    def __show_failed_message(self):
        mbox = QMessageBox(self)
        mbox.setIcon(QMessageBox.Icon.Critical)
        mbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.__delete_obj:
            mbox.setWindowTitle("Excluir registro")
            mbox.setText("Falha ao excluir o registro.")
        elif self.__is_update:
            mbox.setWindowTitle("Atualizar registro")
            mbox.setText("Falha ao atualizar o registro.")
        else:
            mbox.setWindowTitle("Criar registro")
            mbox.setText("Falha ao criar o registro.")

        mbox.exec_()

    def __show_cancel_message(self):
        mbox = QMessageBox(self)
        mbox.setIcon(QMessageBox.Icon.Critical)
        mbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.__is_update:
            mbox.setWindowTitle("Atualizar registro")
            mbox.setText("Atualização de registro cancelada, alterações não foram salvas.")
        else:
            mbox.setWindowTitle("Criar registro")
            mbox.setText("Criação de registro cancelada, alterações não foram salvas.")

        mbox.exec_()

    def __update_entity(self):
        pass

    def __delete_entity(self):
        pass

    def open_create_window(self) -> None:
        self.__obj = None
        self.__is_update = False
        self._fill_fields()
        self.show()

    def open_update_window(self, delete_obj: bool = False) -> None:
        self.__select_ui.tableWidget.clear()
        _fill_select_header(self.__select_ui.tableWidget, self._get_column_attr_map())

        self.__select_window.show()
