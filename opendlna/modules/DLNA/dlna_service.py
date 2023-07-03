import subprocess, json




class device:
    def __init__(self, 
                 location,
                 host,
                 friendly_name,
                 action_url,
                 manufacturer, 
                 manufacturer_url):
        
        self.location 
        self.host
        self.friendly_name
        self.action_url
        self.manufacturer
        self.manufacturer_url 
    
    def connect():
        pass
    
    def disconnect():
        pass
    
    


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
    devices_json = json.loads(scan_result)
    return devices_json