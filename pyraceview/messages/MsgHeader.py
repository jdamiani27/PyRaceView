from ..util import ByteArray


class MsgHeader(object):
    def __init__(self, msg_bytes):
        msg_ba = ByteArray(msg_bytes)
        self.sync = int(msg_ba.read_unsigned_short())
        self.clock = int(msg_ba.read_unsigned_short())
        self.size = int(msg_ba.read_unsigned_short())
        self.byte_type = chr(msg_ba.read_unsigned_byte())

    def __str__(self):
        return "Sync: {}, Clock: {}, Size: {}, Type: {}".format(
            self.sync, self.clock, self.size, self.byte_type
        )
