from common.test_base.page_base import PageBase
from configuration.config import LoadConfig
import os


class EditPage(PageBase):

    def input_texts_into_edit_then_save(self, texts, file_name):
        self.log.info("Input texts into edit area")
        self.element("edit_input").input_value(texts)
        main_window = self.element_info("main_window")
        self.behavior.select_menu(main_window, ["File", "Save As..."])
        file_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data", file_name)
        self.element("save_file_input").input_value(file_path)
        self.element("save_button").click()

    def check_file_exists_in_test_data(self, file_path):
        if os.path.exists(file_path):
            return True
        else:
            return False

    def remove_file_if_exists_in_test_data(self, file_name):
        file_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data", file_name)
        if self.check_file_exists_in_test_data(file_path):
            os.remove(file_path)

    # assertions below
    def notepad_is_able_to_save_content_to_file(self, file_name):
        file_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data", file_name)
        assert self.check_file_exists_in_test_data(file_path), "not find the file: %s" % str(file_path)
