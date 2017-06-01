from hashlib import md5

s = '963ba5'
# print s[:2]

for i in range(9999999):
	if(md5(str(i)).hexdigest()[:6] == s):
		print i
		break