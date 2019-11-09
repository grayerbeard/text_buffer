# text_buffer
This is a **logging facility** for a Python 3 program that is running continuously to control and or monitor a process on a long term basis.

This has been used as part of a set of Py scripts for:
  * Control and monitoring using an RPI 3 to control the heating of a community workshop.   Two heaters were controlled via Smartplugs and five temperatures were monitored in the room and outside air.
  * Control and monitor a Sauna Heater.
  * Control and monitor a cooling fan on an R Pi 4.
  
The class in the file **text_buffer.py** is used to generate an HTML file to periodically display recent data and log data to a csv file.
The data shown is held in a rotating buffer so that only recent data is shown.
The HTML file is saved to the code directory and is also (optionally) copied to the local web server directory and (optionally) by FTP to a rempote web site by so the data can be viewed from anywhere with an internet connection.  The logging functions are in the class in the file **log_buffer.py**.  Various utility functions including FTP are in the **utility.py".
  
An earlier version of the code is in near continuos use and shown at [R Pi 4 Blog](https://www.smalle.uk/r-pi-4-blog)

The further code to do the R Pi PWM Fan control will be published on this account in due course.
