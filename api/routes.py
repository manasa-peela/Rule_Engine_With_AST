from flask import Blueprint, request, jsonify
from backend.rule_ast import Node
from backend.evaluate import evaluate_rule
from backend.combine import combine_rules

app = Blueprint('app', __name__)

def node_to_dict(node):
    """Convert a Node object to a dictionary."""
    if not node:
        return None
    
    return {
        "node_type": node.node_type,
        "value": node.value,
        "left": node_to_dict(node.left),
        "right": node_to_dict(node.right)
    }

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule')

    ast = Node("operator", value="OR",
               left=Node("operator", value="AND", 
                         left=Node("operand", value="age > 30"), 
                         right=Node("operand", value="department == 'Sales'")),
               right=Node("operand", value="salary > 50000"))
    
    ast_dict = node_to_dict(ast)
    return jsonify({"message": "Rule created", "ast": ast_dict})

def dict_to_node(data):
    """Convert a dictionary back to a Node object."""
    if not data:
        return None
    
    node = Node(node_type=data["node_type"], value=data["value"])
    node.left = dict_to_node(data.get("left"))
    node.right = dict_to_node(data.get("right"))
    
    return node

@app.route('/evaluate_rule', methods=['POST'])
def evaluate():
    try:
        ast_dict = request.json.get('ast')
        data = request.json.get('data')
        
        if not ast_dict or not data:
            return jsonify({"error": "AST or data missing"}), 400
        
        ast = dict_to_node(ast_dict)
        
        result = evaluate_rule(ast, data)
        
        return jsonify({"result": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
