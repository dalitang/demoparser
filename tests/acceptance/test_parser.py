import pytest

from src.parser.parser import parse_and_gen_csv


@pytest.mark.parametrize(
    "input_file, output_file",
    [
        ("./tests/data/input_normal_left_aligned.dat", "./tests/data/output_normal_left_aligned.csv"),
        ("./tests/data/input_normal_right_aligned.dat", "./tests/data/output_normal_right_aligned.csv"),
        ("./tests/data/input_normal_center_aligned.dat", "./tests/data/output_normal_center_aligned.csv"),
        ("./tests/data/input_header_only.dat", "./tests/data/output_header_only.csv"),
    ]
)
def test_parser_normal(input_file, output_file):
    try:
        parse_and_gen_csv(input_file, output_file)
    except Exception as e:
        assert False, f"parse_and_gen_csv() raise an exception {e}"


@pytest.mark.parametrize(
    "input_file, output_file",
    [
        ("./tests/data/input_len_err_long.dat", "null"),
        ("./tests/data/input_len_err_short.dat", "null"),
    ]
)
def test_parser_length_error(input_file, output_file):
    with pytest.raises(Exception) as e:
        parse_and_gen_csv(input_file, output_file)
    assert e.type == RuntimeError
    assert "Wrong fixed width!" in str(e.value)


@pytest.mark.parametrize(
    "input_file, output_file",
    [
        ("./tests/data/input_header_missing.dat", "null")
    ]
)
def test_header(input_file, output_file):
    with pytest.raises(Exception) as e:
        parse_and_gen_csv(input_file, output_file)
    assert e.type == RuntimeError
