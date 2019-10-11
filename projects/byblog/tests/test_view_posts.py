from .web_test_case import BlogWebTestCase


class TestViewPosts(BlogWebTestCase):

    def test_view_posts_in_search_result(self):
        """ByBlog-1: user is able to search posts and view the search result"""
        with self.precondition():
            keyword = "openstf"

        with self.steps():
            self.main_page.search_posts(keyword)

        with self.verify():
            self.post_list_page.title_or_content_should_contains_search_keyword_in_search_result(keyword)

    def test_view_posts_when_jump_page(self):
        """ByBlog-2: user is able to view posts when jump page"""
        with self.precondition():
            page_num = 2

        with self.steps():
            self.main_page.go_to_post_list_page()
            self.post_list_page.navigate_to_page_num(page_num)

        with self.verify():
            self.post_list_page.current_url_contains("?page=%d" % page_num)
            self.post_list_page.blog_post_amount_should_equal_to_num(5)

    def test_post_id_in_detail_page_url(self):
        """ByBlog-4: details page url contains post id"""
        with self.precondition():
            random_id_title = self.post_list_page.get_id_title_of_random_post()
            new_url = "/".join([self.post_list_page.current_url(), f"article-01{random_id_title['id']}"])

        with self.steps():
            self.browse_page(new_url)

        with self.verify():
            self.post_detail_page.blog_post_title_equals(random_id_title["title"])
