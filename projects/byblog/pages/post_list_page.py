from .common_component import CommonComponent


class PostListPage(CommonComponent):

    def navigate_to_page_num(self, number):
        self.log.info("Navigate to page num %d" % number)
        self.element("page_jump_input").input_value(number)
        self.element("page_jump_button").click()
        self.element("page_jump_button").wait_clickable()

    def go_to_next_page(self):
        self.log.info("Go to next page by click next button")
        self.element("next_page_button").click()
        self.element("page_jump_button").wait_clickable()

    def go_to_previous_page(self):
        self.log.info("Go to previous page by click previous button")
        self.element("previous_page_button").click()
        self.element("page_jump_button").wait_clickable()

    def get_post_amount_on_current_page(self):
        all_blog_posts = self.behavior.find_elements(self.element_info("all_blog_post"))
        return len(all_blog_posts)

    # assertions below
    def blog_post_amount_should_equal_to_num(self, expect_num):
        self.log.info("Check blog post amount on current page should be %d" % expect_num)
        actual_num = self.get_post_amount_on_current_page()
        assert expect_num == actual_num, "wrong amount.. expect is %d but actual is %d" % (expect_num, actual_num)

    def title_or_content_should_contains_search_keyword_in_search_result(self, search_keyword):
        # all_blog_posts = self.behavior.find_elements(self.element_info("all_blog_post"))
        all_blog_posts = self.element("all_blog_post").all()
        self.log.info("check %d blog posts in search result" % len(all_blog_posts))
        check_result = False
        for index in range(len(all_blog_posts)):
            index += 1
            title = self.element("blog_post_title", index).get_element_text()
            content = self.element("blog_post_preview_content", index).get_element_text()
            self.log.info("post%d has title: %s" % (index, title))
            self.log.info("post%d has preview content: %s" % (index, content))
            if search_keyword in title or search_keyword in content:
                self.log.info("post%d check search keyword pass" % index)
                check_result = True
            else:
                self.log.critical("post%d check search keyword fail" % index)
                check_result = False
        assert check_result, "not all title or content of posts on search result match keyword: %s" % search_keyword

    def post_view_dropdown_should_appear_after_login(self):
        self.element("post_view_dropdown").wait_presence()

    def post_view_dropdown_should_arrange_posts_order_by_view_count(self):
        self.element("post_view_dropdown").select_by_text("按阅读量")
        self.behavior.wait_page_load()
        all_blog_posts = self.element("all_blog_post").all()
        self.log.info("check %d blog posts in new order by view count" % len(all_blog_posts))
        view_count_temp = None
        check_result = False
        for index in range(len(all_blog_posts)):
            index += 1
            title = self.element("blog_post_title", index).get_element_text()
            view_count = self.element("blog_post_view_count", index).get_element_text().split(" ")[0]
            self.log.info("post%d has title: %s" % (index, title))
            self.log.info("post%d has view count: %s" % (index, view_count))
            if view_count_temp:
                self.log.info("check view count between %d and %d" % (int(view_count), int(view_count_temp)))
                if view_count > view_count_temp:
                    check_result = False
                    break
                else:
                    check_result = True
            view_count_temp = view_count
        assert check_result, "not sort posts by view count"
