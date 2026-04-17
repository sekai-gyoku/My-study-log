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

            raise ValueError(

                f"Expected {expected_type}, but got {token.token_type}"

            )

        self.pos += 1

        return token

    def parse_number(self):

        token = self.eat("NUMBER")

        return NumberNode(token.value)

    def parse_expression(self):

        left = self.parse_number()

        while self.current_token() is not None:

            token = self.current_token()

            if token.token_type == "PLUS":

                self.eat("PLUS")

                right = self.parse_number()

                left = BinaryOpNode(left, "+", right)

            elif token.token_type == "MINUS":

                self.eat("MINUS")

                right = self.parse_number()

                left = BinaryOpNode(left, "-", right)

            else:

                raise ValueError(f"Unexpected token in expression: {token.token_type}")

        return left
    
def evaluate(node):
    print("Evaluating node type:", node.node_type)
    
    if node.node_type == "Number":
        return node.value
    
    if node.node_type == "BinaryOp":
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)
        
        if node.op == "+":
            return left_value + right_value
        elif node.op == "-":
            return left_value - right_value
        else:
            return ValueError(f"Unknown node type: {node.node_type}")
        
def main():

    text = input("Enter expression: ")

    while not text:

        text = input("Input is empty, please re-enter: ")

    tokens = tokenize(text)

    print("\n=== Tokens ===")

    for token in tokens:

        print(token)

    parser = Parser(tokens)

    ast = parser.parse_expression()

    print("\n=== AST ===")

    pprint(ast.to_dict())
    
    result = evaluate(ast)
    
    print("\n=== Evaluation Result ===")
    print(result)
    
if __name__ == "__main__":
    main()