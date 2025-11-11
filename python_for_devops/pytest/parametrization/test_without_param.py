from my_module import string_to_bool


class TestStringToBool(object):

    def test_it_detects_lowercase_yes(self):
        assert string_to_bool('yes')

    def test_it_detects_odd_case_yes(self):
        assert string_to_bool('YeS')

    def test_it_detects_uppercase_yes(self):
        assert string_to_bool('YES')

    def test_it_detects_positive_str_integers(self):
        assert string_to_bool('1')

    def test_it_detects_true(self):
        assert string_to_bool('true')

    def test_it_detects_true_with_trailing_spaces(self):
        assert string_to_bool('true ')

    def test_it_detects_true_with_leading_spaces(self):
        assert string_to_bool(' true')
    