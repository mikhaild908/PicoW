class EPDImage:
    """Display full-screen, 1-bit image buffers with either 2.13 V4 driver."""

    def __init__(self, display_driver):
        self.display_driver = display_driver

    def display_bytes(self, image, partial=False, invert=False):
        """Display a driver-native framebuffer byte array.

        The buffer must be the same size and byte layout as the selected
        driver's ``buffer``. Use the landscape driver's layout for landscape
        images; its display controller expects a different byte order.
        """
        image_buffer = bytearray(image)
        expected_size = len(self.display_driver.buffer)
        if len(image_buffer) != expected_size:
            raise ValueError(
                "Image buffer must be {} bytes; got {}".format(
                    expected_size, len(image_buffer)
                )
            )

        if invert:
            for index in range(expected_size):
                image_buffer[index] ^= 0xff

        if partial:
            self.display_driver.displayPartial(image_buffer)
        else:
            self.display_driver.display(image_buffer)
