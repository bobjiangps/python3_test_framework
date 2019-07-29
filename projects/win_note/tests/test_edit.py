from projects.win_note.tests.win_test_case import NoteWinTestCase


class TestEdit(NoteWinTestCase):

    def test_save_values(self):
        """Case-1: notepad is able to input value and save value"""
        with self.precondition():
            texts = "this is a test"
            self.edit_page.input_texts_into_edit(texts)
