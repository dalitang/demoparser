from os import write
import random

from src.helper.helper import charactor_set, get_colume_and_offset, get_fixed_len, encode_cp1252


def _gen_records(num_line: int) -> bytes:
    """Generate {num_line} rows of records randomly.
    """
    fixed_len = sum(get_fixed_len())
    for _ in range(num_line):
        row_str = "".join(map(str, random.choices(charactor_set(),k=fixed_len)))
        yield row_str


def _gen_header() -> bytes:
    """Generate a header for testing input file.
    """
    header_str = "".join(map(str, [keys.ljust(value) for keys, value in get_colume_and_offset().items()]))
    return header_str


def _gen_blank_line() -> str:
    """Generate fixed length blank line for testing.
    """
    fixed_len = sum(get_fixed_len())
    return " " * fixed_len


def gen_file_cp1252(filename: str, num_line: int) -> None:
    """Generate a fixed width file using the spec with num_line of records.
    """
    with open(filename, "wb") as f:
        header = encode_cp1252(_gen_header()+"\r\n")
        f.write(header)
        for row in _gen_records(num_line):
            body = encode_cp1252(row+"\r\n")
            f.write(body)


if __name__ == "__main__":
    import sys
    gen_file_cp1252(sys.argv[1], int(sys.argv[2]))
