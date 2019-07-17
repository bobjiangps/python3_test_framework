from projects.ios_safari.tests.mobile_test_case import BlogMobileTestCase


class TestViewPosts(BlogMobileTestCase):

    def test_view_posts_in_search_result(self):
        """Case-1: user is able to search posts and view the search result"""
        with self.precondition():
            keyword = "openstf"

        with self.steps():
            self.main_page.go_to_home_page()
            self.main_page.search_posts(keyword)

        with self.verify():
            self.post_list_page.title_or_content_should_contains_search_keyword_in_search_result(keyword)
