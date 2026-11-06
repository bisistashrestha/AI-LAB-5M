print("Name: Bisista Shrestha\nUSN:1WA24CS086")
def unify(expr1, expr2, subst=None):
    if subst is None:
        subst = {}

    # If both expressions are identical
    if expr1 == expr2:
        return subst

    # If first expression is a variable
    if isinstance(expr1, str) and expr1.islower():
        if expr1 in subst:
            return unify(subst[expr1], expr2, subst)

        if occurs_check(expr1, expr2):
            return None

        subst[expr1] = expr2
        return subst

    # If second expression is a variable
    if isinstance(expr2, str) and expr2.islower():
        if expr2 in subst:
            return unify(expr1, subst[expr2], subst)

        if occurs_check(expr2, expr1):
            return None

        subst[expr2] = expr1
        return subst

    # If both are compound expressions
    if isinstance(expr1, tuple) and isinstance(expr2, tuple):
        if len(expr1) != len(expr2):
            return None

        if expr1[0] != expr2[0]:
            return None

        for a, b in zip(expr1[1:], expr2[1:]):
            result = unify(a, b, subst)
            if result is None:
                return None

        return subst

    return None


def occurs_check(var, expr):
    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs_check(var, item) for item in expr[1:])

    return False


# Given expressions
expr1 = ("Eats", "x", "Apple")
expr2 = ("Eats", "Riya", "y")

# Perform unification
result = unify(expr1, expr2)

# Display result
if result is not None:
    print("Unification Successful!")
    print("Substitution Set:", result)
    print("Unified Expression: Eats(Riya, Apple)")
else:
    print("Unification Failed!")
