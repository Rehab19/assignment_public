x = [([1], [2, 3], (4, 5, 6))]
#Desired out → {1, 2, 3, 4, 5, 6}

print(set(for i ls in x[0][1] ))