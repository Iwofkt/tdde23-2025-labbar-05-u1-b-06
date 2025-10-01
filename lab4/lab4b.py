def interpret(expression, info: dict) -> str | None:
    """
    Recursively interprets a logical expression represented as nested lists.

    Operators:
    - "NOT": NOT binary operator, format ["NOT", expr]
    - "AND", "OR": binary operators, format [left, operator, right]

    Operands can be:
    - "true" or "false" (strings)
    - Variables (strings) looked up in info dict
    - Nested expressions (lists)

    :param expression: list or str: logical expression or variable.
    :param info: dict: Mapping variable names to "true" or "false".

    :return: str: Evaluated "true" or "false" string.
    """
    if not isinstance(expression, list):
        # Base case: variable
        return info.get(expression, expression)

    # Handle NOT operator
    if len(expression) == 2 and expression[0] == "NOT":
        val = interpret(expression[1], info)
        return "false" if val == "true" else "true" if val == "false" else val

    # Handle ANDs and ORs
    if len(expression) == 3:
        left, operator, right = expression
        left_val = interpret(left, info)
        right_val = interpret(right, info)

        if operator == "AND":
            return "true" if left_val == "true" and right_val == "true" else "false"
        elif operator == "OR":
            return "true" if left_val == "true" or right_val == "true" else "false"
    return None