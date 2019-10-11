from .web_test_case import BlogWebTestCase


class TestPermission(BlogWebTestCase):

    def test_sort_posts_only_available_for_logged_in_user(self):
        """ByBlog-3: only user who have logged in can see the posts view dropdown in post list page"""
        with self.precondition():
            user_1 = self.get_project_config_data()["users"]["Users_1"]
            account = user_1["account"]
            password = user_1["password"]

        with self.steps():
            self.login_page.login(account, password)
            self.main_page.go_to_post_list_page()

        with self.verify():
            self.post_list_page.post_view_dropdown_should_appear_after_login()
            self.post_list_page.post_view_dropdown_should_arrange_posts_order_by_view_count()

        with self.cleanup():
            self.post_list_page.logout()


