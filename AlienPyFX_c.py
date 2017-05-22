import usb.core
import usb.util
import argparse

class AlienwareDeviceManager(object):
    vendorID = 0x187c
    productID = 0x0527
    handle = None
    dev = None

    def __init__(self):
        print("Init")
        
    def __send_usb_message__(self, line)
        if not line.startswith('#'):
            message = r"\x{0}".format(line.replace(':', r'\x').replace('\n', ''))
            assert dev.ctrl_transfer(0x21, 9, 0, 0, message.decode("string-escape")) == len(message.decode("string-escape"))

    def apply_theme(self, themeFilePath)
        f = open(themeFilePath)
        for line in f.readlines():
            __send_usb_message__(line)                

    def attach_usb_device(self):
        self.dev = usb.core.find(idVendor=self.vendorID, idProduct=self.productID)
        endpoint = self.dev[0][(0,0)][0]
        config = self.dev.get_active_configuration()
        intf = config[(0,0)]
        if self.dev.is_kernel_driver_active(0) is True:
            self.dev.detach_kernel_driver(0)
        elif self.dev.is_kernel_driver_active(1) is True:
            self.dev.detach_kernel_driver(1)
        usb.util.claim_interface(self.dev, 0)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()
    print("Main")