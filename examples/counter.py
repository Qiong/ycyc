#python from collections import counter

from collections import Counter
import collections

print collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])

print collections.Counter({'a':2, 'b':3, 'c':1})

print collections.Counter(a=2, b=3, c=1)

print collections.Counter(['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'])

print collections.Counter(['testing', '1', '2', 'testing'])

"""
An empty Counter can be constructed with no arguments and populated via the update() method.

import collections

c = collections.Counter()
print 'Initial :', c

c.update('abcdaab')
print 'Sequence:', c

c.update({'a':1, 'd':5})
print 'Dict    :', c

The count values are increased based on the new data, rather than replaced. In this example, the count for a goes from 3 to 4.

$ python collections_counter_update.py

Initial : Counter()
Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})

"""