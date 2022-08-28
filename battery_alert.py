import time
import psutil
import os
from plyer import notification
notification.notify(title="Battery Alert", message="Battery Alert has started")
while True:
	battery = psutil.sensors_battery()
	if battery.power_plugged == False:
		print("battery.power_plugged: False")
		break
	if battery.percent >= 75:
		print("battery.percent: ", battery.percent, "%. Plug out the power calbe !!!")
		notification.notify(title="Battery Alert", message="Battery Charged Over: "+str(battery.percent)+"%. Unplug immediately!!!")
		os.system("msg * Battery Charge: " + str(battery.percent) + "% !!! Disconnect the power cable")
		break
	# else:
	# 	print("battery.percent: ", battery.percent, "%. You are safe")
	time.sleep(120)
