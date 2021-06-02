import csv
import pathlib
import struct
import logging
from typing import List

from src.helper.helper import get_fixed_len, get_column_names


# newline "\r\n" charactor length 
NEWLINE_CHAR_LEN=2


def parse_and_gen_csv(input_file: str, output_csv: str) -> None:
    """Parse fixed width file and output as csv file.
    """
    if not pathlib.Path(input_file).exists():
        raise FileNotFoundError(input_file)

    # get offsets, column names and total fixed length each row
    # (the order of column and offset exactly matches spec.json)
    offsets = get_fixed_len()
    column_names = get_column_names()
    fixed_len = sum(offsets)

    with open(input_file, "rb") as reader, open(output_csv, "w", encoding="utf-8") as csv_file:
        # create writer
        writer = csv.writer(csv_file, delimiter=",")

        # frist line must be the header
        header = reader.readline()[:-NEWLINE_CHAR_LEN]
        if _split_decode_cp1252(offsets, header) == column_names:
            writer.writerow(column_names)
        else: # found none blank line before finding header
            raise RuntimeError("Wrong Header or not found!")

        for row in reader:
            # read and remove blank line
            body = row[:-NEWLINE_CHAR_LEN]
            if not body:
                logging.warning("Skip an empty line.")
                continue

            # check boundary
            if not len(body) == fixed_len:
                raise RuntimeError(f"Wrong fixed width! Expect {fixed_len} but got {len(body)}.")

            # write body
            writer.writerow(_split_decode_cp1252(offsets, body))


def _split_decode_cp1252(field_width: List[int], row: bytes) -> List[bytes]:
    """Decode and return each field in a list.
    """
    fmtstr = " ".join([str(offset)+"s" for offset in field_width])
    return [ e.decode("cp1252") for e in struct.unpack(fmtstr, row)]
    

if __name__ == "__main__":
    import sys
    parse_and_gen_csv(sys.argv[1], sys.argv[2])
