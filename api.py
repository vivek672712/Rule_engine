from rule_ast import RuleNode  # Assume this is your AST structure
from database import Session, Rule
from parser import parse_to_ast

def create_rule(rule_string):
    ast = parse_to_ast(rule_string)
    session = Session()
    new_rule = Rule(rule_string=rule_string)
    session.add(new_rule)
    session.commit()
    return ast

def combine_rules(rules):
    ast_nodes = [create_rule(rule) for rule in rules]
    
    # Combine logic: Let's say we combine them with an AND operation for simplicity
    if not ast_nodes:
        return None

    combined_ast = {
        'type': 'operator',
        'value': 'AND',
        'left': ast_nodes[0],
        'right': ast_nodes[1] if len(ast_nodes) > 1 else None
    }
    
    # If there are more than two rules, you can further extend this logic
    for ast in ast_nodes[2:]:
        combined_ast = {
            'type': 'operator',
            'value': 'AND',
            'left': combined_ast,
            'right': ast
        }

    return combined_ast

def evaluate_rule(ast, user_data):
    # Example evaluation logic for a simple AST
    if ast.type == 'operator':
        left_result = evaluate_rule(ast.left, user_data)
        right_result = evaluate_rule(ast.right, user_data)
        if ast.value == 'AND':
            return left_result and right_result
        elif ast.value == 'OR':
            return left_result or right_result
    elif ast.type == 'operand':
        # Here you would compare user_data[ast.value] with the value in the AST node
        if ast.operator == '>':
            return user_data[ast.value] > ast.comparison_value
        # Add more conditions as needed for other operators
    return False  # Default return for unsupported cases

