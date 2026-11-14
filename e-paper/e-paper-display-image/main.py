from ePaper213v4 import EPD_2in13_V4_Portrait
from ePaperImage import EPDImage
import utime
from lauren_image_data import image_bytes as lauren_image_bytes
from polgas_image_data import image_bytes as polgas_image_bytes

epd = EPD_2in13_V4_Portrait()
display = EPDImage(epd)

display.display_bytes(lauren_image_bytes)
epd.delay_ms(2000)
epd.Clear()

display.display_bytes(polgas_image_bytes)
epd.delay_ms(2000)
epd.Clear()

epd.fill(0xff)
epd.text("sleeping in 2s", 0, 70, 0x00)
epd.display(epd.buffer)
epd.delay_ms(2000)
epd.Clear()

epd.sleep()