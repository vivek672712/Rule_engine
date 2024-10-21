from flask import Flask, request, jsonify
from api import create_rule, combine_rules
from parser import parse_to_ast  # Ensure this import is correct
from rule_evaluator import evaluate_rule  # Import the evaluate_rule function

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi vivek ! Welcome to the Rule Engine API."

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    ast = create_rule(rule_string)
    return jsonify({"ast": str(ast)}), 201

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": str(combined_ast)}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.json
    user_data = data.get('user_data')
    rule_ast = data.get('rule_ast')

    # Check if both user_data and rule_ast are provided
    if user_data is None or rule_ast is None:
        return jsonify({"error": "AST and user data are required."}), 400

    print(f"Evaluating rule: {rule_ast} with user data: {user_data}")

    # Proceed to evaluate the rule
    ast = parse_to_ast(rule_ast)  # Ensure parse_to_ast is defined and imported
    if ast is None:
        return jsonify({"error": "Failed to parse the rule into AST."}), 400
    
    result = evaluate_rule(ast, user_data)  # This should now work
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
