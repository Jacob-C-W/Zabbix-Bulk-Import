# SNMPv3 credentials (only used if SNMP_MODE == "v3")
SNMPV3_SECURITYNAME = "yoursecurityname"
SNMPV3_SECURITYLEVEL = 2  # 0=noAuthNoPriv, 1=authNoPriv, 2=authPriv (common)
SNMPV3_AUTHPROTOCOL = 1   # 0=MD5, 1=SHA1 (varies by Zabbix version; keep consistent with your environment)
SNMPV3_PRIVPROTOCOL = 1   # 0=DES, 1=AES (varies by Zabbix version; keep consistent with your environment)
SNMPV3_AUTHPASSPHRASE = "yourauthpass"
SNMPV3_PRIVPASSPHRASE = "yourprivpass"
SNMPV3_CONTEXTNAME = ""   # Usually blank unless you use contexts