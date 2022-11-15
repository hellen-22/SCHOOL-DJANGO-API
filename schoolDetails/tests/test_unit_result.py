import pytest
from rest_framework import status
from model_bakery import baker

from account.models import Student
from schoolDetails.models import Unit, UnitDetails

@pytest.fixture
def create_unit_result(api_client):
    def do_create_unit_result(unit_result):
        unit = baker.make(Unit)
        return api_client.post(f'/school_details/unit/{unit.id}/result/', unit_result)
    return do_create_unit_result

@pytest.mark.django_db
class TestCreateUnitResult():
    def test_if_is_admin_return_201(self, authenticate_user, create_unit_result):
        authenticate_user()
        student = baker.make(Student)
        unit = baker.make(Unit)
        unit_result = {
            'student': student.id,
            'unit': unit.id,
            'cat': 10,
            'exam': 10
        }

        response = create_unit_result(unit_result)

        assert response.status_code == status.HTTP_201_CREATED
        
    def test_if_data_is_valid_return_201(self, authenticate_user, create_unit_result):
        authenticate_user()
        student = baker.make(Student)
        unit = baker.make(Unit)
        unit_result = {
            'student': student.id,
            'unit': unit.id,
            'cat': 10,
            'exam': 10
        }

        response = create_unit_result(unit_result)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['student'] is not None
        assert response.data['unit'] is not None
        assert response.data['cat'] <= 30
        assert response.data['exam'] <= 70

    def test_if_data_is_invalid_return_400(self, authenticate_user, create_unit_result):
        authenticate_user()
        unit_result = {
            'student': 1,
            'unit': 1,
            'cat': 70,
            'exam': 100
        }

        response = create_unit_result(unit_result)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        

@pytest.mark.django_db
class TestRetrieveUnitResult():
    def test_if_is_admin_and_unit_result_exists_return_200(self, api_client, authenticate_user):
        authenticate_user()
        unit_result = baker.make(UnitDetails)

        response = api_client.get(f'/school_details/unit/{unit_result.unit.id}/result/{unit_result.id}/')

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': unit_result.id,
            'student': unit_result.student.id,
            'unit': unit_result.unit.id,
            'cat': unit_result.cat,
            'exam': unit_result.exam
        }


