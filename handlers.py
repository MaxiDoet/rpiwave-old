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
        self.interface.set_page(8)

    # Register all home buttons
    def page_3_component_3_touch(self):
        self.interface.set_page(1)

    def page_4_component_3_touch(self):
        self.interface.set_page(3)

    def page_5_component_2_touch(self):
        self.interface.set_page(3)

    def page_7_component_3_touch(self):
        self.interface.set_page(3)

    def page_7_component_12_touch(self):
        self.interface.set_page(8)

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

    #def page_7_component_9_touch(self):

    def page_8_component_2_touch(self):
        self.interface.set_page(3)

    def page_8_component_5_touch(self):
        utils.shutdown(self.interface)

    # Register all 24 station buttons :-( :
    def page_8_component_7_touch(self):
        radio.playStation(0)
        self.interface.set_page(7)

    def page_8_component_8_touch(self):
        radio.playStation(1)
        self.interface.set_page(7)

    def page_8_component_9_touch(self):
        radio.playStation(2)
        self.interface.set_page(7)

    def page_8_component_10_touch(self):
        radio.playStation(3)
        self.interface.set_page(7)

    def page_8_component_11_touch(self):
        radio.playStation(4)
        self.interface.set_page(7)

    def page_8_component_12_touch(self):
        radio.playStation(5)
        self.interface.set_page(7)

    def page_8_component_13_touch(self):
        radio.playStation(6)
        self.interface.set_page(7)

    def page_8_component_14_touch(self):
        radio.playStation(7)
        self.interface.set_page(7)

    def page_8_component_15_touch(self):
        radio.playStation(8)
        self.interface.set_page(7)

    def page_8_component_16_touch(self):
        radio.playStation(9)
        self.interface.set_page(7)

    def page_8_component_17_touch(self):
        radio.playStation(10)
        self.interface.set_page(7)

    def page_8_component_18_touch(self):
        radio.playStation(11)
        self.interface.set_page(7)

    def page_8_component_19_touch(self):
        radio.playStation(12)
        self.interface.set_page(7)

    def page_8_component_20_touch(self):
        radio.playStation(13)
        self.interface.set_page(7)

    def page_8_component_21_touch(self):
        radio.playStation(14)
        self.interface.set_page(7)

    def page_8_component_22_touch(self):
        radio.playStation(15)
        self.interface.set_page(7)

    def page_8_component_23_touch(self):
        radio.playStation(16)
        self.interface.set_page(7)

    def page_8_component_24_touch(self):
        radio.playStation(17)
        self.interface.set_page(7)

    def page_8_component_25_touch(self):
        radio.playStation(18)
        self.interface.set_page(7)

    def page_8_component_26_touch(self):
        radio.playStation(19)
        self.interface.set_page(7)

    def page_8_component_27_touch(self):
        radio.playStation(20)
        self.interface.set_page(7)

    def page_8_component_28_touch(self):
        radio.playStation(21)
        self.interface.set_page(7)

    def page_8_component_29_touch(self):
        radio.playStation(22)
        self.interface.set_page(7)

    def page_8_component_30_touch(self):
        radio.playStation(23)
        self.interface.set_page(7)

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

    # def page_7_change(self):
    # radio.stopStreams()
    # utils.displayStationList(self.interface)
    # self.interface.set_text("wSC0", utils.getStations()[0]["name"])
    # radio.playStream(utils.getStreams()[0])

    def page_8_change(self):
        utils.displayStationList(self.interface)
