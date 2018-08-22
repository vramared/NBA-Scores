from flask import Flask
import requests, bs4


nba = requests.get("http://www.nbaboxscoregenerator.com/")
soup = bs4.BeautifulSoup(nba.text, 'html.parser')

opts = soup.findAll('option')
if(len(opts) == 0) : 
	print('No games to report right now. Check back later.')
	
else : 

	str1 = "Totals"
	totalScore = []
	counter = 0;
	athletes = []
	points = []
	rebs = []
	asts = []

	def truncate(f, n):
	    s = '{}'.format(f)
	    if 'e' in s or 'E' in s:
	        return '{0:.{1}f}'.format(f, n)
	    i, p, d = s.partition('.')
	    return '.'.join([i, (d+'0'*n)[:n]])

	for i in range(len(opts)):
		print(opts[i].text)

		nbaGame = requests.get("http://www.nbaboxscoregenerator.com/?gameID=" + str(i))
		soupGame = bs4.BeautifulSoup(nbaGame.text, 'html.parser')
		players = soupGame.findAll('td', {'style': 'text-align: left'})	
		for j in range(len(players)):
			if players[j].text == str1:
				pass
			else:	
				athletes.append(players[j].text)

		stats = soupGame.findAll('td')
		totalScore = []
		for k in range(len(stats)):
			#print(stats[k].text)
			temp = stats[k].text
			if temp == str1:
				totalScore.append(stats[k+13].text)
			elif len(temp) > 1 and (temp[1] == '.' or temp[1] == 'e'):
				if stats[k+1].text == ' DNP -- INACTIVE' or stats[k+1].text == ' DNP -- DNP' or stats[k+1].text == ' DNP -- NWT' or stats[k+1].text == ' DNP -- ' or stats[k+1].text == ' DNP -- DND':
					points.append(int(0))
					rebs.append(int(0))
					asts.append(int(0))
				else:
					points.append(int(stats[k+13].text))
					rebs.append(int(stats[k+7].text))
					asts.append(int(stats[k+8].text))

		test = opts[i].text
		teams = test.split(' @ ')
		print(str(teams[0]) + ': ' + str(totalScore[0]))
		print(str(teams[1]) + ': ' + str(totalScore[1]))
		score0 = int(totalScore[0])
		score1 = int(totalScore[1])

		if score0 > score1 :
			print(str(teams[0]) + ' beat ' + str(teams[1]) + ' by a score of ' + str(score0) + ' to ' + str(score1) + '.' )
		elif score1 > score0 :
			print(str(teams[1]) + ' beat ' + str(teams[0]) + ' by a score of ' + str(score1) + ' to ' + str(score0) + '.' )

	potd = []


	for l in range(len(athletes)):
		score = (.8 * points[l]) + (.3 * rebs[l]) + (.6 * asts[l])
		potd.append(score)

	maxScore = max(potd)
	indOfMax = 0;



	for m in range(len(potd)):
		if potd[m] == maxScore:
			indOfMax = m

	maxScore = truncate(maxScore, 3)

	print('Your Player of the Day is ' + str(athletes[indOfMax]) + ' with a POTD score of ' + str(maxScore) + '.')
	print('Statline: ' + str(points[indOfMax]) + 'pts/ ' + str(rebs[indOfMax]) + 'rebs/ ' + str(asts[indOfMax]) + 'asts')



