from common.test_base.win_test_case import WinTestCase
from projects.win_note.pages.edit_page import EditPage


class NoteWinTestCase(WinTestCase):
    """Test case for testing window notepad"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.edit_page = EditPage(cls._driver, cls.log)
