import requests
from testcontainers.compose import DockerCompose

BASE_URL = "http://localhost:5000"

def test_root_endpoint_json():
    compose = DockerCompose(
        "demo_flask_app", compose_file_name="compose.yaml", build=True, pull=True
    )

    with compose:
        stdout, stderr = compose.get_logs()
        print(stdout)
        print(stderr)

        compose.wait_for(BASE_URL + "/")

        response = requests.get(BASE_URL, headers={"Accept": "application/json"})
        actual_response_json = response.json()

        expected_response_json = { "message": "Hello World!" }
        assert actual_response_json == expected_response_json
