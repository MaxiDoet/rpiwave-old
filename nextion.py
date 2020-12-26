import serial
from time import sleep

NEXTION_COMMAND_END=b'\xff\xff\xff'

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

    def read(self, size):
        self.ser.flush()
        if self.debug: print("Debug: read")

        data = self.ser.read(size)

        return data

class NextionDisplayInterface:
    def __init__(self, nextionDisplay, eventHandler):
        self.display = nextionDisplay
        self.handler = eventHandler

    def send(self, command):
        self.display.write(command)

    def set_page(self, num):
        self.display.write('page ' + str(num))

    def set_text(self, name, text):
        self.display.write('%s.txt="%s"' % (name, text))

    def set_color(self, name, code, colorProperty="pco"):
        self.display.write('%s.%s=%s' % (name, colorProperty, code))

    def set_brightness(self, value):
        self.display.write('dim=%s' % str(value))

    def get_color(self, name, colorProperty="pco"):
        self.display.write('get %s.%s' % (name, colorProperty))
        return self.display.read(2)

    def get_current_page(self):
        self.send("sendme")
        return self.display.read(5)[1]

    def handle_touch_event(self, data):
        print("New touch event!, ComponentID:%s, Page:%s" % (data[2], data[1]))
        try:
            methodName = "page_%s_component_%s_touch" % (data[1], data[2])
            getattr(self.handler, methodName)()
        except AttributeError:
            print("No eventhandler is defined for component %s. Please define %s" % (data[2], methodName))

    def sleep(self):
        self.display.write("sleep=1")

    def wake(self):
        self.display.write("sleep=0")

class NextionEffects:
    def typewrite(interface, name, text, time):
        interface.set_text(name, "")
        tmp = ""
        for num in range(0, len(text)):
            tmp+= text[num]
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
