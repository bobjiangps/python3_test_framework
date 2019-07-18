# -*- coding:utf-8 -*- 
from common.test_base.page_base import PageBase


class RoutePage(PageBase):       
    
    def input_destination_and_search_route(self, destination):
        self.log.info("user input destination to go and search route")
        self.switch_to_bus_mode()
        self.element("destination_input").click()
        self.element("destination_edit").input_value(destination)
        self.element("search_button").click()
        try:
            self.element("first_suggest_destination").click()
            self.log.info("select the suggest destination")
        except:
            self.log.info("no suggest destination")
        
    def switch_to_drive_mode(self):
        self.log.info("switch to drive mode")
        self.element("category_car").click()

    def switch_to_bus_mode(self):
        self.log.info("switch to bus mode")
        self.element("category_bus").click()
        
    def back_to_main_page(self):
        self.log.info("user go back to main page")
        self.element("route_search_back").click()

    # assertions below
    def is_able_to_navigate(self):
        start_navigate_button = self.element("start_navigation_button").wait_clickable()
        assert start_navigate_button, "unable to find the start navigation button"
