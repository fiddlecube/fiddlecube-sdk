import requests
import json


class FiddleCube:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, context_str: list[str], num_rows: int):
        url = "https://api.fiddlecube.ai/api/generate/sync"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }
        dataset = [{"contexts": [ctx]} for ctx in context_str]
        data = {
            "dataset": dataset,
            "question_types": [
                "SIMPLE",
                "REASONING",
                "NEGATIVE",
                "CONDITIONAL",
                "UNSAFE",
                "MCQ",
            ],
            "num_rows": num_rows,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Data generation successful.")
            return response.json()
        else:
            print("Failed to generate data.")
            print("==response==", response)
            return None
