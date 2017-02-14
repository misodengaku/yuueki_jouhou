import csv

with open('r18.csv', 'r') as f:
	reader = csv.reader(f)

	r18_map = {}
	for row in reader:
		cp = "×".join(row)	
		if cp not in r18_map:
			r18_map[cp] = 1
		else:
			r18_map[cp] = r18_map[cp] + 1
		
	r18_rank = []
	for key,count in r18_map.items():
		r18_rank.append((key, count))
	
	r18_rank = sorted(r18_rank, key=lambda x: x[1])
	
	for v in r18_rank:
		print("%s, %d" % (v[0], v[1]))