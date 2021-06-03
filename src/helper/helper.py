import json
from typing import List, Dict

from src import constants


def get_colume_and_offset() -> Dict[str, int]:
    """Read spec json and return a dict as {"column_name":offset}.
    """
    with open(constants.spec_json_path, 'r') as f:
        spec = json.load(f)
        return dict(zip(spec['ColumnNames'], list(map(int, spec['Offsets']))))


def charactor_set() -> List[str]:
    """Return a list of "Windows-1252" (cp1252) charactors.
    """
    return [charactor for lines in constants.charactor_subset.splitlines() for charactor in lines.split(" ")]


def get_column_names() -> List[str]:
    """Return each column name in a list according to spec.json.
    """
    return [k for k,_ in get_colume_and_offset().items()]


def get_fixed_len() -> List[int]:
    """Return offset of each field in a list.
    """
    return [v for _,v in get_colume_and_offset().items()]


def get_payload(orig: List[str]) -> List[str]:
    """Remove whitepace (right/left/center aligned) of each field and return the list. 
    """
    return [e.strip() for e in orig]


def encode_cp1252(inputs: str) -> bytes:
    """Return binary string with cp1252 encoding. 
    """
    return inputs.encode("cp1252")


def decode_cp1252(inputs: bytes) -> str:
    """Return string with cp1252 decoding.
    """
    return inputs.decode("cp1252")


if __name__ == "__main__":
    pass
