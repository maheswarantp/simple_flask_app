
import blynklib
import random

BLYNK_AUTH = '9aLW3XYVbec0CsSQv5dUFQrk4hFeoYNp'
#define BLYNK_TEMPLATE_NAME "Quickstart Template"
#define BLYNK_AUTH_TOKEN "9aLW3XYVbec0CsSQv5dUFQrk4hFeoYNp"'

# initialize blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

READ_PRINT_MSG = "[READ_VIRTUAL_PIN_EVENT] Pin: V{}"


# register handler for virtual pin V11 reading
@blynk.handle_event('read V3')
def read_virtual_pin_handler(pin):
    print(READ_PRINT_MSG.format(pin))
    blynk.virtual_write(pin, random.randint(0, 255))


###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()