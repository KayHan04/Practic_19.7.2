import pytest
from settings import  valid_email,valid_password
from api import PetFriends
import datetime
pf = PetFriends()
@pytest.fixture
def auth_key():
    _, key = pf.get_api_key(valid_email, valid_password)
    return key

@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print (f"\nТест шел: {end_time} - {start_time}")
