# Print a list of all hosts configured in zabbix server

def getInventory(zbx):
    params = {
        "output": [
            "hostid",
            "host"
        ],
        "selectInterfaces": [
            "ip"
        ]
    }
    resp = zbx.makeRequest("host.get", params)
    print('{0:10}\t{1:50}\t{2:15}'.format("ID", "Server Name", "Interface IP"))
    print('{0:10}\t{1:50}\t{2:15}'.format("--", "-"*11, "-"*12))
    for server in resp:
        print('{0:10}\t{1:50}\t{2:15}'.format(server["hostid"], server["host"], server["interfaces"][0]["ip"]))


def getHostDetails(zbx, host):
    params = {
        "filter": {
            "host": [host]
        }
    }
    resp = zbx.makeRequest("host.get", params)
    print('{0:33}\t{1}'.format("Parameter", "Value"))
    print('{0:33}\t{1}'.format("-"*9, "-"*5))
    for param, val in resp[0].items():
        if type(val) == list:
            print('{0:30} : \t{1}'.format(param, ', '.join(val)))
        else:
            print('{0:30} : \t{1}'.format(param, val))



