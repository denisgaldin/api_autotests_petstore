import allure
from allure_commons.types import Severity

from petstore_api_test_project.api.create_new_pet import create_new_pet
from petstore_api_test_project.api.delete_pet import delete_pet
from petstore_api_test_project.api.find_pet import get_pet_by_id, get_nonexistent_pet_by_id, get_pet_by_status
from petstore_api_test_project.utils.validate_schema import validate_response_to_json_schema


@allure.epic('Pet API')
@allure.feature('Tests about pets')
@allure.link('https://petstore.swagger.io/', name='Swagger Petstore')
class TestPet:
    @allure.title('Add new pet to the store')
    @allure.story('Create pet')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_add_new_pet_to_store(self, api_url):
        new_pet = create_new_pet(api_url, pet_name='Spike')

        with allure.step('Проверка, что API возвращает код статуса 200.'):
            assert new_pet.status_code == 200
        with allure.step('Проверка, что имя питомца - "Spike".'):
            assert new_pet.json()['name'] == 'Spike'
        validate_response_to_json_schema(json_schema='post_pet.json', response=new_pet)
