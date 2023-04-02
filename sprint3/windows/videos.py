from collections import OrderedDict
from typing import Any

from .base_ui.video_ui import Ui_VideoWindow
from .base import BaseWindow


class VideosWindow(BaseWindow):
    def __init__(self, url_base: str, endpoint: str = "", parent: Any | None = None):
        super().__init__(Ui_VideoWindow, url_base, endpoint, parent=parent)

    def fill_fields(self) -> None:
        if self.is_update:
            title = self.obj.get("title", "")
            author = self.obj.get("author", "")
            source = self.obj.get("source", "")
            link = self.obj.get("link", "")
        else:
            title = ""
            author = ""
            source = ""
            link = ""

        self.ui.titleEdit.setText(title)
        self.ui.authorEdit.setText(author)
        self.ui.sourceEdit.setText(source)
        self.ui.linkEdit.setText(link)

    def get_object(self) -> dict:
        obj = dict()

        obj["title"] = self.ui.titleEdit.text()
        obj["author"] = self.ui.authorEdit.text()
        obj["source"] = self.ui.sourceEdit.text()
        obj["link"] = self.ui.sourceEdit.text()

        return obj

    def get_column_attr_map(self) -> dict:
        ca_map = OrderedDict()
        ca_map["Título"] = "title"
        ca_map["Autor"] = "author"
        ca_map["Fonte"] = "source"
        ca_map["Link"] = "link"

        return ca_map
