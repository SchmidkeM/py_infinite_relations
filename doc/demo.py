from infinite_relations import *

# constants for the demo functions
s = ["name", "age"]
names = ["Dani", "Emil", "Franta", "Martin", "Karel", "Standa", "Rudolf", "Tereza"]
ages = [23, 26, 25, 23, 28, 19, 25, 14]


def demo_create_a_list_relation():
    print("\n\nDEMO CREATE A LIST RELATION")
    print(
        "A new list relation can be created by using 'list_relation(schema, content)'."
    )
    print("\nSchema is a list of strings - attribute names.")
    print(
        "\nContent is a list of dictionaries - tuples, keyset of all the dictionaries must be identical and must match the schema."
    )
    r = list_relation(
        ["name", "age"], [{"name": "Martin", "age": 23}, {"name": "Emil", "age": 26}]
    )
    print(
        '\nFor example, By using\n\'r = list_relation(["name", "age"], [{"name": "Martin", "age": 23}, {"name": "Emil", "age": 26}])\'\nwe will receive a binary relation \'r\' containing two tuples:'
    )
    r.print()
    print("We can print the relation by using 'r.print()'\n")


def demo_create_an_infinite_relation():
    print("\n\nDEMO CREATE AN INFINITE RELATION")
    print(
        "A new infinite relation can be created by using 'general_integer_relation(schema, condition)'."
    )
    print("\nSchema is a list of strings - attribute names.")
    print(
        "\nCondition is a function whose number of arguments is equal to the length of the schema and outputs a true/false value."
    )
    r = general_integer_relation(["x", "y"], lambda x, y: x + 1 == y)
    print(
        "\nFor example, By using\n'r = general_integer_relation([\"x\", \"y\"], lambda x, y: x + 1 == y)'\nwe will receive a binary relation 'r' that theoretically contains all couples of numbers, where the second number is larger by 1."
    )
    r.print(10)
    print("We can print the first 10 members of the relation by using 'r.print(10)'\n")


def demo_premade_infinite_relations():
    print("\n\nDEMO PREMADE INFINITE RELAION")
    print(
        "Apart from creating your own infinite relations with 'general_integer_relation(schema, condition)' there are some otimized pre-made ones."
    )
    a = add_relation()
    print(
        "\nFor example using 'a = add_relation()' we get a ternary relation containing all the possible sums of two numbers."
    )
    print("\n Using 'a.print(10)', we can take a look at the first few members:")
    a.print(10)


def demo_union():
    print("\n\nDEMO UNION")
    S = ["name", "age"]
    print("To unite two relations, their schemas must be equal, for example: " + str(S))
    r1 = list_relation(
        s, [{"name": name, "age": age} for (name, age) in zip(names[0:5], ages[0:5])]
    )
    print("We have a relation 'r1' that has 5 tuples:")
    r1.print()
    r2 = list_relation(
        s, [{"name": name, "age": age} for (name, age) in zip(names[3:8], ages[3:8])]
    )
    print("And 'r2' that has 3 different tuples and 2 identical ones:")
    r2.print()
    u = union(r1, r2)
    print(
        "After uniting 'r1' and 'r2' by using 'u = union(r1, r2)' the resulting relation 'u' should contain all 8 different tuples: "
    )
    u.print()


def demo_difference():
    print("\n\nDEMO DIFFERENCE")
    S = ["x", "y", "sum"]
    print(
        "To subtract one relation from another, their schemas must be equal. For example: "
        + str(S)
    )
    Rf = list_relation(
        S,
        [
            {"x": 1, "y": 2, "sum": 3},
            {"x": 0, "y": 0, "sum": 1},
            {"x": 0, "y": 1, "sum": 1},
        ],
    )
    print("We will subtract a list relation 'Rf' with a few tuples:")
    Rf.print()
    add = add_relation()
    print(
        "From an infinite relation 'add' containing all possible sums of two integers: (first 10 members shown)"
    )
    add.print(10)
    print("After using 'difference(add, Rf).print(10)'")
    print("The result should look like this:")
    difference(add, Rf).print(10)
    print("Notice the two tuples [1, 2, 3] and [0, 1, 1]) missing from the list.")
    print(
        "\nWe can also subtract the infinite relation from the finite one: 'difference(Rf, add).print(10)'"
    )
    difference(Rf, add).print(10)
    print(
        "Only one tuple should remain - [0, 0, 1] - which isn't included in the add relation, because 0 + 0 != 1."
    )


def demo_cross_join():
    print("\n\nDEMO CROSS JOIN")
    print(
        "To multiply two relations, there are no requirements regarding their schemas."
    )
    print("We will be multiplying a relation 'Rf' containing a few people:")
    Rf = list_relation(
        ["name", "age"],
        [{"name": name, "age": age} for (name, age) in zip(names[0:3], ages[0:3])],
    )
    Rf.print()
    print(
        "With an infinite unary relation of natural numbers which can for represent rounds of a game: (first 10 members shown)"
    )
    N = integer_relation(["round"])
    N.print(10)
    print(
        "The result of 'cross_join(Rf, N)' will be an infinite ternary relation: (first 20 members shown)"
    )
    cross_join(Rf, N).print(20)
    print(
        "If the schemas have any of the same attributes, one of each will get renamed:"
    )
    print(
        "We will demonstrate by multiplying the 'Rf' relation with itself. 'cross_join(Rf, Rf)' will yield:"
    )
    cross_join(Rf, Rf).print()


def demo_projection():
    print("\n\nDEMO PROJECTION")
    print(
        "Projection can be used on any relation, you can only project the relation on attributes it has:"
    )
    print("For example, we can take only the names from the relation 'Rf':")
    Rf = list_relation(
        ["name", "age"],
        [{"name": name, "age": age} for (name, age) in zip(names[0:5], ages[0:5])],
    )
    Rf.print()
    print("'projection(Rf, [\"name\"])' will yield:")
    projection(Rf, ["name"]).print()
    print("\nOr we can ommit the sum from add relation:")
    add = add_relation()
    add.print(10)
    print('\'projection(add, ["x", "y"])\' will yield:')
    projection(add, ["x", "y"]).print(10)


def demo_selection():
    print("\n\nDEMO SELECTION")
    print(
        "Selection filters the relation using a lambda function provided in the input, and names of attributes from the schema whose values will be passed to the lambda function."
    )
    print("For example, restricting relation 'Rf' of a few people base on age:")
    Rf = list_relation(
        ["name", "age"],
        [{"name": name, "age": age} for (name, age) in zip(names[0:5], ages[0:5])],
    )
    Rf.print()
    print("'selectin(Rf, lambda age: age > 23, [\"age\"])' will yield:")
    selection(Rf, lambda x: x > 23, ["age"]).print()
    print(
        "You can do without specifying the names of attributes in the third parameter, if the lambda function has 0 parameters:"
    )
    print("'selection(Rf, lambda: False)' will yield:")
    selection(Rf, lambda: False).print()
    print(
        "Or if the lambda has the same number of parameters as there are attributes in the schema (2 in here):"
    )
    print("'selection(Rf, lambda name, age: age > 23)' will yield:")
    selection(Rf, lambda name, age: age > 23).print()
    print(
        "Names of the parameters when defining the actual lambda function have no effect."
    )


def demo_intersection():
    print("\n\nDEMO INTERSECTION")
    S = ["x", "y", "sum"]
    print(
        "To intersect two relations they must have the same schema, for example: "
        + str(S)
    )
    print("We will intersect a finite relation Rf:")
    Rf = list_relation(
        S,
        [
            {"x": 1, "y": 2, "sum": 3},
            {"x": 0, "y": 0, "sum": 1},
            {"x": 0, "y": 1, "sum": 1},
        ],
    )
    Rf.print()
    print("With an infinite add relation:")
    add = add_relation()
    add.print(10)
    print("'intersection(add, Rf)' should yield relation containing two tuples:")
    intersection(add, Rf).print()
    print("And the same should be true for 'intersection(Rf, add)'")
    intersection(Rf, add).print()
    print(
        "As a derived operation, intersection merely calls difference two times, with some added logic based on finiteness of the relations trying to avoid infinite loops with no output as much as possible."
    )


def demo_natural_join():
    print("\n\nDEMO NATURAL JOIN")
    print(
        "To join two relations, there are no requirements regarding their schemas, but they affect the output."
    )
    print("We will join a finite relation of a few people and their grades:")
    S = ["name", "math", "english"]
    grades1 = [1, 2, 2, 4, 3]
    grades2 = [2, 1, 4, 3, 3]
    Rf = list_relation(
        S,
        [
            {"name": name, "math": g1, "english": g2}
            for (name, g1, g2) in zip(names[:5], grades1, grades2)
        ],
    )
    Rf.print()
    print("With an infinite add relation where we name the attributes in preparation: ")
    add = add_relation(["math", "english", "grades_sum"])
    add.print(10)
    print(
        "The result should add one column to the finite relation containing the sums:"
    )
    natural_join(Rf, add).print(5)
    print(
        "As a derived operation, natural join is just a combination of cross_join, projection and n selections, where n is the number of common attributes."
    )


def demo_rename():
    print("\n\nDEMO RENAME")
    print(
        "To rename attributes of a relation, you need to provide a list of the attributes you want to rename, and a list of new_names of the same length."
    )
    print(
        "For example, we can rename an infinite add relation, to represent sums of grades instead of an abstract sum:"
    )
    add = add_relation()
    add.print(10)
    print('\'rename(add, ["x", "y"], ["math", "english"])\' will yield:')
    add.rename(["x", "y"], ["math", "english"])
    add.print(10)
    print(
        "Rename is not derived from any other operation, but E.F. Codd doesn't include it in his set of basic relational operations, hence it being in this group."
    )
    print(
        "It's the only operation that mutates the original relation instead of creating a new instance!"
    )


def demo_division():
    print("\n\nDEMO DIVISION")
    print(
        "To divide a relation by another one, the second one's schema must be a subset of the first one's"
    )
    print(
        "For example, we will use a relation 'Rf' of a few names and subjects they've completed:"
    )
    subjects = ["math", "math", "math", "math", "english", "english"]
    Rf = list_relation(
        ["name", "subject"],
        [
            {"name": name, "subject": sub}
            for (name, sub) in zip(names[:4] + names[:2], subjects)
        ],
    )
    Rf.print()
    print(
        "We will try to get only the names of people who've completed both subjects, by dividing it by a unary relation containing both subjects' names:"
    )
    subs = list_relation(["subject"], [{"subject": "math"}, {"subject": "english"}])
    subs.print()
    print("'division(Rf, subs)' should yield:")
    division(Rf, subs).print()
    print(
        "As a derived operation, division only calls Difference, Cross_join and Projection in a certain order."
    )
