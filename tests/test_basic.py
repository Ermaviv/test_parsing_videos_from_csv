import main

# python main.py --files stats1.csv stats2.csv --report clickbait


class TestValidation:

    def test_extract_necessary_data(
            self,
            file_names,
            input_data,
            extract_output, fix_ctr
    ):
        headers, report_data_unsort, ctr_order = main.extract_necessary_data(
            [
                file_names['FILE_1'], file_names['FILE_2']
            ]
        )
        assert headers == input_data[0]
        assert report_data_unsort == extract_output
        assert ctr_order == fix_ctr

    def test_sort_data(self, fix_ctr, extract_output, sort_extract_data):
        check_sort_data = main.sort_data(fix_ctr, extract_output)
        assert check_sort_data == sort_extract_data

    def test_write_to_file(self, file_names, sort_extract_data):
        main.write_to_file(file_names['REPORT_test'], sort_extract_data)
        with (open(
                file_names['REPORT_test'], 'r', encoding='utf-8') as test_file,
            open(file_names['REPORT_fix'], 'r', encoding='utf-8') as fix_file):
            assert test_file.read() == fix_file.read()
