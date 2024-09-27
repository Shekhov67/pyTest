import pytest
def test_suite_polls():
    pytest.main(['class/test_create_polls_class.py'])
    pytest.main(['class/test_compl_polls_class.py'])