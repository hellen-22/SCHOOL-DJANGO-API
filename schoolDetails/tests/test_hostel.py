import pytest 
from rest_framework import status
from model_bakery import baker

from schoolDetails.models import Hostel


@pytest.fixture
def create_hostel(api_client):
    def do_hostel(hostel):
        return api_client.post('/school_details/hostel/', hostel)
    return do_hostel

@pytest.fixture
def update_hostel(api_client):
    def do_hostel(hostel):
        hostel_ = baker.make(Hostel)
        return api_client.patch(f'/school_details/hostel/{hostel_.id}/', hostel)
    return do_hostel


@pytest.fixture
def delete_hostel(api_client):
    def do_hostel(hostel):
        hostel_ = baker.make(Hostel)
        return api_client.delete(f'/school_details/hostel/{hostel_.id}/', hostel)
    return do_hostel


@pytest.mark.django_db
class TestCreateHostel():
    def test_is_anonymous_return_403(self, create_hostel, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_hostel({'hostel_name': 'School of Computing', 'capacity': 10})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_hostel):
        authenticate_user(is_staff=False)

        response = create_hostel({'hostel_name': 'School of Computing', 'capacity': 10})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, create_hostel, authenticate_user):
        authenticate_user()

        response = create_hostel({'hostel_name':'', 'capacity': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['hostel_name'] is not None
        assert response.data['capacity'] is not None
        

    def test_if_data_is_valid_return_201(self, create_hostel, authenticate_user):
        authenticate_user()

        response = create_hostel({'hostel_name': 'School of Computing', 'capacity': 10})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['hostel_name'] is not None
        assert response.data['capacity'] is not None


@pytest.mark.django_db
class TestRetrieveHostel():
    def test_if_hostel_exists_return_200(self, api_client):
        hostel = baker.make(Hostel)

        response = api_client.get(f'/school_details/hostel/{hostel.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': hostel.id,
            'hostel_name': hostel.hostel_name,
            'capacity': hostel.capacity
        }


@pytest.mark.django_db
class TestUpdateHostel():
    def test_if_is_not_admin_return_403(self, authenticate_user, update_hostel):
        authenticate_user(is_staff=False)

        response = update_hostel({'hostel_name': 'School of Computing', 'capacity': 0})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_is_admin_return_200(self, authenticate_user, update_hostel):
        authenticate_user()

        response = update_hostel({})

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_valid_return_200(self, authenticate_user, update_hostel):
        authenticate_user()

        response = update_hostel({'hostel_name': 'School of Computing', 'capacity': 10})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['hostel_name'] is not None
        assert response.data['capacity'] is not None


    def test_if_data_is_invalid_return_400(self, authenticate_user, update_hostel):
        authenticate_user()

        response = update_hostel({'hostel_name': '', 'capacity': ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['hostel_name'] is not None
        assert response.data['capacity'] is not None


@pytest.mark.django_db
class TestDeleteHostel():
    def test_if_is_admin_return_204(self, authenticate_user, delete_hostel):
        authenticate_user()
        unit = {
            'id': 1,
            'hostel_name': 'School',
            'capacity': 0
        }

        response = delete_hostel(unit)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    def test_if_is_not_admin_return_403(self, authenticate_user, delete_hostel):
        authenticate_user(is_staff=False)

        unit = {
            'id': 1,
            'hostel_name': 'School',
            'capacity': 0
        }

        response = delete_hostel(unit)

        assert response.status_code == status.HTTP_403_FORBIDDEN

