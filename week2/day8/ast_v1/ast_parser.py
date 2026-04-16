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
            tokens.append(Token("+", ch))
            i += 1
            continue

        if ch == "-":
            tokens.append(Token("-", ch))
            i += 1
            continue

        raise ValueError(f"Unexpected character: {ch}")

    return tokens

class NumberNode:
    def __init__(self,value):
        self.node_type = "NUMBER"
        self.value = value
        
    def to_direct(self):
        return{
            "type": self.node_type,
            "value": self.value
        }
        
class BinaryOpnode:
    def __init__(self, left, op, right):
        self.node_type = "BinaryOp"
        self.left = left
        self.op = op
        self.right = right
        
    def to_direct(self):
        return{
            "type": self.node_type,
            "op": self.op,
            "left": self.left.to_direct(),
            "right": self.right.to_direct()
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
            
            if token.token_type == "+":
                self.eat("+")
                right = self.parse_number()
                left = BinaryOpnode(left, "+", right)
            elif token.token_type == "-":
                self.eat("-")
                right = self.parse_number()
                left = BinaryOpnode(left, "-", right)
            else:
                raise ValueError(f"Unexpected token in expression: {token.token_type}")
            
        return left
    
def main():
    text = input("Enter expression: ")
    
    while not text:
        text = input("Input is Empty, please re-enter: ")
        
    tokens = tokenize(text)
    
    print("\n=== Tokens ===")
    for token in tokens:
        print(token)
        
    parser = Parser(tokens)
    ast = parser.parse_expression()
    
    print("\n=== AST ===")
    pprint(ast.to_direct())
    
    print("\nAST root type: ",ast.node_type)
    
if __name__ == "__main__":
    main()