# Import the commands from the zabbix_utils project for this file
from zabbix_login import zabbix_login

def main():
    api = zabbix_login()
    # Retrieve a list of users, including their user ID and name.
    # "api" is the instance above, "user" is a part of the "api" object, and "get" is a function of the "user".
    hostgroupid = api.hostgroup.get(
        output=['name', 'groupid']
    )
    templateid = api.template.get(
        output=['name', 'templateid']
    )
    # Print the names of the retrieved users
    print (hostgroupid)
    print (templateid)

if __name__ == "__main__":
    main()