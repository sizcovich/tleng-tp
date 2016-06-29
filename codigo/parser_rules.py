from lexer_rules import tokens

from expressions import Addition, Multiplication, Number

#funciones a definir:
#indent
#insertOrUpdate
#table(var.value)
#table.isArray(var.value):
#table.getType(var.value)


def p_program(subexpressions):
    'program : list_sentencies'

    #{LIST SENTENCIES.level = 0, PROGRAM.value = LIST SENTENCIES.value}
    list_sentencies = subexpressions[1]

    subexpressions[0] = {"level": 0, "value": list_sentencies["value"]}
    print(list_sentencies["value"])

def p_list_sentencies(subexpressions):
    'list_sentencies : g a'
    #{G.level = LIST_SENTENCIES.level, A.level = LIST_SENTENCIES.level, LIST_SENTENCIES.value= IF(G.value=='' , '', G.value + '\n') + A.value, LIST_SENTENCIES.element = G.element,A.element = G.element}
    g = subexpressions[1]
    a = subexpressions[2]

    if (g["value"] == ""):
        list_sentencies_value = ""
    else:
        list_sentencies_value = g["value"] + "\n" + a["value"]

    subexpressions[0] = {"value": list_sentencies_value, "element": g["element"]}
    subexpressions[1] = {"level": list_sentencies["level"]}
    subexpressions[2] = {"level": list_sentencies["level"], "element": g["element"]}

def p_g_comment(subexpressions):
    'g : COMMENT'

    #{G.value = comment.value + '\n', G.element = 'comment'}
    comment = subexpressions[1]
    subexpressions[0] = {"value": comment["value"] + '\n', "element": "comment"}

def p_g_sentence(subexpressions):
    'g : sentence'

    #{G.value = indent(G.level) + SENTENCE.value, SENTENCE.level = G.level}
    g = subexpressions[0]
    sentence = subexpressions[1]

    subexpressions[0] = {"value": indent(g["level"]) + sentence["value"]}
    subexpressions[1] = {"level": g["level"]}


def p_g_newline(subexpressions):
    'g : NEWLINE'

    #{G.value = ''}
    subexpressions[0] = {"value": ""}


def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'

    #{LIST_SENTENCIES.level = A.level, A.value = IF(((LIST_SENTENCIES.element == 'sentence' || LIST_SENTENCIES.element == 'newline') && A.element == 'sentence') || A.element =='comment', '\n') + LIST_SENTENCIES.value}
    a = subexpressions[0]
    list_sentencies = subexpressions[1]

    if (((list_sentencies["element"] == 'sentence' or list_sentencies["element"] == 'newline') and a["element"] == 'sentence') or a["element"] == 'comment'):
        a_value = '\n' + list_sentencies["value"]
    else:
        a_value = list_sentencies["value"]

    subexpressions[0] = {"value": a_value}
    subexpressions[1] = {"level": a["level"]}


def p_a_lambda(subexpressions):
    'a : '

    #{A.value = '\n'}
    subexpressions[0] = {"value": "\n"}



def p_sentence_semicolon(subexpressions):
    'sentence : e SEMICOLON'

    #{E.level = SENTENCE.level, SENTENCE.value = E.value + ';'}
    sentence = subexpressions[0]
    e = subexpressions[1]

    subexpressions[0] = {"value": e["value"] + "; "}
    subexpressions[1] = {"level": sentence["level"]}


def p_sentence_while(subexpressions):
    'sentence : while'

    #{WHILE.level = SENTENCE.level, SENTENCE.value = WHILE.value}
    sentence = subexpressions[0]
    while1 = subexpressions[1]

    subexpressions[0] = {"value": while1["value"]}
    subexpressions[1] = {"level": sentence["level"]}


def p_sentence_if_else(subexpressions):
    'sentence : if_else'

    #{IF_ELSE.level = SENTENCE.level, SENTENCE.value = IF_ELSE.value}
    sentence = subexpressions[0]
    if_else = subexpressions[1]

    subexpressions[0] = {"value": if_else["value"]}
    subexpressions[1] = {"level": sentence["level"]}


def p_sentence_for(subexpressions):
    'sentence : for'

    #{FOR.level = SENTENCE.level, SENTENCE.value = FOR.value}
    sentence = subexpressions[0]
    for1 = subexpressions[1]

    subexpressions[0] = {"value": for1["value"]}
    subexpressions[1] = {"level": sentence["level"]}

def p_sentence_do_while(subexpressions):
    'sentence : do_while'

    #{DO_WHILE.level = SENTENCE.level, SENTENCE.value = DO_WHILE.value}
    sentence = subexpressions[0]
    do_while = subexpressions[1]

    subexpressions[0] = {"value": do_while["value"]}
    subexpressions[1] = {"level": sentence["level"]}

#semantica corregida
def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON'

    #{FUNCTION.level = SENTENCE.level, SENTENCE.value = FUNCTION.value + ';'}
    sentence = subexpressions[0]
    function = subexpressions[1]

    subexpressions[0] = {"value": function["value"] + ";"}
    subexpressions[1] = {"level": sentence["level"]}


def p_e_assignation(subexpressions):
    'e : assignation'

    #{E.value = ASSIGNATION.value}
    assignation = subexpressions[1]

    subexpressions[0] = {"value": assignation["value"]}


def p_e_expression(subexpressions):
    'e : expression'

    #{E.value = EXPRESSION.value}
    expression = subexpressions[1]

    subexpressions[0] = {"value": expression["value"]}


def p_e_conditional(subexpressions):
    'e : conditional'

    #{E.value = CONDITIONAL.value}
    conditional = subexpressions[1]

    subexpressions[0] = {"value": conditional["value"]}


def p_possiblecomment_comment(subexpressions):
    'possiblecomment : COMMENT'

    #{POSSIBLECOMMENT.value = comment.value}
    comment = subexpressions[1]

    subexpressions[0] = {"value": comment["value"]}


def p_possiblecomment_lambda(subexpressions):
    'possiblecomment : '

    #{POSSIBLECOMMENT.value = ''}

    subexpressions[0] = {"value": ""}


#semantica corregida
def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'

    #{COMMENT_LIST1.value = comment.value + '\n' + COMMENT_LIST2.value}
    comment = subexpressions[1]
    comment_list2 = subexpressions[2]

    subexpressions[0] = {"value": comment["value"] + "\n" + comment_list2["value"]}


def p_comment_list_newline(subexpressions):
    'comment_list : NEWLINE comment_list'

    #{COMMENT_LIST1.value = '\n' + COMMENT_LIST2}
    comment_list2 = subexpressions[1]

    subexpressions[0] = {"value":  '\n' + comment_list2["value"]}


def p_comment_list_lambda(subexpressions):
    'comment_list : '

    #{COMMENT LIST.value = ''}
    subexpressions[0] = {"value": ""}


def p_while(subexpressions):
    'while : WHILE LPAREN condition RPAREN possiblecomment keys'

    #{KEYS.level = WHILE.level + 1, WHILE.value = indent(WHILE.level) + 'while (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    while1 = subexpressions[0]
    condition = subexpressions[3]
    possiblecomment = subexpressions[5]
    keys = subexpressions[6]

    subexpressions[0] = {"value": indent(while1["level"]) + "while(" + condition["value"] + ")" + possiblecomment["value"] + "\n" + keys["value"]}
    subexpressions[6] = {"level": while1["level"] + 1}


def p_if_else(subexpressions):
    'if_else : if ELSE possiblecomment keys'

    #{KEYS.level = IF_ELSE.level + 1, IF_ELSE.value = indent(IF_ELSE.level) + IF.value + 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if_else = subexpressions[0]
    if1 = subexpressions[1]
    possiblecomment = subexpressions[3]
    keys = subexpressions[4]

    subexpressions[0] = {"value": indent(if_else["level"]) + if1["value"] + "else" + possiblecomment["value"] + "\n" + keys["value"]}
    subexpressions[6] = {"level": if_else["level"] + 1}



def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN possiblecomment keys'

    #{KEYS.level = IF.level + 1, IF.value = 'if (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if1 = subexpressions[0]
    condition = subexpressions[3]
    possiblecomment = subexpressions[5]
    keys = subexpressions[6]

    subexpressions[0] = {"value": "if(" + condition["value"] + ")" + possiblecomment["value"] + "\n" + keys["value"]}
    subexpressions[6] = {"level": if1["level"] + 1}

def p_conditional(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK expression COLON expression'

    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + EXPRESSION1.value + ':' + EXPRESSION2.value}
    condition = subexpressions[2]
    expression1 = subexpressions[5]
    expression2 = subexpressions[7]

    subexpressions[0] = {"value": "(" + condition["value"] + ")?" + expression1["value"] + ":" + expression2["value"]}


def p_for(subexpressions):
    'for : FOR LPAREN assignationorlambda SEMICOLON condition SEMICOLON advance RPAREN possiblecomment keys'

    #{KEYS.level = FOR.level + 1, FOR.value = indent(FOR.level) + 'for (' + ASSIGNATIONORLAMBDA.value + ';' + CONDITION.value + ';' + ADVANCE.value ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}

    for1 = subexpressions[0]
    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advance = subexpressions[7]
    possiblecomment = subexpressions[9]
    keys = subexpressions[10]

    subexpressions[0] = {"value": indent(for1["level"]) + "for(" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advance["value"]+ ")" + possiblecomment["value"] + "\n" + keys["value"]}
    subexpressions[10] = {"level": for1["level"] + 1}


def p_do_while(subexpressions):
    'do_while : DO RKEY possiblecomment list_sentencies LKEY WHILE LPAREN condition RPAREN SEMICOLON possiblecomment'

    #{LIST_SENTENCIES.level = DO_WHILE.level + 1, DO_WHILE.value = indent(DO_WHILE.level) + 'do' + POSSIBLECOMMENT1.value + '\n' + LIST_SENTENCIES.value + ' while(' + CONDITION.value + '); ' + POSSIBLECOMMENT2.value + '\n'}
    do_while = subexpressions[0]
    possiblecomment1 = subexpressions[3]
    list_sentencies = subexpressions[4]
    condition = subexpressions[8]
    possiblecomment2 = subexpressions[11]

    subexpressions[0] = {"value": indent(do_while["level"]) + "do(" + possiblecomment1["value"] + "\n" + list_sentencies["value"] + "while(" + condition["value"]+ ");" + possiblecomment2["value"] + "\n"}
    subexpressions[10] = {"level": do_while["level"] + 1}


def p_keys_append_sentence(subexpressions):
    'keys : comment_list sentence'

    #{COMMENT_LIST.level = KEYS.level, SENTENCE.level = KEYS.level, KEYS.value = COMMENT_LIST.value + indent(KEYS.level) + SENTENCE.value}
    keys = subexpressions[0]
    comment_list = subexpressions[1]
    sentence = subexpressions[2]

    subexpressions[0] = {"value": comment_list["value"] +  indent(keys["level"]) + sentence["value"]}
    subexpressions[1] = {"level": keys["level"]}
    subexpressions[2] = {"level": keys["level"]}


def p_keys_append_possiblecomment(subexpressions):
    'keys : RKEY possiblecomment list_sentencies LKEY'

    #{LIST_SENTENCIES.level = KEYS.level, KEYS.value = '{' + POSSIBLECOMMENT.value + '\n' + LIST_SENTENCIES.value + '} \n'}
    keys = subexpressions[0]
    possiblecomment = subexpressions[2]
    list_sentencies = subexpressions[3]

    subexpressions[0] = {"value": "{ " + possiblecomment["value"] +  "\n" + list_sentencies["value"] + "}\n"}
    subexpressions[3] = {"level": keys["level"]}




def p_assignationorlambda_assignation(subexpressions):
    'assignationorlambda : assignation'

    #{ASSIGNATIONORLAMBDA.value = ASSIGNATION.value}
    assignation = subexpressions[1]

    subexpressions[0] = {"value": assignation["value"]}




def p_assignationorlambda_lambda(subexpressions):
    'assignationorlambda : '

    #{ASSIGNATIONORLAMBDA.value = ''}
    subexpressions[0] = {"value": ""}


def p_assignation(subexpressions):
    'assignation : VAR b'

    #{ASSIGNATION.value = var.value + B.value, IF(B.isArray, COND(table(var.value) != None && table.getType(var.value) == B.type && B.isArray==table.isArray(var.value)), table.insertOrUpdate(var.value,B.type, B.isArray)}
    b = subexpressions[2]
    var = subexpressions[1]

    if not(b["isArray"] and table(var["value"])!= None and table.getType(var["values"]) == b["type"] and b["isArray"] == table.isArray(var["value"])):
        raise SemanticException("No puede agregarle a un array un elemento de tipo distinto al tipo del array")

    table.insertOrUpdate(var["value"],b["type"], b["isArray"])

    subexpressions[0] = {"value": var["value"] + b["value"]}


def p_b_array(subexpressions):
    'b : LBRACKET NATURAL RBRACKET ASSIGN expression'


    #{B.value = '[' + natural.value + '] = ' + EXPRESSION.value, B.type = IF(EXPRESSION.type == 'natural', 'decimal', EXPRESSION.type), B.isArray = true}
    natural = subexpressions[2]
    expression =  subexpressions[5]

    if expression["type"] == "natural":
    	b_type = "decimal"
    else:
    	b_type = expression["type"]

    subexpressions[0] = {"value": "[" +  natural["value"] + "] = " +  expression["value"], "type": b_type, "isArray": true}


def p_b_expression(subexpressions):
    'b : ASSIGN expression'

    #{B.value = '=' + EXPRESSION.value, B.type = EXPRESSION.type, B.isArray = false}
    expression =  subexpressions[2]

    subexpressions[0] = {"value": expression["value"] , "type": expresion["type"], "isArray": false}


#semantica corregida
def p_advance_var(subexpressions):
    'advance : VAR c'

    var = subexpressions[1]
    c = subexpressions[2]

    #{COND(table.getType(var.value) == 'natural' || table.getType(var.value)  == 'decimal'), ADVANCE.value = var.value + C.value}
    if (not(table.getType(var.value) == "natural" or table.getType(var.value) == "decimal")) :
        raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  var["value"] + c["value"]}


def p_advance_lambda(subexpressions):
    'advance : '

    #{ADVANCE.value = '' }
    subexpressions[0] = {"value": ""}


def p_c_plus(subexpressions):
    'c : PLUS d'

    #{ C.value = '+' + D.value }
    d = subexpressions[2]

    subexpressions[0] = {"value": "+" + d["value"]}

def p_c_minus(subexpressions):
    'c : MINUS f'

    #{ C.value = '-' + F.value }
    f = subexpressions[2]

    subexpressions[0] = {"value": "-" + f["value"]}


def p_d_plus(subexpressions):
    'd : PLUS'

    #{ D.value = '+' }
    subexpressions[0] = {"value": "+"}

def p_d_num(subexpressions):
    'd : EQUAL num'

    #{ D.value = '=' + NUM.value }
    num = subexpressions[2]

    subexpressions[0] = {"value": "=" + num["value"]}

def p_f_minus(subexpressions):
    'f : MINUS'

    #{ F.value = '-' }
    subexpressions[0] = {"value": "-"}

def p_f_num(subexpressions):
    'f : EQUAL num'

    #{ F.value = '=' + NUM.value}
    num = subexpressions[2]

    subexpressions[0] = {"value": "=" + num["value"]}


def p_condition_logical_condition(subexpressions):
    'condition : logical_condition'

    #{CONDITION.value = LOGICAL_CONDITION.value}
    logical_condition = subexpressions[1]

    subexpressions[0] = {"value": logical_condition["value"]}


def p_condition_boolean_condition(subexpressions):
    'condition : boolean_condition'

    #{ CONDITION.value = BOOLEAN_CONDITION.value}
    boolean_condition = subexpressions[1]

    subexpressions[0] = {"value": boolean_condition["value"]}


def p_boolean_condition(subexpressions):
    'boolean_condition : logical_condition h'

    #{BOOLEAN_CONDITION.value = LOGICAL_CONDITION + H.value}
    logical_condition = subexpressions[1]
    h = subexpressions[2]

    subexpressions[0] = {"value": logical_condition["value"] + h["value"]}


def p_h_and(subexpressions):
    'h : AND boolean_condition'

    #{ H.value = 'and' + BOOLEAN_CONDITION.value}
    boolean_condition = subexpressions[2]

    subexpressions[0] = {"value": "and" + boolean_condition["value"]}


def p_h_or(subexpressions):
    'h : OR boolean_condition'

    #{ H.value = 'or' + BOOLEAN_CONDITION.value}
    boolean_condition = subexpressions[2]

    subexpressions[0] = {"value": "or" + boolean_condition["value"]}


def p_h_lambda(subexpressions):
    'h : '

    #{H.value = ''}
    subexpressions[0] = {"value": ""}


def p_logical_condition(subexpressions):
    'logical_condition : e i'

    #{ LOGICAL_CONDITION.value = E.value + I.value}
    e = subexpressions[1]
    i = subexpressions[2]

    subexpressions[0] = {"value": e["value"] + i["value"]}

def p_logical_condition_less(subexpressions):
    'i : LESS e'

    #{ I.value = '<' + E.value }
    e = subexpressions[2]

    subexpressions[0] = {"value": " <" + e["value"]}


def p_logical_condition_greater(subexpressions):
    'i : GREATER e'

    #{ I.value = '>' + E.value }
    e = subexpressions[2]

    subexpressions[0] = {"value": " > " + e["value"]}


def p_logical_condition_equal(subexpressions):
    'i : EQUAL e'

    #{ I.value = '==' + E.value}
    e = subexpressions[2]

    subexpressions[0] = {"value": " == " +  e["value"]}


def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL e'

    #{ I.value = '!=' + E.value}
    e = subexpressions[2]

    subexpressions[0] = {"value": " != " +  e["value"]}


def p_value_string(subexpressions):
    'value : STRING'

    #{VALUE.value = string.value, VALUE.type = 'string'}
    string = subexpressions[1]

    subexpressions[0] = {"value": string["value"], "type": "string"}


def p_value_bool(subexpressions):
    'value : bool'

    #{VALUE.value = bool.value, VALUE.type = 'bool'}
    bool1 = subexpressions[1]
    if(j_isArray):
        value_type = table.getType(var_value)

    subexpressions[0] = {"value":  bool1["value"], "type": "bool"}



def p_value_num(subexpressions):
    'value : num'

    #{VALUE.value = NUM.value , VALUE.type = NUM.type}
    num = subexpressions[1]

    subexpressions[0] = {"value": num["value"], "type": num["type"]}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    #{VALUE.value = FUNCTION_WITH_RETURN.value, VALUE.type = FUNCTION_WITH_RETURN.type}
    function_with_return = subexpressions[1]

    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}


def p_value_list_values(subexpressions):
    'value : LBRACKET value list_values RBRACKET'

    #{VALUE1.value = '[ ' + VALUE2.value + LIST_VALUES.value + ']', LIST_VALUES.type = IF(VALUE2.type == 'natural','decimal',VALUE2.type), VALUE1.type = VALUE2.type}
    value2 = subexpressions[2]
    list_values = subexpressions[3]

    if value_type == "natural":
    	value1_type = "decimal"
    else:
    	value1_type = value2["type"]

    subexpressions[0] = {"value": "[" + value2["value"] + list_values["value"] + "]", "type": value1_type}


#semantica corregida
def p_value_list_registers(subexpressions):
    'value : LKEY list_registers RKEY'
    #{VALUE.value = '{' + LIST_REGISTERS.value + '}', VALUE.type = 'register'}
    list_registers = subexpressions[1]

    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": "register"}


def p_value_var(subexpressions):
    'value : VAR j'

    #{VALUE.value = var.value + J.value, VALUE.type = IF(J.isArray, table.getType(var.value), var.type)}
    j = subexpressions[2]
    var = subexpressions[1]

    value_type = var["type"]

    if(j["isArray"]):
        value_type = table.geType(var["value"])

    subexpressions[0] = {"value": var["value"] + j["value"], "type": value_type}


def p_j_array(subexpressions):
    'j : LBRACKET num RBRACKET'

    #{J.value = '[' + NUM.value + ']', J.isArray = true }
    num = subexpressions[1]

    subexpressions[0] = {"value": "[" + num["value"] + "]", "isArray": true}


def p_j_lambda(subexpressions):
    'j : '

    #{J.value = '', J.isArray = false}
    subexpressions[0] = {"value": "", "isArray": false}


def p_list_registers(subexpressions):
    'list_registers : assignation l'

    #{LIST_REGISTERS.value = ASSIGNATION.value + L.value}
    assignation = subexpressions[1]
    l = subexpressions[2]

    subexpressions[0] = {"value": assignation["value"] + l["value"]}


def p_l_list_registers(subexpressions):
    'l : COMA list_registers'

    #{L.value = ',' + LIST REGISTERS.value}
    list_registers = subexpressions[1]

    subexpressions[0] = {"value": ", " + list_registers["value"]}




def p_l_lambda(subexpressions):
    'l : '
    subexpressions[0] = {"value": ""}

def p_list_values_comma(subexpressions):
    'list_values : COMMA value list_values'
    subexpressions[0] = subexpressions[1]

def p_list_values_lambda(subexpressions):
    'list_values : '
    subexpressions[0] = ""

def p_expression_arithmetic(subexpressions):
    'expression : arithmetic_expression'
    subexpressions[0] = subexpressions[1]

def p_expression_exp_string(subexpressions):
    'expression : expression_string'
    subexpressions[0] = subexpressions[1]

def p_expression_value(subexpressions):
    'expression : value'
    subexpressions[0] = subexpressions[1]

def p_expression_string_exp_string(subexpressions):
    'expression_string : expression_string PLUS STRING'
    subexpressions[0] = subexpressions[1]

def p_arithmetic_expression_plus(subexpressions):
    'arithmetic_expression : arithmetic_expression PLUS term'
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

def p_factor_number(subexpressions):
    'factor : num'
    subexpressions[0] = Number(subexpressions[1])

def p_factor_vector(subexpressions):
    'factor : VAR LBRACKET NATURAL RBRACKET'
    subexpressions[0] = Number(subexpressions[1])

def p_func_func_wr(subexpressions):
    'function : function_with_return'
    subexpressions[0] = subexpressions[1]

def p_func_print(subexpressions):
    'function : PRINT LPAREN expression RPAREN'
    subexpressions[0] = subexpressions[1]

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'
    subexpressions[0] = subexpressions[1]


def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN STRING RPAREN'
    texto = subexpressions[3]
    subexpressions[0]["Value"] = "capitalizar( " + texto["Value"] + " )"
    subexpressions[0]["Type"] = "string"
    #faltan cosas

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN VAR COMMA VAR  RPAREN'
    var1 = subexpressions[3]
    var2 = subexpressions[5]
    subexpressions[0]["Value"] = "colineales( " + var1["Value"] + ", " + var2["Value"] + " )"
    #faltan cosas

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN param_length  RPAREN'
     fwr  = subexpressions[0]
     pl = subexpressions[1]
     fwr["Value"] = "length( " + pl["Value"] + " )"
     fwr["Type"] = "natural"
     subexpressions[0] = fwr
     #faltan cosas

def p_param_me_var(subexpressions):
    'param_me : VAR COMMA num n'
    param_me = subexpressions[0]
    var = subexpressions[1]
    comma = subexpressions[2]
    num = subexpressions[3]
    n = subexpressions[4]
    param_me["Value"] = var["Value"] + "," + num["Value"] + n["Value"]
    table_var_type = table.getType(var["Value"])
    assert( table_var_type == "natural" or table_var_type == "decimal" )
    assert( table.isArray(var["Value"]))
    if table_var_type == "decimal" and n["isTrue"] :
        param_me["Type"] = "decimal"
    else:
        param_me["Type"] = table_var_type
    subexpressions[0] = param_me



def p_n_bool(subexpressions):
    'n : COMMA bool'
    n = subexpressions[0]
    booleano = subexpressions[2]
    n["Value"] = ", " + booleano["Value"]
    n["isTrue"] = booleano["Value"] == "true"
    subexpressions[0] = n

def p_n_lambda(subexpressions):
    'n : '
    subexpressions[0] = {"Value": "", "isTrue": false}

def p_param_l_var(subexpressions):
    'param_length : VAR '
    var = subexpressions[1]
    assert( table.isArray(var["Value"]) or table.getType(var["Value"]) )
    subexpressions[0] = {"Value": var["Value"]}

def p_param_l_vector(subexpressions):
    'param_length : LBRACKET value list_values RBRACKET '
    val = subexpressions[2]
    list_val = subexpressions[3]
    res =  subexpressions[0]
    res["Value"] = "["+ val["Value"] + list_val["Value"] + "]"
    if val["Type"] == "natural":
        res["Type"] = "decimal"
    else:
        res["Type"] = val["Type"]
    subexpressions[0] = res

#esta mas arriba?
def p_param_l_string(subexpressions):
    'param_length : STRING '
    subexpressions[0] = subexpressions[1]


def p_num_decimal(subexpressions):
    'num : DECIMAL '
    dec = subexpressions[1]
    subexpressions[0] = {"value": dec["Value"], "Type": "decimal"}

def p_num_natural(subexpressions):
    'num : NATURAL '
    nat = subexpressions[1]
    subexpressions[0] = {"value": nat["Value"], "Type": "natural"}

def p_bool_true(subexpressions):
    'bool : TRUE '
    subexpressions[0] = {"value": "true"}

def p_bool_false(subexpressions):
    'bool : FALSE '
    subexpressions[0] = {"value": "false"}

def p_error(subexpressions):
    raise Exception("Syntax error.")
