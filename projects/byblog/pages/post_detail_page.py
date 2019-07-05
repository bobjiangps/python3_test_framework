from projects.byblog.pages.common_component import CommonComponent


class PostDetailPage(CommonComponent):

    # assertions below
    def blog_post_title_equals(self, text):
        self.log.info(f"Check the blog post title should be {text}")
        self.element("blog_post_title").check_text(text)
