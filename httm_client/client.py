import requests


class HttpClient:
    @staticmethod
    def send_get_request(url: str):
        response = requests.get(
            url=url,
        )
        return response
