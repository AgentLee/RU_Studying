# Takes campus and displays all open rooms based on time
# Needs data structure for buildings/rooms
# Only deals with undergrad 

import json
import os
import time
from pprint import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def processTime(time):
	time2 = ""
	time2 += time[0]
	time2 += time[1]
	time2 += ":"
	time2 += time[2]
	time2 += time[3]

	return time2

def getDay(day):
	if day[0] == 'M':
		day = "Mon"
	elif day[0] == 'T':
		day = "Tue"
	elif day[0] == 'W':
		day = "Wed"
	elif day[0] == 'Th':
		day = "Thu"
	elif day[0] == 'F':
		day = "Fri"

	return day

def hourtoint(time):
	hour = time[0]
	hour += time[1]
	hour = int(hour)
	return hour

def mintoint(time):
	minute = time[3]
	minute += time[4]
	minute = int(minute)
	return minute

def checkOpen(startTime, endTime, pm):
	currTime = str(time.strftime("%H:%M"))

	# change currTime to integers
	currHour = hourtoint(currTime)
	currMin = mintoint(currTime)

	# change start time to integers
	startHour = hourtoint(startTime)
	startMin = mintoint(startTime)

	# change end time to integers
	endHour = hourtoint(endTime)
	endMin = mintoint(endTime)

	if currHour > 12:
		if pm == "P":
			twelvehour = currHour-12

			# if same hour check minute
			if twelvehour == startHour: 
				if currMin < startMin:
					return True
				else:
					return False
			# if current hour is greater than start hour
			# check if current time is in between class
			elif twelvehour > startHour:
				if twelvehour < endHour:
					return False

			# if same end hour check minute
			if twelvehour == endHour:
				if currMin > endMin:
					return True
				else: 
					return False
			elif twelvehour > endHour:
				return True
	else:
		# if same hour check minute
		if currHour == startHour: 
			if currMin < startMin:
				return True
			else:
				return False
		# if current hour is greater than start hour
		# check if current time is in between class
		elif currHour > startHour:
			if currHour < endHour:
				return False

		# if same end hour check minute
		if currHour == endHour:
			if currMin > endMin:
				return True
			else: 
				return False
		elif currHour > endHour:
			return True

def selectCampus():
	campusChoice = -1

	campusChoice = input("Select your campus\n1. Livingston\n2. Busch\n3. C/D\n4. College Ave\n")

	if campusChoice == 1:
		return "LIVINGSTON"
	elif campusChoice == 2:
		return "BUSCH"
	elif campusChoice == 3:
		return "DOUGLAS/COOK"
	elif campusChoice == 4:
		return "COLLEGE AVENUE"
	else:
		selectCampus()

def main():
	print(bcolors.FAIL+ "If the room in question is not displayed, it may still be available"+bcolors.ENDC)
	campusChoice = selectCampus()
	currDay = time.strftime("%a")
	path = 'data/'

	for dir_entry in os.listdir(path):
		dir_entry_path = os.path.join(path, dir_entry)

		# need to go through 332, bug with digital logic design
		if dir_entry_path == "data/data_332.json":
			continue
		if os.path.isfile(dir_entry_path):
			with open(dir_entry_path) as outfile:
				data = json.load(outfile)

			numClasses = len(data)

			i = 0

			while i in range(0, numClasses):
				course = data[i]["title"]
				numSections = len(data[i]['sections'])

				j = 0
				while j in range(0, numSections):
					numTimes = len(data[i]['sections'][j]['meetingTimes'])

					k = 0
					while k in range(0, numTimes):
						s = data[i]['sections'][j]['meetingTimes'][k]['startTime']
						e = data[i]['sections'][j]['meetingTimes'][k]['endTime']
						pm = data[i]['sections'][j]['meetingTimes'][k]['pmCode']
						building = data[i]['sections'][j]['meetingTimes'][k]['buildingCode']
						room = data[i]['sections'][j]['meetingTimes'][k]['roomNumber']
						campus = data[i]['sections'][j]['meetingTimes'][k]['campusName']
						day = data[i]['sections'][j]['meetingTimes'][k]['meetingDay']

						if campus == campusChoice:
							if s is not None and e is not None:
								day = getDay(day)

								if day == currDay:
									start = processTime(s)
									end = processTime(e)

									currTime = str(time.strftime("%I:%M"))

									if checkOpen(start, end, pm) is True:
										print(bcolors.WARNING + currTime + bcolors.ENDC)
										print "Class starts at ", start, " and ends at ", end, pm
										print(bcolors.OKBLUE + "ROOM OPEN" + bcolors.ENDC)
										print campus, building, room
										print(bcolors.HEADER + "*************************************" + bcolors.ENDC)
									#print day, start, end, pm	
									#print currTime		

						k += 1

					j += 1

				i += 1

if __name__ == "__main__":
    main()