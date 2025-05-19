import requests

def test_google():
    response = requests.get("https://www.google.com")
    assert response.status_code == 200
    print("Test passed: Google is reachable.")

if __name__ == "__main__":
    test_google()
