#A program that can decipher expressions consisting of logic operators and variables

def interpret(expression, info):

    # First, evaluate the expression to replace variables with their values
    for index, i in enumerate(expression):
        # Interpret all nestled lists
        if isinstance(i, list):
            expression[index] = interpret(i, info)

        # Exchange all varietals for info counterpart
        elif i in info:
            expression[index] = info[i]


    # Handle the "NOT" logic
    if "NOT" in expression:
        for index, i in enumerate(expression):

            #Update the value after NOT in the expression
            if i == "NOT" and index + 1 < len(expression):
                next_value = expression[index + 1]
                if next_value == "true":
                    return "false"

                elif next_value == "false":
                    return "true"

    # Handle the "OR" logic
    if "OR" in expression:
        if "true" in (expression[2], expression[0]):
            return "true"
        return "false"

    # Handle the "AND" logic
    if "AND" in expression:
        if "true" in expression[2] and "true" in expression[0]:
            return "True"
        return "false"

    # Return the expression unchanged
    return expression


interpret(["NOT", ["NOT", ["NOT", ["cat_asleep", "OR", ["NOT", "cat_asleep"]]]]],
               {"cat_asleep": "false"})