import requests
import json


class FiddleCube:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fiddlecube.ai/api"

    def generate(self, context_str: list[str], num_rows: int):
        url = self.base_url + "/generate/sync"
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

    def diagnose(self, logs: list[dict]):
        """
        Run diagnostics on a log of LLM interactions.
        Step-by-step analysis of how the LLM output was achieved
        based on the query, prompt, answer and context.
        """
        url = self.base_url + "/debug/"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }
        data = {"dataset": logs}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print("Debugging successful.")
            return response.json()
        else:
            print("Failed to debug.")
            print("==response==", response)
            return None

    def test(
        self, prompt: str, ground_truth_dataset: list[dict], model: str = "gpt=4o"
    ):
        url = self.base_url + "/eval/test"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }
        data = {
            "prompt": prompt,
            "ground_truth_dataset": ground_truth_dataset,
            "model": model,
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
