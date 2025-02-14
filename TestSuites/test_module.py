import pytest

# количество циклов прохождения опроса
num_polls = 15

#Выбрать портал для текста
url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'

def test_suite_polls():
    #pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Structure\\create_departament_cls.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\poll_ver2\\test_create_polls_ver2.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\poll_ver2\\test_compl_polls_ver2.py'])
