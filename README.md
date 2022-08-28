# batteryAlert
Helps me not to charge my laptop over 80%. Why? To extend longevity of my battery...
## Installation
`pip install psutil`
## Easy way to get working on Windows
Run "battery_alert.exe"
Modify "battery_alert.py" in case you have to

# Advanced
## Launching the python script automatically when power supply gets plugged in
1. Find for the event in event viewer which  represnts kernel-power
2. Bind a task with the above event to start the python script
