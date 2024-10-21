def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        field = ast.value.split(" ")[0]
        operator = ast.value.split(" ")[1]
        right_value = ast.value.split(" ")[2]

        actual_value = data.get(field)

        if isinstance(actual_value, str) and right_value.isnumeric():
            actual_value = float(actual_value)

        if operator == ">":
            return actual_value > float(right_value)
        elif operator == "<":
            return actual_value < float(right_value)
        elif operator == "==":
            return actual_value == right_value

    if ast.node_type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)

        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result

    return False

