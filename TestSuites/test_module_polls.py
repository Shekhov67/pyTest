import pytest
def test_suite_polls():
    pytest.main(['Polls/class/test_create_polls_class.py'])
    pytest.main(['Polls/class/test_compl_polls_class.py'])