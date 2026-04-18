from pprint import pprint

class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"Token(type={self.token_type}, value={self.value})"


def tokenize(text):
    tokens = []
    i = 0

    while i < len(text):
        ch = text[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit():
            start = i
            while i < len(text) and text[i].isdigit():
                i += 1
            number_text = text[start:i]
            tokens.append(Token("NUMBER", int(number_text)))
            continue

        if ch == "+":
            tokens.append(Token("PLUS", ch))
            i += 1
            continue

        if ch == "-":
            tokens.append(Token("MINUS", ch))
            i += 1
            continue

        if ch == "*":
            tokens.append(Token("STAR", ch))
            i += 1
            continue

        if ch == "/":
            tokens.append(Token("SLASH", ch))
            i += 1
            continue

        if ch == "(":
            tokens.append(Token("LPAREN", ch))
            i += 1
            continue

        if ch == ")":
            tokens.append(Token("RPAREN", ch))
            i += 1
            continue

        raise ValueError(f"Unexpected character: {ch}")

    return tokens


class NumberNode:
    def __init__(self, value):
        self.node_type = "Number"
        self.value = value

    def to_dict(self):
        return {
            "type": self.node_type,
            "value": self.value
        }


class BinaryOpNode:
    def __init__(self, left, op, right):
        self.node_type = "BinaryOp"
        self.left = left
        self.op = op
        self.right = right

    def to_dict(self):
        return {
            "type": self.node_type,
            "op": self.op,
            "left": self.left.to_dict(),
            "right": self.right.to_dict()
        }


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, expected_type):
        token = self.current_token()

        if token is None:
            raise ValueError(f"Expected {expected_type}, but reached end of input")

        if token.token_type != expected_type:
            raise ValueError(f"Expected {expected_type}, but got {token.token_type}")

        self.pos += 1
        return token

    def parse_factor(self):
        token = self.current_token()

        if token is None:
            raise ValueError("Unexpected end of input while parsing factor")

        if token.token_type == "NUMBER":
            number_token = self.eat("NUMBER")
            return NumberNode(number_token.value)

        if token.token_type == "LPAREN":
            self.eat("LPAREN")
            expr = self.parse_expression()
            self.eat("RPAREN")
            return expr

        raise ValueError(f"Unexpected token in factor: {token.token_type}")

    def parse_term(self):
        left = self.parse_factor()

        while self.current_token() is not None and self.current_token().token_type in ("STAR", "SLASH"):
            token = self.current_token()

            if token.token_type == "STAR":
                self.eat("STAR")
                right = self.parse_factor()
                left = BinaryOpNode(left, "*", right)
            elif token.token_type == "SLASH":
                self.eat("SLASH")
                right = self.parse_factor()
                left = BinaryOpNode(left, "/", right)

        return left

    def parse_expression(self):
        left = self.parse_term()

        while self.current_token() is not None:
            token = self.current_token()

            if token.token_type == "PLUS":
                self.eat("PLUS")
                right = self.parse_term()
                left = BinaryOpNode(left, "+", right)
            elif token.token_type == "MINUS":
                self.eat("MINUS")
                right = self.parse_term()
                left = BinaryOpNode(left, "-", right)
            else:
                break

        return left


def evaluate(node):
    if node.node_type == "Number":
        return node.value

    if node.node_type == "BinaryOp":
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)

        if node.op == "+":
            return left_value + right_value
        elif node.op == "-":
            return left_value - right_value
        elif node.op == "*":
            return left_value * right_value
        elif node.op == "/":
            if right_value == 0:
                raise ValueError("division by zero")
            return left_value / right_value
        else:
            raise ValueError(f"Unknown operator: {node.op}")

    raise ValueError(f"Unknown node type: {node.node_type}")

def node_to_expr_string(node):
    if node.node_type == "Number":
        return str(node.value)
    
    if node.node_type == "BinaryOp":
        left_text = node_to_expr_string(node.left)
        right_text = node_to_expr_string(node.right)
        return f"({left_text} {node.op} {right_text})"
    
def fold_constants(node):
    if node.node_type == "Number":
        return node
    
    if node.node_type == "BinaryOp":
        folded_left = fold_constants(node.left)
        folded_right = fold_constants(node.right)
        
        if folded_left.node_type == "Number" and folded_right.node_type == "Number":
            left_value = folded_left.value
            right_value = folded_right.value
            
            if node.op == "+":
                folded_value = left_value + right_value
            elif node.op == "-":
                folded_value = left_value - right_value
            elif node.op == "*":
                folded_value = left_value * right_value
            elif node.op == "/":
                if right_value == 0:
                    raise ValueError("division by zero")
                folded_value = left_value / right_value
            else:
                raise ValueError(f"Unknown operator: {node.op}")
            
            print(f"Folding: {node_to_expr_string(BinaryOpNode(folded_left, node.op, folded_right))} -> {folded_value}")
            return NumberNode(folded_value)
        
        return BinaryOpNode(folded_left, node.op, folded_right)
    
    raise ValueError(f"Unkonwn node type: {node.node_type}")

def format_number(value):
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def main():
    while True:
        text = input("Enter expression: ")

        while not text.strip():
            text = input("Input is empty, please re-enter: ")

        try:
            tokens = tokenize(text)

            print("\n=== Tokens ===")
            for token in tokens:
                print(token)

            parser = Parser(tokens)
            ast = parser.parse_expression()

            if parser.current_token() is not None:
                raise ValueError(
                    f"Unexpected token after expression: {parser.current_token().token_type}"
                )

            print("\n=== Original AST ===")
            pprint(ast.to_dict())

            print("\n=== Constant Folding Log ===")
            folded_ast = fold_constants(ast)

            print("\n=== Folded AST ===")
            pprint(folded_ast.to_dict())

            result = evaluate(folded_ast)

            print("\n=== Evaluation Result ===")
            print(f"Result = {format_number(result)}")
            break

        except ValueError as e:
            print(f"\nInput error, please re-enter. ({e})\n")


if __name__ == "__main__":
    main()