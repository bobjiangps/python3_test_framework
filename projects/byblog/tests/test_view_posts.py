#from common.test_base.web_test_case import WebTestCase
from projects.byblog.tests.web_test_case import BlogWebTestCase


class TestViewPosts(BlogWebTestCase):

    def test_view_posts_in_search_result(self):
        """Case-1: user is able to search posts and view the search result"""
        with self.precondition():
            keyword = "webdriver"

        with self.steps():
            self.post_list_page.search_posts(keyword)

        with self.verify():
            self.post_list_page.title_or_content_should_contains_search_keyword_in_search_result(keyword)

    def test_view_posts_when_jump_page(self):
        """Case-2: user is able to view posts when jump page"""
        with self.precondition():
            page_num = 2

        with self.steps():
            self.post_list_page.navigate_to_page_num(page_num)

        with self.verify():
            self.post_list_page.current_url_contains("?page=%d" % page_num)
            self.post_list_page.blog_post_amount_should_equal_to_num(5)
