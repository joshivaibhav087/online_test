def kRSA(n,c,m):
	return((c*m)%n)

def geraChaveKRSA(A,B,a,b):
	M = A*B - 1
	e = a*M + A
	d = b*M + B
	n = int((e*d -1)/M)
	return ({'n':n,'pub':e,'priv':d})
