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

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.pos = 0;
        
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
    
    def parser_expression(self):
        left = self.eat("NUMBER")
        
        operations = []
        
        while self.current_token() is not None:
            token = self.current_token()
        
            if token.token_type == "PLUS":
                op = self.eat("PLUS")
                right = self.eat("NUMBER")
                operations.append({
                    "op": op.token_type,
                    "value": right.value
                })
            elif token.token_type == "MINUS":
                op = self.eat("MINUS")
                right = self.eat("NUMBER")
                operations.append({
                    "op": op.token_type,
                    "value": right.value
                })
            else:
                raise ValueError(f"Unpected token in expression:{token.token_type}")
        
        return {
            "type": "Expression",
            "first": left.value,
            "rest": operations
        }
    
def main():
    text = input("Enter expression: ")
    while not text:
        text = input("Input is empty, please re-enter:")
    tokens = tokenize(text)
    
    print("\nToken:")
    for token in tokens:
        print(token)
        
    parser = Parser(tokens)
    parsed = parser.parser_expression()
    
    print("\nParsed structure:")
    print(parsed)
    
        
if __name__ == "__main__":
    main()

            
    