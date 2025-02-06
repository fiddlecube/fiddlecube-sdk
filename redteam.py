import requests
import json


class RedTeam:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.fiddlecube.ai/api"
    def redteam_transform(self, context_str: list[str]):
        """
         Red team
        """
        url = self.base_url + "/redteam"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Api-Key": self.api_key,
        }
        ## you can access our redteaming capabilities from here
        pass
