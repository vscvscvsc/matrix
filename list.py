
def init_set():
	ret = []
	for i in range(1, 11):
		for j in range(1, 11):
			for k in range(1, 11):
				for l in range(1, 11):
					for m in range(1, 11):
						ret.append((i, j, k, l,m))
	return ret

i = init_set()

num = 0

for x in i:
	num +=1
print num