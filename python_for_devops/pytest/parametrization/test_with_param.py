import pytest
from my_module import string_to_bool


true_values = ['yes', '1', 'YeS', 'TRUE', 'TruE', 'True', 'true']

class TestStrToBool(object):

    @pytest.mark.parametrize('value', true_values)
    def test_it_detects_truish_strings(self, value):
        assert string_to_bool(value)


