from numpy import uint32
from ..util import BitBuffer, ByteArray


TRACKCONFIG_BITS_ORIGIN_X = uint32(32)
TRACKCONFIG_BITS_ORIGIN_Y = uint32(32)
TRACKCONFIG_BITS_ORIGIN_Z = uint32(32)
TRACKCONFIG_BITS_TRACK_NAME = uint32(64)


class MsgTrackConfig(object):
    def __init__(self, msg_bytes):
        byte_array = ByteArray(msg_bytes)
        bit_buffer = BitBuffer(byte_array)
        bit_buffer.set_position(7)
        self.local_origin_x = int(bit_buffer.get_bits(TRACKCONFIG_BITS_ORIGIN_X))
        self.local_origin_y = int(bit_buffer.get_bits(TRACKCONFIG_BITS_ORIGIN_Y))
        self.local_origin_z = int(bit_buffer.get_bits(TRACKCONFIG_BITS_ORIGIN_Z))
        self.track_name = byte_array.read_utf_bytes(
            TRACKCONFIG_BITS_TRACK_NAME // uint32(8)
        )
