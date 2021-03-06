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
	'SEMICOLON',
	'UNEQUAL',
	'EQUAL',
	'DECREMENT',
	'INCREMENT',
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
	'RETURN',
	'COMMA',
	'LBRACKET',
	'RBRACKET',
	'POW',
	'COLON',
	'VAR',
	'COMMENT',
	'STRING',
	'NEGATIVO',
	'NEWLINE'
)

#Reserved words
reserved = {
    'RES' : 'RES',
    'res' : 'res',
    'begin' : 'begin',
    'BEGIN' : 'BEGIN',
    'end' : 'end',
    'END' : 'END',
    'while' : 'while',
    'for' : 'for',
    'multiplicacionEscalar' : 'multiplicacionEscalar',
    'length' : 'length',
    'and' : 'and',
    'return' : 'return',
    'capitalizar' : 'capitalizar',
    'colineales' : 'colineales',
    'print' : 'print',
    'or' : 'or',
    'false' : 'false',
    'true' : 'true',
    'do' : 'do',
    'not' : 'not',
    'if' : 'if',
    'else' : 'else'
}

# Regular expression rules for simple tokens
def t_INCREMENT(t):
	r'\+\+'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_DECREMENT(t):
 	r'--'
 	t.value = { "line": t.lineno, "value": t.value }
 	return t

def t_PLUSEQUAL(t):
 r'\+='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_DIVEQUAL(t):
 r'/='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_MULEQUAL(t):
 r'\*='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_MINEQUAL(t):
 r'-='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_DECIMAL(t):
	r'\d+\.\d+|-\d+\.\d+'
	t.value = { "line": t.lineno, "value": float(t.value), "type": "decimal"  }
	return t

def t_NEGATIVO(t):
 	r'-\d+'
 	t.value = { "line": t.lineno, "value": int(t.value), "type": "negativo"  }
 	return t


def t_NATURAL(t):
	r'\d+'
	t.value = { "line": t.lineno, "value": int(t.value), "type": "natural" }
	return t

def t_MINUS(t):
 r'-'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_TIMES(t):
 r'\*'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_DIVIDE(t):
 r'/'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_LPAREN(t):
 r'\('
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_RPAREN(t):
 r'\)'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_MODULE(t):
 r'%'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_PLUS(t):
	r'\+'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_LESS(t):
 r'<'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_GREATER(t):
 r'>'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_EQUAL(t):
 r'=='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_ASSIGN(t):
 r'='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_SEMICOLON(t):
 r';'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_UNEQUAL(t):
 r'!='
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_RKEY(t):
 r'\}'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_LKEY(t):
 r'\{'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_QUESTIONMARK(t):
 r'\?'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_LBRACKET(t):
 r'\['
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_RBRACKET(t):
 r'\]'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_POW(t):
 r'\^'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_COLON(t):
 r':'
 t.value = { "line": t.lineno, "value": t.value }
 return t

def t_COMMA(t):
 r','
 t.value = { "line": t.lineno, "value": t.value }
 return t

#regular expression rules with some action code
#Reserved symbols:
# Define a rule so we can track line numbers

def t_ELSE(t):
	r'else|ELSE'
	t.value = { "line": t.lineno, "value": t }
	return t

def t_IF(t):
	r'if|IF'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_WHILE(t):
	r'while|WHILE'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_FOR(t):
	r'for|FOR'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_RETURN(t):
	r'return\s|RETURN\s'
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
	r'and\s|AND\s'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_OR(t):
	r'or\s|OR\s'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_NOT(t):
	r'not\s|NOT\s'
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

def t_DO(t):
	r'do\s|DO\s'
	t.value = { "line": t.lineno, "value": t.value }
	return t

#end Reserved symbols
def t_VAR(t):
	r'[a-zA-Z]{1}[a-zA-Z0-9_]*((\.[a-zA-Z]{1})?[a-zA-Z0-9_])*'
	if t.value.lower() in reserved:
		msg = "Token reservado: " + t.value
		raise Exception (msg)
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_STRING(t):
	r'\"([^\"]+)\"'
	if t.value.lower() in reserved:
		msg = "Token reservado: " + t.value
		raise Exception (msg)
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_COMMENT(t):
	r'\#.*'
	t.value = { "line": t.lineno, "value": t.value }
	return t

def t_NEWLINE(token):
  r"\n+"
  token.lexer.lineno += len(token.value)
  return ''

# A string containing ignored characters (spaces, tabs and newlines)


t_ignore = '\t '

# Error handling rule
def t_error(token):
	print("TOKEN")
	print(token)
	message = "Token desconocido:"
	message += "\ntype:" + token.type
	message += "\nvalue:" + str(token.value)
	message += "\nline:" + str(token.lineno)
	message += "\nposition:" + str(token.lexpos)
	raise Exception(message)

# Build the lexer
lexer = lex.lex()
