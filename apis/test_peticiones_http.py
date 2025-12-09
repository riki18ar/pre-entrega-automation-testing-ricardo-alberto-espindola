import requests
import pytest
import pytest_check as check
from faker import Faker
from datetime import datetime
from conftest import logger
fake = Faker()

def validate_date_response(response, excpected_status,expected_fields=None,max_time=1.0):
    """Función para validar la respuesta de una petición HTTP."""
    # Nivel 1: Status 
    assert response.status_code == excpected_status
    # Nivel 2: Headers
    if excpected_status != 204: # 204 No Content puede no tener Contet-Type
        assert "application/json" in response.headers("Content-Type", "")
    # Nivel 3-4 : Estructura y tipos de datos
    if expected_fields and response.text:
        body = response.json()
        assert expected_fields <= set(body.keys())
    # Nivel 5: Tiempo de respuesta
    assert response.elapsed.total_seconds() < max_time
    assert response.json() if response.text else {}    
        
class TestGetUsers:
    URL_API = "https://jsonplaceholder.typicode.com/"

    @pytest.mark.get
    def test_get_response_code(self, api_url):
        response = requests.get(api_url + "/users")
        data = validate_date_response(
            response= response,
            excpected_status=200,
            excepted_fields=[],
            max_time=2.0
        )
        assert response.status_code == 200
    @pytest.mark.get 
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + "/users")
        data = response.json()
        assert len(data) > 0 
        assert isinstance(data, list)

        first_user = data[0]
        print(first_user)
        key_structure = {"id", "name", "username", "phone", "address", "website"}

        for i in key_structure:
            assert i in first_user , f"la llave {i} no esta en el {first_user}"
        # Valida tipos de datos
        # for user in data[:3]:
        #     assert isinstance(user["id"], int), f"el id no es int en {user}"
        #     assert isinstance(user["name"], str), f"el name no es str en {user}"
        #     assert "@" in user["email"], f"el email no es valido en {user}" 
class TestPostUser:
    URL_API = "https://jsonplaceholder.typicode.com/"

    @pytest.mark.post
    def test_post_response_code(self, api_url):
        new_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "createdAt": "2025-06-10T12:00:00Z"
            }
        
        response = requests.post(api_url + "/users", new_user)
        assert response.status_code == 201 

        data = response.json()
        print(data)
        assert "id" in data       

        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year = datetime.now().year
            assert str(current_year) in created_at , f"no esta en el año actual"


class TestUserWorksFlow:
    
    def test_completo_users(self,api_url):
        logger.info("TEST ENCADENADO DE USUARIOS: GET, POST, PUT, PATCH, DELETE")
        logger.info("1.GET Obtener usuarios")
        # GET OBTENER USUARIOS
        response = requests.get(api_url + "/users")
        data = response.json()
        check.equal(response.status_code, 200)
        check.is_true(len(data) > 0)
        print("1.POST Crear un nuevo usuario")

        new_user = {
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            }
        
        response = requests.post(api_url + "/users", new_user)
        assert response.status_code == 201 