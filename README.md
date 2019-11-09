# **Circular Buffer** for logging and display of recent data.

The concept of the buffer is explained very well here [Wikipedia : Circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)

This is a **logging facility** for a Python 3 program that is running continuously to control and or monitor a process on a long term basis.

This set of classes has been used with several Python scripts for:
  * Control and monitoring using an RPI 3 to control the heating of a community workshop.   Two heaters were controlled via Smartplugs and five temperatures were monitored in the room and outside air.
  * Control and monitor a Sauna Heater.
  * Control and monitor a cooling fan on an R Pi 4.

Here it is just running on its own logging dummy data for demo test peurposes.

The class in the file **text_buffer.py** is used to generate an HTML file to periodically display recent data and log data to a csv file.
The data shown is held in a rotating buffer so that only recent data is shown.
The HTML file is saved to the code directory and is also (optionally) copied to the local web server directory and (optionally) by FTP to a rempote web site by so the data can be viewed from anywhere with an internet connection.  The logging functions are in the class in the file **log_buffer.py**.  Various utility functions including FTP are in the **utility.py".
  
The web location that is currently used for logging is shown at [test_text_buffer_log.html](https://www.ftp4rpi.smalle.uk/house/test_text_buffer_log.html)
An earlier version of the code is in near continuos use and shown at [R Pi 4 Blog](https://www.smalle.uk/r-pi-4-blog) controlling an R Pi Cooling fan and logging data from the R Pi 4. Control uses PWM Fan Speed Control.

The further code to do the R Pi PWM Fan control will be published on this account in due course.
