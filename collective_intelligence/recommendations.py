

critics = { 'Lisa Rose': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.5, 'Just My Luck': 3.0, 
'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0}, 

'Gene Seymour': {'Lady in the Water': 3.0, 'Snake on a Plane': 3.5, 'Just My Luck': 1.5, 
'Superman Returns': 5.0, 'You, Me and Dupree':3.5, 'The Night Listener': 3.0 },

'Michael Phillips': {'Lady in the Water': 2.5, 'Snake on a Plane': 3.0, 'Superman Returns': 3.5, 'The Night Listener': 4.0}, 
'Claudia Puig': {'Snake on a Plane': 3.5, 'Just My Luck': 3.0, 'The Night Listener': 4.5, 'Superman Returns': 4.0, 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snake on a Plane': 4.0, 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree' :2.0},
'Jack Mattews': {'Lady in the Water': 3.0, 'Snake on a Plane': 4.0, 'Superman Returns': 5.0, 'The Night Listener':3.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snake on a Plane': 4.5, 'You Me and Dupree': 1.0, 'Superman Returns': 4.0}}

#Finding Similar Users

 #Eucidean Distance Score

from math import sqrt
def sim_distance(prefs, person1, person2):
	# share_items
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	if len(si) == 0: return 0

	sum_of_squares= sum([(prefs[person1][item] - prefs[person2][item]) ** 2 for item in prefs[person1] if item in prefs[person2]])

	return 1/(1 + sqrt(sum_of_squares))

print(sim_distance(critics, 'Lisa Rose', 'Gene Seymour'))


#Pearson Correlation Score
def sim_pearson(prefs, p1, p2):
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item] = 1

	n = len(si)
	if n == 0: return 1

	sum1 = sum( [prefs[p1][it] for it in si])
	sum2 = sum( [prefs[p2][it] for it in si])

	sum1Sq = sum( [pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum( [pow(prefs[p2][it], 2) for it in si])

	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

	num = pSum - (sum1*sum2/n)
	
	den = sqrt( (sum1Sq- pow(sum1, 2)/n) * (sum2Sq - pow(sum2, 2)/n))
	if den == 0: return 0
	r = num / den
	return r 

print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))

# Ranking the critics
def topMatches(prefs, person, n=5, similarity = sim_pearson):
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

	scores.sort()
	scores.reverse()
	return scores[0:n]

print(topMatches(critics, 'Toby', n=3))