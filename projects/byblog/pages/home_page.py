from projects.byblog.pages.common_component import CommonComponent


class HomePage(CommonComponent):

    def navigate_to_page_num(self, number):
        self.log.info("Navigate to page num %d" % number)
        #todo
