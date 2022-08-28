/*
This file is not necessary to run the python script 
automatically when the user inserts the power cable.
This is available if for some reason automation
doesn't work and the user wants the previous method
of keeping the .exe file pinned to taskbar.
*/
#include <stdlib.h>
int main()
{ 
	
	system("python battery_alert.py");
	return 0;
}
