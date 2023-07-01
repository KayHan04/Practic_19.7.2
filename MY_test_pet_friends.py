from api import PetFriends
from settings import valid_email, valid_password, sec_email
import os
import  pytest
pf = PetFriends()
import datetime

def test_get_api_with_valid_data(auth_key,email = valid_email, password = valid_password):
    status,resault = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in resault

def test_add_new_pet_with_valid_data(auth_key,name='Бобкин',animal_type='Кот',
                                     age='3',pet_photo='images/Cat_2.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)

    # _, auth_key =pf.get_api_key(valid_email,valid_password)

    status, result = pf.add_new_pet(auth_key,name,animal_type,age,pet_photo)

    assert status == 200

    assert result['name'] == name


def test_update_pet_info(auth_key,name='Бобкинсбир',animal_type='КотЭ',age='5'):

    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key,'my_pets')

    if len(my_pets['pets']) > 0:

        status, result = pf.update_pet_info(auth_key,my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name

    else:
        raise Exception('Not pets')


def test_successful_delete_self_pet(auth_key):

    # _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][1]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_get_api_key_for_false_email(auth_key,email=sec_email, password=valid_password):

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not  in result


def test_add_new_pet_with_255_symblname(auth_key,name='Ae00sSUNE5WImzMwjw02eN3tsGN2SSGg05jXVO7pLLqJ9WxeIyDHdQ5qN2WDhID6Zo8r2vQSiDb2z7Rl4z5wfBlwFL1JuZ5TmOoa15RrVP7V6X56xvQd68U54N7A845UzUkZJXEp0Slvdvhbe9vfo3w2BxQC7ZcCNGNxgdWSrI95e6LoYZCrCIMNvOdxDY7KvBTP3lBIof8y82r2MSg6AmOlKQmRciQEhIbmCeskGXBM7fe88BubhMTxpAC8liWi', animal_type='Кот',
                                     age='3', pet_photo='images/Cat_2.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200

    if len(name) > 255:

        print('Недопустимое количество строк')

@pytest.mark.skip
def test_add_pet_without_photo(auth_key,name='Либик',animal_type ='крокодилиус',age='32'):

    # _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200

    assert result['name'] == name

@pytest.mark.xfail
def test_add_photo_pet(auth_key,pet_photo='images/Cat_2.jpg'):

    pet_photo = os.path.join(os.path.dirname(__file__),pet_photo)

    # _, auth_key =pf.get_api_key(valid_email,valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status, result = pf.add_photo_pet(auth_key,pet_id,pet_photo)

    assert status == 200

    assert result['pet_photo'] == pet_photo