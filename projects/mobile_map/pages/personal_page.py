from common.test_base.page_base import PageBase


class PersonalPage(PageBase):

    def go_to_favorite_page(self):
        self.log.info("go to favorite")
        self.element("favorite_link").click()
        sync = self.element("sync_complete_toast").wait_presence()
        self.log.info(sync.text)
        self.element("sync_complete_toast").wait_disappear()

    def count_favorite_items(self):
        self.element("favorite_item_address").wait_presence()
        favorite_items = self.element("favorite_item_address").all()
        self.log.info("there are %d favorite items" % len(favorite_items))
        return len(favorite_items)

    def back_to_main_page_from_favorite_page(self):
        self.log.info("go back to main page from favorite page")
        self.element("favorite_back").click()
        self.element("personal_page_back").click()

    # assertions below
    def favorite_items_should_more_than_five(self):
        count = self.count_favorite_items()
        assert count == 5, "there are %d favorite items not 5" % count
