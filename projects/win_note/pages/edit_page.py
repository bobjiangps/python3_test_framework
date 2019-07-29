from common.test_base.page_base import PageBase


class EditPage(PageBase):

    def input_texts_into_edit(self, texts):
        self.log.info("Input texts into edit area")
        self.element("edit_area").input_value(texts)
