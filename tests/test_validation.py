import pytest

import main


class TestValidation:
    def test_create_parser(self):
        parser = main.create_parser()
        args = parser.parse_args(["--files", "fix_data_1.csv", "--report", "clickbait"])
        assert args.files == ["fix_data_1.csv"]

    def test_create_parser_2(self):
        parser = main.create_parser()
        args = parser.parse_args(["--files", "fix_data_1.csv", "--report", "clickbait"])
        assert args.report == "clickbait"

    @pytest.mark.parametrize(
        "params",
        [
            ("--files", "--report"),
            ("--files", "fix_data_1.csv"),
            ("--files", "fix_data_1.csv", "--report"),
            ("--files", "fix_data_1.csv", "--report", "clickbait"),
        ])
    def test_validate_files_names(self, params):
        parser = main.create_parser()
        try:
            parser.parse_args(params)
        except SystemExit as exc_info:
            assert exc_info.code == 2

    @pytest.mark.parametrize(
        "params",
        [
            "fix_data_1csv",
            "fix_data_1.cs",
        ])
    def test_validate_files_format(self, params):
        with pytest.raises(ValueError):
            main.validate_files_format(params)

    @pytest.mark.parametrize(
        "params",
        [
            ['Я бросил IT и стал фермером', 18.2, 35, 45200, 1240, 4.2],
        ])
    def test_validate_headers(self, params):
        with pytest.raises(ValueError):
            main.validate_headers(params)
