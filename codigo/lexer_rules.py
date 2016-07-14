import lex

# List of token names.
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
	#'RES',
	'DOT',
	'COMMA',
	'LBRACKET',
	'RBRACKET',
	'POW',
	'COLON',
	'VAR',
	'COMMENT',
	'STRING'
)

# Regular expression rules for simple tokens
t_PLUS	= r'\+'
t_MINUS	= r'-'
t_TIMES	= r'\*'
t_DIVIDE	= r'/'
t_LPAREN	= r'\('
t_RPAREN	= r'\)'
t_MODULE = r'%'
t_DOT = r'\.'
t_LESS = r'<'
t_GREATER = r'>'
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
t_HASH = r'\#'
t_RKEY = r'\}'
t_LKEY = r'\{'
t_QUESTIONMARK = r'\?'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_POW = r'\^'
t_COLON = r':'
t_COMMA = r','

#regular expression rules with some action code
#Reserved symbols:
# Define a rule so we can track line numbers

def t_INCREMENT(t):
	r'\+\+'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_ELSE(t):
	r'else|ELSE'
	t.value = { "line": t.lineno, "value": t }

def t_IF(t):
	r'if|IF'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_WHILE(t):
	r'while|WHILE'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_BEGIN(t):
	r'begin|BEGIN'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_END(t):
	r'end|END'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_FOR(t):
	r'for|FOR'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_DO(t):
	r'do|DO'
	t.value = { "line": t.lineno, "value": t.value }
	return t

#def t_RES(t):
#	r'res'
#	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_RETURN(t):
	r'return|RETURN'
	t.value = { "line": t.lineno, "value": t.value }
	return t
	


def t_TRUE(t):
	r'true|TRUE'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_FALSE(t):
	r'false|FALSE'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_AND(t):
	r'and|AND'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_OR(t):
	r'or|OR'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_NOT(t):
	r'not|NOT'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_PRINT(t):
	r'print|PRINT'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_MULTIPLICACIONESCALAR(t):
	r'multiplicacionEscalar|MULTIPLICACIONESCALAR'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_CAPITALIZAR(t):
	r'capitalizar|CAPITALIZAR'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_COLINEALES(t):
	r'colineales|COLINEALES'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_LENGTH(t):
	r'length|LENGTH'
	t.value = { "line": t.lineno, "value": t.value }
	return t

#end Reserved symbols
def t_VAR(t):
	r'[a-zA-Z]{1}[a-zA-Z0-9_]*((\.[a-zA-Z]{1})?[a-zA-Z0-9_])*'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_DECIMAL(t):
	r'\d+\.\d+'
	t.value = { "line": t.lineno, "value": float(t.value) }
	return t

def t_NATURAL(t):
	r'\d+'
	t.value = { "line": t.lineno, "value": int(t.value) }
	return t


def t_STRING(t):
	r'\"([^\"]+)\"'
	t.value = { "line": t.lineno, "value": t.value }
	return t


def t_COMMENT(t):
	r'\#.*'
	t.value = { "line": t.lineno, "value": t.value }
	return t

# A string containing ignored characters (spaces and tabs)
t_ignore	= '\t \n'

# Error handling rule
def t_error(token):
	message = "Token desconocido:"
	message += "\ntype:" + token["value"].type
	message += "\nvalue:" + str(token["value"].value)
	message += "\nline:" + str(token["value"].lineno)
	message += "\nposition:" + str(token["value"].lexpos)
	raise Exception(message)

# Build the lexer
lexer = lex.lex()
