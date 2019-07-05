from numpy import uint32, int32


class BitBuffer(object):

    def __init__(self, byte_array):
        self.buffer = byte_array
        self.bit_position = uint32(0)

    def extract_bits_from_byte(self, byte, position, size):
        bit_mask = 255 >> 8 - size
        bits = byte >> 8 - position - size
        bits = bits & bit_mask
        return bits

    @staticmethod
    def make_bits_signed(value, size):
        return int32(value << 32 - size) >> 32 - size

    def set_position(self, position):
        self.buffer.position = position

    def get_bits(self, size):
        bits_remaining = size
        unpacked_value = 0

        # If the bit position is not 0, then we need to extract bits from the current
        # partially unpacked byte
        if self.bit_position != 0:
            extract_size = uint32(min(8 - self.bit_position, bits_remaining))
            extracted_bits = uint32(self.extract_bits_from_byte(self.current_byte, self.bit_position, extract_size))
            unpacked_value = uint32(unpacked_value | extracted_bits)
            self.bit_position = self.bit_position + extract_size
            self.bit_position = self.bit_position % 8
            bits_remaining = bits_remaining - extract_size

        while bits_remaining >= 8:
            self.current_byte = 255 & self.buffer.read_unsigned_byte()

            unpacked_value = uint32(unpacked_value << 8 | self.current_byte)
            bits_remaining = bits_remaining - 8

        if bits_remaining > 0:
            self.current_byte = 255 & self.buffer.read_unsigned_byte()

            extracted_bits = uint32(self.extract_bits_from_byte(self.current_byte, 0, bits_remaining))
            unpacked_value = uint32(unpacked_value << bits_remaining | extracted_bits)
            self.bit_position = self.bit_position + bits_remaining
            bits_remaining = 0

        return unpacked_value
