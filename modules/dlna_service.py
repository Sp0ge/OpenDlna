import subprocess, json

def devices_scan():
    cmd_out = subprocess.run(['dlna','device'], capture_output=True, text=True).stdout.replace("Scanning...\n","")
    devices = cmd_out.split('=> Device ')
    scan_result = ''
    for device in devices:
        #print(device[2:])
        if len(device[2:]) > 10:
            data = json.loads(str(device[2:]))
            scan_result += f'"{str(data["friendly_name"])}":[{str(device[2:-2])}]'
    scan_result = "{\n" + scan_result + "\n}"
    print(scan_result)
    devices_json = json.loads(scan_result)
    return devices_json
