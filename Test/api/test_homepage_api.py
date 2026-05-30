import requests
import time


def test_homepage_response_time():
    start_time = time.time()

    response = requests.get("https://play.ludigames.com")

    response_time = time.time() - start_time

    assert response.status_code == 200, (
        f"Expected status code 200 but got {response.status_code}"
    )

    assert response_time < 3, (
        f"Response time exceeded 3 seconds: {response_time:.2f}s"
    )
