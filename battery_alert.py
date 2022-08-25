import time
import psutil
import os
while True:
	battery = psutil.sensors_battery()
	if battery.power_plugged == False:
		print("battery.power_plugged: False")
		break
	if battery.percent >= 75:
		print("battery.percent: ", battery.percent, "%. Plug out the power calbe !!!")
		os.system("msg * Battery Charge: " + str(battery.percent) + "% !!! Disconnect the power cable")
		break
	else:
		print("battery.percent: ", battery.percent, "%. You are safe")
	time.sleep(120)
