import requests

def test_get_book_by_id():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Activities/1"  # Replace with your mock API URL
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    print(response.headers)
    assert response.headers["content-type"] == "application/json; charset=utf-8; v=1.0"

    # Verify response structure (Assuming a book object with 'id', 'title', and 'author')
    data = response.json()
    print(data['id'])

    # assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "dueDate" in data

def test_create_author():
    url = "https://fakerestapi.azurewebsites.net/api/v1/Authors"  # Replace with your mock API URL
    new_author = {
        # "title": "The Hobbit", "author": "J.R.R. Tolkien"
            "id": 350,
            "idBook": 350,
            "firstName": "Narayan",
            "lastName": "Amare"
    }
    response = requests.post(url, json=new_author)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8; v=1.0"

    # Check if the author was created (specifics depend on your mock API's response)
    data = response.json()
    assert "id" in data
    assert data["firstName"] == "Narayan"
    assert data["lastName"] == "Amare"

test_get_book_by_id()
test_create_author()
