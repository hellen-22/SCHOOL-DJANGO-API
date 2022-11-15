import pytest 
from rest_framework import status
from model_bakery import baker

from schoolDetails.models import Department, School
from django.contrib.auth.models import User


@pytest.fixture
def create_department(api_client):
    def do_department(department):
        school = baker.make(School)
        return api_client.post(f'/school_details/school/{school.id}/department/', department)
    return do_department

@pytest.fixture
def update_department(api_client):
    def do_department(department):
        department_ = baker.make(Department)
        return api_client.patch(f'/school_details/school/1/department/{department_.id}/', department)
    return do_department


@pytest.fixture
def delete_department(api_client):
    def do_department(department):
        department_ = baker.make(Department)
        return api_client.delete(f'/school_details/school/1/department/{department_.id}/', department)
    return do_department


@pytest.mark.django_db
class TestCreateDepartment():
    def test_is_anonymous_return_401(self, create_department, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_department({'department_name': 'School of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    
    def test_if_is_not_admin_return_403(self, authenticate_user, create_department):
        authenticate_user(is_staff=False)

        response = create_department({'department_name': 'School Of Computing'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_invalid_return_400(self, create_department, authenticate_user):
        authenticate_user()

        response = create_department({'department_name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['department_name'] is not None

    def test_if_data_is_valid_return_201(self, create_department, authenticate_user):
        authenticate_user()

        response = create_department({'department_name':'School Of Computing'})

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['department_name'] is not None


@pytest.mark.django_db
class TestRetrieveDepartment():
    def test_if_department_exists_return_200(self, api_client):
        department = baker.make(Department)

        response = api_client.get(f'/school_details/school/1/department/{department.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': department.id,
            'department_name': department.department_name
        }


@pytest.mark.django_db
class TestUpdateDepartment():
    def test_if_is_admin_return_200(self, authenticate_user, update_department):
        authenticate_user()

        response = update_department({'department_name':'School'})

        assert response.status_code == status.HTTP_200_OK



    def test_if_is_not_admin_return_403(self, authenticate_user, update_department):
        authenticate_user(is_staff=False)

        response = update_department({'department_name':'School'})

        assert response.status_code == status.HTTP_403_FORBIDDEN


    def test_if_data_is_valid_return_200(self, authenticate_user, update_department):
        authenticate_user()

        response = update_department({'department_name':'School'})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['department_name'] is not None


    def test_if_data_is_invalid_return_400(self, authenticate_user, update_department):
        authenticate_user()

        response = update_department({'department_name':''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['department_name'] is not None


@pytest.mark.django_db
class TestDeleteDepartment():
    def test_if_is_admin_return_204(self, authenticate_user, delete_department):
        authenticate_user()
        department = {
            'id': 1,
            'department_name':'School'
        }

        response = delete_department(department)

        assert response.status_code == status.HTTP_204_NO_CONTENT

    
    def test_if_is_not_admin_return_403(self, authenticate_user, delete_department):
        authenticate_user(is_staff=False)

        department = {
            'id': 1,
            'department_name':'School'
        }

        response = delete_department(department)

        assert response.status_code == status.HTTP_403_FORBIDDEN

