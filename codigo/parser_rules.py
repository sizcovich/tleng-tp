from lexer_rules import tokens

#from expressions import Addition, Multiplication, Number

class SemanticException(Exception):
    pass


#funciones a definir:
#indent
#insertOrUpdate
#table(var.value)
#table.isArray(var.value):
#table.getType(var.value)


table = {}

def insertOrUpdate(name, type, isArray):
    datos = (type, isArray)
    table[name] = datos

def isArray(name):

    isArray = False
    if (table.has_key(name)!= False):
        datos =table[name]
        isArray = datos[1]

    return isArray

def getType(name):
    type = ""

    if (table.has_key(name)!= False):
        datos =table[name]
        type = datos[0]

    return type

def indent(cant):
    return "        "



def p_program(subexpressions):
    'program : list_sentencies'

    #{PROGRAM.value = LIST SENTENCIES.value}
    list_sentencies = subexpressions[1]

    subexpressions[0] = {"value": list_sentencies["value"]}

    #print(list_sentencies["value"])

def p_list_sentencies_newline(subexpressions):
    'list_sentencies : NEWLINE a'
    #{LIST_SENTENCIES.value= A.value, LIST_SENTENCIES.element = 'newline'}
    a = subexpressions[2]

    subexpressions[0] = {"value":  a["value"], "element": "newline"}

def p_list_sentencies_comment(subexpressions):
    'list_sentencies : COMMENT a'
    #{LIST_SENTENCIES.value= comment.value + '\n' + A.value, LIST_SENTENCIES.element = 'comment'}
    comment = subexpressions[1]
    a = subexpressions[2]

    subexpressions[0] = {"value": comment + "\n" + a["value"], "element": "comment"}

def p_list_sentencies_sentence(subexpressions):
    'list_sentencies : sentence a'
    #{LIST_SENTENCIES.value= SENTENCE.value  + IF(a.element!='comment' , '\n') + A.value, LIST_SENTENCIES.element = 'sentence'}
    sentence = subexpressions[1]
    a = subexpressions[2]

    if (a["element"] != "comment"):
        list_sentencies_value = sentence["value"] + "\n" + a["value"]
    else:
        list_sentencies_value = sentence["value"]  + a["value"]

    subexpressions[0] = {"value": list_sentencies_value, "element": "sentence"}

def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'

    #{A.value = LIST_SENTENCIES.value, A.element =LIST_SENTENCIES.element}
    list_sentencies = subexpressions[1]

    subexpressions[0] = {"value": list_sentencies["value"], "element":list_sentencies["element"]}


def p_a_lambda(subexpressions):
    'a : '

    #{A.value = '', A.element=''}
    subexpressions[0] = {"value": "", "element":""}



def p_sentence_semicolon(subexpressions):
    'sentence : e SEMICOLON'

    #{SENTENCE.value = E.value + ';'}
    e = subexpressions[1]

    subexpressions[0] = {"value": e["value"] + "; "}


def p_sentence_while(subexpressions):
    'sentence : while'

    #{SENTENCE.value = WHILE.value}
    while1 = subexpressions[1]

    subexpressions[0] = {"value": while1["value"]}


def p_sentence_if_else(subexpressions):
    'sentence : if_else'

    #{SENTENCE.value = IF_ELSE.value}
    if_else = subexpressions[1]

    subexpressions[0] = {"value": if_else["value"]}


def p_sentence_for(subexpressions):
    'sentence : for'

    #{SENTENCE.value = FOR.value}
    for1 = subexpressions[1]

    subexpressions[0] = {"value": for1["value"]}

def p_sentence_do_while(subexpressions):
    'sentence : do_while'

    #{SENTENCE.value = DO_WHILE.value}
    do_while = subexpressions[1]

    subexpressions[0] = {"value": do_while["value"]}

#semantica corregida
def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON'

    #{SENTENCE.value = FUNCTION.value + ';'}
    function = subexpressions[1]

    subexpressions[0] = {"value": function["value"] + ";"}


def p_e_ecomparable(subexpressions):
    'e : ecomparable'

    #{E.value = ASSIGNATION.value}
    ecomparable = subexpressions[1]

    subexpressions[0] = {"value": ecomparable["value"]}

def p_e_advance(subexpressions):
    'e : advance'

    #{E.value = ASSIGNATION.value}
    advance = subexpressions[1]

    subexpressions[0] = {"value": advance["value"]}


def p_e_assignation(subexpressions):
    'e : assignation'
    #{E.value = ASSIGNATION.value}
    assignation = subexpressions[1]

    subexpressions[0] = {"value": assignation["value"]}

def p_ecomparable_expression(subexpressions):
    'ecomparable : expression'

    #{ECOMPARABLE.value = EXPRESSION.value}
    expression = subexpressions[1]

    subexpressions[0] = {"value": expression["value"]}

def p_ecomparable_conditional(subexpressions):
    'ecomparable : conditional'

    #{ECOMPARABLE.value = CONDITIONAL.value}
    conditional = subexpressions[1]

    subexpressions[0] = {"value": conditional["value"]}


def p_possiblecomment_comment(subexpressions):
    'possiblecomment : COMMENT'

    #{POSSIBLECOMMENT.value = comment.value}
    comment = subexpressions[1]

    subexpressions[0] = {"value": comment}


def p_possiblecomment_lambda(subexpressions):
    'possiblecomment : '

    #{POSSIBLECOMMENT.value = ''}

    subexpressions[0] = {"value": ""}

def p_possiblenewline_newline(subexpressions):
    'possiblenewline : NEWLINE'

    #{POSSIBLECOMMENT.value = ''}

    subexpressions[0] = {"value": ""}

def p_possiblenewline_lambda(subexpressions):
    'possiblenewline : '

    #{POSSIBLECOMMENT.value = comment.value}

    subexpressions[0] = {"value": ""}




#semantica corregida
def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'

    #{COMMENT_LIST1.value = comment.value + '\n' + COMMENT_LIST2.value}
    comment = subexpressions[1]
    comment_list2 = subexpressions[2]

    subexpressions[0] = {"value": comment + "\n" + comment_list2["value"]}


def p_comment_list_newline(subexpressions):
    'comment_list : NEWLINE comment_list'

    #{COMMENT_LIST1.value = '\n' + COMMENT_LIST2}
    comment_list2 = subexpressions[2]

    subexpressions[0] = {"value":  "\n" + comment_list2["value"]}


def p_comment_list_lambda(subexpressions):
    'comment_list : '

    #{COMMENT LIST.value = ''}
    subexpressions[0] = {"value": ""}


def p_while(subexpressions):
    'while : WHILE LPAREN condition RPAREN possiblecomment possiblenewline keys'

    #{WHILE.value = 'while (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    while1 = subexpressions[0]
    condition = subexpressions[3]



    possiblecomment = subexpressions[5]
    keys = subexpressions[7]

    subexpressions[0] = {"value": "while(" + condition["value"] + ")" + possiblecomment["value"] + "\n" + keys["value"]}


def p_if_else(subexpressions):
    'if_else : if ELSE possiblecomment possiblenewline keys'

    #{IF_ELSE.value = IF.value + 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if_else = subexpressions[0]
    if1 = subexpressions[1]
    possiblecomment = subexpressions[3]
    keys = subexpressions[5]

    subexpressions[0] = {"value": if1["value"] + "else" + possiblecomment["value"] + "\n" + keys["value"]}




def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN possiblecomment possiblenewline keys'

    #{IF.value = 'if (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if1 = subexpressions[0]
    condition = subexpressions[3]
    possiblecomment = subexpressions[5]
    keys = subexpressions[7]

    subexpressions[0] = {"value": "if(" + condition["value"] + ")" + possiblecomment["value"] + "\n" + keys["value"]}


def p_conditional(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK expression COLON expression'

    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + EXPRESSION1.value + ':' + EXPRESSION2.value}
    condition = subexpressions[2]
    expression1 = subexpressions[5]
    expression2 = subexpressions[7]

    subexpressions[0] = {"value": "(" + condition["value"] + ")?" + expression1["value"] + ":" + expression2["value"]}


def p_for(subexpressions):
    'for : FOR LPAREN assignationorlambda SEMICOLON condition SEMICOLON advanceorlambda RPAREN possiblecomment possiblenewline keys'

    #{FOR.value ='for (' + ASSIGNATIONORLAMBDA.value + ';' + CONDITION.value + ';' + ADVANCE.value ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}

    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advance = subexpressions[7]
    possiblecomment = subexpressions[9]
    keys = subexpressions[11]

    subexpressions[0] = {"value": "for(" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advance["value"]+ ")" + possiblecomment["value"] + "\n" + keys["value"]}


def p_do_while(subexpressions):
    'do_while : DO LKEY possiblecomment list_sentencies RKEY WHILE LPAREN condition RPAREN SEMICOLON possiblecomment possiblenewline'

    #{DO_WHILE.value = 'do' + POSSIBLECOMMENT1.value + '\n' + LIST_SENTENCIES.value + ' while(' + CONDITION.value + '); ' + POSSIBLECOMMENT2.value + '\n'}
    do_while = subexpressions[0]
    possiblecomment1 = subexpressions[3]
    list_sentencies = subexpressions[4]
    condition = subexpressions[8]
    possiblecomment2 = subexpressions[11]

    subexpressions[0] = {"value": "do(" + possiblecomment1["value"] + "\n" + list_sentencies["value"] + "while(" + condition["value"]+ ");" + possiblecomment2["value"] + "\n"}


def p_keys_append_sentence(subexpressions):
    'keys : comment_list sentence'

    #{ KEYS.value = COMMENT_LIST.value + SENTENCE.value}
    keys = subexpressions[0]
    comment_list = subexpressions[1]
    sentence = subexpressions[2]

    subexpressions[0] = {"value": comment_list["value"] +  sentence["value"]}


def p_keys_append_possiblecomment(subexpressions):
    'keys : LKEY possiblenewline possiblecomment list_sentencies RKEY possiblenewline'


    #{KEYS.value = '{' + POSSIBLECOMMENT.value + '\n' + LIST_SENTENCIES.value + '} \n'}
    keys = subexpressions[0]
    possiblecomment = subexpressions[3]
    list_sentencies = subexpressions[4]

    subexpressions[0] = {"value": "{ " + possiblecomment["value"] +  "\n" + list_sentencies["value"] + "}\n"}




def p_assignationorlambda_assignation(subexpressions):
    'assignationorlambda : assignation'

    #{ASSIGNATIONORLAMBDA.value = ASSIGNATION.value}
    assignation = subexpressions[1]

    subexpressions[0] = {"value": assignation["value"]}




def p_assignationorlambda_lambda(subexpressions):
    'assignationorlambda : '

    #{ASSIGNATIONORLAMBDA.value = ''}
    subexpressions[0] = {"value": ""}


#ojo cambie la condicion
def p_assignation(subexpressions):
    'assignation : VAR b'

    #{ASSIGNATION.value = var.value + B.value, IF(B.isArray, COND(table(var.value) != None && table.getType(var.value) == B.type && B.isArray==table.isArray(var.value)), table.insertOrUpdate(var.value,B.type, B.isArray)}
    b = subexpressions[2]
    var = subexpressions[1]


    if table.has_key(var) == True:
        if b["isArray"] == isArray(var):
            if isArray(var):
                if getType(var) != b["type"]:
                    raise SemanticException("No puede agregarle a un array un elemento de tipo distinto al tipo del array")

    insertOrUpdate(var,b["type"], b["isArray"])


    subexpressions[0] = {"value": var + b["value"]}


def p_b_array(subexpressions):
    'b : LBRACKET expression RBRACKET ASSIGN expression'


    #{B.value = '[' + natural.value + '] = ' + EXPRESSION.value, B.type = IF(EXPRESSION.type == 'natural', 'decimal', EXPRESSION.type), B.isArray = true}
    expression1 = subexpressions[2]
    expression2 =  subexpressions[5]

    if expression1["type"] != "natural":
        raise SemanticException("El valor para acceder a un array debe ser natural")


    if expression2["type"] == "natural":
        b_type = "decimal"
    else:
        b_type = expression2["type"]

    subexpressions[0] = {"value": "[" +  expression1["value"] + "] = " +  expression2["value"], "type": b_type, "isArray": True}


def p_b_expression(subexpressions):
    'b : ASSIGN expression'

    #{B.value = '=' + EXPRESSION.value, B.type = EXPRESSION.type, B.isArray = false}
    expression =  subexpressions[2]

    subexpressions[0] = {"value": "= " + expression["value"] , "type": expression["type"], "isArray": False}

def p_advanceorlambda_advance(subexpressions):
    'advanceorlambda : advance'

    advance = subexpressions[1]
    subexpressions[0] = {"value":  advance["value"]}

def p_advanceorlambda_lambda(subexpressions):
    'advanceorlambda : '

    subexpressions[0] = {"value":  ""}

#semantica corregida
def p_advance_var(subexpressions):
    'advance : VAR c'

    var = subexpressions[1]
    c = subexpressions[2]

    #{COND(table.getType(var.value) == 'natural' || table.getType(var.value)  == 'decimal'), ADVANCE.value = var.value + C.value}
    if (not(getType(var) == "natural" or getType(var) == "decimal" or  getType(var) == "string")) :
        raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  var + c["value"]}



def p_c_increment(subexpressions):
    'c : INCREMENT'

    #{ C.value = '++'}
    subexpressions[0] = {"value": "++"}

def p_c_plus(subexpressions):
    'c : PLUSEQUAL value'

    #{ C.value = '+=' + value.value}
    value = subexpressions[2]

    if value["type"] != 'natural' and value["type"] != 'decimal' and value["type"] != 'string':
        raise SemanticException("No es un tipo valido para la operacion +=")

    subexpressions[0] = {"value": "+=" + value["value"]}


def p_c_decrement(subexpressions):
    'c : DECREMENT'

    #{ C.value = '--'}
    subexpressions[0] = {"value": "--"}

def p_c_minequal(subexpressions):
    'c : MINEQUAL value'

    #{ C.value = '-=' + value.value}

    if value["type"] != 'natural' and value["type"] != 'decimal' and value["type"] != 'string':
        raise SemanticException("No es un tipo valido para la operacion -=")

    value = subexpressions[2]
    subexpressions[0] = {"value": "-=" + value["value"]}



def p_condition_or(subexpressions):
    'condition : condition OR x'

    #{BOOLEAN_CONDITION.value = LOGICAL_CONDITION + H.value}
    condition1 = subexpressions[1]
    x = subexpressions[3]

    subexpressions[0] = {"value": condition1["value"] + " or " + x["value"]}


def p_condition_x(subexpressions):
    'condition : x'


    #{BOOLEAN_CONDITION.value = LOGICAL_CONDITION + H.value}
    x = subexpressions[1]

    subexpressions[0] = {"value": x["value"]}


def p_y_and(subexpressions):
    'x : x AND y'

    #{ H.value = 'and' + BOOLEAN_CONDITION.value}

    x = subexpressions[1]
    y = subexpressions[3]

    subexpressions[0] = {"value": x["value"] + " and " + y["value"]}

def p_x_y(subexpressions):
    'x : y'

    #{ H.value = 'and' + BOOLEAN_CONDITION.value}

    y = subexpressions[1]

    subexpressions[0] = {"value": y["value"]}



def p_y_not(subexpressions):
    'y : NOT y'

    #{ H.value = 'or' + BOOLEAN_CONDITION.value}
    y = subexpressions[2]


    subexpressions[0] = {"value": " not " + y["value"]}


def p_y_parent(subexpressions):
    'y : LPAREN y RPAREN'

    #{ H.value = 'or' + BOOLEAN_CONDITION.value}
    y = subexpressions[2]

    subexpressions[0] = {"value": " ( " + y["value"] + " ) "}


def p_y_logical_condition(subexpressions):
    'y : logical_condition'
    #{H.value = ''}
    logical_condition = subexpressions[1]

    subexpressions[0] = {"value": logical_condition["value"]}

def p_y_bool(subexpressions):
    'y : bool'
    #{H.value = ''}
    bool = subexpressions[1]

    subexpressions[0] = {"value": bool["value"]}


def p_logical_condition(subexpressions):
    'logical_condition : ecomparable i'

    #{ LOGICAL_CONDITION.value = E.value + I.value}
    ecomparable = subexpressions[1]
    i = subexpressions[2]

    subexpressions[0] = {"value": ecomparable["value"] + i["value"]}

def p_logical_condition_less(subexpressions):
    'i : LESS ecomparable'

    #{ I.value = '<' + E.value }
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " <" + ecomparable["value"]}


def p_logical_condition_greater(subexpressions):
    'i : GREATER ecomparable'

    #{ I.value = '>' + E.value }
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " > " + ecomparable["value"]}


def p_logical_condition_equal(subexpressions):
    'i : EQUAL ecomparable'

    #{ I.value = '==' + E.value}
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " == " +  ecomparable["value"]}


def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL ecomparable'

    #{ I.value = '!=' + E.value}
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " != " +  ecomparable["value"]}


def p_value_string(subexpressions):
    'value : STRING'

    #{value.value = string.value, value.type = 'string'}
    string = subexpressions[1]

    subexpressions[0] = {"value": string, "type": "string"}


def p_value_bool(subexpressions):
    'value : bool'

    #{value.value = bool.value, value.type = 'bool'}
    bool1 = subexpressions[1]

    subexpressions[0] = {"value":  bool1["value"], "type": "bool"}



def p_value_num(subexpressions):
    'value : num'

    #{value.value = NUM.value , value.type = NUM.type}
    num = subexpressions[1]

    subexpressions[0] = {"value": num["value"], "type": num["type"]}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    #{value.value = FUNCTION_WITH_RETURN.value, value.type = FUNCTION_WITH_RETURN.type}
    function_with_return = subexpressions[1]

    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}


def p_value_list_values(subexpressions):
    'value : LBRACKET value list_values RBRACKET'

    #{value1.value = '[ ' + value2.value + LIST_valueS.value + ']', LIST_valueS.type = IF(value2.type == 'natural','decimal',value2.type), value1.type = value2.type}
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
    #{value.value = '{' + LIST_REGISTERS.value + '}', value.type = 'register'}
    list_registers = subexpressions[1]

    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": "register"}

def p_value_var_array(subexpressions):
    'value : VAR j'

    #{value.value = var.value + J.value, value.type = IF(J.isArray, table.getType(var.value), var.type)}
    j = subexpressions[2]
    var = subexpressions[1]

    type = getType(var)

    subexpressions[0] = {"value":  var + j["value"], "type": type}


def p_j_array(subexpressions):
    'j : LBRACKET expression RBRACKET'

    #{J.value = '[' + NUM.value + ']', J.isArray = true }
    expression = subexpressions[2]

    if expression["type"] != 'natural':
        raise SemanticException("El valor para acceder a un array debe ser natural")

    subexpressions[0] = {"value": "[" + expression["value"] + "]", "isArray": True}


def p_j_lambda(subexpressions):
    'j : '

    #{J.value = '', J.isArray = false}
    subexpressions[0] = {"value": "", "isArray": False}


def p_list_registers(subexpressions):
    'list_registers : assignation l'

    #{LIST_REGISTERS.value = ASSIGNATION.value + L.value}
    assignation = subexpressions[1]
    l = subexpressions[2]

    subexpressions[0] = {"value": assignation["value"] + l["value"]}


def p_l_list_registers(subexpressions):
    'l : COMMA list_registers'

    #{L.value = ',' + LIST REGISTERS.value}
    list_registers = subexpressions[1]

    subexpressions[0] = {"value": ", " + list_registers["value"]}



#aca habria que agregar en la tabla que cambia el tipo de la lista no?

def p_list_values_comma(subexpressions):
    'list_values : COMMA value list_values'

    #{LIST_valueS1 .value = ',' + value.value + LIST_valueS2.value, LIST_valueS1.type = LIST_valueS2.type, COND(LIST_valueS2.type == IF(value.type == 'natural','decimal',value.type))}
    value = subexpressions[2]
    list_values2 = subexpressions[3]

    if(value["type"] == 'natural'):
        value["type"] == 'decimal'

    if ( list_values2["value"] != "" and list_values2["type"] != value["type"]) :
        raise SemanticException("El tipo del valor no coincide con el tipo de la lista")

    subexpressions[0] = {"value": "," + value["value"] + list_values2["value"], "type": value["type"]}



def p_list_values_lambda(subexpressions):
    'list_values : '

    #{LIST valueS.value = ''}
    subexpressions[0] = {"value": ""}


def p_l_lambda(subexpressions):
    'l : '
    #{LIST REGISTERS.value = '' }
    subexpressions[0] = {"value": ""}


def p_expression_arithmetic_expression(subexpressions):
    'expression : arithmetic_expression'

    #{EXPRESSION.value = ARITHMETIC_EXPRESSION.value, EXPRESSION.type = ARITHMETIC_EXPRESSION.type }
    arithmetic_expression = subexpressions[1]

    subexpressions[0] = {"value": arithmetic_expression["value"], "type": "decimal"}


#modificado el nombre de expression_string a string_expression
def p_expression_string_exp(subexpressions):
    'expression : string_expression'

    #{EXPRESSION.value = STRING_EXPRESSION.value, EXPRESSION.type = 'string' }
    string_expression = subexpressions[1]

    subexpressions[0] = {"value": string_expression["value"], "type": string_expression["type"]}

def p_expression_value(subexpressions):
    'expression : value'

    #{EXPRESSION.value = value.value, EXPRESSION.type = value.type }
    value = subexpressions[1]

    subexpressions[0] = {"value": value["value"], "type": value["type"]}

def p_string_expression_exp_string(subexpressions):
    'string_expression : string_expression w'

    #{STRING1_EXPRESSION.value = STRING2_EXPRESSION.value + w}
    string_expression = subexpressions[1]
    w =  subexpressions[2]

    subexpressions[0] = {"value": string_expression["value"] + w["value"]}

#agregada porque tenia recursion infinita
def p_string_expression_lambda(subexpressions):
    'string_expression : '

    #{W.value =  ''}
    subexpressions[0] = {"value": ""}

#agregada porque tenia recursion infinita
def p_w_lambda(subexpressions):
    'w : '

    #{W.value =  ''}
    subexpressions[0] = {"value": ""}

def p_w_string(subexpressions):
    'w  : PLUS STRING'

    #{W.value =  '+' + string.value}
    subexpressions[0] = {"value": "+" + string}


def p_arithmetic_expression_plus(subexpressions):
    'arithmetic_expression : arithmetic_expression PLUS term'

    #{ARITHMETIC_EXPRESSION1.value = ARITHMETIC_EXPRESSION 2.value + '+' + TERM.value, ARITHMETIC_EXPRESSION2.type = TERM.type}
    arithmetic_expression = subexpressions[1]
    term  = subexpressions[3]

    subexpressions[0] = {"value": arithmetic_expression["value"] + " + " + term["value"]}
    subexpressions[1] = {"type": term["type"]}

def p_arithmetic_expression_minus(subexpressions):
    'arithmetic_expression : arithmetic_expression MINUS term'

    #{ARITHMETIC_EXPRESSION1.value = ARITHMETIC_EXPRESSION2.value + '-' + TERM.value, ARITHMETIC_EXPRESSION1.type = TERM.type}
    arithmetic_expression = subexpressions[1]
    term  = subexpressions[3]

    subexpressions[0] = {"value": arithmetic_expression["value"] + " - " + term["value"]}
    subexpressions[1] = {"type": term["type"]}


def p_arithmetic_expression_term(subexpressions):
    'arithmetic_expression : term'

    #{ARITHMETIC_EXPRESSION.value = TERM.value, ARITHMETIC_EXPRESSION.type = TERM.type}
    term = subexpressions[1]

    subexpressions[0] = {"value": term["value"], "type": term["type"]}


def p_term_times(subexpressions):
    'term : term TIMES factor'
    #{TERM.value = TERM1.value +'*'+FACTOR.value, TERM.type=FACTOR.type }
    term = subexpressions[1]
    factor = subexpressions[3]

    subexpressions[0] = {"value": term["value"] + " * " + factor["value"], "type": factor["type"]}

def p_term_divide(subexpressions):
    'term : term DIVIDE factor'
    #{TERM.value = TERM1.value + '/' + FACTOR.value, TERM.type = FACTOR.type}
    term = subexpressions[1]
    factor = subexpressions[3]

    subexpressions[0] = {"value": term["value"] + " / " + factor["value"], "type": factor["type"]}

def p_term_module(subexpressions):
    'term : term MODULE factor'
    #{TERM.value = TERM1.value + '%' + FACTOR.value, TERM.type = FACTOR.type}
    term = subexpressions[1]
    factor = subexpressions[3]

    subexpressions[0] = {"value": term["value"] + " % " + factor["value"], "type": factor["type"]}


def p_term_factor(subexpressions):
    'term : factor'

    #{TERM.value = FACTOR.value, TERM.type = FACTOR.type}
    factor = subexpressions[1]
    subexpressions[0] = {"value": factor["value"], "type": factor["type"]}


def p_factor_value(subexpressions):
    'factor : value'
    #{FACTOR.value = NUM.value, FACTOR.type = 'decimal'}
    value = subexpressions[1]

    if value["type"] != 'natural' and value["type"] != 'decimal':
        raise SemanticException("No puede hacer operaciones con tipos que no son numericos")

    subexpressions[0] = {"value": value["value"], "type": value["type"]}


def p_func_func_wr(subexpressions):
    'function : function_with_return'
    function_with_return = subexpressions[1]

    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"] }

def p_func_print(subexpressions):
    'function : PRINT LPAREN expression RPAREN'
    expression = subexpressions[3]
    subexpressions[0] = {"value": "(" + expression["value"] + ")"}

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'
    subexpressions[0] = subexpressions[1]


def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN STRING RPAREN'
    texto = subexpressions[3]
    subexpressions[0]["value"] = "capitalizar( " + texto["value"] + " )"
    subexpressions[0]["Type"] = "string"
    #faltan cosas

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN VAR COMMA VAR  RPAREN'
    var1 = subexpressions[3]
    var2 = subexpressions[5]
    subexpressions[0]["value"] = "colineales( " + var1["value"] + ", " + var2["value"] + " )"
    #faltan cosas

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN param_length  RPAREN'
    fwr  = subexpressions[0]
    pl = subexpressions[3]

    subexpressions[0] = {"value": "length( " + pl["value"] + " )", "type": "natural"}
    #faltan cosas

def p_param_me_var(subexpressions):
    'param_me : VAR COMMA num n'
    param_me = subexpressions[0]
    var = subexpressions[1]
    comma = subexpressions[2]
    num = subexpressions[3]
    n = subexpressions[4]
    param_me["value"] = var["value"] + "," + num["value"] + n["value"]
    table_var_type = table.getType(var["value"])
    assert( table_var_type == "natural" or table_var_type == "decimal" )
    assert( table.isArray(var["value"]))
    if table_var_type == "decimal" and n["isTrue"] :
        param_me["Type"] = "decimal"
    else:
        param_me["Type"] = table_var_type
    subexpressions[0] = param_me



def p_n_bool(subexpressions):
    'n : COMMA bool'
    n = subexpressions[0]
    booleano = subexpressions[2]
    n["value"] = ", " + booleano["value"]
    n["isTrue"] = booleano["value"] == "true"
    subexpressions[0] = n

def p_n_lambda(subexpressions):
    'n : '
    subexpressions[0] = {"value": "", "isTrue": false}

def p_param_l_var(subexpressions):
    'param_length : VAR '
    var = subexpressions[1]
    assert( isArray(var) or getType(var) == "string")
    subexpressions[0] = {"value": var}

def p_param_l_vector(subexpressions):
    'param_length : LBRACKET value list_values RBRACKET '
    val = subexpressions[2]
    list_val = subexpressions[3]
    res =  subexpressions[0]
    res["value"] = "["+ val["value"] + list_val["value"] + "]"
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
    subexpressions[0] = {"value": str(dec), "type": "decimal"}

#ojo cambiada
def p_num_natural(subexpressions):
    'num : NATURAL'
    nat = subexpressions[1]
    subexpressions[0] = {"value": str(nat), "type": "natural"}

def p_bool_true(subexpressions):
    'bool : TRUE '
    subexpressions[0] = {"value": "true"}

def p_bool_false(subexpressions):
    'bool : FALSE '
    subexpressions[0] = {"value": "false"}

def p_error(subexpressions):
    print subexpressions
    raise Exception("Syntax error.")
