import requests
import json


class RedTeam:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fiddlecube.ai/api"
    def redteam_transform(self, context_str: list[str]):
        """
        Red team transformation using the provided context strings.
        """
        url = self.base_url + "/redteam"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }
        payload = json.dumps({"context": context_str})

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
