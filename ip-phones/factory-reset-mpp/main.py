import requests
import time

def execute_commands(ip_address):
    
    try:
        print("\n")
        response = requests.get(f'https://{ip_address}/admin/direct-factory-reset', verify=False)
        print(response)

        with open("logfile.txt", "a") as file:
            if response.status_code == 200:
                print(f"Request successful. Status code: {response.status_code} \n")
                time.sleep(1)
                file.write(f"{ip_address} request was successful. Status code: {str(response.status_code)} \n")
                time.sleep(2)
            else:
                print(f"Request unsuccessful. Status code: {response.status_code} \n")
                time.sleep(1)
                file.write(f"{ip_address} request unsuccessful. Status code: {str(response.status_code)} \n")
                time.sleep(2)

    except Exception as e:
        with open("logfile.txt", "a") as file:
            print(f"Failed to connect or execute command at {ip_address} \n")
            print(f"Error: {str(e)} \n")
            file.write(f"{ip_address} Failed to connect or execute command , Error: {str(e)} \n")
            time.sleep(2)
    
    

# Read the list of IP addresses from text file
with open('ip_addresses.txt', 'r') as f:
    ip_addresses = [line.strip() for line in f]

# Perform the operations for each IP address
for ip_address in ip_addresses:
    execute_commands(ip_address)
    
