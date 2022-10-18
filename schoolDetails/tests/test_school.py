import pytest 
from rest_framework import status
from model_bakery import baker

from schoolDetails.models import School


@pytest.fixture
def create_school(api_client):
    def do_school(school):
        return api_client.post('/school_details/school/', school)
    return do_school

@pytest.fixture
def update_school(api_client):
    def do_school(school):
        school_ = baker.make(School)
        return api_client.patch(f'/school_details/school/{school_.id}/', school)
    return do_school


@pytest.fixture
def delete_school(api_client):
    def do_school(school):
        school_ = baker.make(School)
        return api_client.delete(f'/school_details/school/{school_.id}/', school)
    return do_school


@pytest.mark.django_db
class TestCreateSchool():
    def test_is_anonymous_return_401(self, create_school, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_school({'school_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_school):
        authenticate_user(is_staff=False)

        response = create_school({'school_name': 'School Of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, create_school, authenticate_user):
        authenticate_user()

        response = create_school({'school_name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['school_name'] is not None

    def test_if_data_is_valid_return_201(self, create_school, authenticate_user):
        authenticate_user()

        response = create_school({'school_name':'School Of Computing'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['school_name'] is not None


@pytest.mark.django_db
class TestRetrieveSchool():
    def test_if_school_exists_return_200(self, api_client):
        school = baker.make(School)

        response = api_client.get(f'/school_details/school/{school.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': school.id,
            'school_name': school.school_name,
            'departments': [],
            'number_of_departments': 0
        }


@pytest.mark.django_db
class TestUpdateSchool():
    def test_if_is_not_admin_return_403(self, authenticate_user, update_school):
        authenticate_user(is_staff=False)

        response = update_school({'school_name':'School'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_is_admin_return_200(self, authenticate_user, update_school):
        authenticate_user()

        response = update_school({})

        assert response.status_code == status.HTTP_200_OK

    def test_if_data_is_valid_return_200(self, authenticate_user, update_school):
        authenticate_user()

        response = update_school({'school_name':'School'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['school_name'] is not None


    def test_if_data_is_invalid_return_400(self, authenticate_user, update_school):
        authenticate_user()

        response = update_school({'school_name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['school_name'] is not None


@pytest.mark.django_db
class TestDeleteSchool():
    def test_if_is_admin_return_204(self, authenticate_user, delete_school):
        authenticate_user()
        school = {
            'id': 1,
            'school_name':'School'
        }

        response = delete_school(school)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    def test_if_is_not_admin_return_403(self, authenticate_user, delete_school):
        authenticate_user(is_staff=False)

        school = {
            'id': 1,
            'school_name':'School'
        }

        response = delete_school(school)

        assert response.status_code == status.HTTP_403_FORBIDDEN

