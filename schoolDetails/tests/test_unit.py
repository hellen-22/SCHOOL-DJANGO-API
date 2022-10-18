import pytest 
from rest_framework import status
from model_bakery import baker

from schoolDetails.models import Unit


@pytest.fixture
def create_unit(api_client):
    def do_unit(unit):
        return api_client.post('/school_details/unit/', unit)
    return do_unit

@pytest.fixture
def update_unit(api_client):
    def do_unit(unit):
        unit_ = baker.make(Unit)
        return api_client.patch(f'/school_details/unit/{unit_.id}/', unit)
    return do_unit


@pytest.fixture
def delete_unit(api_client):
    def do_unit(unit):
        unit_ = baker.make(Unit)
        return api_client.delete(f'/school_details/unit/{unit_.id}/', unit)
    return do_unit


@pytest.mark.django_db
class TestCreateUnit():
    def test_is_anonymous_return_403(self, create_unit, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_unit({'unit_code':'BIT 333', 'unit_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_unit):
        authenticate_user(is_staff=False)

        response = create_unit({'unit_code':'BIT 333', 'unit_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, create_unit, authenticate_user):
        authenticate_user()

        response = create_unit({'unit_code':'', 'unit_name': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['unit_code'] is not None
        assert response.data['unit_name'] is not None
        

    def test_if_data_is_valid_return_201(self, create_unit, authenticate_user):
        authenticate_user()

        response = create_unit({'unit_code':'BIT 333', 'unit_name': 'School of Computing'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['unit_code'] is not None
        assert response.data['unit_name'] is not None


@pytest.mark.django_db
class TestRetrieveUnit():
    def test_if_unit_exists_return_200(self, api_client):
        unit = baker.make(Unit)

        response = api_client.get(f'/school_details/unit/{unit.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': unit.id,
            'unit_code': unit.unit_code,
            'unit_name': unit.unit_name
        }


@pytest.mark.django_db
class TestUpdateUnit():
    def test_if_is_not_admin_return_403(self, authenticate_user, update_unit):
        authenticate_user(is_staff=False)

        response = update_unit({'unit_code':'BIT 333', 'unit_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_is_admin_return_200(self, authenticate_user, update_unit):
        authenticate_user()

        response = update_unit({})

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_valid_return_200(self, authenticate_user, update_unit):
        authenticate_user()

        response = update_unit({'unit_code':'BIT 333', 'unit_name': 'School of Computing'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['unit_code'] is not None
        assert response.data['unit_name'] is not None


    def test_if_data_is_invalid_return_400(self, authenticate_user, update_unit):
        authenticate_user()

        response = update_unit({'unit_code':'', 'unit_name': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['unit_code'] is not None
        assert response.data['unit_name'] is not None


@pytest.mark.django_db
class TestDeleteUnit():
    def test_if_is_admin_return_204(self, authenticate_user, delete_unit):
        authenticate_user()
        unit = {
            'id': 1,
            'unit_code': 'BIT 333',
            'unit_name':'School'
        }

        response = delete_unit(unit)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    def test_if_is_not_admin_return_403(self, authenticate_user, delete_unit):
        authenticate_user(is_staff=False)

        unit = {
            'id': 1,
            'unit_code': 'BIT 333',
            'unit_name':'School'
        }

        response = delete_unit(unit)

        assert response.status_code == status.HTTP_403_FORBIDDEN

