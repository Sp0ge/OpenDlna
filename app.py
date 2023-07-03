import sys
from opendlna.GUI import app as flask_web_gui

web_interface_active = True

for arg_n in range(1,len(sys.argv),2):
    arg = sys.argv[arg_n]
    param = sys.argv[arg_n+1]
    if arg == "-h" or arg == "--help":
        params = [
            '-h, --help \t  info about commands',
            '-wg, --web \t  web gui (True/False) default=true'
        ]
        
        for param in params:
            print(param)
            
    if arg == "-wg" or arg == "--web":
        web_interface_active = str(param)
        

if web_interface_active:
    flask_web_gui.run(host="localhost", port=80)