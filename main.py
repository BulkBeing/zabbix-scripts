from api import Zabbix
from scripts import getInventory, getHostDetails

API = "http://0.0.0.0/zabbix/api_jsonrpc.php"
USER = ""
PASSWORD = ""

def main():
    zbx = Zabbix(API, USER, PASSWORD)
    #getHostDetails(zbx, "compute")

if __name__ == '__main__':
    main()