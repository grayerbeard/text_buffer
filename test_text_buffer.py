#!/usr/bin/env python3

#cpu_monitor_037.py a python3 script to monitor the cpu and control the pimorini fan_shim
#first writen August 2019 this version October 2019

# Standard library imports
#from subprocess import call as subprocess_call
from time import sleep as time_sleep
#from datetime import datetime
from os import getpid
from os import path
#import sys
from sys import argv as sys_argv
from sys import exit as sys_exit
from datetime import datetime
from random import randint as random_randint
from shutil import copyfile
#import subprocess
#import RPi.GPIO as GPIO

import plasma

# Third party imports
# None
# Local application imports
from config import class_config
from text_buffer import class_text_buffer
#from cpu_037 import class_cpu
from utility import fileexists,pr,make_time_text
#from wd_037 import class_wd

#cpu = class_cpu()
#pwm = c
config = class_config()
#wd = class_wd("cpu_wd")
my_pid = getpid()
config.prog_path = path.dirname(path.realpath(__file__)) + "/"
config.prog_name = str(sys_argv[0][:-3])

init_printout = ["My PID is : " + str(my_pid)]

#config.prog_name = str(sys_argv[0][:-3])
#prg_version = config.prog_name[-3:]

# make a random number string  between 1 and a thousand
random_text_number = str(random_randint(1,1001))

#try:
#	print("start copy using: ", random_text_number)
#	copyfile("cpu_log.html", "old/" + prg_version + "cpu_log" + random_text_number + ".html")
#	print("finish copy")
#except:
#	print("Cannot copy old files")

#config.config_filename = "config_" + prg_version + ".cfg"
config.config_filename = "config.cfg"
config.set_filename(config.config_filename)

print("config file is : ",config.config_filename)

if fileexists(config.config_filename):		
	init_printout.append("Config taken from file")
	print( "will try to read Config File : " ,config.config_filename)
	config.read_file() # overwrites from file
else : # no file so my_sensorneeds to be written
	config.write_file()
	init_printout.append("New Config File Made with default values, you probably need to edit it")

config.scan_count = 0

example_buffer_width = 11
##########  set up ?????????????????????
headings = ["Count","Val1","Val2","Val33","Val4","Val5"]
example_log_buffer_flag = True
example_buffer = class_text_buffer(100,headings,"example",config,example_log_buffer_flag)

# NOTE NOT NEEDED
#example_buffer_values = [""] * (example_buffer_width-1)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Fan shim related
#plasma.set_clear_on_exit(True)
#plasma.set_light_count(1)
#plasma.set_light(0, 0, 0, 0)

#Target Range temperatures
#max_temp =  69.0
#min_temp = 61.0   
#lower_mid_temp =   (max_temp  + min_temp)/2  - ((max_temp - min_temp)/4)
#upper_mid_temp =   (max_temp  + min_temp)/2  + ((max_temp - min_temp)/4)
#lower_min_temp =   min_temp - ((max_temp  - min_temp)/2)

#print(lower_min_temp,min_temp,lower_mid_temp,upper_mid_temp,max_temp)

target_loop_time = 2   # target cycle time in secounds, code self adjusts to acheive this
#min_speed = 75 # minimum percent speed
#max_speed = 90 # max percent PWM speed
#print("lower_mid_temp is : ",lower_mid_temp)
#brightness = 80
#freq = 2
#check = 0.001
#speed = 0 
#throttle = 0
#try_throttle_calc_smoothed = 0
#last_cpu_temp = min_temp
buffer_increment_flag = True

end_time = datetime.now()
last_total = 0
loop_time = 0
correction = 4.02

while (config.scan_count <= config.max_scans) or (config.max_scans == 0):
	loop_start_time = datetime.now()
#	cpu.get_data()
#	check += 0.001
#	count_for_WD = int(100*(config.scan_count + check))
#	try_throttle_calc = 100 * (cpu.temp - min_temp)/(max_temp - min_temp)
#	try_throttle_calc_smoothed = try_throttle_calc_smoothed + 0.1*(try_throttle_calc - try_throttle_calc_smoothed)
#	change = cpu.temp - last_cpu_temp
#	if change > 1.1:
#		print("---------------- Big CTemp Increase : ",last_cpu_temp, " to ",cpu.temp, " so ", change)
#	last_cpu_temp = cpu.tempincrement_flag

	# Check CPU temperature situation to use in below IF  statements
	# Display data occasionally
#	c_or_1 = check >= 0.998increment_flag
	# Turn off Fan when on and below target range
#	c_or_2 = (throttle > 0) and (cpu.temp<lower_min_temp)  # e.g. if using 61 to 69 then 57
	# Turn fan on when temperaturincrement_flage increasing fast
#	c_or_3 = (change > 2.1) and (cpu.temp > lower_mid_temp)# e.g. if using 61 to 69 then 63
	# Turn fan on when temperaincrement_flagture approaching top of target range.
#	c_or_4 = cpu.temp >= upper_mid_temp 				   # e.g. if using 61 to 69 then 67	

#	if c_or_1 or c_or_2 or c_or_3 or c_or_4:

#		buffer_increment_flag = True

#		cpu.calc_averages()

#		if cpu.temp >= max_temp:
#			throttle = 100
#		elif cpu.temp<= min_temp:
#			throttle = 0
#		elif cpu.temp >= upper_mid_temp:
			#increment_flag use lastest info when temperature high
#			throttle = try_throttle_calc
#		elif try_throttle_calc_smoothed > 0:
			# use smoothed data when temperature lower and smoother value over zero
#			throttle = try_throttincrement_flagle_calc_smoothed
#		else:
#			throttle = 6

#		if throttle <= 0 :increment_flag
#			speed = 0
#			freq = 2
#		else:
#			speed = min_speed + (throttle*(max_speed-min_speed)/100)
#			freq = 5increment_flag

#		cpu.set_pwm_control_fan(freq,speed)

#		cpu.update_led_temperature(cpu.temp,max_temp,min_temp,brightness)

#######????????????????????
	example_buffer.line_values[0] = str(config.scan_count)
	example_buffer.line_values[1] = str(round(float(example_buffer.line_values[1]) + 0.11,2))
	example_buffer.line_values[2] = str(round(float(example_buffer.line_values[2]) + 0.22,2))
	example_buffer.line_values[3] = str(round(float(example_buffer.line_values[3]) + 0.33,2))
	example_buffer.line_values[4] = str(round(float(example_buffer.line_values[4]) + 0.44,2))
	example_buffer.line_values[5] = str(round(float(example_buffer.line_values[5]) + 0.55,2))

	test_update_buffer_rate = 4

	if(config.scan_count % test_update_buffer_rate == 0):
		buffer_increment_flag = True
		print(buffer_increment_flag)
	else:
		buffer_increment_flag = False
		print(buffer_increment_flag)
	refresh_time = target_loop_time + (target_loop_time/3)
	example_buffer.pr(buffer_increment_flag,0,loop_start_time,refresh_time)

	config.scan_count += 1
#		check = 0
	
#	else:
		#Uncomment following Two lines to observe if curious
		#print(" Count : ",round(config.scan_count+check,2),cpu.get_av_cpu_load_so_far(),"Temp : ",
		#	round(cpu.temp,2),"Throttle/smoothed : ",round(try_throttle_calc,2),"/",round(try_throttle_calc_smoothed,2)) 
#		example_buffer.line_values[0] = str(round(config.scan_count + check,3))
		
#		if buffer_increment_flag:
#			example_buffer.line_values[1] = str(cpu.average_load) + "%"
#			example_buffer.line_values[2] = str(round(cpu.temp,2) ) + "C"
#			example_buffer.line_values[3] = str(round(throttle,1))+ "%"
#		else:
#			example_buffer.line_values[1] = str(cpu.cpu_load) + "%"
#			example_buffer.line_values[2] = str(round(cpu.temp,2) ) + "C"
#			example_buffer.line_values[3] = str(round(try_throttle_calc,1))+ "%"
#		example_buffer.line_values[4] = str(round(speed,1))+ "%"
#		example_buffer.line_values[5] = str(cpu.cpu_freq.current/1000) + "GHz"
#		example_buffer.line_values[6] = str(cpu.cpu_mem) + "%"
#		example_buffer.line_values[7] = str(cpu.cpu_disk) + "%"
#		example_buffer.line_values[8] = str(round(last_total,6)) +"s/" + str(round(loop_time,6)) +"s"
#		example_buffer.line_values[9] = "NoFlag"
#		example_buffer.pr(buffer_increment_flag,0,loop_start_time)
#		if throttle == 0:
#			buffer_increment_flag = False
#	cpu.control_fan()
#	wd.put_wd(count_for_WD,"ok")
	loop_end_time = datetime.now()
	loop_time = (loop_end_time - loop_start_time).total_seconds()

	# Adjust the sleep time to aceive the target loop time and apply
	# with a slow acting correction added in to gradually improve accuracy
	sleep_time = target_loop_time - loop_time - (correction/1000)
	try:
		time_sleep(sleep_time)
	except:
		print("Sleep_time error :",sleep_time) 
	last_end = end_time
	end_time = datetime.now()
	last_total = (end_time - last_end).total_seconds()
	error = 1000*(last_total - target_loop_time)
	correction = correction + (0.1*error)
	
