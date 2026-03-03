from zabbix_hostcreate_settings import SNMPV3_SECURITYNAME, SNMPV3_SECURITYLEVEL,SNMPV3_AUTHPROTOCOL, SNMPV3_PRIVPROTOCOL, SNMPV3_AUTHPASSPHRASE, SNMPV3_PRIVPASSPHRASE, SNMPV3_CONTEXTNAME, GROUPID1, GROUPID2, TEMPLATEID1, TEMPLATEID2
print ("successfully imported zabbix_hostcreate_settings_peplink.")

def zabbix_hostcreate(api, hostname: str, host_ip: str):
    """
    Create one host using the provided api client, hostname, and IP.
    This is the version your bulk CSV importer should call.
    """
    print("[SUCCESS] host.create started", flush=True)
    print("[INFO] host.create process called API", flush=True)

    hostcreate = api.host.create(
        host=str(hostname).strip(),
        interfaces=[
            {
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": str(host_ip).strip(),
                "dns": "",
                "port": "161",
                "details": {
                    "version": 3,
                    "bulk": 0,
                    "securityname": SNMPV3_SECURITYNAME,
                    "contextname": SNMPV3_CONTEXTNAME or "",
                    "securitylevel": int(SNMPV3_SECURITYLEVEL),
                    "authprotocol": int(SNMPV3_AUTHPROTOCOL),
                    "privprotocol": int(SNMPV3_PRIVPROTOCOL),
                    "authpassphrase": SNMPV3_AUTHPASSPHRASE,
                    "privpassphrase": SNMPV3_PRIVPASSPHRASE,
                },
            }
        ],
        groups=[
            {"groupid": str(GROUPID1)},
            # {"groupid": str(GROUPID2)}, # Add if using multiple groupids
        ],
        templates=[
            {"templateid": str(TEMPLATEID1)},
            # {"templateid": str(TEMPLATEID2)}, # Add if using multiple templateids
        ],
    )

    print(f"[COMPLETE] Host created successfully! result={hostcreate}", flush=True)
    # print(f"[COMPLETE] Host created. hostids={hostcreate.get('hostids')}", flush=True)
    return hostcreate