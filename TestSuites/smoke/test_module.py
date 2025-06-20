import pytest

# количество циклов прохождения опроса
num_polls = 15

#Выбрать портал для текста
url = 'https://staging.connectable.site/'
#url = 'https://connectable.site/'
#url = 'https://intranetable.team/'

def test_suite_polls():
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Structure\\create_departament_cls.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\playwrith\\test_create_polls_playwrigth.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\Polls\\playwrith\\test_compl_poll_playwrigth.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\wall\\test_create_post.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\wall\\test_create_comments.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\wall\\test_like.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\IDP\\test_create_and_delete.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\IDP\\test_create_idp.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\IDP\\test_delete.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Events\\test_create_event.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Events\\test_edit_event.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Events\\test_delete_event.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Group\\test_group_create.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_add_achiv.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_add_achiv_coins.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_add_coins.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_create_achiv.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_create_shop_item.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\API\\Shop\\test_settings.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\SuperAdmin\\test_create_new_client_and_delete.py'])
    pytest.main(['C:\\Users\\shehs\\PycharmProjects\\pyTest\\SuperAdmin\\test_clone_connectable.py'])
