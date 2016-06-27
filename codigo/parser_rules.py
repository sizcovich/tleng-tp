from lexer_rules import tokens

from expressions import Addition, Multiplication, Number


#escribir la funcion indent

def p_program(subexpressions):
    'program : list_sentencies'

    #{LIST SENTENCIES.level = 0, PROGRAM.value = LIST SENTENCIES.value, print(PROGRAM.value)}
    list_sentencies = subexpressions[1]
    value = list_sentencies["value"]
    subexpressions[0] = {"level": 0, "value": value, print(value)}

def p_list_sentencies(subexpressions):
    'list_sentencies : g a'

     #{G.level = LIST SENTENCIES.level, A.level = LIST SENTENCIES.level, LIST SENTENCIES.value = IF(G.value==”, ”, G.value + ’\n’) + A.value}
     g_value = subexpressions[1]["value"]
     a_value = subexpressions[2]["value"]
     list_sentencies_level = subexpressions[0]["level"]

     if (g_value == ""):
         list_sentencies_value = ""
     else:
         list_sentencies_value = g_value + "\n" + a_value

     subexpressions[0] = {"value": list_sentencies_value}
     subexpressions[1] = {"level": list_sentencies_level}
     subexpressions[2] = {"level": list_sentencies_level}

def p_g_comment(subexpressions):
    'g : COMMENT'

    #{G.value = comment.value}
    subexpressions[0] = subexpressions[1]

def p_g_sentence(subexpressions):
    'g : sentence'

    #{G.value = indent(G.level) + SENTENCE.value, SENTENCE.level = G.level}
    g_level = subexpressions[0]["level"]
    sentence_value = subexpressions[1]["value"]
    g_value = indent(g_level) + sentence_value

    subexpressions[0] = {"value": g_value}
    subexpressions[1] = {"level": g_level}


def p_g_newline(subexpressions):
    'g : newline'

    #{G.value = ’ ’}
    subexpressions[0] = {"value": ""}


def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'
    a_level = subexpressions[0]["level"]
    list_sentencies_value = subexpressions[1]["value"]

    #{LIST SENTENCIES.level = A.level, A.value = LIST SENTENCIES.value}
    subexpressions[0] = {"value": list_sentencies_value}
    subexpressions[1] = {"level": a_level}

#se representa como vacio el lamnda?
def p_g_lambda(subexpressions):
    'g : '

    #{A.value = ’ ’}
    subexpressions[0] = {"value": ""}



def p_sentence_semicolon(subexpressions):
    'sentence : e SEMICOLON possiblecomment'

    #{E.level = SENTENCE.level, SENTENCE.value = E.value + ’;’ + POSSIBLECOMMENT.value}
    sentence_level = subexpressions[0]["level"]

    e_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    sentence_value = e_value + "; " + possiblecomment_value

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_while(subexpressions):
    'sentence : while'

    #{WHILE.level = SENTENCE.level, SENTENCE.value = WHILE.value}
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_if_else(subexpressions):
    'sentence : if_else'

    #{IF ELSE.level = SENTENCE.level, SENTENCE.value = IF ELSE.value}
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_for(subexpressions):
    'sentence : for'

    #{FOR.level = SENTENCE.level, SENTENCE.value = FOR.value}
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}

def p_sentence_do_while(subexpressions):
    'sentence : do_while'

    #{DO WHILE .level = SENTENCE.level, SENTENCE.value = DO WHILE .value}
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}

def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON possiblecomment'

    #{FUNCTION.level = SENTENCE.level, SENTENCE.value = FUNCTION.value + ’;’ + POSSIBLECOMMENT.value}
    sentence_level = subexpressions[0]["level"]

    function_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    sentence_value = function_value + "; " + possiblecomment_value

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_e_assignation(subexpressions):
    'e : assignation'

    #{E.value = ASSIGNATION.value}
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_e_expression(subexpressions):
    'e : expression'

    #{E.value = EXPRESSION.value, E.type = EXPRESSION.type}
    subexpressions[0] = {"value": subexpressions[1]["value"], "type": subexpressions[1]["type"]}


def p_e_conditional(subexpressions):
    'e : conditional'

    #{E.value = CONDITIONAL.value, E.type = CONDITIONAL.type}
    subexpressions[0] = {"value": subexpressions[1]["value"], "type": subexpressions[1]["type"]}


def p_possiblecomment_comment(subexpressions):
    'possiblecomment : comment'

    #{POSSIBLECOMMENT.value = comment.value}
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_possiblecomment_lambda(subexpressions):
    'possiblecomment : '

    #{POSSIBLECOMMENT.value = ’ ’}
    subexpressions[0] = {"value": ""}


def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'

    #{COMMENT_LIST1.value = comment.value + ’\n’ + COMMENT_LIST2 }
    comment_value = subexpressions[1]["value"]
    comment_list2_value = subexpressions[2]["value"]
    comment_list1_value =  comment_value + "\n" + comment_list2_value

    subexpressions[0] = {"value": comment_list1_value}

def p_comment_list_newline(subexpressions):
    'comment_list : NEWLINE comment_list'

    #{COMMENT_LIST1.value = COMMENT_LIST2 }
    subexpressions[0] = {"value": subexpressions[1]["value"]}

def p_comment_list_lambda(subexpressions):
    'comment_list : '

    #{COMMENT_LIST.value = ''}
    subexpressions[0] = {"value": ""}

def p_while(subexpressions):
    'while : WHILE LPAREN condition RPAREN possiblecomment keys'

    #{KEYS.level = WHILE.level + 1, WHILE.value = indent(WHILE.level) + ’while (’ + CONDITION.value + ’) ’ + POSSIBLECOMMENT.value + ’\n’ + KEYS.value}
    while_level = subexpressions[0]["level"]

    condition_value = subexpressions[3]["value"]
    possiblecomment_value = subexpressions[5]["value"]
    keys_value = subexpressions[6]["value"]
    while_value = indent(while_level) + "while(" + condition_value + ")" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": while_value}
    subexpressions[6] = {"level": while_level + 1}


def p_if_else(subexpressions):
    'if_else : if ELSE possiblecomment keys'

    #{KEYS.level = IF ELSE.level + 1, IF ELSE.value = indent(IF ELSE.level) + IF.value + ’else’ + POSSIBLECOMMENT.value + ’\n’ + KEYS.value}
    if_else_level = subexpressions[0]["level"]

    if_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    keys_value = subexpressions[4]["value"]

    if_else_value = indent(if_else_level) + if_value + "else" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": if_else_value}
    subexpressions[6] = {"level": if_else_level + 1}



def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN possiblecomment keys'

    #{KEYS.level = IF.level + 1, IF.value = ’if (’ + CONDITION.value + ’) ’ + POSSIBLECOMMENT.value + ’\n’ + KEYS.value}
    if_level = subexpressions[0]["level"]

    condition_value = subexpressions[3]["value"]
    possiblecomment_value = subexpressions[5]["value"]
    keys_value = subexpressions[6]["value"]

    if_value = "if(" + condition_value + ")" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": if_value}
    subexpressions[6] = {"level": if_level + 1}

def p_conditional(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK expression COLON expression'

    #{CONDITIONAL.value = ’(’ + CONDITION.value + ’)?’ + EXPRESSION1 .value + ’:’ +EXPRESSION2 .value}
    condition_value = subexpressions[2]["value"]
    expression1_value = subexpressions[5]["value"]
    expression2_value = subexpressions[7]["value"]

    conditional_value = "(" + condition_value + ")?" + expression1_value + ":" + expression2_value

    subexpressions[0] = {"value": conditional_value}



def p_for(subexpressions):
    'for : FOR LPAREN assignationorlamba SEMICOLON condition SEMICOLON advance RPAREN possiblecomment keys'

    #{KEYS.level = FOR.level + 1, FOR.value = indent(FOR.level) + ’for (’ + ASSIGNATIONORLAMBDA.value + ’;’ + CONDITION.value + ’;’ + ADVANCE.value ’) ’ + POSSIBLECOMMENT.value + ’\n’ + KEYS.value}
    for_level = subexpressions[0]["level"]

    assignationorlamba_value = subexpressions[3]["value"]
    condition_value = subexpressions[5]["value"]
    advance_value = subexpressions[7]["value"]
    possiblecomment_value = subexpressions[9]["value"]
    keys_value = subexpressions[10]["value"]

    for_value = indent(for_level) + "for(" + assignationorlamba_value + "; "+condition_value+ "; " +advance_value+ ")" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": for_value}
    subexpressions[10] = {"level": for_level + 1}


def p_do_while(subexpressions):
    'do_while : DO RKEY possiblecomment list_sentencies LKEY WHILE LPAREN condition RPAREN SEMICOLON possiblecomment'

    #{LIST SENTENCIES.level = DO WHILE.level + 1, DO WHILE.value = indent(DO WHILE.level) + ’do’ + POSSIBLECOMMENT1 .value + ’\n’ + LIST SENTENCIES.value + ’ while(’ + CONDITION.value + ’); ’ + POSSIBLECOMMENT2 .value + ’\n’}
    do_while_level = subexpressions[0]["level"]

    possiblecomment1_value = subexpressions[3]["value"]
    list_sentencies_value = subexpressions[4]["value"]
    condition_value = subexpressions[8]["value"]
    possiblecomment2_value = subexpressions[11]["value"]

    do_while_value = indent(do_while_level) + "do(" + possiblecomment1_value + "\n" + list_sentencies_value + "while(" + condition_value+ ");" + possiblecomment2_value + "\n"

    subexpressions[0] = {"value": do_while_value}
    subexpressions[10] = {"level": do_while_level + 1}


def p_keys_append_sentence(subexpressions):
    'keys : comment_list sentence'

    #{COMMENT LIST.level = KEYS.level, SENTENCE.level = KEYS.level, KEYS.value = COMMENT LIST.value + indent(KEYS.level) + SENTENCE.value}
    keys_level = subexpressions[0]["level"]

    comment_list_value = subexpressions[1]["value"]
    sentence_value = subexpressions[2]["value"]

    keys_value = comment_list_value +  indent(keys_level) + sentence_value

    subexpressions[0] = {"value": keys_value}
    subexpressions[1] = {"level": keys_level}
    subexpressions[2] = {"level": keys_level}



def p_keys_append_possiblecomment(subexpressions):
    'keys : RKEY possiblecomment list_sentencies LKEY'

    #{LIST SENTENCIES.level = KEYS.level, KEYS.value = ’{’ + POSSIBLECOMMENT.value + ’\n’ + LIST SENTENCIES.value + ’}’ + ’\n’}
    keys_level = subexpressions[0]["level"]

    possiblecomment_value = subexpressions[2]["value"]
    list_sentencies_value = subexpressions[3]["value"]

    keys_value = "{ " + possiblecomment_value +  "\n" + list_sentencies_value + "}\n"

    subexpressions[0] = {"value": keys_value}
    subexpressions[3] = {"level": keys_level}



def p_assignationorlambda_assignation(subexpressions):
    'assignationorlambda : assignation'

    #{ASSIGNATIONORLAMBDA.value = ASSIGNATION.value}
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_assignationorlambda_lambda(subexpressions):
    'assignationorlambda : '

    #{ASSIGNATIONORLAMBDA.value = ’ ’}
    subexpressions[0] = {"value": ""}

#cuando inserta en la tabla no se si esta bien
def p_assignation(subexpressions):
    'assignation : VAR b'

    #{ASSIGNATION.value = var.value + B.value, IF(B.isArray, COND(tabla(var.value)!= None && tabla(var.value) == B.type ), table.insertOrUpdate(var.value, B.type) )}
    b_isArray = subexpressions[2]["isArray"]
    b_type = subexpressions[2]["type"]
    b_value = subexpressions[2]["value"]

    var_value = subexpressions[1]["value"]

    if table.has_key(var_value) != None and table[var_value] != b_type and table[var_isArray] == true:
        raise SemanticException("No puede agregarle a un array un tipo diferente al tipo del array")


    table.insertOrUpdate(var_value, b_type, b_isArray)

    subexpressions[0] = {"value": var_value + b_value}


def p_b_array(subexpressions):
    'b : LBRACKET NATURAL RBRACKET ASSIGN expression'

    #{B.value = ’[’ + natural.value + ’] = ’ + EXPRESSION.value, B.type = ’array<’ + EXPRESSION.type + ’>’, B.isArray = true}
    natural_value = subexpressions[2]["value"]
    expression_value =  subexpressions[5]["value"]
    expresion_type =  subexpressions[5]["type"]

    b_value = "[" +  natural_value + "] = " +  expression_value
    b_type = "array<"+expresion_type + ">"
    b_isArray = true

    subexpressions[0] = {"value": b_value, "type": b_type, "isArray": b_isArray}



def p_b_expression(subexpressions):
    'b : ASSIGN expression'

    #{B.value = ’=’ + EXPRESSION.value, B.type = EXPRESSION.type, B.isArray = false}
    expression_value =  subexpressions[2]["value"]
    expresion_type =  subexpressions[2]["type"]

    subexpressions[0] = {"value": expression_value, "type": expresion_type, "isArray": false}


def p_advance_var(subexpressions):
    'advance : VAR c'

    #{COND(var.type == NUM), ADVANCE.value = var.value + C.value }
    var_type = subexpressions[1]["type"]
    var_value = subexpressions[1]["value"]
    c_value = subexpressions[2]["value"]

    if var_type != "natural" :
        raise SemanticException("El tipo a avanzar no es un natural")

    advance_value =  var_value + c_value

    subexpressions[0] = {"value": advance_value}


def p_advance_lambda(subexpressions):
    'advance : '

    #{ADVANCE.value = ’ ’}
    subexpressions[0] = {"value": ""}


def p_c_plus(subexpressions):
    'c : PLUS d'

    #{ C.value = ’+’ + D.value }
    d_value = subexpressions[2]["value"]
    c_value = "+" + d_value

    subexpressions[0] = {"value": c_value}

def p_c_minus(subexpressions):
    'c : MINUS f'

    #{ C.value = ’-’ + F.value }
    f_value = subexpressions[2]["value"]
    c_value = "-" + f_value

    subexpressions[0] = {"value": c_value}



def p_d_plus(subexpressions):
    'd : PLUS'

    #{ D.value = ’+’ }
    subexpressions[0] = {"value": "+"}

def p_d_num(subexpressions):
    'c : num'

    #{ D.value = ’=’ + NUM.value }
    num_value = subexpressions[1]["value"]
    d_value = "=" + num_value

    subexpressions[0] = {"value": d_value}

def p_f_minus(subexpressions):
    'f : MINUS'

    #{ F.value = ’-’ }
    subexpressions[0] = {"value": "-"}

def p_f_num(subexpressions):
    'f : num'

    #{ F.value = ’=’ + NUM.value }
    num_value = subexpressions[1]["value"]
    f_value = "=" + num_value

    subexpressions[0] = {"value": f_value}

def p_condition_logical_condition(subexpressions):
    'condition : logical_condition'

    #{CONDITION.value = LOGICAL CONDITION.value}
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_condition_boolean_condition(subexpressions):
    'condition : boolean_condition'

    #{ CONDITION.value = BOOLEAN CONDITION.value }
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_boolean_condition(subexpressions):
    'boolean_condition : logical_condition h'

    #{BOOLEAN CONDITION.value = LOGICAL CONDITION + H.value }
    boolean_condition_value = subexpressions[1]["value"] + subexpressions[2]["value"]

    subexpressions[0] = {"value": boolean_condition_value}


def p_h_and(subexpressions):
    'h : AND boolean_condition'

    #{ H.value = ’and’ + BOOLEAN CONDITION.value }
    boolean_condition_value = subexpressions[2]["value"]
    h_value = "and" + boolean_condition_value

    subexpressions[0] = {"value": h_value}


def p_h_or(subexpressions):
    'h : OR boolean_condition'

    #{ H.value = or + BOOLEAN CONDITION.value }
    boolean_condition_value = subexpressions[2]["value"]
    h_value = "or" + boolean_condition_value

    subexpressions[0] = {"value": h_value}


def p_h_lambda(subexpressions):
    'h : '

    #{H.value = ’ ’}
    subexpressions[0] = {"value": ""}


def p_logical_condition(subexpressions):
    'logical_condition : e i'

    #{ LOGICAL CONDITION.value = E.value + I.value }
    logical_condition_value = subexpressions[1]["value"] + subexpressions[2]["value"]

    subexpressions[0] = {"value": logical_condition_value}

def p_logical_condition_less(subexpressions):
    'i : LESS e'

    #{ I.value = ’>’ + E.value }
    e_value = subexpressions[1]["value"]
    i_value = " > " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_greater(subexpressions):
    'i : GREATER e'

    #{ I.value = ’>’ + E.value }
    e_value = subexpressions[1]["value"]
    i_value = " < " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_equal(subexpressions):
    'i : EQUAL e'

    #{ I.value = ’==’ + E.value }
    e_value = subexpressions[1]["value"]
    i_value = " == " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL e'

    #{ I.value = ’!=’ + E.value }
    e_value = subexpressions[1]["value"]
    i_value = " != " + e_value

    subexpressions[0] = {"value": i_value}


def p_value_string(subexpressions):
    'value : STRING'

    #{VALUE.value = ’string’ , VALUE.type = ’string’}
    subexpressions[0] = {"value": "string", "type": "string"}

def p_value_bool(subexpressions):
    'value : BOOL'

    #{VALUE.value = ’bool’ , VALUE.type = ’bool’}
    subexpressions[0] = {"value": "bool", "type": "bool"}

def p_value_var(subexpressions):
    'value : VAR j'

    #{VALUE.value = var.value , VALUE.type = IF( J.isArray, getArrayType(table(var.value)) , var.type)}
    j_isArray = subexpressions[2]["isArray"]
    var_value = subexpressions[1]["value"]
    var_type = subexpressions[1]["type"]

    value_type = var_type

    if(j_isArray):
        value_type = table.gatTipe(var_value)

    subexpressions[0] = {"value": var_value, "type": var_type}



def p_value_num(subexpressions):
    'value : NUM'

    #{VALUE.value = NUM.value , VALUE.type = NUM.type}
    num_value = subexpressions[1]["value"]
    num_type = subexpressions[1]["type"]

    subexpressions[0] = {"value": num_value, "type": num_type}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    #{VALUE.value = FUNCTION WITH RETURN.value, VALUE.type = FUNCTION WITH RETURN.type}
    function_with_return_value = subexpressions[1]["value"]
    function_with_return_value = subexpressions[1]["type"]

    subexpressions[0] = {"value": function_with_return_value, "type": function_with_return_value}


def p_j_array(subexpressions):
    'value : LBRACKET num RBRACKET'

    #{ J.value = ’[’ + NUM.value + ’]’, J.isArray = true }
    num_value = subexpressions[1]["value"]
    j_value = "[" + num_value + "]"

    subexpressions[0] = {"value": j_value, "isArray": true}


def p_j_lambda(subexpressions):
    'value : '

    #{J.value = ’ ’, J.isArray = false}
    subexpressions[0] = {"value": "", "isArray": false}


def p_value_list_values(subexpressions):
    'value : LBRACKET list_values RBRACKET'

    #{VALUE.value = ’[ ’ + LIST VALUES.value + ’]’, VALUE.type = LIST VALUES.type}
    list_values_value = subexpressions[2]["value"]
    list_values_type = subexpressions[2]["type"]
    value_value = "[" + list_values_value + "]"

    subexpressions[0] = {"value": value_value, "type": list_values_type}


#aca la condicion creo que no va es una lista de registros y cada registro puede tener su tipo
def p_list_registers(subexpressions):
    'list_registers : assignation l'

    #{LIST REGISTERS.value = ASSIGNATION.value + L.value, COND(L.value == ’ ’ || L.type == ASSIGNATION.type) }
    assignation_value = subexpressions[1]["value"]
    assignation_type  = subexpressions[1]["type"]
    l_value = subexpressions[2]["value"]
    l_type = subexpressions[2]["type"]

    list_registers_value = assignation_value + l_value

    #if l_value != "" and l_type !=  assignation_type:
    #    raise SemanticException("se quiere ")

    subexpressions[0] = {"value": list_registers_value}


#es condicion el type?
def p_l_coma(subexpressions):
    'l : COMA list_registers'

    #{ L.value = ’,’ + LIST REGISTERS.value, L.type == LIST REGISTERS.type }
    list_registers_value = subexpressions[1]["value"]
    list_registers_type  = subexpressions[1]["type"]

    l_value = ", " + list_registers_value
    l_type = list_registers_type


    #if l_value != "" and l_type !=  assignation_type:
    #    raise SemanticException("se quiere ")

    subexpressions[0] = {"value": l_value}


def p_l_lambda(subexpressions):
    'l : '

    #{LIST REGISTERS.value = ’ ’ }
    subexpressions[0] = {"value": ""}


#es condicion el type?
def p_list_values(subexpressions):
    'list_values : value m'

    #{LIST VALUES.value = VALUE.value + M.value, LIST VALUES.type = VALUE.type}
    value_value = subexpressions[1]["value"]
    value_type  = subexpressions[1]["type"]

    m_value =subexpressions[2]["value"]

    list_values_value = value_value + m_value
    list_values_type = value_type
    #if l_value != "" and l_type !=  assignation_type:
    #    raise SemanticException("se quiere ")

    subexpressions[0] = {"value": list_values_value, "type" : list_values_type}



def p_error(subexpressions):
    raise Exception("Syntax error.")
