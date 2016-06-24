from lexer_rules import tokens

from expressions import Addition, Multiplication, Number


def p_program(subexpressions):
    'program : statements_list'
    subexpressions[0] = subexpressions[1]

def p_statements_list_statement(subexpressions):
    'statements_list : statement'
    subexpressions[0] = subexpressions[1]

def p_statements_list_append(subexpressions):
    'statements_list : statements_list statement'
    subexpressions[0] = subexpressions[1]

def p_statement_e_semicolon(subexpressions):
    'statement : e SEMICOLON'
    subexpressions[0] = subexpressions[1]

def p_statement_while(subexpressions):
    'statement : while'
    subexpressions[0] = subexpressions[1]

def p_statement_if_else(subexpressions):
    'statement : if_else'
    subexpressions[0] = subexpressions[1]

def p_statement_conditional(subexpressions):
    'statement : conditional'
    subexpressions[0] = subexpressions[1]

def p_statement_for(subexpressions):
    'statement : for'
    subexpressions[0] = subexpressions[1]

def p_statement_do_while(subexpressions):
    'statement : do_while'
    subexpressions[0] = subexpressions[1]

def p_statement_comentario(subexpressions):
    'statement : comment'
    subexpressions[0] = subexpressions[1]

def p_while_statement(subexpressions):
    'while : WHILE LPAREN condition RPAREN statement'
    subexpressions[0] = subexpressions[1]

def p_while_statements_list(subexpressions):
    'while : WHILE LPAREN condition RPAREN RKEY statements_list LKEY'
    subexpressions[0] = subexpressions[1]

def p_if_else_statement(subexpressions):
    'if_else : if ELSE statement'
    subexpressions[0] = subexpressions[1]

def p_if_else_statements_list(subexpressions):
    'if_else : if ELSE RKEY statements_list LKEY'
    subexpressions[0] = subexpressions[1]

def p_if_statement(subexpressions):
    'if : IF LPAREN condition RPAREN statement'
    subexpressions[0] = subexpressions[1]

def p_if_statements_list(subexpressions):
    'if : IF LPAREN condition RPAREN RKEY statements_list LKEY'
    subexpressions[0] = subexpressions[1]

def p_conditional(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK statement COLON statement'
    subexpressions[0] = subexpressions[1]

def p_for_statement(subexpressions):
    'for : FOR LPAREN assignment SEMICOLON condition SEMICOLON advance RPAREN statemen'
    subexpressions[0] = subexpressions[1]

def p_for_statements_list(subexpressions):
    'for : FOR LPAREN assignment SEMICOLON condition SEMICOLON advance RPAREN RKEY statements_list LKEY'
    subexpressions[0] = subexpressions[1]

def p_assignment_var(subexpressions):
    'assignment : var ASSIGN expression'
    subexpressions[0] = subexpressions[1]

def p_assignment_vector(subexpressions):
    'assignment : var LBRACKET INDEX RBRACKET ASSIGN expression'
    subexpressions[0] = subexpressions[1]

def p_assignment_record(subexpressions):
    'assignment : var DOT CADENA ASSIGN expression'
    subexpressions[0] = subexpressions[1]

def p_assignment_empty(subexpressions):
    'assignment : '
    #subexpressions[0] = subexpressions[1]

def p_advance_increment(subexpressions):
    'advance : var INCREMENT'
    subexpressions[0] = subexpressions[1]

def p_advance_decrement(subexpressions):
    'advance : var DECREMENT'
    subexpressions[0] = subexpressions[1]

def p_advance_minequal(subexpressions):
    'advance : var MINEQUAL num'
    subexpressions[0] = subexpressions[1]

def p_advance_plusequal(subexpressions):
    'advance : var PLUSEQUAL num'
    subexpressions[0] = subexpressions[1]

def p_advance_empty(subexpressions):
    'advance : ' 
    #subexpressions[0] = subexpressions[1]

def p_do_while_statements_list(subexpressions):
    'do_while : DO RKEY statements_list LKEY WHILE LPAREN condition RPAREN'
    subexpressions[0] = subexpressions[1]

def p_condition_logical_condition(subexpressions):
    'condition : logical_condition'
    subexpressions[0] = subexpressions[1]

def p_condition_and_condition(subexpressions):
    'condition : and_condition'
    subexpressions[0] = subexpressions[1]

def p_condition_or_condition(subexpressions):
    'condition : or_condition'
    subexpressions[0] = subexpressions[1]

def p_logical_condition_less(subexpressions):
    'logical_condition : e1 LESS e2'
    subexpressions[0] = subexpressions[1]

def p_logical_condition_greater(subexpressions):
    'logical_condition : e1 GREATER e2'
    subexpressions[0] = subexpressions[1]

def p_logical_condition_equal(subexpressions):
    'logical_condition : e1 EQUAL e2'
    subexpressions[0] = subexpressions[1]

def p_logical_condition_unequal(subexpressions):
    'logical_condition : e1 UNEQUAL e2'
    subexpressions[0] = subexpressions[1]

def p_and_condition(subexpressions):
    'and_condition : logical_condition AND logical_condition'
    subexpressions[0] = subexpressions[1]

def p_or_condition(subexpressions):
    'or_condition : logical_condition OR logical_condition'
    subexpressions[0] = subexpressions[1]

def p_e_assignment(subexpressions):
    'e : assignment'
    subexpressions[0] = subexpressions[1]

def p_e_expression(subexpressions):
    'e : expression'
    subexpressions[0] = subexpressions[1]

def p_value_string(subexpressions):
    'value : STRING'
    subexpressions[0] = subexpressions[1]

def p_value_bool(subexpressions):
    'value : BOOL'
    subexpressions[0] = subexpressions[1]

def p_value_var(subexpressions):
    'value : VAR'
    subexpressions[0] = subexpressions[1]

def p_value_num(subexpressions):
    'value : NUM'
    subexpressions[0] = subexpressions[1]

def p_value_function(subexpressions):
    'value : function'
    subexpressions[0] = subexpressions[1]

def p_value_vector(subexpressions):
    'value : var LBRACKET indice RBRACKET'
    subexpressions[0] = subexpressions[1]

def p_value_registro(subexpressions):
    'value : var DOT cadena'
    subexpressions[0] = subexpressions[1]

def p_value_list_vector(subexpressions):
    'value : LBRACKET list_values RBRACKET'
    subexpressions[0] = subexpressions[1]

def p_value_list_records(subexpressions):
    'value : RKEY list_records LKEY'
    subexpressions[0] = subexpressions[1]

def p_list_records_record(subexpressions):
    'list_records : record'
    subexpressions[0] = subexpressions[1]

def p_list_records_record(subexpressions):
    'list_records : record'
    subexpressions[0] = subexpressions[1]

def p_list_records_append(subexpressions):
    'list_records : list_records COMA record'
    subexpressions[0] = subexpressions[1]

def p_recor(subexpressions):
    'record : CADENA DOT value'
    subexpressions[0] = subexpressions[1]

def p_list_values_value(subexpressions):
    'list_values : value'
    subexpressions[0] = subexpressions[1]

def p_list_values_append(subexpressions):
    'list_values : list_values COMA value'
    subexpressions[0] = subexpressions[1]


def p_expression_arithmetic(subexpressions):
    'expression : expression_arithmetic'
    subexpressions[0] = subexpressions[1]

def p_expression_value(subexpressions):
    'expression : value'
    subexpressions[0] = subexpressions[1]


def p_arithmetic_expression_plus(subexpressions):
    'arithmetic_expression : arithmetic_expression PLUS termino'
    subexpressions[0] = Addition(subexpressions[1], subexpressions[3])


def p_arithmetic_expression_minus(subexpressions):
    'arithmetic_expression : arithmetic_expression MINUS term'
    subexpressions[0] = Subtract(subexpressions[1], subexpressions[3])



def p_arithmetic_expression_term(subexpressions):
    'arithmetic_expression : term'
    subexpressions[0] = subexpressions[1]


def p_term_times(subexpressions):
    'term : term TIMES factor'
    subexpressions[0] = Multiplication(subexpressions[1], subexpressions[3])


def p_term_divide(subexpressions):
    'term : term DIVIDE factor'
    subexpressions[0] = Division(subexpressions[1], subexpressions[3])

def p_term_module(subexpressions):
    'term : term MODULE factor'
    subexpressions[0] = Module(subexpressions[1], subexpressions[3])

def p_term_factor(subexpressions):
    'term : factor'
    subexpressions[0] = subexpressions[1]

#OJO CON ESTO PORQUE NOSOTROS TENEMOS DIVIDIDO ENTRE NATURALES Y DECIMALES
def p_factor_number(subexpressions):
    'factor : NUMBER'
    subexpressions[0] = Number(subexpressions[1])

#ACA CUAL ES EL VALOR DE var[INDICE]? de donde sale?
def p_factor_vector(subexpressions):
    'factor : var[NATURAL]'
    subexpressions[0] = Number(subexpressions[1])

#ACA CUAL ES EL VALOR DE var.cadena? de donde sale?
def p_factor_registro(subexpressions):
    'factor : var.cadena'
    subexpressions[0] = Number(subexpressions[1])

#def p_factor_expression(subexpressions):
#    'factor : LPAREN expression RPAREN
#    subexpressions[0] = subexpressions[2]


def p_error(subexpressions):
    raise Exception("Syntax error.")
