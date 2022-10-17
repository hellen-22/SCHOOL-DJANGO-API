from urllib import response
import pytest 
from rest_framework import status
from rest_framework.test import APIClient
from model_bakery import baker

from schoolDetails.models import School


@pytest.fixture
def create_school(api_client):
    def do_school(school):
        return api_client.post('/school_details/school/', school)
    return do_school



@pytest.mark.django_db
class TestCreateSchool():
    def test_is_anonymous_return_403(self, create_school):
        response = create_school({'school_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_is_admin_and_data_is_invalid_return_400(self, create_school, authenticate_user):
        authenticate_user()
        response = create_school({'school_name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['school_name'] is not None


@pytest.mark.django_db
class TestRetrieveSchool():
    def test_if_collection_exists_return_200(self, api_client):
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
    def test_if_is_admin_and_data_is_invalid_return_400(self, api_client, authenticate_user):
        authenticate_user()
        old_school = baker.make(School)
        new_school = baker.prepare(School)
        current_school = {
            'id': new_school.id,
            'school_name': new_school.school_name,
            'departments': new_school.departments
        }

        response = api_client.patch(f'/school_details/school/{old_school.id}/', current_school, content_type="application/json")


        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == current_school


        
