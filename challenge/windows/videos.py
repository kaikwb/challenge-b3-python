from collections import OrderedDict
from typing import Any

from .base import BaseWindow
from .base_ui.video_ui import Ui_VideoWindow


class VideosWindow(BaseWindow):
    def __init__(self, url_base: str, endpoint: str = "", parent: Any | None = None):
        super().__init__(Ui_VideoWindow, url_base, endpoint, parent=parent)

    def fill_fields(self) -> None:
        if self.is_update:
            title = self.obj.get("title", "")
            author = self.obj.get("author", "")
            source = self.obj.get("source", "")
            link = self.obj.get("link", "")
            video_id = self.obj.get("video_id", "")
            thumbnail = self.obj.get("thumbnail", "")
        else:
            title = ""
            author = ""
            source = ""
            link = ""
            video_id = ""
            thumbnail = ""

        self.ui.titleEdit.setText(title)
        self.ui.authorEdit.setText(author)
        self.ui.sourceEdit.setText(source)
        self.ui.linkEdit.setText(link)
        self.ui.idEdit.setText(video_id)
        self.ui.thumbnailEdit.setText(thumbnail)

    def get_object(self) -> dict:
        obj = dict()

        obj["title"] = self.ui.titleEdit.text()
        obj["author"] = self.ui.authorEdit.text()
        obj["source"] = self.ui.sourceEdit.text()
        obj["link"] = self.ui.linkEdit.text()
        obj["video_id"] = self.ui.idEdit.text()
        obj["thumbnail"] = self.ui.thumbnailEdit.text()

        return obj

    def get_column_attr_map(self) -> dict:
        ca_map = OrderedDict()
        ca_map["Título"] = "title"
        ca_map["Autor"] = "author"
        ca_map["Fonte"] = "source"
        ca_map["Link"] = "link"
        ca_map["Video ID"] = "video_id"
        ca_map["Thumbnail"] = "thumbnail"

        return ca_map
