# SNMPv3 credentials (only used if SNMP_MODE == "v3")
SNMPV3_SECURITYNAME = "{$SNMPV3_SECURITYNAME}"
SNMPV3_SECURITYLEVEL = 2  # 0=noAuthNoPriv, 1=authNoPriv, 2=authPriv (common)
SNMPV3_AUTHPROTOCOL = 1   # 0=MD5, 1=SHA1 (varies by Zabbix version; keep consistent with your environment)
SNMPV3_PRIVPROTOCOL = 1   # 0=DES, 1=AES (varies by Zabbix version; keep consistent with your environment)
SNMPV3_AUTHPASSPHRASE = "{$DEVICE1_SNMPV3_AUTHPASSPHRASE}"
SNMPV3_PRIVPASSPHRASE = "{$DEVICE1_SNMPV3_PRIVPASSPHRASE}"
SNMPV3_CONTEXTNAME = ""   # Usually blank unless you use contexts

# Zabbix can store Macros.
# This way the files on our PCs don't hold the secure information, only the server holds it. 
# Also the API traffic will be encrypted by TLS when used with HTTPS. 
# The server will be protected given it will be holding sensitive data. 