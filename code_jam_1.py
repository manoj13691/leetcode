def life_lost(s,D):
	a = [ s[i] for i in range(len(s))]
	charge = 1
	D_ = 0
	for i in a:
		if i == "C":
			charge = charge *2
		else:
			D_ = D_ + charge
	return D_

print life_lost("SCSSC",6)

