from nextion import NextionEffects
from time import sleep
import utils
from radio import radio

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

    def page_7_component_11_touch(self):
        radio.stopStreams()
        selected = self.interface.get_selected("wSC0")
        streams = utils.getStreams()
        radio.playStream(streams[selected])

    # Register all back buttons
    def page_6_component_7_touch(self):
        self.interface.set_page(4)

    def page_9_component_2_touch(self):
        self.interface.set_page(3)

    # Register all power buttons
    def page_3_component_7_touch(self):
        utils.shutdown(self.interface)

    def page_4_component_7_touch(self):
        utils.shutdown(self.interface)

    def page_5_component_5_touch(self):
        utils.shutdown(self.interface)

    def page_7_component_7_touch(self):
        utils.shutdown(self.interface)

    def page_8_component_5_touch(self):
        utils.shutdown(self.interface)

    # Page change events
    def page_1_change(self):
        utils.displayNews(self.interface)

    def page_2_change(self):
        print("Do nothing")

    def page_3_change(self):
        print("Do nothing")

    def page_4_change(self):
        print("Do nothing")

    def page_5_change(self):
        print("Do nothing")

    def page_6_change(self):
        print("Do nothing")

    def page_7_change(self):
        radio.stopStreams()
        utils.displayStationList(self.interface)
        #self.interface.set_text("wSC0", utils.getStations()[0]["name"])
        #radio.playStream(utils.getStreams()[0])
