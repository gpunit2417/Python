s = "Even Length Words In A String"

wrds = s.split()

even_wrds = [w for w in wrds if len(w) % 2 == 0]

res = " ".join(even_wrds)
print(res)
