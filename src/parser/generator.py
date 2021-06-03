from enum import Enum
import random

from src.helper.helper import charactor_set, get_colume_and_offset, get_fixed_len, encode_cp1252


def _gen_field(len: int) -> str:
    """Generate a ramdon field according to length.
    """ 
    return "".join(map(str, random.choices(charactor_set(),k=len)))


def _gen_row(alignment: str) -> str:
    """Generate a row with given alignment (right/left/center) for each field 
    """
    row = [f"{f'{_gen_field([v, v-2][v-2 > 0])}' : {alignment}{v}}" for _, v in get_colume_and_offset().items()]
    return "".join(row)


def _gen_header(alignment: str) -> str:
    """Generate a header for testing input file according to alignment(left/right/center).
    """
    header = [f"{f'{keys}' : {alignment}{value}}" for keys, value in get_colume_and_offset().items()]
    return "".join(header)


def _gen_blank_line() -> str:
    """Generate fixed length blank line for testing.
    """
    fixed_len = sum(get_fixed_len())
    return " " * fixed_len


def gen_file_cp1252(filename: str, num_line: int, alignment: str) -> None:
    """Generate a fixed width file using the spec with num_line of records.
    """
    with open(filename, "wb") as f:
        header = encode_cp1252(_gen_header(alignment)+"\r\n")
        f.write(header)
        for _ in range(num_line):
            body = encode_cp1252(_gen_row(alignment)+"\r\n")
            f.write(body)


class Alignment(Enum):
    LEFT = '<'
    RIGHT = '>'
    CENTER = '^'


if __name__ == "__main__":
    import sys
    # print(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    gen_file_cp1252(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    # print(_gen_header(Alignment.LEFT.value))
    # print(_gen_header(Alignment.RIGHT.value))
    # print(_gen_header(Alignment.CENTER.value))
    # print(_gen_row(Alignment.LEFT.value))
    # print(_gen_row(Alignment.RIGHT.value))
    # print(_gen_row(Alignment.CENTER.value))
