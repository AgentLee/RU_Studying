import json
import urllib2
"""""
Successful parse through all departments
"""""

"""""
data = {
	"country abbreviation": "US",
	"places": [
    	{
        	"place name": "Belmont",
        	"longitude": "-71.4594",
        	"post code": "02178",
        	"latitude": "42.4464"
    	},
    	{
        	"place name": "Belmont",
        	"longitude": "-71.2044",
        	"post code": "02478",
        	"latitude": "42.4128"
    	}
	],
		"country": "United States",
		"place name": "Belmont",
		"state": "Massachusetts",
		"state abbreviation": "MA"
	}

print data['places'][1]['post code']

link = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=b05b7682688883918976e21cb75d5eeb&semester=92015&subj=198&campus=NB&level=U"
data = urllib2.urlopen(link)
obj = json.load(data)

print(obj[0]['sections'][0]['meetingTimes'][0]['startTime'])
print(obj[0]['sections'][1]['index'])
"""""

dep = 0
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

	#subj starts at 105
	#link = "http://sauron.rutgers.edu/~rfranknj/soc/api.php?key=b05b7682688883918976e21cb75d5eeb&semester=92015&subj=198&campus=NB&level=U"
	#dept1 = link[105]
	#dept2 = link[106]
	#dept3 = link[107]
	#dept = dept1+dept2+dept3

	data = urllib2.urlopen(dept)

	objs = json.load(data)

	if objs is not None:
		numClasses = len(objs)

		i = 0

		while i in range(0, numClasses):
			course = objs[i]['title']
			numSections = len(objs[i]['sections'])

			j = 0
			while j in range(0, numSections):
				numTimes = len(objs[i]['sections'][j]['meetingTimes'])

				print subj, numTimes, course

				j += 1
			i += 1

	dep += 1		