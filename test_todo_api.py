import requests

endpoint = "https://todo.pixegami.io"


def test_can_call_endpoint():
    response = requests.get(endpoint)
    status_code = response.status_code
    assert status_code == 200


def test_can_create_task():
    payload = {
        "content": "string",
        "user_id": "string",
        "task_id": "string",
        "is_done": False
    }
    response = requests.put(endpoint + "/create-task", json=payload)
    status_code = response.status_code
    assert status_code == 200
