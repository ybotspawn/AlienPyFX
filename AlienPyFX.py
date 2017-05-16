import usb.core
import usb.util
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
    def __claim_usb_device__(self):
        # get config
        # detach_kernel_driver
        # set config
        # claim_interface
        dev.detach_kernel_driver(0)
        usb.util.claim_interface(dev, 0)
        ep.write('test')
        for cfg in dev:
            cfg.set()
    def temp_doTheThing(self):
        dev = usb.core.find(idVendor=0x187c, idProduct=0x0527)
        endpoint = dev[0][(0,0)][0]
        config = dev.get_active_configuration()
        intf = config[(0,0)]
        if dev.is_kernel_driver_active(1) is True:
            dev.detach_kernel_driver(1)
        usb.util.claim_interface(dev, 0)
        dev.set_configuration(config)

        commit = "02:04"
        lineOne = "02:03:02:00:00:08:f0:00"
        lineTwo = "02:03:03:00:00:04:f0:00"
        lineThree = "02:03:04:00:00:02:f0:00"
        lineFour = "02:03:05:00:00:01:f0:00"
        lineFive = "02:03:06:00:00:60:f0:00"
        lineSix = "02:03:07:00:01:00:f0:00"
        lineSeven = "02:03:08:00:02:00:f0:00"
        lineEight = "02:03:09:00:48:00:f0:00"
        lineNine = "02:03:0a:00:00:80:f0:00"

        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineOne) == len(lineOne)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineTwo) == len(lineTwo)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineThree) == len(lineThree)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineFour) == len(lineFour)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineFive) == len(lineFive)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineSix) == len(lineSix)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineSeven) == len(lineSeven)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineEight) == len(lineEight)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, lineNine) == len(lineNine)
        assert dev.ctrl_transfer(0x21, 9, 0, 0, commit) == len(commit)
    def scratch_code(self):
        #ret = dev.ctrl_transfer(0xC0, CTRL_LOOPBACK_READ, 0, 0, len(msg))
        #sret = ''.join([chr(x) for x in ret])
        #assert sret == msg


        for ep in intf:
            print('\t\t' + str(ep.bEndpointAddress) + '\n')


        # ep.write('test')

        c = 1
        for cfg in dev:
            print 'config', c
            print 'Interfaces', cfg.bNumInterfaces
            for i in range(cfg.bNumInterfaces):
                if dev.is_kernel_driver_active(i):
                    dev.detach_kernel_driver(i)
                print i
            c+=1


def main():
    print("Main")
    lineOne = "02:03:02:00:00:08:0f:00"
    lineTwo = "02:04"
