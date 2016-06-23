import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NATURAL',
   'DECIMAL',
   'MODULE',
   'LESS',
   'GREATER',
   'AND',
   'OR',
   'NOT',
   'PLUSEQUAL',
   'DIVEQUAL',
   'MULEQUAL',
   'MINEQUAL',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'ASSIGN',
   'QUOTMARK',
   'SEMICOLON',
   'UNEQUAL',
   'EQUAL',
   'DECREMENT',
   'INCREMENT',
   'HASH',
   'RKEY',
   'LKEY',
   'RPAREN',
   'IF',
   'ELSE',
   'WHILE',
   'FOR',
   'DO',
   'LENGTH',
   'PRINT',
   'MULTIPLICACIONESCALAR',
   'CAPITALIZAR',
   'COLINEALES',
   'QUESTIONMARK',
   'TRUE',
   'FALSE',
   'BEGIN',
   'END',
   'RETURN',
   'RES',
   'DOT',
   'COMMA',
   'LBRACKET',
   'RBRACKET',
   'POW',
   'COLON',
   'VAR',
   'COMMENT',
   'STRING',
   'COMA'
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MODULE = r'%'
t_DOT = r'\.'
t_LESS = r'<'
t_GREATER = r'>'
#t_AND = r'AND'
#t_OR = r'OR'
#t_NOT = r'NOT'
t_PLUSEQUAL = r'\+='
t_DIVEQUAL = r'/='
t_MULEQUAL = r'\*='
t_MINEQUAL = r'-='
t_ASSIGN = r'='
t_QUOTMARK = r'"'
t_SEMICOLON = r';'
t_UNEQUAL = r'!='
t_EQUAL = r'=='
t_DECREMENT = r'--'
#t_INCREMENT = r'\++'
t_HASH = r'\#'
t_RKEY = r'\}'
t_LKEY = r'\{'
#t_IF = r'if'
#t_ELSE = r'else'
#t_WHILE = r'while'
#t_FOR = r'for'
#t_DO = r'do'
#t_LENGTH = r'length'
#t_PRINT = r'print'
#t_MULTIPLICACIONESCALAR = r'multiplicacionEscalar'
#t_CAPITALIZAR = r'capitalizar'
#t_COLINEALES = r'colineales'
t_QUESTIONMARK = r'\?'
#t_TRUE = r'true'
#t_FALSE = r'false'
#t_BEGIN = r'begin'
#t_END = r'end'
#t_RETURN = r'return'
#t_RES = r'res'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_POW = r'\^'
t_COLON = r':'
t_COMA = r','


#regular expression rules with some action code
#Reserved symbols:

def t_INCREMENT(t):
    r'\+\+'
    return t

def t_ELSE(t):
	r'else'
	return t

def t_IF(t):
	r'if'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_BEGIN(t):
	r'begin'
	return t

def t_END(t):
	r'end'
	return t

def t_FOR(t):
	r'for'
	return t

def t_DO(t):
	r'do'
	return t

def t_RES(t):
	r'res'
	return t

def t_RETURN(t):
	r'return'
	return t

def t_TRUE(t):
	r'true'
	return t

def t_FALSE(t):
	r'false'
	return t

def t_AND(t):
	r'and'
	return t

def t_OR(t):
	r'or'
	return t

def t_NOT(t):
	r'not'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_MULTIPLICACIONESCALAR(t):
	r'multiplicacionEscalar'
	return t

def t_CAPITALIZAR(t):
	r'capitalizar'
	return t

def t_COLINEALES(t):
	r'colineales'
	return t

def t_LENGTH(t):
	r'length'
	return t

#end Reserved symbols

def t_NATURAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z]{1}[a-zA-Z0-9_]*'
    t.value = t.value
    return t

def t_STRING(t):
    r'".*"'
    t.value = t.value
    return t

def t_COMMENT(t):
    r'\#(.|\n)*?\n'
    t.value = t.value
    return t

# Define a rule so we can track line numbers
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(token):
    message = "Token desconocido:"
    message += "\ntype:" + token.type
    message += "\nvalue:" + str(token.value)
    message += "\nline:" + str(token.lineno)
    message += "\nposition:" + str(token.lexpos)
    raise Exception(message)

# Build the lexer
lexer = lex.lex()
