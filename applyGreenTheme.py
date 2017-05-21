import usb.core
import usb.util
dev = usb.core.find(idVendor=0x187c, idProduct=0x0527)
endpoint = dev[0][(0,0)][0]
config = dev.get_active_configuration()
intf = config[(0,0)]
if dev.is_kernel_driver_active(1) is True:
    dev.detach_kernel_driver(1)
    dev.detach_kernel_driver(0)
print("placeholder")
usb.util.claim_interface(dev, 0)
#dev.set_configuration(config)
f = open('afx-allred')
lines = f.readlines()
for line in lines:
    # add handler for lines that have comments
    testLine = line.replace(':', r'\x')
    testLine = testLine.replace('\n', '')
    testLine = r"\x{0}".format(testLine)
    message = testLine.decode("string-escape")
    dev.ctrl_transfer(0x21, 9, 0, 0, message)