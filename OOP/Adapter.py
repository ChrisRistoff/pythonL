class UsbCable():

    def __init__(self):
        self.is_plugged = False

    def plug_usb(self):
        self.is_plugged = True


class UsbPort():

    def __init__(self):
        self.port_available = True

    def plug(self, usb):
        if self.port_available:
            usb.plug_usb()
            self.port_available = False

    def unplug(self, usb):
        if not self.port_available:
            usb.is_plugged = False
            self.port_available = True


usb_cable = UsbCable()
usb_port = UsbPort()
usb_port.plug(usb_cable)
usb_port.unplug(usb_cable)
print(usb_cable.is_plugged)


class MicroUsbCable():

    def __init__(self):
        self.is_plugged = False

    def plug_micro_usb(self):
        self.is_plugged = True


class MicroToUsbAdapter(UsbCable):

    def __init__(self, micro_usb_cable):
        self.micro_usb_cable = micro_usb_cable
        self.micro_usb_cable.plug_micro_usb()


micro_to_usb = MicroToUsbAdapter(MicroUsbCable())
usb_port2 = UsbPort()
usb_port2.plug(micro_to_usb)

print(usb_port2)
