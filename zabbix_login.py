# Function for connecting to the Zabbix API.

# import necessary libraries if needed
from zabbix_env import zabbix_token, zabbix_url
from zabbix_utils import ZabbixAPI

#Zabbix API login function
def zabbix_login():
    print("[BOOT] Script started", flush=True)
    ZABBIX_AUTH = {
        "url": zabbix_url,
        "token": zabbix_token
        }
    if not zabbix_url or not zabbix_token:
        print("[FAIL] Missing zabbix_url or zabbix_token.", flush=True)
    api = ZabbixAPI(**ZABBIX_AUTH)
    conntest = api.apiinfo.version()
    if conntest == "7.4.3":
        print ("[LOGIN] Reached Zabbix API")
    else:
        print ("[FAIL] Cannot reach Zabbix API")
    authtest = api.hostgroup.get()
    if len(authtest) > 0:
        print ("[SUCCESS] Authenticated with Zabbix API")
        #session auto terminates on invalid token
    
    return api
# Only runs if you execute THIS file directly: python zabbix_login.py
# It will NOT run when imported.

#if __name__ == "__main__":
#    _api = zabbix_login()
#    print("[DONE] Login helper works.", flush=True)

# Uncomment for testing