Readme
=======================================================================

So basically using Rutgers API to get available classrooms for studying.

Plan is to get this to work as a webapp eventually with django.

Files
=======================================================================

	* * * * * * * * * * * * * * * * * * * * * * * * * * * *
	* parse2.py			--> 	bug fixed			    *
	* parsetester.py 	-->		use to debug parse2  	  *
	* * * * * * * * * * * * * * * * * * * * * * * * * * * *

	data.json		-->		all classes/departments
	guitest.py		--> 	exactly what it sounds like
	parse.py		--> 	parses through all departments through url
	parsetest.py	-->		JSON parse test
	rustudy.py 		-->		duplicate of selective.py
	selective.py	--> 	bug with 332 through url
	simplecgi.py	--> 	html test aka need to use django
	test.py			-->		loop through directory test
	timetest.py		--> 	get time and stuff 

Directories
=======================================================================
	data  			--> 	all json files for all departments
	gui 			--> 	gui .py files in development
	json 			--> 	random json files for testing
