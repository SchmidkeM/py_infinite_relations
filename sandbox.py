from itertools import islice
from infinite_relations import *

even = selection(integer_relation("x"), lambda x: x % 2 == 0)
odd = selection(integer_relation("x"), lambda x: x % 2 != 0)

N = union(even, odd)

N.print(10)

#################################

w = word_relation()

ws = selection(w, lambda w: len(w) > 3)
ws.print(10)

#################################

add_relation().print(10)

#################################


class Evens(Relation):
    def __init__(self, schema: list = ["n"]):
        if not len(schema) == 1:  # standardní kontrola
            raise Exception("Schema of Evens must have 1 attribute")
        super().__init__(schema)

    def is_member(self, tpl: dict) -> bool:
        return len(tpl) == 1 and list(tpl.values())[0] % 2 == 0

    def members(self):
        n = 0
        while True:
            yield {self.get_schema()[0]: n}
            n += 2

    def can_is_member_loop(self):
        return False


e = Evens()
e.print(10)
