import time

import pytest

from src.commonUtility.DataProvider import TestDataLoader
from src.scenario.LoginPagescenario import LoginScenario

test_data = TestDataLoader.load_json(
    "src/testData/credentials.json"
)

@pytest.mark.smoke
def test_verifyLoginWithValidCredentials(page):
    data = test_data["valid_user"]
    actual_result = LoginScenario(page).login_with_valid_credentials(
        data["username"],
        data["password"]
    )
    time.sleep(2)
    assert data["expected_result"] == actual_result


def test_verifyLoginWithInValidCredentials(page):
    data = test_data["invalid_user"]
    actual_result = LoginScenario(page).login_with_invalid_credentials(
        data["username"],
        data["password"]
    )
    time.sleep(2)
    assert data["expected_result"] != actual_result

