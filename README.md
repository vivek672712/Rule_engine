A simple API for creating, combining, and evaluating business rules using Abstract Syntax Trees (AST).

**Technologies Used**
Flask: Web framework for API.
SQLAlchemy: ORM for database interactions.
PostgreSQL/MySQL/SQLite: Database support.
Setup
**Prerequisites**
Python 3.x
Database (PostgreSQL, MySQL, or SQLite)
**Installation**
cd Rule-Engine-API

**Install dependencies:**
pip install -r requirements.txt

**Run the application:**
python app.py
API Endpoints
**1. Create Rule**
POST /create_rule
Body:
{
    "rule_string": "age > 30 AND department = 'Sales'"
}
Response:
{
    "ast": "<AST representation>"
}
**2. Combine Rules**
POST /combine_rules
Body:
{
    "rules": ["age > 30", "department = 'Sales'"]
}
Response:
{
    "combined_ast": "<Combined AST representation>"
}
**3. Evaluate Rule**
POST /evaluate_rule
Body:
{
    "rule_string": "age > 30 AND department = 'Sales'",
    "context": {
        "age": 35,
        "department": "Sales"
    }
}
Response:

{
    "result": true
}
Example Usage (via Postman)
Create Rule: POST /create_rule
Combine Rules: POST /combine_rules
Evaluate Rule: POST /evaluate_rule
