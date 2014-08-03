##python zip example

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print "matrix = ", matrix


print "transposed"
print [[row[i] for row in matrix] for i in range(4)]

print "zip function"
print zip(*matrix)
