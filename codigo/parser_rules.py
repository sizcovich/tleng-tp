from lexer_rules import tokens

from expressions import Addition, Multiplication, Number



def p_program(subexpressions):
    'program : list_sentencies'

    
    list_sentencies = subexpressions[1]
    value = list_sentencies["value"]
    subexpressions[0] = {"level": 0, "value": value}
    print(value)

def p_list_sentencies(subexpressions):
    'list_sentencies : g a'
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

    
    subexpressions[0] = subexpressions[1]

def p_g_sentence(subexpressions):
    'g : sentence'

    
    g_level = subexpressions[0]["level"]
    sentence_value = subexpressions[1]["value"]
    g_value = indent(g_level) + sentence_value

    subexpressions[0] = {"value": g_value}
    subexpressions[1] = {"level": g_level}


def p_g_newline(subexpressions):
    'g : NEWLINE'

    
    subexpressions[0] = {"value": ""}


def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'
    a_level = subexpressions[0]["level"]
    list_sentencies_value = subexpressions[1]["value"]

    
    subexpressions[0] = {"value": list_sentencies_value}
    subexpressions[1] = {"level": a_level}


def p_g_lambda(subexpressions):
    'g : '

    
    subexpressions[0] = {"value": ""}



def p_sentence_semicolon(subexpressions):
    'sentence : e SEMICOLON possiblecomment'

    
    sentence_level = subexpressions[0]["level"]

    e_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    sentence_value = e_value + "; " + possiblecomment_value

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_while(subexpressions):
    'sentence : while'

    
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_if_else(subexpressions):
    'sentence : if_else'

    
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_sentence_for(subexpressions):
    'sentence : for'

    
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}

def p_sentence_do_while(subexpressions):
    'sentence : do_while'

    
    sentence_level = subexpressions[0]["level"]

    sentence_value = subexpressions[1]["value"]

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}

def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON possiblecomment'

    
    sentence_level = subexpressions[0]["level"]

    function_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    sentence_value = function_value + "; " + possiblecomment_value

    subexpressions[0] = {"value": sentence_value}
    subexpressions[1] = {"level": sentence_level}


def p_e_assignation(subexpressions):
    'e : assignation'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_e_expression(subexpressions):
    'e : expression'

    
    subexpressions[0] = {"value": subexpressions[1]["value"], "type": subexpressions[1]["type"]}


def p_e_conditional(subexpressions):
    'e : conditional'

    
    subexpressions[0] = {"value": subexpressions[1]["value"], "type": subexpressions[1]["type"]}


def p_possiblecomment_comment(subexpressions):
    'possiblecomment : comment'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_possiblecomment_lambda(subexpressions):
    'possiblecomment : '

    
    subexpressions[0] = {"value": ""}


def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'

    
    comment_value = subexpressions[1]["value"]
    comment_list2_value = subexpressions[2]["value"]
    comment_list1_value =  comment_value + "\n" + comment_list2_value

    subexpressions[0] = {"value": comment_list1_value}

def p_comment_list_newline(subexpressions):
    'comment_list : NEWLINE comment_list'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}

def p_comment_list_lambda(subexpressions):
    'comment_list : '

    
    subexpressions[0] = {"value": ""}

def p_while(subexpressions):
    'while : WHILE LPAREN condition RPAREN possiblecomment keys'

    
    while_level = subexpressions[0]["level"]

    condition_value = subexpressions[3]["value"]
    possiblecomment_value = subexpressions[5]["value"]
    keys_value = subexpressions[6]["value"]
    while_value = indent(while_level) + "while(" + condition_value + ")" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": while_value}
    subexpressions[6] = {"level": while_level + 1}


def p_if_else(subexpressions):
    'if_else : if ELSE possiblecomment keys'

    
    if_else_level = subexpressions[0]["level"]

    if_value = subexpressions[1]["value"]
    possiblecomment_value = subexpressions[3]["value"]
    keys_value = subexpressions[4]["value"]

    if_else_value = indent(if_else_level) + if_value + "else" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": if_else_value}
    subexpressions[6] = {"level": if_else_level + 1}



def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN possiblecomment keys'

    
    if_level = subexpressions[0]["level"]

    condition_value = subexpressions[3]["value"]
    possiblecomment_value = subexpressions[5]["value"]
    keys_value = subexpressions[6]["value"]

    if_value = "if(" + condition_value + ")" + possiblecomment_value + "\n" + keys_value

    subexpressions[0] = {"value": if_value}
    subexpressions[6] = {"level": if_level + 1}

def p_conditional(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK expression COLON expression'

    
    condition_value = subexpressions[2]["value"]
    expression1_value = subexpressions[5]["value"]
    expression2_value = subexpressions[7]["value"]

    conditional_value = "(" + condition_value + ")?" + expression1_value + ":" + expression2_value

    subexpressions[0] = {"value": conditional_value}



def p_for(subexpressions):
    'for : FOR LPAREN assignationorlamba SEMICOLON condition SEMICOLON advance RPAREN possiblecomment keys'

    
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

    
    keys_level = subexpressions[0]["level"]

    comment_list_value = subexpressions[1]["value"]
    sentence_value = subexpressions[2]["value"]

    keys_value = comment_list_value +  indent(keys_level) + sentence_value

    subexpressions[0] = {"value": keys_value}
    subexpressions[1] = {"level": keys_level}
    subexpressions[2] = {"level": keys_level}



def p_keys_append_possiblecomment(subexpressions):
    'keys : RKEY possiblecomment list_sentencies LKEY'

    
    keys_level = subexpressions[0]["level"]

    possiblecomment_value = subexpressions[2]["value"]
    list_sentencies_value = subexpressions[3]["value"]

    keys_value = "{ " + possiblecomment_value +  "\n" + list_sentencies_value + "}\n"

    subexpressions[0] = {"value": keys_value}
    subexpressions[3] = {"level": keys_level}



def p_assignationorlambda_assignation(subexpressions):
    'assignationorlambda : assignation'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_assignationorlambda_lambda(subexpressions):
    'assignationorlambda : '

    
    subexpressions[0] = {"value": ""}


def p_assignation(subexpressions):
    'assignation : VAR b'

    
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

    
    natural_value = subexpressions[2]["value"]
    expression_value =  subexpressions[5]["value"]
    expresion_type =  subexpressions[5]["type"]

    b_value = "[" +  natural_value + "] = " +  expression_value
    if expression_type == "natural": 
    	b_type = "decimal" 
    else: 
    	b_type = expression_type
    b_isArray = true

    subexpressions[0] = {"value": b_value, "type": b_type, "isArray": b_isArray}



def p_b_expression(subexpressions):
    'b : ASSIGN expression'

    
    expression_value =  subexpressions[2]["value"]
    expresion_type =  subexpressions[2]["type"]

    subexpressions[0] = {"value": expression_value, "type": expresion_type, "isArray": false}


def p_advance_var(subexpressions):
    'advance : VAR c'

    
    var_type = subexpressions[1]["type"]
    var_value = subexpressions[1]["value"]
    c_value = subexpressions[2]["value"]

    if var_type != "natural" :
        raise SemanticException("El tipo a avanzar no es un natural")

    advance_value =  var_value + c_value

    subexpressions[0] = {"value": advance_value}


def p_advance_lambda(subexpressions):
    'advance : '

    
    subexpressions[0] = {"value": ""}


def p_c_plus(subexpressions):
    'c : PLUS d'

    
    d_value = subexpressions[2]["value"]
    c_value = "+" + d_value

    subexpressions[0] = {"value": c_value}

def p_c_minus(subexpressions):
    'c : MINUS f'

    
    f_value = subexpressions[2]["value"]
    c_value = "-" + f_value

    subexpressions[0] = {"value": c_value}



def p_d_plus(subexpressions):
    'd : PLUS'

    
    subexpressions[0] = {"value": "+"}

def p_d_num(subexpressions):
    'c : num'

    
    num_value = subexpressions[1]["value"]
    d_value = "=" + num_value

    subexpressions[0] = {"value": d_value}

def p_f_minus(subexpressions):
    'f : MINUS'

    
    subexpressions[0] = {"value": "-"}

def p_f_num(subexpressions):
    'f : num'

    
    num_value = subexpressions[1]["value"]
    f_value = "=" + num_value

    subexpressions[0] = {"value": f_value}

def p_condition_logical_condition(subexpressions):
    'condition : logical_condition'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_condition_boolean_condition(subexpressions):
    'condition : boolean_condition'

    
    subexpressions[0] = {"value": subexpressions[1]["value"]}


def p_boolean_condition(subexpressions):
    'boolean_condition : logical_condition h'

    
    boolean_condition_value = subexpressions[1]["value"] + subexpressions[2]["value"]

    subexpressions[0] = {"value": boolean_condition_value}


def p_h_and(subexpressions):
    'h : AND boolean_condition'

    
    boolean_condition_value = subexpressions[2]["value"]
    h_value = "and" + boolean_condition_value

    subexpressions[0] = {"value": h_value}


def p_h_or(subexpressions):
    'h : OR boolean_condition'

    
    boolean_condition_value = subexpressions[2]["value"]
    h_value = "or" + boolean_condition_value

    subexpressions[0] = {"value": h_value}


def p_h_lambda(subexpressions):
    'h : '

    
    subexpressions[0] = {"value": ""}


def p_logical_condition(subexpressions):
    'logical_condition : e i'

    
    logical_condition_value = subexpressions[1]["value"] + subexpressions[2]["value"]

    subexpressions[0] = {"value": logical_condition_value}

def p_logical_condition_less(subexpressions):
    'i : LESS e'

    
    e_value = subexpressions[1]["value"]
    i_value = " > " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_greater(subexpressions):
    'i : GREATER e'

    
    e_value = subexpressions[1]["value"]
    i_value = " < " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_equal(subexpressions):
    'i : EQUAL e'

    
    e_value = subexpressions[1]["value"]
    i_value = " == " + e_value

    subexpressions[0] = {"value": i_value}


def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL e'

    
    e_value = subexpressions[1]["value"]
    i_value = " != " + e_value

    subexpressions[0] = {"value": i_value}


def p_value_string(subexpressions):
    'value : STRING'

    
    subexpressions[0] = {"value": "string", "type": "string"}

def p_value_bool(subexpressions):
    'value : BOOL'

    
    subexpressions[0] = {"value": "bool", "type": "bool"}

def p_value_var(subexpressions):
    'value : VAR j'

    j_isArray = subexpressions[2]["isArray"]
    var_value = subexpressions[1]["value"]
    var_type = subexpressions[1]["type"]

    value_type = var_type

    if(j_isArray):
        value_type = table.gatTipe(var_value)

    subexpressions[0] = {"value": var_value, "type": var_type}



def p_value_num(subexpressions):
    'value : NUM'

    
    num_value = subexpressions[1]["value"]
    num_type = subexpressions[1]["type"]

    subexpressions[0] = {"value": num_value, "type": num_type}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    
    function_with_return_value = subexpressions[1]["value"]
    function_with_return_value = subexpressions[1]["type"]

    subexpressions[0] = {"value": function_with_return_value, "type": function_with_return_value}


def p_j_array(subexpressions):
    'value : LBRACKET num RBRACKET'

    
    num_value = subexpressions[1]["value"]
    j_value = "[" + num_value + "]"

    subexpressions[0] = {"value": j_value, "isArray": true}


def p_j_lambda(subexpressions):
    'value : '

    
    subexpressions[0] = {"value": "", "isArray": false}


def p_value_list_values(subexpressions):
    'value : LBRACKET value list_values RBRACKET'

    value_value1 = subexpressions[2]["value"]
    list_values_value = subexpressions[3]["value"]
    if value_type == "natural":
    	list_values_type = "decimal"
    else:
    	list_values_type = subexpressions[3]["type"]
    value_value = "[" + value_value1 + list_values_value + "]"

    subexpressions[0] = {"value": value_value, "type": list_values_type}


def p_list_registers(subexpressions):
    'list_registers : assignation l'

    assignation_value = subexpressions[1]["value"]
    assignation_type  = subexpressions[1]["type"]
    l_value = subexpressions[2]["value"]
    l_type = subexpressions[2]["type"]

    list_registers_value = assignation_value + l_value

    subexpressions[0] = {"value": list_registers_value}


def p_l_coma(subexpressions):
    'l : COMA list_registers'

    
    list_registers_value = subexpressions[1]["value"]
    list_registers_type  = subexpressions[1]["type"]

    l_value = ", " + list_registers_value
    l_type = list_registers_type

    subexpressions[0] = {"value": l_value}


def p_l_lambda(subexpressions):
    'l : '

    
    subexpressions[0] = {"value": ""}



def p_list_values(subexpressions):


def p_error(subexpressions):
    raise Exception("Syntax error.")
