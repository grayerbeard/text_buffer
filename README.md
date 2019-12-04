# **Circular Buffer** for logging and display of recent data.

## Note 
For latest version please go to the [R_Pi_4_Fanshim_PWM](https://github.com/grayerbeard/R_Pi_4_Fanshim_PWM) repository.

## Concept of a Circular Buffer
The concept of the buffer is explained very well here [Wikipedia : Circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)

So here it is a **logging facility** for a Python 3 program that is running continuously to control and or monitor a process on a long term basis.  Data is writtem into buffer rows with a pointer advanced by one every time new data is written.  By careful use of indexes pointers the data can then be read out so that the latest item is at the top and the oldest at the bottom even though the last data might have been put in half way down the list of data.   
The virtical size of the buffer is set in the config,cfg file. If the size is set to (say) ten then the buffer can only outpiut the last ten sets of data.  However the size of the buffer can be far larger  e.g. 100.
The "horizontal" size of the buffer is set from the number of headings entered when the class is set up (plus an extra column for the time/date stamp).

## A Set of Classes (Would that be called a school of Classes or maybe a College?)
This set of classes has been used with several Python scripts for:
  * Control and monitoring using an RPI 3 to control the heating of a community workshop.   Two heaters were controlled via Smartplugs and five temperatures were monitored in the room and outside air.
  * Control and monitor a Sauna Heater.
  * Control and monitor a cooling fan on an R Pi 4.

Here it is just running on its own logging dummy data for demo test purposes.

The class in the file **text_buffer.py** is used to generate an HTML file to periodically display recent data and log data to a csv file.
The data shown is held in a rotating buffer so that only recent data is shown.
The HTML file is saved to the code directory and is also (optionally) copied to the local web server directory and (optionally) by FTP to a rempote web site by so the data can be viewed from anywhere with an internet connection.  The logging functions are in the class in the file **log_buffer.py**.  Various utility functions including FTP are in the **utility.py".

##Applications
The [R_Pi_4_Fanshim_PWM](https://github.com/grayerbeard/R_Pi_4_Fanshim_PWM) repository shows an example application.

Other applications are being developed in my [RPi4_Python_FanshimPWM_Temperature_Control_with_logging](https://github.com/grayerbeard/RPi4_Python_FanshimPWM_Temperature_Control_with_logging) repository.
