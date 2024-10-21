class ASTNode:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type  # 'operand' or 'operator'
        self.value = value
        self.left = left
        self.right = right

def parse_rule(rule):
    tokens = rule.split()
    if len(tokens) < 3:
        return None

    left_operand = tokens[0]
    operator = tokens[1]
    right_operand = tokens[2]

    left_node = ASTNode('operand', left_operand)
    right_node = ASTNode('operand', right_operand)
    root_node = ASTNode('operator', operator, left_node, right_node)

    return root_node

def combine_rules(rules):
    combined_ast = None
    operator_counts = {'AND': 0, 'OR': 0}

    for rule in rules:
        ast = parse_rule(rule)
        
        def count_operators(node):
            if node is not None:
                if node.node_type == 'operator':
                    if node.value not in operator_counts:
                        operator_counts[node.value] = 0
                    operator_counts[node.value] += 1
                    count_operators(node.left)
                    count_operators(node.right)

        count_operators(ast)

        if combined_ast is None:
            combined_ast = ast
        else:
            if operator_counts['AND'] >= operator_counts['OR']:
                new_root = ASTNode('operator', 'AND', combined_ast, ast)
            else:
                new_root = ASTNode('operator', 'OR', combined_ast, ast)

            combined_ast = new_root

    return combined_ast

