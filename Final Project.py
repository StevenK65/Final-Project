###ERRORS


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.error_name = error_name
        self.details = details
        self.pos_start = pos_start
        self.pos_end = pos_end

    def as_string(self):
        result = f'{self.error_name} : {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character Entered', details)


###POSITION
        

#ln and col track line and column of course; index tracks character total
#note that in the future, ln should = #formula+#axioms+conclusion
class Position:
    def __init__(self, idx, ln, col):     
        self.idx = idx
        self.ln = ln
        self.col = col

    def advancePos(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col)


###TOKENS
    

TT_VAR    = 'VAR'
TT_AND    = 'AND'
TT_OR     = 'OR'
TT_COND   = 'COND'
TT_EQUIV  = 'EQUIV'
TT_NEG    = 'NEG'

VARIABLES = 'abcdefghijklmnopqrstuvwxyz'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


###LEXER


#go through input character by character; breaks list into tokens
#token has a type, optionally a value

class Lexer:
    def __init__(self, text):             #text is what we're processing
        self.text = text
        self.pos = Position(-1, 0, -1)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advancePos(self.current_char)
        if self.pos.idx < len(self.text):
            self.current_char = self.text[self.pos.idx]
        else:
            self.current_char = None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in VARIABLES:
                tokens.append(Token(TT_VAR))
                self.advance()
            elif self.current_char == 'K':
                tokens.append(Token(TT_AND))
                self.advance()
            elif self.current_char == 'A':
                tokens.append(Token(TT_OR))
                self.advance()
            elif self.current_char == 'C':
                tokens.append(Token(TT_COND))
                self.advance()
            elif self.current_char == 'E':
                tokens.append(Token(TT_EQUIV))
                self.advance()
            elif self.current_char == 'N':
                tokens.append(Token(TT_NEG))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'"+char+"'")
        return tokens, None


###NODES


class VarNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'

#for and, or, conditionals, equivalence
class BinOpNode:
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_token}, {self.right_node})'

#for negation
class UnOpNode:
    def __init(self, op_token, right_node):
        self.op_token = op_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.op_token}, {self.right_node})'


###PARSER


"""
class Parser:
    def 
"""


###RUN


def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error

text = input('input line:')
result, error = run(text)

if error:
    print(error.as_string())
else:
    print(result)
