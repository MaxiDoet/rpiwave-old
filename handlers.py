from nextion import NextionEffects
from time import sleep
import utils

class WebRadioEventHandler:
    def __init__(self, interface):
        self.interface = interface

    def page_1_component_0_touch(self):
        self.interface.set_page(3)

    def page_3_component_8_touch(self):
        self.interface.set_page(5)

    def page_3_component_10_touch(self):
        self.interface.set_page(7)

    # Register all home buttons
    def page_3_component_3_touch(self):
        self.interface.set_page(1)
    def page_4_component_3_touch(self):
        self.interface.set_page(3)
    def page_5_component_2_touch(self):
        self.interface.set_page(3)
    def page_7_component_3_touch(self):
        self.interface.set_page(3)

    # Register all back button
    def page_6_component_7_touch(self):
        self.interface.set_page(4)
    def page_9_component_2_touch(self):
        self.interface.set_page(3)

    # Register all power button
    def page_3_component_7_touch(self):
        self.interface.set_page(10)
        NextionEffects.typewrite_reverse(self.interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(self.interface, 1)
        self.interface.sleep()
    def page_4_component_7_touch(self):
        self.interface.set_page(10)
        NextionEffects.typewrite_reverse(self.interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(self.interface, 1)
        self.interface.sleep()
    def page_5_component_5_touch(self):
        self.interface.set_page(10)
        NextionEffects.typewrite_reverse(self.interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(self.interface, 1)
        self.interface.sleep()
    def page_7_component_7_touch(self):
        self.interface.set_page(10)
        NextionEffects.typewrite_reverse(self.interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(self.interface, 1)
        self.interface.sleep()
    def page_8_component_5_touch(self):
        self.interface.set_page(10)
        NextionEffects.typewrite_reverse(self.interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(self.interface, 1)
        self.interface.sleep()

    # Page change events
    def page_1_change(self):
        utils.displayNews(self.interface)
    def page_7_change(self):
        utils.displayStationList(self.interface)