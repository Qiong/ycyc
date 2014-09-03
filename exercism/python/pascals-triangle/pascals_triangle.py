def next_line(line):
    next = [ 1 ]
    for ix in range(1, len(line)):
        next.append(line[ix] + line[ix-1])
    next.append(1)
    return next

def triangle(num):
    next = [ [ 1 ] ]
    out = [ '1' ]
    for ix in range(1, num+1):
        next = next_line( next )
        out.append( ' '.join(map(str, next)) )
    return out

def row(num):
    tri = triangle(num)
    return tri[len(tri) - 1]

def is_triangle(test):
    comp = triangle(len(test)-1)
    for ix in range(len(test)):
        if test[ix] != comp[ix]:
            return False
    return True

"""

Pascal's triangle

from itertools import imap, islice, izip


def triangle(n):
    #Return Pascal's triangle up to row n (zero-based
    return list(islice(rows_str(), n + 1))


def is_triangle(tri):
    #Return true if Pascal's triangle.
    return all(r1 == r2 for r1, r2 in izip(tri, rows_str()))


def row(n):
    #Return row n (zero-based) of Pascal's triangle.
    r = next(islice(rows(), n, n + 1))
    return " ".join(imap(str, r))


def rows_str():
    #Generate the rows (str) of Pascal's triangle.
        for r in rows():
        yield " ".join(imap(str, r))


def rows():
    #Generate the rows (list of int) of Pascal's triangle.
    curr_row = [1]
    yield curr_row
    while True:
        prev_row = curr_row
        curr_row = []
        # curr_row[0] = 1
        curr_row.append(1)
        # For 1 <= i < len(prev_row),
        #   curr_row[i] = prev_row[i - 1] + prev_row[i]
        curr_row.extend(
            prev_row[i - 1] + prev_row[i] for i in xrange(1, len(prev_row)))
        # curr_row[len(prev_row)] = 1
        curr_row.append(1)
        yield curr_row
"""