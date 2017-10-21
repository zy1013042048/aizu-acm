n = int(input().strip())
elem = 0
a = []
sub = []
temp = 0
for i in range(0,n):
	temp = int(input().strip())
	a.append(temp)
	if i == 0:
		continue
	for j in range(0,i):
		elem = a[i] - a[j]
		if elem not in sub:
			sub.append(elem)
print("%d"%max(sub))