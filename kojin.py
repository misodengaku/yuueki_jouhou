import csv

with open('r18.csv', 'r') as f:
	reader = csv.reader(f)
	header = next(reader)  # ヘッダーを読み飛ばしたい時

	r18_map = {}
	for row in reader:
		for kojin in row:
			if kojin not in r18_map:
				r18_map[kojin] = 1
			else:
				r18_map[kojin] = r18_map[kojin] + 1
		
	r18_rank = []
	for key,count in r18_map.items():
		r18_rank.append((key, count))
	
	r18_rank = sorted(r18_rank, key=lambda x: x[1])
	
	for v in r18_rank:
		print("%s, %d" % (v[0], v[1]))