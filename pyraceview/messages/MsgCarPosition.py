from ..percar import PerCarPositionData
from ..util import BitBuffer
from numpy import uint32


class MsgCarPosition(object):
    CAR_POSITION_CAR_BITS = uint32(8)
    CAR_POSITION_VITC_TIME_BITS = uint32(32)

    def __init__(self, msg_header, byte_array):
        self._car_data = [] # PerCarPositionData
        self._car_reverse_lookup = {}

        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        self._number_of_cars = bit_buffer.get_bits(self.CAR_POSITION_CAR_BITS)
        self._vitc_time = bit_buffer.get_bits(self.CAR_POSITION_VITC_TIME_BITS)
        i = 0

        while i < self._number_of_cars:
            position = PerCarPositionData(bit_buffer)
            self._car_data.append(position)
            self._car_reverse_lookup[position.car_id] = position
            i += 1

    @property
    def car_data(self):
        return self._car_data

    def get_car_by_id(self, car_id):
        return self._car_reverse_lookup[car_id]

    @property
    def vitcTime(self):
        return self._vitc_time

    @property
    def number_of_cars(self):
        return self._number_of_cars
