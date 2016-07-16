from lexer_rules import tokens
import pdb;

class SemanticException(Exception):
    pass

table = {}

def isBoolean(expresion, isTerminal):

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]
        esArray =  expresion["isArray"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos[0]
        esArray =  datos[1]

    res = False
    if (tipo == 'bool'):
        res = True

    return res

def isString(expresion, isTerminal):

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]
        esArray =  expresion["isArray"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos[0]
        esArray =  datos[1]

    res = False
    if (tipo == 'string'):
        res = True

    return res


def isNumerical(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]
        esArray =  expresion["isArray"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos[0]
        esArray =  datos[1]

    res = False

    if (tipo == 'natural' or tipo == 'decimal' or tipo == 'negativo'):
        res = True

    return res

def indent( texto ):
	#agrega la indentacion necesaria
    arregloDeLineas = texto.splitlines(True)
    res = ""
    for line in arregloDeLineas:
        res = res + "\t" + line
    return res


def multiplo(a, b):
    res = False
    for x in range(1, int(b)):
        if (int(b) == int(a) * x):
            res = True
    return res


def insertOrUpdate(name, type, isArray):
	#inserta o actualiza la tabla
    datos = (type, isArray)
    table[name] = datos

def isArray(expresion, isTerminal):
	#devuelve si una expression es array o no: si esta definida en la tabla devuelve esos datos, sino devuelve los datos que vienen por parametro
    esArray  = False
    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]
        esArray =  expresion["isArray"]

    if (table.get(name) != None):
        datos =table[name]
        esArray = datos[1]

    return esArray

def getType(expresion, isTerminal):
    #obtiene el tipo de una variable: si esta definida en la tabla devuelve esos datos, sino devuelve los datos que vienen por parametro
    #es necesario que sepa si expression es terminal o no

    #print expresion

    tipo = ""
    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]
        esArray =  expresion["isArray"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos[0]

    return tipo


def p_program(subexpressions):
    'program : list_sentencies'
    #{PROGRAM.value = LIST_SENTENCIES.value, print(LIST_SENTENCIES.value)}
    list_sentencies = subexpressions[1]
    subexpressions[0] = {"value": list_sentencies["value"]}

def p_list_sentencies_comment(subexpressions):
    'list_sentencies : COMMENT a'
    #{LIST_SENTENCIES.value= comment.value + '\n' + A.value, LIST_SENTENCIES.element = 'comment'}
    comment = subexpressions[1]
    a = subexpressions[2]
    subexpressions[0] = {"value": comment["value"] + "\n" + a["value"], "element": "comment", "line": comment["line"]}

def p_list_sentencies_sentence(subexpressions):
    'list_sentencies : sentence a'
    #{LIST_SENTENCIES.value= SENTENCE.value + IF(a.element!='comment', '\n') + A.value, LIST_SENTENCIES.element = 'sentence'}
    sentence = subexpressions[1]
    a = subexpressions[2]
    list_sentencies_value = sentence["value"]
    if (a["element"] != "comment"):
        list_sentencies_value = list_sentencies_value + "\n"
    else:
        if sentence["value"][0].upper() == 'D' and sentence["value"][1].upper() == 'O' and sentence["line"] == a["line"]:
            list_sentencies_value = list_sentencies_value
        else:
            list_sentencies_value = list_sentencies_value + "\n"
    list_sentencies_value = list_sentencies_value + a["value"]
    subexpressions[0] = {"value": list_sentencies_value, "element": "sentence"}

def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'
    #{A.value = LIST_SENTENCIES.value, A.element = LIST_SENTENCIES.element}
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
    'sentence : WHILE LPAREN expression RPAREN keys'
    #{SENTENCE.value = WHILE.value}
    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "while(" + condition["value"] + ")" + new}

def p_sentence_if_else(subexpressions):
    'sentence : IF LPAREN expression RPAREN keys possibleelse'
    #{SENTENCE.value = 'if (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value + POSSIBLEELSE.value}
    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    newline = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        newline = "\n"
    new = newline + keys["value"]
    possibleelse = subexpressions[6]
    subexpressions[0] = {"value": "if(" + condition["value"] + ")" + new + possibleelse["value"]}





def p_sentence_for(subexpressions):
    'sentence : FOR LPAREN assignationorlambda SEMICOLON expression SEMICOLON advancefor RPAREN keys'
    #{SENTENCE.value = FOR.value}
    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advancefor = subexpressions[7]
    keys = subexpressions[9]
    lastElement = subexpressions[8]
    lastElementLine = lastElement["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "for(" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advancefor["value"]+ ")" + new}

def p_sentence_do_while(subexpressions):
    'sentence : DO keys_do WHILE LPAREN expression RPAREN SEMICOLON'
    #{SENTENCE.value = DO_WHILE.value}
    keysdo = subexpressions[2]
    condition = subexpressions[5]
    subexpressions[0] = {"value": "do \n" + keysdo["value"] + "while(" + condition["value"] + ");", "line": subexpressions[7]["line"]}

def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON'
    #{SENTENCE.value = FUNCTION.value + ';'}
    function = subexpressions[1]
    subexpressions[0] = {"value": function["value"] + ";"}

def p_sentence_return(subexpressions):
    'sentence : RETURN expression'
    #{SENTENCE.value = 'return' + E.value + ';'}
    exp = subexpressions[2]
    subexpressions[0] = {"value": "return " + exp["value"] + ";"}

def p_possibleelse_else(subexpressions):
    'possibleelse : ELSE keys'
    #{POSSIBLEELSE.value = 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    keys = subexpressions[2]
    lastElementLine = subexpressions[1]["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": " else " + new}

def p_possibleelse_lambda(subexpressions):
    'possibleelse : '
    #{POSSIBLEELSE.value = ''}
    subexpressions[0] = {"value": ""}

def p_e_advance(subexpressions):
    'e : advance'
    #{E.value = ADVANCE.value}
    advance = subexpressions[1]
    subexpressions[0] = {"value": advance["value"]}

def p_e_assignation(subexpressions):
    'e : assignation'
    #{E.value = ASSIGNATION.value}
    assignation = subexpressions[1]
    subexpressions[0] = {"value": assignation["value"]}

def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'
    #{COMMENT_LIST1.value = comment.value + '\n' + COMMENT_LIST2.value}
    comment = subexpressions[1]
    comment_list2 = subexpressions[2]
    subexpressions[0] = {"value": comment["value"] + "\n" + comment_list2["value"]}

def p_comment_list_lambda(subexpressions):
    'comment_list : '
    #{COMMENT LIST.value = ''}
    subexpressions[0] = {"value": ""}

def p_keys_do_append_sentence(subexpressions):
    'keys_do : comment_list sentence'
    #{KEYS_DO.value = indent(COMMENT_LIST.value) + SENTENCE.value}
    comment_list = subexpressions[1]
    sentence = subexpressions[2]
    subexpressions[0] = {"value":indent(comment_list["value"] +  sentence["value"])}

def p_keys_do_append_possiblecomment(subexpressions):
    'keys_do : LKEY list_sentencies RKEY'
    #{KEYS_DO.value = '{' + POSSIBLECOMMENT.value + '\n' + LIST_SENTENCIES.value + '}'}
    sentence = subexpressions[2]
    text = sentence["value"]
    if (sentence["element"] != "comment"):
        text = "\n" + text
    else:
        if sentence["line"] != subexpressions[1]["line"]:
            text = "\n" + text
    subexpressions[0] = {"value": "{ " + indent(text) + "} "}

def p_keys_append_sentence(subexpressions):
    'keys : comment_list sentence'
    #{ KEYS.value = indent(COMMENT_LIST.value) + SENTENCE.value}

    keys = subexpressions[0]
    comment_list = subexpressions[1]
    sentence = subexpressions[2]
    subexpressions[0] = {"value":indent(comment_list["value"] +  sentence["value"])}

def p_keys_append_possiblecomment(subexpressions):
    'keys : LKEY list_sentencies RKEY'
    #{KEYS.value = '{' + indent(POSSIBLECOMMENT.value) + '\n' + LIST_SENTENCIES.value + '}\n'}

    sentence = subexpressions[2]
    text = sentence["value"]


    if (sentence["element"] != "comment"):
        text = "\n" + text
    else:
        if sentence["line"] != subexpressions[1]["line"]:
            text = "\n" + text
    subexpressions[0] = {"value": "{ " + indent(text) + "}\n"}

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

    isTerminal = True
    b = subexpressions[2]
    var = subexpressions[1]
    if table.has_key(var["value"]) == True:
        if b["isArray"] == isArray(var, isTerminal):
            if isArray(var, isTerminal):
                if getType(var, isTerminal) != b["type"]:
                    raise SemanticException("No puede agregarle a un array un elemento de tipo distinto al tipo del array")


    insertOrUpdate(var["value"],b["type"], b["isArray"])

    subexpressions[0] = {"value": var["value"] + b["value"], "type": b["type"], "isArray": b["isArray"]}

def p_b_array(subexpressions):
    'b : LBRACKET expression RBRACKET ASSIGN expression'
    #{B.value = '[' + natural.value + '] = ' + EXPRESSION.value, B.type = IF(EXPRESSION.type == 'natural', 'decimal', EXPRESSION.type), B.isArray = true}
    expression1 = subexpressions[2]
    expression2 =  subexpressions[5]
    if expression1["type"] != "natural":
        raise SemanticException("El valor para acceder a un array debe ser natural")
    b_type = expression2["type"]
    subexpressions[0] = {"value": "[" +  expression1["value"] + "] = " +  expression2["value"], "type": b_type, "isArray": expression2["isArray"]}

def p_b_expression(subexpressions):
    'b : ASSIGN expression'
    #{B.value = '=' + ECOMPARABLE.value, B.type = ECOMPARABLE.type, B.isArray = ECOMPARABLE.isArray}
    ecomparable =  subexpressions[2]


    subexpressions[0] = {"value": "= " + ecomparable["value"] , "type": ecomparable["type"], "isArray": ecomparable["isArray"]}

def p_b_registers(subexpressions):
    'b : COLON expression'
    #{B.value = '=' + ECOMPARABLE.value, B.type = ECOMPARABLE.type, B.isArray = ECOMPARABLE.isArray}
    ecomparable =  subexpressions[2]
    subexpressions[0] = {"value": ": " + ecomparable["value"] , "type": ecomparable["type"], "isArray": ecomparable["isArray"]}

def p_advancefor_advance(subexpressions):
    'advancefor : advance'
    #{ADVANCEFOR.value = ADVANCE.value}
    advance = subexpressions[1]
    subexpressions[0] = {"value":  advance["value"]}

def p_advancefor_assignationorlambda(subexpressions):
    'advancefor : assignationorlambda'
	#{ADVANCEFOR.value = ASSIGNATIONORLAMBDA.value}
    assignationorlambda = subexpressions[1]
    subexpressions[0] = {"value": assignationorlambda["value"]}

def p_advance_var_c(subexpressions):
    'advance : VAR c'
    #{COND(table.getType(var.value) == 'natural' || table.getType(var.value)  == 'decimal' || table.getType(var.value)  == 'string'), ADVANCE.value = var.value + C.value}
    var = subexpressions[1]
    c = subexpressions[2]
    isTerminal = True

    if not isNumerical(var, isTerminal) :
        raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  var["value"] + c["value"]}

def p_advance_d_var(subexpressions):
    'advance : d VAR'
    #{COND(table.getType(var.value) == 'natural' || table.getType(var.value)  == 'decimal' || table.getType(var.value)  == 'string'), ADVANCE.value = var.value + C.value}
    d = subexpressions[1]
    var = subexpressions[2]
    isTerminal = True
    if (not(getType(var, isTerminal) == "natural" or getType(var, isTerminal) == "decimal" or getType(var, isTerminal) == "string")) :
        raise SemanticException("El tipo a avanzar no es un numero")
    subexpressions[0] = {"value":  d["value"] + var["value"]}

def p_c_d(subexpressions):
    'c : d'
    d = subexpressions[1]
    #{C.value = d.value}
    subexpressions[0] = {"value": d["value"]}

def p_d_increment(subexpressions):
    'd : INCREMENT'
    #{C.value = '++'}
    subexpressions[0] = {"value": "++"}

def p_c_plus(subexpressions):
    'c : PLUSEQUAL expression'
    #{C.value = '+=' + value.value}
    expression = subexpressions[2]

    isTerminal = False
    if not isNumerical(expression, isTerminal) and not isString(expression, isTerminal):
        raise SemanticException("No es un tipo valido para la operacion +=")

    subexpressions[0] = {"value": "+=" + expression["value"]}

def p_d_decrement(subexpressions):
    'd : DECREMENT'
    #{ C.value = '--'}
    subexpressions[0] = {"value": "--"}

def p_c_minequal(subexpressions):
    'c : MINEQUAL expression'
    #{COND(VALUE.type != "natural" && VALUE.type != "decimal" && VALUE.type != "string"), C.value = '-=' + VALUE.value}
    value = subexpressions[2]
    if value["type"] != 'natural' and value["type"] != 'decimal' and value["type"] != 'string':
        raise SemanticException("No es un tipo valido para la operacion -=")
    subexpressions[0] = {"value": "-=" + value["value"]}

def p_c_mulequal(subexpressions):
    'c : MULEQUAL expression'
    #{COND(VALUE.type != "natural" && VALUE.type != "decimal" && VALUE.type != "string"), C.value = '*=' + VALUE.value}
    value = subexpressions[2]
    if value["type"] != 'natural' and value["type"] != 'decimal':
        raise SemanticException("No es un tipo valido para la operacion *=")
    subexpressions[0] = {"value": "*=" + value["value"]}

def p_c_divequal(subexpressions):
    'c : DIVEQUAL expression'
    #{COND(VALUE.type != "natural" && VALUE.type != "decimal" && VALUE.type != "string"), C.value = '*=' + VALUE.value}
    value = subexpressions[2]
    if value["type"] != 'natural' and value["type"] != 'decimal':
        raise SemanticException("No es un tipo valido para la operacion /=")
    subexpressions[0] = {"value": "/=" + value["value"]}




def p_value_minus_paren_num(subexpressions):
    'value : MINUS LPAREN num RPAREN'
    #{VALUE.value = NUM.value , VALUE.type = NUM.type, VALUE.isArray = "False"}
    num = subexpressions[3]


    subexpressions[0] = {"value": "-("+ num["value"]+ ")", "type": num["type"], "isArray": False}



def p_value_minus_paren_function_with_return(subexpressions):
    'value : MINUS LPAREN function_with_return RPAREN'
    #{VALUE.value = FUNCTION_WITH_RETURN.value, VALUE.type = FUNCTION_WITH_RETURN.type, VALUE.isArray = FUNCTION_WITH_RETURN.isArray}
    function_with_return = subexpressions[3]

    isTerminal = False
    if not(isNumeric(function_with_return, isTerminal)):
        raise SemanticException("No puede agregarle un - a un tipo que no es numerico")


    subexpressions[0] = {"value": "-("+ function_with_return["value"] + ")", "type": function_with_return["type"], "isArray": function_with_return["isArray"]}

def p_value_minus_paren_var(subexpressions):
    'value :  MINUS LPAREN VAR RPAREN'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    var = subexpressions[3]
    isTerminal = True
    typ = getType(var, isTerminal)


    subexpressions[0] = {"value":  "-(" + var["value"] + ")", "type": typ, "isArray": True}

def p_value_minus_paren_array(subexpressions):
    'value :  MINUS LPAREN VAR LBRACKET expression RBRACKET RPAREN'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    expression = subexpressions[5]
    var = subexpressions[3]
    isTerminal = True
    typ = getType(var, isTerminal)
    isArray = isArray(var, isTerminal)

    subexpressions[0] = {"value":  "-(" + var["value"] + "[" +expression["value"] + "])", "type": typ, "isArray": True}



def p_value_minus_function_with_return(subexpressions):
    'value : MINUS function_with_return'
    #{VALUE.value = FUNCTION_WITH_RETURN.value, VALUE.type = FUNCTION_WITH_RETURN.type, VALUE.isArray = FUNCTION_WITH_RETURN.isArray}
    function_with_return = subexpressions[2]

    isTerminal = False


    if not(isNumeric(function_with_return, isTerminal)):
        raise SemanticException("No puede agregarle un - a un tipo que no es numerico")


    subexpressions[0] = {"value": "-"+ function_with_return["value"] , "type": function_with_return["type"], "isArray": function_with_return["isArray"]}

def p_value_minus_array(subexpressions):
    'value :  MINUS VAR LBRACKET expression RBRACKET'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    expression = subexpressions[4]
    var = subexpressions[2]
    isTerminal = True
    typ = getType(var, isTerminal)
    isArray = isArray(var, isTerminal)

    subexpressions[0] = {"value":  "-(" + var["value"] + "["+expression["value"] + "]" + ")", "type": typ, "isArray": j["isArray"]}

def p_value_minus_var(subexpressions):
    'value :  MINUS VAR'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    var = subexpressions[2]
    isTerminal = True
    typ = getType(var, isTerminal)


    subexpressions[0] = {"value":  "-(" + var["value"] + ")", "type": typ, "isArray": False}

def p_value_string(subexpressions):
    'value : STRING'
    #{VALUE.value = string.value, VALUE.type = 'string', VALUE.isArray = "False"}
    string = subexpressions[1]

    subexpressions[0] = {"value": string["value"], "type": "string", "isArray": False}


def p_value_bool(subexpressions):
    'value : bool'
    #{VALUE.value = bool.value, VALUE.type = "bool", VALUE.isArray = "False"}
    bool1 = subexpressions[1]

    subexpressions[0] = {"value":  bool1["value"], "type": "bool", "isArray": False}

def p_value_num(subexpressions):
    'value : num'
    #{VALUE.value = NUM.value , VALUE.type = NUM.type, VALUE.isArray = "False"}
    num = subexpressions[1]

    subexpressions[0] = {"value": num["value"], "type": num["type"], "isArray": False}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'
    #{VALUE.value = FUNCTION_WITH_RETURN.value, VALUE.type = FUNCTION_WITH_RETURN.type, VALUE.isArray = FUNCTION_WITH_RETURN.isArray}
    function_with_return = subexpressions[1]
    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"], "isArray": function_with_return["isArray"]}




def p_value_var_array(subexpressions):
    'value : VAR LBRACKET expression RBRACKET'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    expression = subexpressions[3]
    var = subexpressions[1]

    isTerminal = True
    typ = getType(var, isTerminal)
    isArra = isArray(var, isTerminal)

    subexpressions[0] = {"value":  var["value"] + "["+expression["value"] + "]", "type": typ, "isArray": isArra}


def p_value_var(subexpressions):
    'value : VAR'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    var = subexpressions[1]
    isTerminal = True

    typ = getType(var, isTerminal)

    esArray = isArray(var, isTerminal)

    subexpressions[0] = {"value":  var["value"] , "type": typ, "isArray": esArray}



def p_value_list_values(subexpressions):
    'value : LBRACKET expression list_values RBRACKET'
    #{VALUE.value = '[ ' + EXPRESSION.value + LIST_VALUES.value + ']', VALUE.type = IF(LIST_VALUES.value == "", EXPRESSION.type, IF(LIST_VALUES.type == 'decimal' && EXPRESSION.type == 'natural','decimal',IF(LIST_VALUES.type == 'natural' && EXPRESSION.type == 'decimal', 'decimal', EXPRESSION.value))), VALUE.isArray = "True"}
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


def p_list_registers(subexpressions):
    'list_registers : VAR COLON expression l'
    var = subexpressions[1]
    exp = subexpressions[3]
    l = subexpressions[4]
    newdict = l["dict"].update({ var["value"] : exp["type"]})
    subexpressions[0] = {"value": var["value"] + " : " + exp["value"] + l["value"], "dict": newdict}

def p_l_list_registers(subexpressions):
    'l : COMMA list_registers'
    #{L.value = ',' + LIST REGISTERS.value}
    list_registers = subexpressions[2]
    subexpressions[0] = {"value": ", " + list_registers["value"], "dict": list_registers["dict"] }

def p_l_lambda(subexpressions):
    'l : '
    # {L.value = '' }
    subexpressions[0] = {"value": "", "dict": {}}


def p_list_values_comma(subexpressions):
    'list_values : COMMA expression list_values'
    #{LIST_VALUES1.value = ',' + EXPRESSION.value + LIST_VALUES2.value, LIST_VALUES1.type = IF(LIST_VALUES2.value == "", EXPRESSION.type, IF(LIST_VALUES2.type == 'decimal' && EXPRESSION.type == 'natural','decimal',IF(LIST_VALUES2.type == 'natural' && EXPRESSION.type == 'decimal', 'decimal', EXPRESSION.value))), COND(LIST_VALUES2.value != "" && LIST_VALUES2.type != EXPRESSION.type)}
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
    #{LIST_VALUES.value = ''}
    values = []
    subexpressions[0] = {"value": "", "values" : values}



def p_value_list_registers(subexpressions):
    'value : LKEY list_registers RKEY'
    #{VALUE.value = '{' + LIST_REGISTERS.value + '}', VALUE.type = 'register', VALUE.isArray = "True"}
    list_registers = subexpressions[2]

    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": "register", "isArray": True}



def p_expression_conditional(subexpressions):
    'expression : t QUESTIONMARK expression COLON expression'
    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + ECOMPARABLE.value + ':' + EXPRESSION2.value, CONDITIONAL.type = ECOMPARABLE.type}
    m = subexpressions[1]
    expression1 = subexpressions[3]
    expression2 = subexpressions[5]

    isTerminal = False
    if getType(expression1, isTerminal) != getType(expression2, isTerminal):
        raise SemanticException("Los tipos de las expresiones del condicional deben ser iguales")
    if not isBoolean(m, isTerminal):
        raise SemanticException("La condicion del condicional debe ser booleana")
    subexpressions[0] = {"value": m["value"] + "?" + expression1["value"] + ":" + expression2["value"], "type": expression1["type"], "isArray" : expression1["isArray"]}

def p_expression_t(subexpressions):
    'expression : t'
    m  = subexpressions[1]
    subexpressions[0] = {"value": m["value"] , "type": m["type"], "isArray": m["isArray"]}

def p_t_or(subexpressions):
    't : term OR t'
    left  = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False
    if (not isBoolean(left, isTerminal) or not isBoolean(right, isTerminal)):
        raise SemanticException("Los tipos para operar con OR deben ser booleanos")

    subexpressions[0] = {"value": left["value"] + " or " + right["value"], "type": "bool", "isArray": False}

def p_t_term(subexpressions):
    't : term'
    term  = subexpressions[1]
    subexpressions[0] = {"value": term["value"], "type": term["type"], "isArray": term["isArray"]}

def p_term_factor_and_term(subexpressions):
    'term : factor AND term'
    left = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False
    if (not isBoolean(left, isTerminal) or not isBoolean(right, isTerminal)):
        raise SemanticException("Los tipos para operar con AND deben ser booleanos")

    subexpressions[0] = {"value": left["value"] + right["value"], "type": "bool", "isArray": False}

def p_term_factor(subexpressions):
    'term : factor'
    factor = subexpressions[1]
    subexpressions[0] = {"value": factor["value"], "type": factor["type"], "isArray": factor["isArray"]}

def p_term_factor_pow_x(subexpressions):
    'factor : factor POW x'
    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los tipos para operar con POW deben ser numericos")

    if getType(left, isTerminal) == 'decimal' or getType(right, isTerminal) == 'decimal':
        typ = 'decimal'
    else:
        typ = 'natural'

    subexpressions[0] = {"value": left["value"] + " ^ " + right["value"], "type": typ, "isArray": False}

def p_factor_x(subexpressions):
    'factor : x'
    x = subexpressions[1]
    subexpressions[0] = {"value": x["value"], "type": x["type"], "isArray": x["isArray"]}

def p_x_y_equal_x(subexpressions):
    'x : y EQUAL x'
    left = subexpressions[1]
    right = subexpressions[3]


    subexpressions[0] = {"value": left["value"] + " == " + right["value"], "type": "bool", "isArray": False}

def p_x_y_unequal_x(subexpressions):
    'x : y UNEQUAL x'
    left = subexpressions[1]
    right = subexpressions[3]

    subexpressions[0] = {"value": left["value"] + " != " + right["value"], "type": "bool", "isArray": False}

def p_x_y(subexpressions):
    'x : y'
    y = subexpressions[1]
    subexpressions[0] = {"value": y["value"], "type": y["type"], "isArray": y["isArray"]}

def p_y_z_greater_y(subexpressions):
    'y : z GREATER y'
    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " > " + right["value"], "type": "bool", "isArray": False}

def p_y_z_less_y(subexpressions):
    'y : z LESS y'
    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " < " + right["value"], "type": "bool", "isArray": False}

def p_y_z(subexpressions):
    'y : z'
    z = subexpressions[1]
    subexpressions[0] = {"value": z["value"], "type": z["type"], "isArray": z["isArray"]}

def p_z_z_plus_h(subexpressions):
    'z : z PLUS h'
    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if ((not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)) and (not isString(left, isTerminal) or not isString(right, isTerminal))):
        raise SemanticException("Los elementos a sumar deben ser numericos o strings")

    if (isString(left, isTerminal) or isString(right, isTerminal)):
        typ = 'string'
    else:
        if getType(left, isTerminal) == 'decimal' or getType(right, isTerminal) == 'decimal':
            typ = 'decimal'
        else:
            typ = 'natural'

    subexpressions[0] = {"value": left["value"] + " + " + right["value"], "type": typ, "isArray": False}

def p_z_zminus(subexpressions):
    'z : z MINUS h'
    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a restar deben ser numericos")

    if getType(left, isTerminal) == 'decimal' or getType(right, isTerminal) == 'decimal':
        typ = 'decimal'
    else:
        typ = 'natural'

    subexpressions[0] = {"value": left["value"] + " - " + right["value"], "type": typ, "isArray": False}

def p_z_h(subexpressions):
    'z : h'
    h = subexpressions[1]
    subexpressions[0] = {"value": h["value"], "type": h["type"], "isArray": h["isArray"]}

def p_h_times(subexpressions):
    'h : h TIMES r'
    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a multiplicar deben ser numericos")

    if getType(left, isTerminal) == 'decimal' or getType(right, isTerminal) == 'decimal':
        typ = 'decimal'
    else:
        typ = 'natural'
    subexpressions[0] = {"value": left["value"] + " * " + right["value"], "type": typ, "isArray": False}


def p_h_divide(subexpressions):
    'h : h DIVIDE r'
    left = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a dividir deben ser numericos")
    typ = 'decimal'
    subexpressions[0] = {"value": left["value"] + " / " +  right["value"], "type": typ, "isArray": False}



def p_h_modulo(subexpressions):
    'h : h MODULE r'
    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a multiplicar deben ser numericos")

    if getType(left, isTerminal) == 'decimal' or getType(right, isTerminal) == 'decimal':
        typ = 'decimal'
    else:
        typ = 'natural'

    subexpressions[0] = {"value": left["value"] + " % " + right["value"], "type": typ, "isArray": False}

def p_h_r(subexpressions):
    'h : r'
    r = subexpressions[1]
    subexpressions[0] = {"value": r["value"], "type": r["type"], "isArray": r["isArray"]}

def p_r_not_value(subexpressions):
    'r : NOT value'
    value = subexpressions[2]

    isTerminal = False
    if not isBoolean(value, isTerminal):
        raise SemanticException("Solo se pueden negar booleanos")

    subexpressions[0] = {"value": "not " + value["value"], "type": "bool", "isArray": False}

def p_r_not_expression(subexpressions):
    'r : NOT LPAREN expression RPAREN'
    expression = subexpressions[3]

    isTerminal = False
    if not isBoolean(expression, isTerminal):
        raise SemanticException("Solo se pueden negar booleanos")

    subexpressions[0] = {"value": "not (" + expression["value"] + ")", "type": "bool", "isArray": False}


def p_r_value(subexpressions):
    'r : value'
    value = subexpressions[1]
    subexpressions[0] = {"value": value["value"], "type": value["type"], "isArray": value["isArray"]}

def p_r_lparen_expression_rparen(subexpressions):
    'r : LPAREN expression RPAREN'
    expression = subexpressions[2]

    subexpressions[0] = {"value": "(" + expression["value"] + ")", "type": expression["type"], "isArray": expression["isArray"]}

def p_func_func_wr(subexpressions):
    'function : function_with_return'
    #{FUNCTION.value = FUNCTION_WITH_RETURN.value, FUNCTION.type = FUNCTION_WITH_RETURN.type}
    function_with_return = subexpressions[1]
    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}

def p_func_print(subexpressions):
    'function : PRINT LPAREN expression RPAREN'
    #{FUNCTION.value = '(' + ECOMPARABLE.value + ')'}
    expression = subexpressions[3]
    subexpressions[0] = {"value": "print (" + expression["value"] + ")"}

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'
    #{FUNCTION_WITH_RETURN.value = "multiplicacionEscalar(" + PARAM_ME.value + ')', FUNCTION_WITH_RETURN.type = PARAM_ME.type, FUNCTION_WITH_RETURN.isArray = "False"}
    param_me = subexpressions[3]
    subexpressions[0] = {"value":"multiplicacionEscalar("+ param_me["value"] + ")", "type": param_me["type"], "isArray": True}

def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN expression RPAREN'
    #{COND(ECOMPARABLE.type == 'string'), FUNCTION_WITH_RETURN.value = "capitalizar(" + ECOMPARABLE.value + ')', FUNCTION_WITH_RETURN.type = "string", FUNCTION_WITH_RETURN.isArray = "False"}
    ecomp = subexpressions[3]
    if not(ecomp["type"] == "string"):
        raise SemanticException("Capitalizar recibe solo strings")
    subexpressions[0] = {"value": "capitalizar( " + ecomp["value"] + " )", "type": "string", "isArray": False}

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN expression COMMA expression  RPAREN'
    #{FUNCTION_WITH_RETURN.value = "colineales(" + var.value + "," + var2.value + ')', FUNCTION_WITH_RETURN.type = "bool", FUNCTION_WITH_RETURN.isArray = "False"}
    expression1 = subexpressions[3]
    expression2 = subexpressions[5]

    isTerminal = False
    type_expression1 = getType(expression1 ,isTerminal)
    isArray_expression1 = isArray(expression1, isTerminal)
    type_expression2 = getType(expression2 ,isTerminal)
    isArray_expression2 = isArray(expression2, isTerminal)
    if not( ( (type_expression1 == "natural" or type_expression1 == "decimal") and isArray_expression1 == True) and ((type_expression2 == "natural" or type_expression2 == "decimal") and isArray_expression2 == True)):
        raise SemanticException("colineales solo puede recibir arrays de numeros")
    subexpressions[0] = {"value": "colineales( " + expression1["value"] + ", " + expression2["value"] + " )", "type": "bool", "isArray": False}

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN expression RPAREN'
    #{FUNCTION_WITH_RETURN.value = "length(" + pl.value + ')', FUNCTION_WITH_RETURN.type = "natural", FUNCTION_WITH_RETURN.isArray = "False"}
    expression = subexpressions[3]
    isTerminal = False
    type_expression = getType(expression ,isTerminal)
    isArray_expression = isArray(expression, isTerminal)
    if not(type_expression == "string" or isArray_expression):
        raise SemanticException("length solo puede recibir un string o un array")

    subexpressions[0] = {"value": "length( " + expression["value"] + " )", "type": "natural", "isArray": False}

def p_param_me_var(subexpressions):
    'param_me : expression COMMA expression n'
    #{COND(VALUE.type == 'natural' || VALUE.type == 'decimal'), COND(var.type == 'natural' || var.type == 'decimal'), PARAM_ME.value = var.value + "," + VALUE.value + N.value, PARAM_ME.type = IF(var.type == 'decimal' && N.isTrue, 'decimal', 'var1.type')}
    expression1 = subexpressions[1]
    comma = subexpressions[2]
    expression2 = subexpressions[3]
    n = subexpressions[4]


    if not(expression2["type"] == "natural" or expression2["type"] == "decimal"):
        raise SemanticException("El segundo parametro de multiplicacionEscalar debe ser un numero")

    if not((expression1["type"] == "natural" or expression1["type"]  == "decimal")):
        raise SemanticException("El primer parametro de multiplicacionEscalar debe ser un numero")

    if expression1["type"] == "decimal" and n["isTrue"] :
        typ = "decimal"
    else:
        typ = expression1["type"]

    subexpressions[0] = {"value": expression1["value"] + "," + expression2["value"] + n["value"], "type": typ}

def p_n_bool(subexpressions):
    'n : COMMA expression'
    #{N.value = string.value, PARAM_LENGTH.type = 'string', PARAM_LENGTH.isArray = "False"}
    expression = subexpressions[2]
    if not(expression["type"] == "bool"):
        raise SemanticException("El tercer parametro de multiplicacionEscalar debe ser un booleano")
    subexpressions[0] = {"value": ", " + expression["value"], "isTrue": expression["value"] == True}

def p_n_lambda(subexpressions):
    'n : '
    #{N.value = "", N.isArray = "False"}
    subexpressions[0] = {"value": "", "isTrue": False}

def p_num_decimal(subexpressions):
    'num : DECIMAL '
    #{NUM.value = decimal.value, NUM.type = 'decimal'}
    dec = subexpressions[1]
    subexpressions[0] = {"value": str(dec["value"]), "type":  dec["type"]}

def p_num_natural(subexpressions):
    'num : NATURAL'
    #{NUM.value = natural.value, NUM.type = 'natural'}
    nat = subexpressions[1]
    subexpressions[0] = {"value": str(nat["value"]), "type": nat["type"]}

def p_num_ngeativo(subexpressions):
    'num : NEGATIVO'
    #{NUM.value = natural.value, NUM.type = 'natural'}
    neg = subexpressions[1]
    subexpressions[0] = {"value": str(neg["value"]), "type": neg["type"]}

def p_bool_true(subexpressions):
    'bool : TRUE '
    #{BOOL.value = "True", BOOL.type = 'bool'}
    true = subexpressions[1]
    subexpressions[0] = {"value": true["value"], "type":"bool"}

def p_bool_false(subexpressions):
    'bool : FALSE '
   	#{BOOL.value = "False", BOOL.type = 'bool'}
    false = subexpressions[1]
    subexpressions[0] = {"value": false["value"], "type":"bool"}

def p_error(subexpressions):
    print subexpressions
    raise Exception("Syntax error.")
