from httm_client.client import HttpClient


if __name__ == "__main__":
    google_response = HttpClient.send_get_request(url="https://google.com")
    print(google_response)

