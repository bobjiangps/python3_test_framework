from .mobile_test_case import MapMobileTestCase


class TestMapRoute(MapMobileTestCase):
    """test route functions""" 

    def test_route_by_car(self):
        """MMap-2: test route by car"""
        with self.precondition():
            self.main_page.start_route()
            destination = u"环球中心停车场"
             
        with self.steps():
            self.route_page.input_destination_and_search_route(destination)
            self.route_page.switch_to_drive_mode()
 
        with self.verify():
            self.route_page.is_able_to_navigate()
            
        with self.cleanup():
            self.route_page.back_to_main_page()
