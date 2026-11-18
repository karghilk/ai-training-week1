import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # Seconds


def explain_status(code):
    messages = {
        200: "OK - Request successful",
        201: "Created - Resource created successfully",
        400: "Bad request - Check the data you sent",
        401: "Unauthorized - Authentication required",
        404: "Not found",
        500: "Internal server error - Try again later",
    }
    return messages.get(code, "Unknown status code")


def main():
    try:
        # GET: Retrieve users and parse the JSON response.
        response = requests.get(f"{BASE_URL}/users", timeout=TIMEOUT)
        response.raise_for_status()

        users = response.json()
        for user in users[:5]:
            print(f"{user['id']} - {user['name']} - {user['email']}")

        # POST: Create a post. json= converts the dictionary to JSON
        # and sets the Content-Type header automatically.
        new_post = {
            "title": "Learning REST APIs",
            "body": "Making HTTP requests with Python.",
            "userId": 1,
        }
        response = requests.post(
            f"{BASE_URL}/posts", json=new_post, timeout=TIMEOUT
        )
        response.raise_for_status()
        print(f"POST: {response.status_code}, id: {response.json()['id']}")

        # PUT: Replace the post's content.
        replacement = {
            "id": 1,
            "title": "Updated title",
            "body": "Updated post content.",
            "userId": 1,
        }
        put_response = requests.put(
            f"{BASE_URL}/posts/1", json=replacement, timeout=TIMEOUT
        )
        put_response.raise_for_status()

        # PATCH: Update only selected fields.
        patch_response = requests.patch(
            f"{BASE_URL}/posts/1",
            json={"title": "Patched title"},
            timeout=TIMEOUT,
        )
        patch_response.raise_for_status()

        # DELETE: Remove a post.
        delete_response = requests.delete(
            f"{BASE_URL}/posts/1", timeout=TIMEOUT
        )
        delete_response.raise_for_status()

        print(
            f"PUT: {put_response.status_code} | "
            f"PATCH: {patch_response.status_code} | "
            f"DELETE: {delete_response.status_code}"
        )

        # Handle the expected 404 directly with a friendly message.
        response = requests.get(
            f"{BASE_URL}/posts/9999", timeout=TIMEOUT
        )
        print(
            f"GET /posts/9999 -> {response.status_code} "
            f"{explain_status(response.status_code)}"
        )

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the API. Check your internet connection.")
    except requests.exceptions.HTTPError as error:
        code = error.response.status_code
        print(f"HTTP error {code}: {explain_status(code)}")
    except requests.exceptions.JSONDecodeError:
        print("The API returned a response that was not valid JSON.")
    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()