import pandas

from httm_client.client import HttpClient


URL_PATTERN = "https://indy-towers.ru/search?korpus=4&section=1&floor={floor}&flat={flat}"


if __name__ == "__main__":
    df = pandas.read_excel("files/file.xlsx")
    for _, row in df.iterrows():
        floor = row[3]
        flat = row[0]

        url = URL_PATTERN.format(floor=floor, flat=flat)
        response = HttpClient.send_get_request(url=url)

        print(f"{floor=}, {flat=}")
