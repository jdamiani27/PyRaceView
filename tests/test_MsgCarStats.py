import pytest
from pyraceview.messages import MsgCarStats


raw = (
    b"\xab\xcd\x1e\xa4\x01\x81a\x04y\xc2q&$8\xee\n\xdb\xe1\x9c(\x9f\xf0&9w\n\xdb!"
    b"\x9c@\x9f\xe4\x169\xa0\n\xde\xe1\x9c\\\x9f\xdc\x088\xc5\n\xd9a\x9c\x84\x9f"
    b"\xcc(8\xf5\x0b\x15\xc1\x9c\xd8\x9f\xac\x129p\n\xe6\x01\x9d\x14\x9f\x94\x048"
    b"\xbe\n\xd4\x81\x9d(\x9f\x8c\x1c8\x9c\n\xf9A\x9dt\x9fpT8\xd3\n\xf6\xa1\x9d"
    b'\x90\x9fd\x0c9%\x0b\n\xc1\x9d\xac\x9fX`9\x8b\x0b\x03\x81\x9d\xa8\x9f\\"8'
    b"\xb8\x0b\x1b\x01\x9d\xbc\x9fT\x029U\n\xf8A\x9d\xcc\x9fL\x189\x17\x0b\x06"
    b"\xe1\x9d\xe8\x9f@\xbe9G\n\xfcA\x9d\xfc\x9f<R9%\x0b\x0b\xe1\x9e\x08\x9f4\x148"
    b"\xee\x0b\x00!\x9e\x14\x9f0D8\xe1\x0b\x16A\x9e8\x9f$,9\x17\x0b&\xa1\x9eT\x9f"
    b"\x18V8\xbe\x0b(\xc1\x9ep\x9f\x0c08\x8f\x0b-\x01\xa0\xf8\x9e\x18L8z\x0b0a\xa1"
    b"\x18\x9e\x0c\xb09\x10\x0b/\xa1\xa1d\x9d\xf0@8/\x0b#\xc1\xa1d\x9d\xec\x068"
    b"\xb8\x0b\x16\x81\xa1t\x9d\xe8\x1a86\x0b>\xe1\xa1\x84\x9d\xe4*8l\x0b4a\xa1"
    b"\x98\x9d\xd8H7\xe4\x0bG\x81\xa1\xac\x9d\xd4\x108s\x0b%a\xa1\xb8\x9d\xccJ8"
    b"\xee\x0b\x19A\xa1\xbc\x9d\xcc^8_\x0b&A\xa1\xd4\x9d\xc4\x018\r\x0b7\xe1\xa1"
    b"\xf0\x9d\xb8f6r\x0bb\xc1\xa58\x9c|h7\x8b\x0bZa\xa8T\x9bXj6P\x0bf\xc1\xa9L"
    b"\x9a\xfc67\xf1\x0be\x01\xab\xa0\x9a(\x9a7\t\x0b^a\xac\xa4\x99\xc8\x1e7v"
    b"\x0bYb.\xd0u\xf4\xab\xcd\x1e\xa4\x00tCd&\x01\x00\x00\x02?\x18\x04@\xb0\x06"
    b"\x0f\xf0\x08A`\x0c?X\x10\x0cH\x12@\x88\x14?\x88\x16@\xb8\x18?\xb8\x1a\x0ep"
    b'\x1c? \x1e\x00\x00"\x0f\xa0$A\x10&A\xa8(>\xf8*\x12\xb0,@\xd80?\xc06\x028@\t'
    b"\x98D\n\x88H\x08\x98J\x11\xe8L\t`R\x15\x00T?\xf0V\x0bh^\x0b``\x13\xe8f\x00Ph"
    b"\x00\x00j\x00\x00\x9a\x02\xd0\xb0?\xa8\xbe\x0f\xd0\xab\xcd\x1e\xa4\x00\x1cl"
    b"\x04y\xc2q%\x02\x02\x0cC\x98\x04\x0b\xaf\x81Z\x905!\x876\x0c>!l\xa0\x00\x00$"
    b"\xab\xcd\x1e\xa6\x01\xcdW&\x04y\xc6X\x01\x05t\x80\xfd\x11\x051\x05 \xcdF\x02"
    b"\xfa\x86?\x07\x91\roD\xe6\xfd\x00\x04\x00Q>\xdda\x13\xd0D\xe9\xa0\xe0\x06\xfe"
    b"\x94\x00\xd7A\x06O\xe9\x03qd\x08\x07\x1e\x00y\x81\x0b\xb2k\x06\x08\xca\x0c"
    b"\xfc\xa6\xfe\xd7\x91\x13\x8f\xcc\xe9\x1f\x00\x10\x02\xb3\x01\x17\xd1\x06\xf0/"
    b"\x080T\x12\x01\xc6~\xf4\xf1\x14px\xea\x81\x86\x14\xf8\xeb\xff\xc7\xf1\x06\x8d"
    b"\x97\x037\x96\x16\x06\x0e\x00\xe3\xe1\x05\xb1\xad\x1b\xac0\x18\xf9\x90?I\xc1"
    b"\x06\x0e\x12\xeb\xdb\x06\x1a\xff\xac@\xebA\x06/\xed\x03\xb1l\x1c\xffG~\xd2"
    b'\xa1\x140 \xe9\xa0d\x1e\xfa\xe8@\x82\x01\x08\x8f1\x082\xa8"\xfbk\xfe\xed\x01'
    b"\x0f\xcf\xa8\xe9]\xf8$\x03\xbd\x01\x19a\x07/\xdf\x11/\x9e&\x05\x00\x81\na\x05"
    b"\xf0\x8f\x1em\xfe(\x05n\x7f\x7fQ\x10\x10\xde\xee\xa3\xca*\x00\xebA\x02\x01"
    b"\x06\xcf\xed\x04q^,\xfa\x80\xc0ra\x08\xaf_\x12s\x0e0\xf8\xfb\x7f\xf4!\t\x8d"
    b"\xb9\x0c\x16`6\x00\x02>\xdb1\x130<\xe9\xa0\xc2@\xfe\x1e\xc0\xcfQ\x06\xaf\xeb"
    b"\x03\xb1hD\xf9w@=!\x0c\xee1\x12\xd4^H\x01\xf7\xc1\x11\xe1\x06\x8f\xed\x04p"
    b"\xe2J\x03\x1f\xc1\x1f\xc1\tP\x17\nP@L\xf9\x8e\x005\xc1\x05N1\x12\xd4pR\xf8"
    b"\xf8\xbf\x9d\x11\x06\x8d\xa0\xf9\x18\xc2T\xfd\xca>\xd2\x11\x12\xcf\xe8\xe9?"
    b"\x8cV\xfb\xaa\xc0\x9a\xc1\x06\xaf\xbb\x05\x12 ^\x04]A\x16!\x07\x901\x19N\xee`"
    b"\xfc^>\xe0Q\x0f\xef\xcc\xe8\x9e\xaef\x06\xb9\xbf\xe9\xb1\t\xd1\x9c\xf5E\x9ah"
    b"\x05\x19\x7fh!\x12\xb0\xd4\xee#\\j\xfa\x8c\xff\x0f\x91\x07\xefD\xe6\xfc\xf2"
    b"\x9a\xf9\x05\xc0\x0bq\x0e\xad\xcd\x0eu\xd6\xb0\xfd\x81\x80\xc3q\x06\xcf\xeb"
    b"\x03\xd1\\\xbe\xf9\n\xffz\xd1\x0bM\xbc\xf1\xd9\xac"
)


@pytest.fixture
def msg_car_stats():
    return MsgCarStats(raw)


def test_header(msg_car_stats):
    header = msg_car_stats.header
    assert (
        header.sync == 43981
        and header.clock == 7844
        and header.size == 385
        and header.byte_type == "a"
    )


def test_timecode(msg_car_stats):
    timecode = msg_car_stats.timecode
    assert timecode == 75088497


def test_number_of_cars(msg_car_stats):
    num_cars = msg_car_stats.num_cars
    assert num_cars == 38
