from itertools import islice
from infinite_relations import *

# even = selection(integer_relation("x"), lambda x: x % 2 == 0)
# odd = selection(integer_relation("x"), lambda x: x % 2 != 0)

# N = union(even, odd)


# w = word_relation()

# ws = selection(w, lambda w: len(w) > 3)
# ws.print(2000)


n1 = integer_relation()
n2 = integer_relation()

cross_join(n1, n2).print(20)
