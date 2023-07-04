import subprocess
class Device:
    def __init__(self, 
                 location,
                 host,
                 friendly_name,
                 action_url,
                 manufacturer, 
                 manufacturer_url):
        
        self.location = location
        self.host = host
        self.friendly_name = friendly_name
        self.action_url = action_url
        self.manufacturer = manufacturer
        self.manufacturer_url = manufacturer_url
    
    def play_file(self, path):
        print(self.friendly_name)
        cmd_out = subprocess.run(['dlna','play', path , '-q', self.friendly_name ], capture_output=True, text=True).stdout
        return cmd_out