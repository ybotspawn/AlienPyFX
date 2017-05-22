import usb.core
import usb.util
import argparse

class AlienwareDeviceManager(object):
    vendorID = 0x187c
    productID = 0x0527
    dev = None

    def __init__(self):
        print("Init")

    def apply_theme(self, themeFilePath):
        attach_usb_device()
        __apply_theme__(themeFilePath)
    
    def lights_off(self):
        pass

    def lights_on(self):
        pass

    def __send_usb_message__(self, line):
        if not line.startswith('#'):
            message = r"\x{0}".format(line.replace(':', r'\x').replace('\n', ''))
            assert dev.ctrl_transfer(0x21, 9, 0, 0, message.decode("string-escape")) == len(message.decode("string-escape"))

    def __apply_theme__(self, themeFilePath):
        f = open(themeFilePath)
        for line in f.readlines():
            __send_usb_message__(line)

    def __attach_usb_device__(self):
        self.dev = usb.core.find(idVendor=self.vendorID, idProduct=self.productID)
        endpoint = self.dev[0][(0,0)][0]
        config = self.dev.get_active_configuration()
        intf = config[(0,0)]
        if self.dev.is_kernel_driver_active(0) is True:
            self.dev.detach_kernel_driver(0)
        elif self.dev.is_kernel_driver_active(1) is True:
            self.dev.detach_kernel_driver(1)
        usb.util.claim_interface(self.dev, 0)

def __setup_argument_parser__():
    parser = argparse.ArgumentParser("AlienPyFX console")
    parser.add_argument('--theme', dest='theme_path', metavar="FILE", help='Path to theme file to apply.  In test mode this validates the configuration of the theme')
    parser.add_argument('--lights-off', help='Toggle lights off', action='store_true')
    parser.add_argument('--lights-on',  help='Toggle lights on', action='store_true')
    parser.set_defaults(off=False)
    parser.set_defaults(on=True)
    return parser

if __name__ == '__main__':
    parser = __setup_argument_parser__()
    option = parser.parse_args()
    adm = AlienwareDeviceManager()
    if option.theme_path is not None:
        adm.apply_theme(option.theme_path)
    elif option.lights_off is True:
        adm.lights_off()
    else:
        adm.lights_on()