import pytest

# количество циклов прохождения опроса
num_polls = 23

#Выбрать портал для текста
url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'

def test_suite_polls():
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Structure\\create_departament_cls.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\class\\test_create_polls_class.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\class\\test_compl_polls_class.py'])
