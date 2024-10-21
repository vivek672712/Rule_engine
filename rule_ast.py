class RuleNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Reference to left child Node
        self.right = right  # Reference to right child Node
        self.value = value  # Optional value for operand nodes

    def __repr__(self):
        if self.type == "operator":
            return f"({self.left} {self.value} {self.right})"
        else:
            return f"{self.value}"
