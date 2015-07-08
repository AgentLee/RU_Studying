import json
import urllib2
import time

from Tkinter import *
import tkMessageBox
import Tkinter

depts = []

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

def selectCampus():
	campusChoice = -1

	campusChoice = input("1. Livingston\n2. Busch\n3. C/D\n4.College Ave\n")

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

def getDepts():
	dep = 0
	i = 0
	while dep in range(0, 1000):
		if dep in range(0, 10):
			subj = "00"
			subj += str(dep)
		elif dep in range(9, 100):
			subj = "0"
			subj += str(dep)
		else:
			subj = str(dep)

		pre = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=b05b7682688883918976e21cb75d5eeb&semester=92015&subj="
		post = "&campus=NB&level=U"
		dept = pre+str(subj)+post 

		data = urllib2.urlopen(dept)
		objs = json.load(data)

		if objs is not None:
			depts.append(subj)
			i += 1

		dep += 1
	
def main():
	# Get current day
	currDay = time.strftime("%a")

	# Get campus 
	campusChoice = selectCampus()

	getDepts()

	i = 0
	while i in range(0, len(depts)):
		pre = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=b05b7682688883918976e21cb75d5eeb&semester=92015&subj="
		post = "&campus=NB&level=U"
		dept = pre+str(subj)+post 

		data = urllib2.urlopen(dept)
		objs = json.load(data)

		if objs is not None:
			numClasses = len(objs)

		j = 0
		while j in range(0, numClasses):
			course = objs[j]['title']
			numSections = len(objs[j]['sections'])
				
			j += 1
		i += 1

"""""
	done = True
	currDay = time.strftime("%a")

	campusChoice = selectCampus()

	while done is True:
		choice = input('Enter department like xyz: ')
		
		pre = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=b05b7682688883918976e21cb75d5eeb&semester=92015&subj="
		post = "&campus=NB&level=U"

		dept = pre+str(choice)+post 

		data = urllib2.urlopen(dept)

		objs = json.load(data)

		if objs is not None:
			#print(subj)
			numClasses = len(objs)

			i = 0

			while i in range(0, numClasses):
				course = objs[i]['title']
				numSections = len(objs[i]['sections'])
				j = 0
				while j in range(0, numSections):
					numProfs = len(objs[i]['sections'][j]['instructors'])
					numTimes = len(objs[i]['sections'][j]['meetingTimes'])
					
					k = 0
					while k in range(0, numProfs):
						prof = objs[i]['sections'][j]['instructors'][k]['name']
						k += 1

					k = 0
					while k in range(0, numTimes):
						s = objs[i]['sections'][j]['meetingTimes'][k]['startTime']
						e = objs[i]['sections'][j]['meetingTimes'][k]['endTime']
						pm = objs[i]['sections'][j]['meetingTimes'][k]['pmCode']
						building = objs[i]['sections'][j]['meetingTimes'][k]['buildingCode']
						room = objs[i]['sections'][j]['meetingTimes'][k]['roomNumber']
						campus = objs[i]['sections'][j]['meetingTimes'][k]['campusName']
						day = objs[i]['sections'][j]['meetingTimes'][k]['meetingDay']
						mode = objs[i]['sections'][j]['meetingTimes'][k]['meetingModeDesc']

						#if s is None and e is None:
							#print "============================="
							#print 'Hours by arrangement'
						#else:
						if s is not None and e is not None:
							day = getDay(day)

							if day == currDay and campus == campusChoice:
								start = processTime(s)
								end = processTime(e)
								
								print course
								print campus
								print building, "-", room
								print start," - ",end, " ", pm
								#print prof
						k += 1
					j += 1
				i += 1
		else:
			print('Invalid Department\n')

		done = input('Continue?\n')
"""""
#getDepts()
main()