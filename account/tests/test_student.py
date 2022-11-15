import pytest
from model_bakery import baker
from rest_framework import status

from account.models import Student
from schoolDetails.models import Department
from custom.models import User

@pytest.fixture
def student_object():
    department = baker.make(Department)

    student = {
        'reg_no': 'GGHHH',
        'department': department.id,
        'user': {
            'username': 'Hellen',
            'first_name': 'Hellen',
            'last_name': 'Wain',
            'email': 'email@email.com',
            'password': 'passweord'

        }
    }

    return student

@pytest.fixture
def create_student(api_client):
    def do_student(student):
        return api_client.post('/account/student/', student, format='json')
    return do_student

@pytest.mark.django_db
class TestCreateStudent():
    def test_if_is_admin_return_201(self, authenticate_user, create_student):
        authenticate_user()
        department = baker.make(Department)

        student = {
            'reg_no': 'GGHHH',
            'department': department.id,
            'user': {
                'username': 'Hellen',
                'first_name': 'Hellen',
                'last_name': 'Wain',
                'email': 'email@email.com',
                'password': 'passweord'

            }
        }

        response = create_student(student)

        assert response.status_code == status.HTTP_201_CREATED

    def test_if_data_is_valid_return_201(self, authenticate_user, create_student):
        authenticate_user()

        department = baker.make(Department)

        student = {
            'reg_no': 'GGHHH',
            'department': department.id,
            'user': {
                'username': 'Hellen',
                'first_name': 'Hellen',
                'last_name': 'Wain',
                'email': 'email@email.com',
                'password': 'passweord'

            }
        }

        response = create_student(student)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data is not None

    def test_if_data_is_invalid_return_400(self, authenticate_user, create_student):
        authenticate_user()

        department = baker.make(Department)
        student = {
            'reg_no': '',
            'department': department.id,
            'user': {
                'username': '',
                'first_name': '',
                'last_name': '',
                'email': '',
                'password': ''

            }
        }

        response = create_student(student)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data is not None


@pytest.mark.django_db
class TestRetrieveStudent():
    def test_if_is_not_admin_return_403(self, authenticate_user, api_client):
        authenticate_user(is_staff=False)

        student = baker.make(Student)

        response = api_client.get(f'/account/student/{student.id}/')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_student_exists_return_200(self, authenticate_user, api_client):
        authenticate_user()

        student = baker.make(Student)
        department = baker.make(Department)

        response = api_client.get(f'/account/student/{student.id}/')

        assert response.status_code == status.HTTP_200_OK

