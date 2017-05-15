import usb1

class AlienwareDeviceManager(object):
    vendorID = 0x187c
    productID = 0x0527
    handle = None

    def __init__(self):
        print("Init")

    # https://stackoverflow.com/questions/8982359/error-in-usb-module-in-python
    def __connect_usb_device__(self):
        self.handle = usb1.USBContext().openByVendorIDAndProductID(
            self.vendorID,
            self.productID,
            skip_on_error=True)
        if self.handle is None:
            print("Fail")
        else:
            with self.handle.claimInterface(0):
                print("Success")

    def __send_message__(self):
        print("Sent")
        print("Message")
        # result = libusb1.libusb_control_transfer
        #   (self.__handle, request_type, request, value, index, data, length,
        # ret = libusb_control_transfer(dev, 0x21, 9, 0x0202, 0, bytes, 9, 0);
        # controlWrite(self, request_type, request, value, index, data, timeout=0):timeout,
        #   self._controlTransfer(request_type, request, value, index, data, sizeof(data), timeout)
        self.handle.controlWrite(0x21, 9, 0x0202, 0, "MESSAGE", 9, 0)

def main():
    print("Main")