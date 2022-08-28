' This script runs battery_alert.bat silently(without the windows/UI)
Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Users\Nayeem\OneDrive\Documents\dev\batteryAlert\battery_alert.bat" & Chr(34), 0
Set WinScriptHost = Nothing