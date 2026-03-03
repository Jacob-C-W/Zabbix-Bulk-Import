# Zabbix Bulk Import Script

I made this script to automate adding devices to Zabbix in bulk, quick and efficiently. My requiurements were to add several hundred devices of the same device to the platform monitored by SNMPv3. 


# Building the Enviorment

Ensure Python is installed.

Install latest stable python (should include pip).

Create a folder in Enviorments, then specify "ProjectName"-Python, like Zabbix-Python
#
In PowerShell, create a virtual enviorment and activate

    python -m venv "venv"
    ./venv/scripts/activate
#
Confirm pip is installed already, then upgrade and install zabbix_utils

    pip
    py -m pip install --upgrade pip

*Ensure you're in the venv before you pull pip libraries in. Otherwise it'll do you no good to pull into the path.*

    pip install zabbix_utils
#
Also create an enviorment requirements file

    pip freeze > requirements.txt
#
Then if someone wants to adopt those requirements to work in the same enviorment they'd run the commands below

    python -m venv "venv"
    ./venv/scripts/activate
    python -m pip install -r requirements.txt

Then make sure to do any updates it asks for until you can run through all three commands above without error.  

**Never touch venv manually except to delete.**

Under your "ProjectName"-Python create a sibling of the vn folder, like tests and scripts. 

If you pulled the env to a new machine then re-run the activate command below, but we gitignore so you shouldnt have to.

    ./venv/scripts/activate
#
Also something I noticed on a new Windows machine was I had to disable advanced app aliasing that links apps to microsoft store and then needed to boot the python app manually and restart my vscode window. Weird.


# Import the Repo
If you haven't yet pull this repo into a folder in the same directory as you venv. 
**Not into the venv directory**. If you have already pulled simply move the folder there in your file manager.


# Config Variables

Create a token in Zabbix 

    Users -> API Tokens -> Create API Token -> set Name, User, Expiration -> Add.

Copy the token and paste it between the parenthesis for the zabbix_token variable. 

Also copy the URL for Zabbix and paste it in the zabbix_env.py file the same way.

    zabbix_token = "token"
    zabbix_url = "https://zabbix.com/zabbix"

Test the API using the zabbix_get_ids.py script, run it in your terminal with the command 

    py zabbix_get_ids.py

This should grab the name and IDs of all groups and polling templates, if the group you want is not present go into Zabbix's webui and create it and run the script again. Similarly, if the polling template is not present then browse the official and community forums for a template to fit your needs. 

*You can also make your own SNMP template, but if you can do that I assume you don't need me.*

Next we'll add those numbers to zabbix_hostcreate_settings.py. 

    GROUPID1 = "1"
    TEMPLATEID1 = "1"

Fill out your SNMP credentials:

    SNMPV3_SECURITYNAME = "yoursecurityname"
    SNMPV3_AUTHPASSPHRASE = "yourauthpass"
    SNMPV3_PRIVPASSPHRASE = "yourprivpass"

And finally, build a two column excel csv with the headers **ip** and **hostname** and then list out your ip addresses and hostnames. Make sure that CSV is called bulk_import.csv and is in the same directory as the scripts. 

*I have provided this already in the repo.*

# Running

First we'll need to change the max create number to match our number of imported host. **Don't include the header.**

We'll run bulk_import_csv.py in the directory of the folder.

    py bulk_import_csv.py

It will prompt for confirmation, enter YES. 

Monitor the print statements to find errors, skips, and for troubleshooting. 

**Good Luck!**

# Process Improvement Notes

However, after developing this script-set I realized that this could easily be converted to a full deployment script. Process improvement will require moving all variables into the CSV and finding a more secure method of storing SNMP data. Once all variables are controlled in a CSV then an entire deployment could be automated through a carefully managed CSV. This script and file pairing will double as deployment and disaster recovery for network monitoring. 

Also, if your cybersecurity department is against storing SNMP credentials in a file, even temporairly, then a quick solution is leveraging getpass to ask for user input before running the scripts. This would then store the input as the SNMP variables and then clear it out after the script has finished. This solution however only works for enviorments where SNMP credentials are homogenous or at least widely consistent otherwise the process becomes manual and the point is lost. 


