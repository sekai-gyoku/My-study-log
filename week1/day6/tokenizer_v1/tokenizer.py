
class Token:
    def __init__(self, token_type,value):
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
            tokens.append(Token("NUMBER", number_text))
            continue
        
        if ch == "+":
            tokens.append(Token("PLUS",ch))
            i += 1
            continue
        
        if ch == "-":
            tokens.append(Token("MINUS",ch))
            i += 1
            continue
        
        if ch == "(":
            tokens.append(Token("LPAREN",ch))
            i += 1
            continue
        
        if ch == ")":
            tokens.append(Token("RPAREN",ch))
            i += 1
            continue
        
        raise ValueError(f"Unexpected charater: {ch}")
    
    return tokens

def main():
    text = input("Enter expression: ")
    tokens = tokenize(text)
    
    print("\n=== Token Report ===")
    print("Input:", text)
    print("Token count:",len(tokens))
    print("Tokens:")
    for token in tokens:
        print(token)
        

if __name__ == "__main__":
    main()