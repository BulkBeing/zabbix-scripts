import requests
from api.logger import Logger

class Zabbix(object):
    def __init__(self, apiurl, username, password):
        self.api = apiurl
        self.user = username
        self.passwd = password
        self.log = Logger()
        self.token = None
        # Get token
        self._login()

    def _login(self):
        params = {
                "user": self.user,
                "password": self.passwd,
            }
        self.token = self.makeRequest("user.login", params)

    
    def makeRequest(self, method, params):
        req = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1,
            "auth": self.token
        }
        try:
            resp = requests.post(self.api, json=req).json()
            return resp["result"]
        except Exception as e:
            self.log.critical("Error in making request: " + str(e) + " : " + str(resp["error"]))


