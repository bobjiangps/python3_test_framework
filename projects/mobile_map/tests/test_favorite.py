from .mobile_test_case import MapMobileTestCase


class TestFavorite(MapMobileTestCase):
    """For favorite functions"""

    def test_favorite_count(self):
        """MMAP-1: test favorite count"""
        with self.precondition():
            self.main_page.go_to_personal_page()
             
        with self.steps():
            self.personal_page.go_to_favorite_page()
 
        with self.verify():
            self.personal_page.favorite_items_should_more_than_five()
            
        with self.cleanup():
            self.personal_page.back_to_main_page_from_favorite_page()
