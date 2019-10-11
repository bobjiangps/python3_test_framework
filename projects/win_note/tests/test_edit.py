from .win_test_case import NoteWinTestCase


class TestEdit(NoteWinTestCase):

    def test_save_values(self):
        """WNote-1: notepad is able to input value and save value"""
        with self.precondition():
            file_name = "save_as.txt"
            self.edit_page.remove_file_if_exists_in_test_data(file_name)

        with self.steps():
            texts = "this is a test"
            self.edit_page.input_texts_into_edit_then_save(texts, file_name)

        with self.verify():
            self.edit_page.notepad_is_able_to_save_content_to_file(file_name)

        with self.cleanup():
            self.edit_page.remove_file_if_exists_in_test_data(file_name)
