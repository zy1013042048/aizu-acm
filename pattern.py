strlist = ['batch1_labelAt0_nonNumeric.txt','batch1_labelAt3_missing_column.txt','batch1_labelAt128.txt','batch1_labelAt1.txt']
loc = 0
num = ""
for i in range(len(strlist)):
	loc = strlist[i].find('labelAt')+7
	for j in range(loc,len(strlist[i])):
		if( strlist[i][j]>=u'\u0030' and strlist[i][j]<=u'\u0039'):
			num+=strlist[i][j]
		else:
			break
print(num)