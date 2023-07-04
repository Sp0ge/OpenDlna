from opendlna.modules.DLNA import devices_scan
import os

devices_list = devices_scan()

user_in_device = str(input('device>> '))
user_in_file = os.path.normpath("C:/Users/deepb/Videos/test.mkv")

for obj in devices_list:
    print(obj.dev)
    if obj.friendly_name == user_in_device:
        print(obj.play_file(str(user_in_file)))

