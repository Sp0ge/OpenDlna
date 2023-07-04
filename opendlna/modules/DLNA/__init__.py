import subprocess, json 
from .classes import Device   

def devices_scan():
    cmd_out = subprocess.run(['dlna','device'], capture_output=True, text=True).stdout.replace("Scanning...\n","")
    devices = cmd_out.split('=> Device ')
    scan_result = ''
    for device in devices:
        if len(device[2:]) > 10:
            data = json.loads(str(device[2:]))
            print(f'[+] New device found - {data["friendly_name"]}')
            scan_result += f'"{str(data["friendly_name"])}":[{str(device[2:-2])}]'
    scan_result = "{\n" + scan_result + "\n}"
    #print(scan_result)
    
    devices_list = json.loads(scan_result)
    devices_classes = list()
    for num,tv in enumerate(devices_list):
        new = devices_list[tv][0]
        obj = Device(
            location = new['location'],
            host = new['host'],
            friendly_name = new['friendly_name'],
            action_url = new['action_url'],
            manufacturer = new['manufacturer'], 
            manufacturer_url = new['manufacturer_url']
            ) 
        devices_classes.append(obj)
    return devices_classes