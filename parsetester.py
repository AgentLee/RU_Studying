import json
import os
import time
from pprint import pprint

path = "data/data_332.json"

with open(path) as json_Data:
	data = json.load(json_Data)

numClasses = len(data)

numSections = 0

""" 
	THIS FIXES 332...maybe
"""
i = 0
while i in range(0, numClasses):
	course = data[i]['title']
	
	if data[i]['sections'] != 0:
		numSections += 1	

	print course, numSections

	i += 1


"""
	FIXES 960+
i = 0
while i in range(0, numClasses):
	course = data[i]['title']
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

			if s is not None or e is not None or pm is not None or building is not None or room is not None or campus is not None:
				print s, e, pm
				print building, room, campus

			k += 1

		j += 1


	i += 1
"""