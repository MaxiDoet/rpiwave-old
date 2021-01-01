import serial
from time import sleep

NEXTION_COMMAND_END = b'\xff\xff\xff'
NEXTION_NEWLINE = b'\x0d\x0a'


class NextionDisplay:
    def __init__(self, port, baudrate=9600, debug=False):
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=2)
        self.debug = debug
        if self.debug: print("Debug: init\nPort: %s\nBautrate: %s" % (port, baudrate))

    def write(self, data):
        data = data.encode('UTF-8') + NEXTION_COMMAND_END
        self.ser.write(data)

        if self.debug:
            print("Debug: write\nData:")
            for b in data:
                print(b, end=' ')

    def write_raw(self, data):
        self.ser.write(data)

        if self.debug:
            print("Debug: write\nData:")
            for b in data:
                print(b, end=' ')

    def read(self, size):
        self.ser.flush()
        if self.debug: print("Debug: read")

        data = self.ser.read(size)

        return data


class NextionDisplayInterface:
    def __init__(self, nextionDisplay):
        self.display = nextionDisplay
        self.handler = None
        self.last_page = 0

    def register_event_handler(self, handler):
        self.handler = handler
        num_events = len([func for func in dir(handler) if callable(getattr(handler, func))][22:])
        print("Registered event handler (%s events)" % num_events)

    def send(self, command, response_size, timeout=10, wait=0.1):
        self.display.write(command)

        while timeout is not 0:
            timeout -= 1
            print("Timeout: ", timeout)
            data = self.display.read(response_size)
            if data != b'': print("Got answer: %s", data); return

        print("Timeout!")
        return 0

    def set_page(self, num):
        self.last_page = self.get_current_page()
        self.display.write('page ' + str(num))

    def set_text(self, name, text):
        self.display.write('%s.txt="%s"' % (name, text))

    def add_line_to_combobox(self, name, text):

        data = ('%s.path+="%s%s"' % (name, text, "\x0D\x0a")).encode("UTF-8") + NEXTION_COMMAND_END

        self.display.write_raw(data)
        """
        self.display.write('%s.path+="%s"' % (name, text))
        self.display.write('%s.path+="%s"' % (name, NEXTION_NEWLINE))
        """
        """
        self.display.write('%s.path+="%s\r"' % (name, text))
        print('%s.path+="%s\r"' % (name, text))
        """

    def get_selected(self, name):
        self.display.write("get %s.val" % name)
        data = self.display.read(8)
        print("Debug: read(8): %s" % data)
        return data[1]

    def trigger_touch_event(self, name, event=1):
        self.display.write("click %s,%s" % (name, event))

    def set_val(self, name, val):
        self.display.write('%s.val="%s"' % (name, val))

    def set_color(self, name, code, colorProperty="pco"):
        self.display.write('%s.%s=%s' % (name, colorProperty, code))

    def set_brightness(self, value):
        self.display.write('dim=%s' % str(value))

    def get_color(self, name, colorProperty="pco"):
        self.display.write('get %s.%s' % (name, colorProperty))
        return self.display.read(2)

    def get_current_page(self):
        # Check if sleep is 1 because then page will be out of index!
        timeout = 10
        self.display.write("sendme")
        while timeout != 0:
            timeout -= 1
            data = self.display.read(5)
            if data and data[1] != 255:
                return data[1]

    def handle_touch_event(self, data):
        if self.handler:
            print("Touch event: ComponentID:%s, Page:%s" % (data[2], data[1]))
            try:
                methodName = "page_%s_component_%s_touch" % (data[1], data[2])
                getattr(self.handler, methodName)()
            except AttributeError:
                print("No eventhandler is defined for component %s. Please define %s" % (data[2], methodName))
        else:
            print("Seems like there is no event handler registered!")

    def handle_page_change_event(self, page):
        if self.handler:
            print("Page change event: Page: %s" % page)
            try:
                methodName = "page_%s_change" % (page)
                getattr(self.handler, methodName)()
            except AttributeError:
                print("No eventhandler is defined for page %s. Please define %s" % (page, methodName))
        else:
            print("Seems like there is no event handler registered!")

    def sleep(self):
        self.display.write("sleep=1")

    def wake(self):
        self.display.write("sleep=0")

    def hide(self, name):
        self.display.write("vis %s,0" % name)

    def show(self, name):
        self.display.write("vis %s,1" % name)


class NextionEffects:
    def typewrite(interface, name, text, time):
        interface.set_text(name, "")
        tmp = ""
        for num in range(0, len(text)):
            tmp += text[num]
            interface.set_text(name, tmp)
            sleep(time)

    def typewrite_reverse(interface, name, text, time):
        interface.set_text(name, text)
        for num in range(0, len(text)):
            interface.set_text(name, text[num:])
            sleep(time)
        interface.set_text(name, "")

    def dim_out_screen(interface, time, end_value=0):
        interface.display.write("get dim")
        dim = interface.display.read(4)[1]

        for cur in range(dim, end_value, -1):
            interface.set_brightness(cur)

    def dim_in_screen(interface, time, end_value=100):
        interface.display.write("get dim")
        dim = interface.display.read(4)[1]

        for cur in range(dim, end_value, 1):
            interface.set_brightness(cur)


class NextionEventHandler:
    def page_0_test_event(self):
        print("This was a test you have to override this")


def convert_hex_to_nextion(r, g, b):
    return ((r >> 3) << 11) + ((g >> 2) << 5) + (b >> 3)
