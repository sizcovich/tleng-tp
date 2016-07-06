from lexer_rules import tokens
import pdb;

#from expressions import Addition, Multiplication, Number

class SemanticException(Exception):
    pass


#funciones a definir:
#indent
#insertOrUpdate
#table(var.value)
#table.isArray(var.value):
#table.getType(var.value)
#multiplo(term, factor)

table = {}

def multiplo(a, b):
    res = False
    for x in range(1, int(b)):
        if (int(b) == int(a) * x):
            res = True

    return res

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

def p_sentence_return(subexpressions):
    'sentence : RETURN expression'

    #{SENTENCE.value = 'return' + E.value + ';'}
    exp = subexpressions[2]

    subexpressions[0] = {"value": "return " + exp["value"] + "; "}


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
    subexpressions[0] = {"value": expression["value"], "type": expression["type"], "isArray": expression["isArray"]}


def p_ecomparable_condition(subexpressions):
    'ecomparable : condition'

    #{ECOMPARABLE.value = CONDITION.value}
    condition = subexpressions[1]
    subexpressions[0] = {"value": condition["value"], "type": condition["type"], "isArray": False}


def p_ecomparable_conditional(subexpressions):
    'ecomparable : conditional'

    #{ECOMPARABLE.value = CONDITIONAL.value}
    conditional = subexpressions[1]

    subexpressions[0] = {"value": conditional["value"], "type": conditional["type"], "isArray": False}


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
    'if_else : if possibleelse'

    #{IF_ELSE.value = IF.value + 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if1 = subexpressions[1]
    possibleelse = subexpressions[2]

    subexpressions[0] = {"value": if1["value"] + possibleelse["value"]}


def p_possibleelse_else(subexpressions):
    'possibleelse : ELSE possiblecomment possiblenewline keys'

    #{IF_ELSE.value = IF.value + 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    possiblecomment = subexpressions[2]
    keys = subexpressions[4]

    subexpressions[0] = {"value":  " else " + possiblecomment["value"] + "\n" + keys["value"]}

def p_possibleelse_lambda(subexpressions):
    'possibleelse : '

    #{IF_ELSE.value = IF.value + 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}

    subexpressions[0] = {"value":  ""}

def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN possiblecomment possiblenewline keys'


    #{IF.value = 'if (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    if1 = subexpressions[0]
    condition = subexpressions[3]
    possiblecomment = subexpressions[5]
    keys = subexpressions[7]

    subexpressions[0] = {"value": "if(" + condition["value"] + ")" + possiblecomment["value"] + "\n" + keys["value"]}


def p_conditional_paren(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK expression COLON expression'

    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + EXPRESSION1.value + ':' + EXPRESSION2.value}
    condition = subexpressions[2]
    expression1 = subexpressions[5]
    expression2 = subexpressions[7]

    subexpressions[0] = {"value": "(" + condition["value"] + ")?" + expression1["value"] + ":" + expression2["value"], "type": expression1["type"]}

def p_conditional(subexpressions):
    'conditional : condition QUESTIONMARK expression COLON expression'

    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + EXPRESSION1.value + ':' + EXPRESSION2.value}
    condition = subexpressions[1]
    expression1 = subexpressions[3]
    expression2 = subexpressions[5]

    subexpressions[0] = {"value": condition["value"] + "?" + expression1["value"] + ":" + expression2["value"], "type": expression1["type"]}



def p_for(subexpressions):
    'for : FOR LPAREN assignationorlambda SEMICOLON condition SEMICOLON advancefor RPAREN possiblecomment possiblenewline keys'

    #{FOR.value ='for (' + ASSIGNATIONORLAMBDA.value + ';' + CONDITION.value + ';' + ADVANCE.value ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}

    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advancefor = subexpressions[7]
    possiblecomment = subexpressions[9]
    keys = subexpressions[11]

    subexpressions[0] = {"value": "for(" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advancefor["value"]+ ")" + possiblecomment["value"] + "\n" + keys["value"]}


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
    'keys : comment_list sentence possiblenewline'

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
    b_type = expression2["type"]

    subexpressions[0] = {"value": "[" +  expression1["value"] + "] = " +  expression2["value"], "type": b_type, "isArray": True}


def p_b_expression(subexpressions):
    'b : ASSIGN ecomparable'

    #{B.value = '=' + EXPRESSION.value, B.type = EXPRESSION.type, B.isArray = false}
    ecomparable =  subexpressions[2]
    subexpressions[0] = {"value": "= " + ecomparable["value"] , "type": ecomparable["type"], "isArray": ecomparable["isArray"]}



def p_advancefor_advance(subexpressions):
    'advancefor : advance'

    advance = subexpressions[1]
    subexpressions[0] = {"value":  advance["value"]}

def p_advancefor_assignationorlambda(subexpressions):
    'advancefor : assignationorlambda'

    assignationorlambda = subexpressions[1]
    subexpressions[0] = {"value": assignationorlambda["value"]}

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
    if (condition1["type"] != "bool") or (x["type"]!="bool"):
        raise SemanticException("Solo puede operar con booleanos")

    subexpressions[0] = {"value": condition1["value"] + " or " + x["value"], "type": "bool"}


def p_condition_x(subexpressions):
    'condition : x'

    #{BOOLEAN_CONDITION.value = LOGICAL_CONDITION + H.value}
    x = subexpressions[1]
    subexpressions[0] = {"value": x["value"], "type": x["type"]}


def p_y_and(subexpressions):
    'x : x AND y'

    #{ H.value = 'and' + BOOLEAN_CONDITION.value}
    x = subexpressions[1]
    y = subexpressions[3]
    if (x["type"] != "bool" or y["type"]!= "bool"):
        raise SemanticException("Solo puede operar con booleanos")
    subexpressions[0] = {"value": x["value"] + " and " + y["value"], "type": x["type"]}

def p_x_y(subexpressions):
    'x : y'

    #{ H.value = 'and' + BOOLEAN_CONDITION.value}

    y = subexpressions[1]

    subexpressions[0] = {"value": y["value"], "type": y["type"]}



def p_y_not(subexpressions):
    'y : NOT y'

    #{ H.value = 'or' + BOOLEAN_CONDITION.value}
    y = subexpressions[2]

    if  y["type"] != 'bool':
        raise SemanticException("Solo puede operar con booleanos")


    subexpressions[0] = {"value": " not " + y["value"], "type": y["type"]}


def p_y_parent(subexpressions):
    'y : LPAREN condition RPAREN'

    #{ H.value = 'or' + BOOLEAN_CONDITION.value}
    condition = subexpressions[2]

    subexpressions[0] = {"value": " ( " + condition["value"] + " ) ", "type": condition["type"]}


def p_y_logical_condition(subexpressions):
    'y : logical_condition'
    #{H.value = ''}
    logical_condition = subexpressions[1]

    subexpressions[0] = {"value": logical_condition["value"], "type": logical_condition["type"]}

def p_y_value(subexpressions):
    'y : value'
    #{H.value = ''}
    value = subexpressions[1]

    subexpressions[0] = {"value": value["value"], "type": value["type"] }


def p_logical_condition(subexpressions):
    'logical_condition : ecomparable i'

    #{ LOGICAL_CONDITION.value = E.value + I.value}
    ecomparable = subexpressions[1]
    i = subexpressions[2]

    subexpressions[0] = {"value": ecomparable["value"] + i["value"], "type": "bool"}

def p_logical_condition_less(subexpressions):
    'i : LESS possibleparen'

    #{ I.value = '<' + E.value }
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " < " + ecomparable["value"], "type": "bool"}


def p_logical_condition_greater(subexpressions):
    'i : GREATER possibleparen'
    #{ I.value = '>' + E.value }
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": " > " + ecomparable["value"], "type": "bool"}


def p_logical_condition_equal(subexpressions):
    'i : EQUAL possibleparen'

    #{ I.value = '==' + E.value}
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " == " +  ecomparable["value"], "type": "bool"}



def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL possibleparen'

    #{ I.value = '!=' + E.value}
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": " != " +  ecomparable["value"], "type": "bool"}


def p_possibleparen_paren(subexpressions):
    'possibleparen : LPAREN ecomparable RPAREN'

    #{ I.value = '==' + E.value}
    ecomparable = subexpressions[2]

    subexpressions[0] = {"value": "(" +  ecomparable["value"] + ")", "type": "bool"}

def p_possibleparen_ecomparable(subexpressions):
    'possibleparen : ecomparable'

    #{ I.value = '==' + E.value}
    ecomparable = subexpressions[1]

    subexpressions[0] = {"value": ecomparable["value"], "type": "bool"}





def p_value_string(subexpressions):
    'value : STRING'

    #{value.value = string.value, value.type = 'string'}
    string = subexpressions[1]

    subexpressions[0] = {"value": string, "type": "string", "isArray": False}


def p_value_bool(subexpressions):
    'value : bool'

    #{value.value = bool.value, value.type = 'bool'}
    bool1 = subexpressions[1]

    subexpressions[0] = {"value":  bool1["value"], "type": "bool", "isArray": False}



def p_value_num(subexpressions):
    'value : num'

    #{value.value = NUM.value , value.type = NUM.type}
    num = subexpressions[1]


    subexpressions[0] = {"value": num["value"], "type": num["type"], "isArray": False}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    #{value.value = FUNCTION_WITH_RETURN.value, value.type = FUNCTION_WITH_RETURN.type}
    function_with_return = subexpressions[1]

    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"], "isArray": function_with_return["isArray"]}


def p_value_list_values(subexpressions):
    'value : LBRACKET expression list_values RBRACKET'

    #{value1.value = '[ ' + value2.value + LIST_valueS.value + ']', LIST_valueS.type = IF(value2.type == 'natural','decimal',value2.type), value1.type = value2.type}
    value2 = subexpressions[2]
    list_values = subexpressions[3]



    if list_values["value"] == "":
        value1 = value2["type"]
    elif (value2["type"] == "natural" and list_values["type"] == "decimal"):
        value1 = "decimal"
    elif (value2["type"] == "decimal" and list_values["type"] == "natural"):
        value1 = "decimal"
    else:
        value1 = value2["type"]

    subexpressions[0] = {"value": "[" + value2["value"] + list_values["value"] + "]", "type": value1, "isArray": True}


#semantica corregida
def p_value_list_registers(subexpressions):
    'value : LKEY list_registers RKEY'
    #{value.value = '{' + LIST_REGISTERS.value + '}', value.type = 'register'}
    list_registers = subexpressions[1]

    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": "register", "isArray": True}

def p_value_var_array(subexpressions):
    'value : VAR j'

    #{value.value = var.value + J.value, value.type = IF(J.isArray, table.getType(var.value), var.type)}
    j = subexpressions[2]
    var = subexpressions[1]

    type = getType(var)

    subexpressions[0] = {"value":  var + j["value"], "type": type, "isArray": False}


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
    'list_values : COMMA expression list_values'

    #{LIST_valueS1 .value = ',' + value.value + LIST_valueS2.value, LIST_valueS1.type = LIST_valueS2.type, COND(LIST_valueS2.type == IF(value.type == 'natural','decimal',value.type))}
    value = subexpressions[2]
    list_values2 = subexpressions[3]

    if list_values2["value"] == "":
        value1 = value["type"]
    elif (value["type"] == "natural" and list_values2["type"] == "decimal"):
        value1 = "decimal"
    elif (value["type"] == "decimal" and list_values2["type"] == "natural"):
        value1 = "decimal"
    else:
        value1 = value["type"]

    if (list_values2["value"] != "" and list_values2["type"] != value["type"]) :
        raise SemanticException("El tipo del valor no coincide con el tipo de la lista")

    subexpressions[0] = {"value": "," + value["value"] + list_values2["value"], "type": value1}


def p_list_values_lambda(subexpressions):
    'list_values : '

    #{LIST valueS.value = ''}
    subexpressions[0] = {"value": ""}


def p_l_lambda(subexpressions):
    'l : '
    #{LIST REGISTERS.value = '' }
    subexpressions[0] = {"value": ""}



def p_expression_plus(subexpressions):
    'expression : expression PLUS term'

    #{ARITHMETIC_EXPRESSION1.value = ARITHMETIC_EXPRESSION 2.value + '+' + TERM.value, ARITHMETIC_EXPRESSION2.type = TERM.type}
    expression = subexpressions[1]
    term  = subexpressions[3]

    if not(((expression["type"] == 'natural' or expression["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')) or (expression["type"] == 'string' and term["type"] == 'string')):
        raise SemanticException("No puede utilizar el + si ambos tipos no son numericos o strings")

    type = 'string'
    if  expression["type"] == 'decimal' or term["type"] == 'decimal':
        type = 'decimal'
    else:
        if expression["type"] == 'natural' or term["type"] == 'natural':
            type = 'natural'

    subexpressions[0] = {"value": expression["value"] + " + " + term["value"], "type": type, "isArray": False}

def p_expression_minus(subexpressions):
    'expression : expression MINUS term'

    #{ARITHMETIC_EXPRESSION1.value = ARITHMETIC_EXPRESSION2.value + '-' + TERM.value, ARITHMETIC_EXPRESSION1.type = TERM.type}
    expression = subexpressions[1]
    term  = subexpressions[3]

    if not((expression["type"] == 'natural' or expression["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')):
        raise SemanticException("No puede restar tipos que no son numericos")


    type = 'natural'
    if  expression["type"] == 'decimal' or term["type"] == 'decimal':
        type = 'decimal'

    subexpressions[0] = {"value": expression["value"] + " - " + term["value"], "type": type, "isArray": False}


def p_expression_term(subexpressions):
    'expression : term'

    #{ARITHMETIC_EXPRESSION.value = TERM.value, ARITHMETIC_EXPRESSION.type = TERM.type}
    term = subexpressions[1]
    subexpressions[0] = {"value": term["value"], "type": term["type"], "isArray": term["isArray"]}



def p_pow_times(subexpressions):
    'term : term POW factor'
    #{TERM.value = TERM1.value +'*'+FACTOR.value, TERM.type=FACTOR.type }
    term = subexpressions[1]
    value = subexpressions[3]

    if not((value["type"] == 'natural' or value["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')):
        raise SemanticException("No puede multiplicar tipos que no son numericos")

    type = 'natural'
    if  value["type"] == 'decimal' or term["type"] == 'decimal':
        type = 'decimal'


    subexpressions[0] = {"value": term["value"] + " * " + value["value"], "type": type, "isArray": False}

def p_term_times(subexpressions):
    'term : term TIMES factor'
    #{TERM.value = TERM1.value +'*'+FACTOR.value, TERM.type=FACTOR.type }
    term = subexpressions[1]
    value = subexpressions[3]

    if not((value["type"] == 'natural' or value["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')):
        raise SemanticException("No puede multiplicar tipos que no son numericos")

    type = 'natural'
    if  value["type"] == 'decimal' or term["type"] == 'decimal':
        type = 'decimal'


    subexpressions[0] = {"value": term["value"] + " * " + value["value"], "type": type, "isArray": False}

def p_term_divide(subexpressions):
    'term : term DIVIDE factor'
    #{TERM.value = TERM1.value + '/' + FACTOR.value, TERM.type = FACTOR.type}
    term = subexpressions[1]
    value = subexpressions[3]

    if(value["value"] == 0):
        raise SemanticException("No puede dividir por cero")

    if not((value["type"] == 'natural' or value["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')):
        raise SemanticException("No puede dividir tipos que no son numericos")

    type = 'decimal'
    #if  value["type"] == 'natural' and term["type"] == 'natural' and multiplo(term["value"], value["value"]):
    #    type = 'natural'

    subexpressions[0] = {"value": term["value"] + " / " + value["value"], "type": type, "isArray": False}

def p_term_module(subexpressions):
    'term : term MODULE factor'
    #{TERM.value = TERM1.value + '%' + FACTOR.value, TERM.type = FACTOR.type}
    term = subexpressions[1]
    value = subexpressions[3]

    #el value debe ser natural y el termino un numero
    if not(value["type"] == 'natural' and (term["type"] == 'natural' or term["type"] == 'decimal')):
        raise SemanticException("No puede hacer operaciones con tipos que no son numericos")

    type = 'natural'
    if term["type"] == 'decimal':
        type = 'decimal'

    subexpressions[0] = {"value": term["value"] + " % " + value["value"], "type": type, "isArray": False}


def p_factor_paren(subexpressions):
    'factor : LPAREN expression RPAREN'

    #{ARITHMETIC_EXPRESSION.value = TERM.value, ARITHMETIC_EXPRESSION.type = TERM.type}
    term = subexpressions[2]
    subexpressions[0] = {"value": "(" + term["value"] + ")", "type": term["type"], "isArray": term["isArray"]}

def p_factor_value(subexpressions):
    'factor : value'

    #{ARITHMETIC_EXPRESSION.value = TERM.value, ARITHMETIC_EXPRESSION.type = TERM.type}
    value = subexpressions[1]
    subexpressions[0] = {"value":  value["value"] , "type": value["type"], "isArray": value["isArray"]}



def p_term_value(subexpressions):
    'term : factor'

    #{TERM.value = FACTOR.value, TERM.type = FACTOR.type}
    value = subexpressions[1]
    subexpressions[0] = {"value": value["value"], "type": value["type"], "isArray": value["isArray"]}


def p_func_func_wr(subexpressions):
    'function : function_with_return'
    function_with_return = subexpressions[1]

    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}

def p_func_print(subexpressions):
    'function : PRINT LPAREN ecomparable RPAREN'
    expression = subexpressions[3]
    subexpressions[0] = {"value": "(" + expression["value"] + ")"}

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'
    param_me = subexpressions[3]
    subexpressions[0] = {"value":"multiplicacionEscalar("+ param_me["value"] + ")", "type": param_me["type"], "isArray": False}

def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN ecomparable RPAREN'
    ecomp = subexpressions[3]
    if not(ecomp["type"] == "string"):
        raise SemanticException("Capitalizar recibe solo strings")
    subexpressions[0] = {"value": "capitalizar( " + ecomp["value"] + " )", "type": "string", "isArray": False}

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN VAR COMMA VAR  RPAREN'
    var1 = subexpressions[3]
    var2 = subexpressions[5]
    subexpressions[0] = {"value": "colineales( " + var1 + ", " + var2 + " )", "type": "bool", "isArray": False}

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN param_length RPAREN'
    pl = subexpressions[3]
    subexpressions[0] = {"value": "length( " + pl["value"] + " )", "type": "natural", "isArray": pl["isArray"]}

def p_param_me_var(subexpressions):
    'param_me : VAR COMMA value n'
    var1 = subexpressions[1]
    comma = subexpressions[2]
    var2 = subexpressions[3]
    n = subexpressions[4]

    if not(var2["type"] == "natural" or var2["type"] == "decimal"):
        raise SemanticException("El tercer parametro de multiplicacionEscalar debe ser un numero")

    table_var1_type = getType(var1)
    if not((table_var1_type == "natural" or table_var1_type == "decimal") and (isArray(var1)) ):
        raise SemanticException("El primer parametro de multiplicacionEscalar debe ser un numero")

    if table_var1_type == "decimal" and n["isTrue"] :
        typ = "decimal"
    else:
        typ = table_var1_type

    subexpressions[0] = {"value": var1 + "," + var2["value"] + n["value"], "type": typ}

def p_n_bool(subexpressions):
    'n : COMMA bool'
    booleano = subexpressions[2]

    subexpressions[0] = {"value": ", " + booleano["value"], "isTrue":booleano["value"] == "true"}

def p_n_lambda(subexpressions):
    'n : '
    subexpressions[0] = {"value": "", "isTrue": False}

def p_param_l_var(subexpressions):
    'param_length : VAR '
    var = subexpressions[1]
    assert(isArray(var) or getType(var) == "string")
    subexpressions[0] = {"value": var, "isArray": False}

def p_param_l_fwr(subexpressions):
    'param_length : function_with_return '
    func = subexpressions[1]
    if not(func["type"] == "string"):
        raise SemanticException("Length recibe funciones a string o a arreglos")
    subexpressions[0] = {"value": func["value"], "type": func["type"], "isArray": func["isArray"]}

def p_param_l_vector(subexpressions):
    'param_length : LBRACKET value list_values RBRACKET '
    val = subexpressions[2]
    list_val = subexpressions[3]
    res =  subexpressions[0]
    res["value"] = "["+ val["value"] + list_val["value"] + "]"

    if list_val["value"] == "":
        res["type"] = value["type"]
    elif (val["type"] == "natural" and list_val["type"] == "decimal"):
        res["type"] = "decimal"
    elif (val["type"] == "decimal" and list_val["type"] == "natural"):
        res["type"] = "decimal"
    else:
        res["type"] = value["type"]

    res["isArray"] = True
    subexpressions[0] = res

def p_param_l_string(subexpressions):
    'param_length : STRING '
    subexpressions[0] = {"value": subexpressions[1], "type": "string", "isArray": False}


def p_num_decimal(subexpressions):
    'num : DECIMAL '
    dec = subexpressions[1]
    subexpressions[0] = {"value": str(dec), "type": "decimal"}

def p_num_natural(subexpressions):
    'num : NATURAL'
    nat = subexpressions[1]
    subexpressions[0] = {"value": str(nat), "type": "natural"}

def p_bool_true(subexpressions):
    'bool : TRUE '
    subexpressions[0] = {"value": "true", "type":"bool"}

def p_bool_false(subexpressions):
    'bool : FALSE '
    subexpressions[0] = {"value": "false", "type":"bool"}

def p_error(subexpressions):
    print subexpressions
    raise Exception("Syntax error.")

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
