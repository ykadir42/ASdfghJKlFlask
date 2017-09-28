import random

#returns the contents of the occupations.csv file
def open_file(filename): 
	source = open(filename, 'rU')
	occupations = source.read()
	source.close()
	return occupations


def make_dict(): #makes a dictionary with occupations as keys and their respective percentages + links in one list as values
	occupations = open_file("data/occupations.csv")
	occupation_list = occupations.split("\n") #makes list of each occupation with its percentage
	occupations_dict={}
	for i in occupation_list[1:-2]:
		#if the occupation has a comma in it
		if(i[0]=='"'):
			#splitting by the quote and comma gets us the occupation and the percentage + link seperated
			occupation = i[1:].split('",')
			#The Link and percentage are still joined by the comma so split those too
			valAndLink = occupation[1].split(",")
			occupations_dict[occupation[0]] =  [float(valAndLink[0]), valAndLink[1]]
		else:
			#Here, the split by comma seperates all 3
			occupation = i.split(',')
			occupations_dict[occupation[0]] = [float(occupation[1]), occupation[2]]
	return occupations_dict

'''
1) Keep track of two variables:
	rand: random float in [0.0, 99.8]
	sum_percents: sum of all the percents of the occupations visited so far
2) Go through the dictionary
3) If rand falls in between [sum_percents, sum_percents + percent of current occupation),
   return the current occupation.
This ensures that every occupation has its own range inside [0.0, 99.8). If rand falls within
an occupation's range, that occupation gets returned.
'''
def random_occupation():
	occupations_dict = make_dict()
	rand=random.random()*99.800000
	sum_percents=0.0
	for o in occupations_dict.keys():
		#accsess the percentage with occupations_dict[<occupation>][0]
		if (rand >= sum_percents and rand<sum_percents+occupations_dict[o][0]):
			return o
		sum_percents+=occupations_dict[o][0]
