from enum import Enum
from typing import Any

from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QDialog, QMessageBox, QTableWidgetItem

from sprint3.api.api import API
from sprint3.api.exceptions import APICreateError, APIUpdateError, APIDeleteError, APIGetError
from .base_ui import select_ui
from .exceptions import MethodMustBeImplemented


class MessageType(Enum):
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    CANCEL = 4


class BaseWindow(QDialog):
    def __init__(self, ui: object, url_base: str, endpoint: str = "", parent: Any | None = None):
        super().__init__(parent)

        self.is_delete = False
        self.__url_base = url_base
        self.__endpoint = endpoint
        self.__is_update = False
        self.__obj_id = None
        self.obj = None

        self.ui = ui()
        self.ui.setupUi(self)
        self.setModal(True)
        self.accepted.connect(self.accepted_dialog)
        self.finished.connect(self.finished_dialog)
        self.rejected.connect(self.rejected_dialog)

        self.__select_window = QDialog(self)
        self.__select_ui = select_ui.Ui_Dialog()
        self.__select_ui.setupUi(self.__select_window)

        self.__api = API(url_base)

    def fill_fields(self) -> None:
        raise MethodMustBeImplemented(self, self.fill_fields.__name__)

    def get_object(self) -> dict:
        raise MethodMustBeImplemented(self, self.get_object.__name__)

    def get_column_attr_map(self) -> dict:
        raise MethodMustBeImplemented(self, self.get_column_attr_map.__name__)

    @property
    def is_update(self):
        return self.__is_update

    @is_update.setter
    def is_update(self, value):
        self.__is_update = value

    @staticmethod
    def fill_select_header(table_widget, ca_map: dict) -> None:
        columns = list(ca_map.keys())
        table_widget.setColumnCount(len(columns))
        table_widget.setHorizontalHeaderLabels(ca_map.keys())

    @staticmethod
    def fill_content(table_widget, obj: dict, ca_map: dict) -> None:
        table_widget.setRowCount(len(obj))
        for i, (item_id, item) in enumerate(obj.items()):
            for j, attr in enumerate(ca_map.values()):
                cell = QTableWidgetItem(item[attr])
                cell.setFlags(Qt.ItemFlag.ItemIsEnabled)
                if j == 0:
                    cell.setData(Qt.ItemDataRole.UserRole, (item_id, item))
                table_widget.setItem(i, j, cell)

    @Slot()
    def accepted_dialog(self):
        if self.is_update:
            self.update_entity(self.__obj_id, self.get_object())
        else:
            self.create_entity()

    @Slot()
    def finished_dialog(self):
        pass

    @Slot()
    def rejected_dialog(self):
        self.show_message(MessageType.CANCEL)

    def create_entity(self):
        try:
            self.__api.create(self.get_object(), self.__endpoint)
            self.show_message(MessageType.CREATE)
        except APICreateError:
            self.show_message(MessageType.CREATE, success=False)

    def get_all_entities(self):
        try:
            result = self.__api.get(self.__endpoint)
            return result
        except APIGetError:
            return None

    def show_message(self, messge_type: MessageType, success: bool = True):
        mbox = QMessageBox(self)
        mbox.setIcon(QMessageBox.Icon.Information)
        mbox.setStandardButtons(QMessageBox.StandardButton.Ok)

        match messge_type:
            case MessageType.CREATE:
                if success:
                    mbox.setWindowTitle("Criar registro")
                    mbox.setText("Registro criado com sucesso.")
                else:
                    mbox.setWindowTitle("Criar registro")
                    mbox.setText("Falha ao criar o registro.")
            case MessageType.UPDATE:
                if success:
                    mbox.setWindowTitle("Atualizar registro")
                    mbox.setText("Registro atualizado com sucesso.")
                else:
                    mbox.setWindowTitle("Atualizar registro")
                    mbox.setText("Falha ao atualizar o registro.")
            case MessageType.DELETE:
                if success:
                    mbox.setWindowTitle("Excluir registro")
                    mbox.setText("Registro excluido com sucesso.")
                else:
                    mbox.setWindowTitle("Excluir registro")
                    mbox.setText("Falha ao excluir o registro.")
            case MessageType.CANCEL:
                if self.is_update:
                    mbox.setWindowTitle("Atualizar registro")
                    mbox.setText("Atualização de registro cancelada, alterações não foram salvas.")
                else:
                    mbox.setWindowTitle("Criar registro")
                    mbox.setText("Criação de registro cancelada, alterações não foram salvas.")

        mbox.exec()

    def update_entity(self, entity_id, entity):
        try:
            self.__api.update(entity_id, entity, self.__endpoint)
            self.show_message(MessageType.UPDATE)
        except APIUpdateError:
            self.show_message(MessageType.UPDATE, success=False)

    def delete_entity(self, entity_id):
        try:
            self.__api.delete(entity_id, self.__endpoint)
            self.show_message(MessageType.DELETE)
        except APIDeleteError:
            self.show_message(MessageType.DELETE, success=False)

    def open_create_window(self) -> None:
        self.obj = None
        self.is_update = False
        self.fill_fields()
        self.show()

    def open_update_window(self, entity_id, entity) -> None:
        self.obj = entity
        self.__obj_id = entity_id
        self.fill_fields()
        self.show()

    def open_select_window(self, delete_obj: bool = False) -> None:
        self.is_update = not delete_obj
        enties = self.get_all_entities()

        if enties is None:
            self.show_message(MessageType.DELETE if delete_obj else MessageType.UPDATE, success=False)
            return

        table = self.__select_ui.tableWidget
        ca_map = self.get_column_attr_map()

        table.clear()
        self.fill_select_header(table, ca_map)
        self.fill_content(table, enties, ca_map)

        self.__select_window.exec()

        item = table.item(table.currentRow(), 0)

        if item is not None:
            entity_id, entity = item.data(Qt.ItemDataRole.UserRole)

            if self.is_update:
                self.open_update_window(entity_id, entity)
            else:
                self.delete_entity(entity_id)
