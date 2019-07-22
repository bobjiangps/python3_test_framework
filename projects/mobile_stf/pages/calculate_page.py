from common.test_base.page_base import PageBase


class CalculatePage(PageBase):

    def add(self, num_a, num_b):
        self.log.info("Input number to add")
        self.element("num_%d" % num_a).click()
        self.element("add_button").click()
        self.element("num_%d" % num_b).click()
        self.element("equal_button").click()

    def get_calculate_result(self):
        result_text = self.element("cal_result").get_element_text()
        self.log.info("calculate result is %s" % str(result_text))
        return result_text

    # assertion below
    def add_function_should_works_when_add_single_digit(self):
        self.add(2, 6)
        result = str(self.get_calculate_result())
        assert result.find("8") >= 0, "get wrong calculate result when add single digit: %s" % result
