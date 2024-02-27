import requests


def test_portal_up():
    url = "http://127.0.0.1:8000/admin"  # Replace with the URL of the portal you want to check

    # Send an HTTP GET request to the portal
    try:
        response = requests.get(url)
        res = response.status_code
    except:
        res = 500
    # Check if the response status code is 200 (OK)
    # print(response.status_code)

    assert res == 200, f"Portal is not up. Status code: {res}"

    # You can add more checks here if needed, such as checking for specific content in the response

    # For example, to check if the response body contains the word "Welcome":

    # assert "Welcome" in response.text, "Expected content not found in the response"

if __name__=="__main__":
    test_portal_up()