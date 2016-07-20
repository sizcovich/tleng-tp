# -*- coding: utf-8 -*-
from __future__ import print_function
from lexer_rules import tokens
import sys

class SemanticException(Exception):
    pass

table = {}


def getTypeRecursivo(stringInterno):

    variables = stringInterno.split(".")

    if len(variables) == 1:
        typ = table[variables[0]]
    else:
        if variables[0] == "[]":
            raise SemanticException("Una variable no puede comenzar con []")
        else:
            typ = table[variables[0]]

            for i in range(1, len(variables)):


                if variables[i] == "[]":
                    if typ["tipo"] == "array":
                        typ = typ["tipoInterno"]
                    else:
                        raise SemanticException("La estructura de la variable no se corresponde con la variable requerida")
                else:
                    typ = typ["tipoInterno"][variables[i]]
                    if typ == None:
                        raise SemanticException("La estructura de la variable no se corresponde con la variable requerida")

    return typ

def laVarEsUnRegistro(value):
    return len(value.split(".")) > 1

def accederAlRegistroYObtenerTipoDeValue(value):
    arrayvar = value.split(".")
    typ = {}
    if len(arrayvar) > 1:
        typ = getType({"value": arrayvar[0], "type": ""}, False)
        if typ["tipo"] != "register":
            raise SemanticException("la variable no es un register")
        for x in range(1, len(arrayvar)):
            if typ["tipo"] != "register":
                raise SemanticException("la variable no es un register")
            typ = typ["tipoInterno"][arrayvar[x]]
    return typ


def EsSubtipo(tipo1, tipo2):
    if tipo1["tipo"] == "decimal":
        return EsSubtipoTipoInterno(tipo1["tipoInterno"], tipo2["tipoInterno"])
    else:
        if (tipo1["tipo"] == "negativo" or  tipo1["tipo"] == "natural") and (tipo2["tipo"] == "negativo" or tipo2["tipo"] == "natural"):
            return EsSubtipoTipoInterno(tipo1["tipoInterno"], tipo2["tipoInterno"])
        else:
            return False


def EsSubtipoTipoInterno(tipo1, tipo2):
    if tipo1 == None and tipo2 == None:
        return True
    if (tipo1 == None and tipo2 != None) or (tipo1 != None and tipo2 == None):
        return False
    else:
        return EsSubtipo( tipo1, tipo2 )



def TienenElMismoTipo(tipo1, tipo2):
    if tipo1["tipo"] != tipo2["tipo"]:
        return False
    if (tipo1["tipo"] == "register" and tipo2["tipo"] == "register"):
        return SonElMismoRegistro(tipo1["tipoInterno"], tipo2["tipoInterno"])
    else:
        return TienenMismoTipoInterno(tipo1["tipoInterno"], tipo2["tipoInterno"])

def TienenMismoTipoInterno(tipo1, tipo2):
    if tipo1 == None and tipo2 == None:
        return True
    if (tipo1 == None and tipo2 != None) or (tipo1 != None and tipo2 == None):
        return False
    else:
        return TienenElMismoTipo( tipo1, tipo2 )

def SonElMismoRegistro(tipoInt1, tipoInt2):
    for k1 in tipoInt1:
        if tipoInt2[k1] == None:
            return False
    for k2 in tipoInt2:
        if tipoInt1[k2] == None:
            return False
    res = True
    for k1 in tipoInt1:
        res = res and TienenElMismoTipo(tipoInt1[k1], tipoInt2[k1])
    return res

def isBoolean(expresion, isTerminal):

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    res = False
    if (tipo == 'bool'):
        res = True

    return res

def isString(expresion, isTerminal):

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    res = False
    if (tipo == 'string'):
        res = True

    return res


def isNegativo(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    return (tipo == 'negativo')

def isArrayNumerical(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    tipoInterno = ""
    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]
        if (tipo =="array"):
            tipoInterno = expresion["type"]["tipoInterno"]["tipo"]
    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]
        if (tipo =="array"):
            tipoInterno = datos["tipoInterno"]["tipo"]

    return (tipoInterno == 'natural' or tipoInterno == 'negativo' or tipoInterno == 'decimal')

def isArrayNatural(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]
        if (tipo =="array"):
            tipoInterno = expresion["type"]["tipoInterno"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    if (tipo =="array"):
        tipoInterno = datos["tipoInterno"]["tipo"]


    return (tipoInterno == 'natural')


def isNatural(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero


    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    return (tipo == 'natural')


def isDecimal(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    if isTerminal:
        name = expresion["value"]
    else:
        name = expresion["value"]
        tipo = expresion["type"]["tipo"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos["tipo"]

    return (tipo == 'decimal')


def isNumericalTypoInterno(expresion, isTerminal):
    tipo = expresion["type"]["tipoInterno"]["tipo"]
    return tipo == "natural" or tipo == "decimal" or tipo == "negativo"

def isNumerical(expresion, isTerminal):
    #chequea que el tipo de la expresion sea un numero

    natural = isNatural(expresion, isTerminal)
    negativo = isNegativo(expresion, isTerminal)
    decimal = isDecimal(expresion, isTerminal)

    return natural or negativo or decimal

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

    datos = (type)
    table[name] = datos


def isArray(expresion, isTerminal):
	#devuelve si una expression es array o no: si esta definida en la tabla devuelve esos datos, sino devuelve los datos que vienen por parametro
    esArray  = False
    if isTerminal:
        name = expresion["value"]
        if laVarEsUnRegistro(name):
            tipo = accederAlRegistroYObtenerTipoDeValue(name)
            esArray = tipo["tipo"] == "array"
    else:
        name = expresion["value"]
        tipo = expresion["type"]

        esArray =  tipo["tipo"] == "array"

    if (table.get(name) != None):
        datos =table[name]
        esArray = datos["tipo"] == "array"

    return esArray

def getType(expresion, isTerminal):
    #obtiene el tipo de una variable: si esta definida en la tabla devuelve esos datos, sino devuelve los datos que vienen por parametro
    #es necesario que sepa si expression es terminal o no
    tipo = ""
    if isTerminal:
        name = expresion["value"]
        if laVarEsUnRegistro(name):
            tipo = accederAlRegistroYObtenerTipoDeValue(name)
    else:
        name = expresion["value"]
        tipo = expresion["type"]

    if (table.get(name) != None):
        datos =table[name]
        tipo = datos

    return tipo


def p_program(subexpressions):
    'program : list_sentencies'

    list_sentencies = subexpressions[1]
    subexpressions[0] = {"value": list_sentencies["value"]}

def p_list_sentencies_comment(subexpressions):
    'list_sentencies : COMMENT a'

    comment = subexpressions[1]
    a = subexpressions[2]
    subexpressions[0] = {"value": comment["value"] + "\n" + a["value"], "element": "comment", "line": comment["line"]}

def p_list_sentencies_sentence(subexpressions):
    'list_sentencies : sentence a'

    sentence = subexpressions[1]
    a = subexpressions[2]
    list_sentencies_value = sentence["value"]
    if (a["element"] != ""):
        list_sentencies_value = list_sentencies_value + "\n"
    else:
        if sentence["value"][0].upper() == 'D' and sentence["value"][1].upper() == 'O':
            list_sentencies_value = list_sentencies_value
        else:
            list_sentencies_value = list_sentencies_value
    list_sentencies_value = list_sentencies_value + a["value"]

    subexpressions[0] = {"value": list_sentencies_value, "element": "sentence"}

def p_a_list_sentencies(subexpressions):
    'a : list_sentencies'

    list_sentencies = subexpressions[1]
    subexpressions[0] = {"value": list_sentencies["value"], "element":list_sentencies["element"]}

def p_a_lambda(subexpressions):
    'a : '

    subexpressions[0] = {"value": "", "element":""}

def p_sentence_semicolon(subexpressions):
    'sentence : e SEMICOLON'

    e = subexpressions[1]
    subexpressions[0] = {"value": e["value"] + ";"}

def p_sentence_while(subexpressions):
    'sentence : WHILE LPAREN expression RPAREN keys'

    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    if keys["value"][0] != '{':
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "while (" + condition["value"] + ")" + new}

def p_sentence_if_else(subexpressions):
    'sentence : IF LPAREN expression RPAREN keys possibleelse'

    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    newline = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        newline = "\n"
    if keys["value"][0] != '{':
        newline = "\n"
    new = newline + keys["value"]
    possibleelse = subexpressions[6]
    subexpressions[0] = {"value": "if (" + condition["value"] + ")" + new + possibleelse["value"]}

def p_sentence_for(subexpressions):
    'sentence : FOR LPAREN assignationorlambda SEMICOLON expression SEMICOLON advancefor RPAREN keys'

    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advancefor = subexpressions[7]
    keys = subexpressions[9]

    lastElement = subexpressions[8]
    lastElementLine = lastElement["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    if keys["value"][0] != '{':
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "for (" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advancefor["value"]+ ")" + new}

def p_sentence_do_while(subexpressions):
    'sentence : DO keys_do WHILE LPAREN expression RPAREN SEMICOLON'

    keysdo = subexpressions[2]
    condition = subexpressions[5]

    lastElementLine = subexpressions[4]["line"]
    newline = ''
    if keysdo["value"][0] == '#' and lastElementLine == keysdo["line"]:
        newline = "\n"
    if keysdo["value"][0] != '{':
        newline = "\n"
    new = newline + keysdo["value"] + "\n"


    subexpressions[0] = {"value": "do " + new + "while(" + condition["value"] + ");\n", "line": subexpressions[7]["line"]}

def p_sentence_function(subexpressions):
    'sentence : function SEMICOLON'

    function = subexpressions[1]
    subexpressions[0] = {"value": function["value"] + ";"}

def p_sentence_return(subexpressions):
    'sentence : RETURN expression'

    exp = subexpressions[2]
    subexpressions[0] = {"value": "return " + exp["value"] + ";"}

def p_possibleelse_else(subexpressions):
    'possibleelse : ELSE keys'

    keys = subexpressions[2]
    lastElementLine = subexpressions[1]["line"]
    new = ''
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    if keys["value"][0] != '{':
        new = "\n" + keys["value"] + "\n"
    subexpressions[0] = {"value": " else " + new}

def p_possibleelse_lambda(subexpressions):
    'possibleelse : '

    subexpressions[0] = {"value": ""}

def p_e_advance(subexpressions):
    'e : advance'

    advance = subexpressions[1]
    subexpressions[0] = {"value": advance["value"]}

def p_e_assignation(subexpressions):
    'e : assignation'

    assignation = subexpressions[1]
    subexpressions[0] = {"value": assignation["value"]}

def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'

    comment = subexpressions[1]
    comment_list2 = subexpressions[2]
    subexpressions[0] = {"value": comment["value"] + "\n" + comment_list2["value"]}

def p_comment_list_lambda(subexpressions):
    'comment_list : '

    subexpressions[0] = {"value": ""}

def p_keys_do_append_sentence(subexpressions):
    'keys_do : comment_list sentence'

    comment_list = subexpressions[1]
    sentence = subexpressions[2]
    subexpressions[0] = {"value":indent(comment_list["value"] +  sentence["value"])}

def p_keys_do_append_possiblecomment(subexpressions):
    'keys_do : LKEY list_sentencies RKEY'

    sentence = subexpressions[2]
    text = sentence["value"]
    if (sentence["element"] != "comment"):
        text = "\n" + text
    else:
        if sentence["line"] != subexpressions[1]["line"]:
            text = "\n" + text
    subexpressions[0] = {"value": " { " + indent(text) + "} "}

def p_keys_append_sentence(subexpressions):
    'keys : comment_list sentence'

    keys = subexpressions[0]
    comment_list = subexpressions[1]
    sentence = subexpressions[2]
    subexpressions[0] = {"value":indent(comment_list["value"] +  sentence["value"])}

def p_keys_append_possiblecomment(subexpressions):
    'keys : LKEY list_sentencies RKEY'

    sentence = subexpressions[2]
    text = sentence["value"]


    if (sentence["element"] != "comment"):
        text = "\n" + text
    else:
        if sentence["line"] != subexpressions[1]["line"]:
            text = "\n" + text
    subexpressions[0] = {"value": " { " + indent(text) + "}\n"}

def p_assignationorlambda_assignation(subexpressions):
    'assignationorlambda : assignation'

    assignation = subexpressions[1]
    subexpressions[0] = {"value": assignation["value"]}

def p_assignationorlambda_lambda(subexpressions):
    'assignationorlambda : '

    subexpressions[0] = {"value": ""}

def p_assignation(subexpressions):
    'assignation : VAR b'

    b = subexpressions[2]
    var = subexpressions[1]
    varIsTerminal = True
    bIsTerminal = False
    if var["value"] in table:
        if isArray(b, bIsTerminal) and isArray(var, varIsTerminal):
            if not TienenElMismoTipo( getType(var, varIsTerminal), getType(b, bIsTerminal)):
                raise SemanticException("No puede agregarle a un array un elemento de tipo distinto al tipo del array")



    insertOrUpdate(var["value"],getType(b, bIsTerminal), isArray(b, bIsTerminal))

    subexpressions[0] = {"value": var["value"] + b["value"], "type": getType(b, bIsTerminal)}

def p_b_array(subexpressions):
    'b : LBRACKET expression RBRACKET ASSIGN expression'

    expression1 = subexpressions[2]
    expression2 =  subexpressions[5]
    isTerminal = False

    if not isNatural(expression1, isTerminal):
        raise SemanticException("El valor para acceder a un array debe ser natural")

    b_type = getType(expression2, isTerminal)

    subexpressions[0] = {"value": "[" +  expression1["value"] + "] = " +  expression2["value"], "type": {"tipo":"array", "tipoInterno": b_type }}

def p_b_expression(subexpressions):
    'b : ASSIGN expression'

    expression =  subexpressions[2]

    subexpressions[0] = {"value": " = " + expression["value"] , "type": expression["type"]}

def p_b_registers(subexpressions):
    'b : COLON expression'

    ecomparable =  subexpressions[2]
    subexpressions[0] = {"value": ":" + ecomparable["value"] , "type": ecomparable["type"]}

def p_advancefor_advance(subexpressions):
    'advancefor : advance'

    advance = subexpressions[1]
    subexpressions[0] = {"value":  advance["value"]}

def p_advancefor_assignationorlambda(subexpressions):
    'advancefor : assignationorlambda'

    assignationorlambda = subexpressions[1]
    subexpressions[0] = {"value": assignationorlambda["value"]}

def p_advance_var_array_c(subexpressions):
    'advance : VAR LBRACKET expression RBRACKET c'

    var = subexpressions[1]
    expression = subexpressions[3]
    c = subexpressions[5]
    isTerminal = True

    if not isNatural(expression, False):
        raise SemanticException("El valor para acceder a un array debe ser natural")


    if c["isPlusEqual"] :
        if  not isNumerical(var, isTerminal) and not isString(var, isTerminal) and not isArrayNumerical(var, isTerminal):
            raise SemanticException("El tipo para += debe ser un numero o un string")
    else:
        if not isNumerical(var, isTerminal) and not isArrayNumerical(var, isTerminal):
            raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  var["value"] + "[" + expression["value"] + "]" +  c["value"]}

def p_advance_var_array_d(subexpressions):
    'advance : VAR LBRACKET expression RBRACKET d'

    var = subexpressions[1]
    expression = subexpressions[3]
    d = subexpressions[5]
    isTerminal = False

    if not isNatural(expression, isTerminal):
        raise SemanticException("El valor para acceder a un array debe ser natural")

    isTerminal = True
    if not isNumerical(var, isTerminal)  and not isArrayNumerical(var, isTerminal):
        raise SemanticException("El tipo a avanzar no es un numero")
    subexpressions[0] = {"value":  var["value"] + "[" + expression["value"] + "]" +  d["value"]}

def p_advance_var_c(subexpressions):
    'advance : VAR c'

    var = subexpressions[1]
    c = subexpressions[2]

    isTerminal = True

    if c["isPlusEqual"] :
        if  not isNumerical(var, isTerminal) and not isString(var, isTerminal):
            raise SemanticException("El tipo para += debe ser un numero o un string")
    else:
        if not isNumerical(var, isTerminal):
            raise SemanticException("El tipo a avanzar no es un numero")
        else:
            if not TienenElMismoTipo(getType(var, True), getType(c, False)):
                raise SemanticException("Los tipos deben coincidir")

    subexpressions[0] = {"value":  var["value"] + c["value"]}


def p_advance_var_d(subexpressions):
    'advance : VAR d'

    var = subexpressions[1]
    d = subexpressions[2]

    isTerminal = True
    if not isNumerical(var, isTerminal):
        raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  var["value"] + d["value"]}

def p_advance_d_var(subexpressions):
    'advance : d VAR'

    d = subexpressions[1]
    var = subexpressions[2]

    isTerminal = True
    if not isNumerical(var, isTerminal):
        raise SemanticException("El tipo a avanzar no es un numero")

    subexpressions[0] = {"value":  d["value"] + var["value"]}

def p_advance_d_array(subexpressions):
    'advance : d VAR LBRACKET expression RBRACKET'

    d = subexpressions[1]
    var = subexpressions[2]
    isTerminal = True
    expression  = subexpressions[4]

    if not isNatural(expression, False):
        raise SemanticException("El valor para acceder a un array debe ser natural")

    if not isNumerical(var, isTerminal):
        raise SemanticException("El tipo a avanzar no es un numero")
    subexpressions[0] = {"value":  d["value"] + var["value"] + "[" + expression["value"] + "]"}

def p_d_increment(subexpressions):
    'd : INCREMENT'

    subexpressions[0] = {"value": "++", "type": ""}

def p_c_plus(subexpressions):
    'c : PLUSEQUAL expression'

    expression = subexpressions[2]
    isTerminal = False


    if not isNumerical(expression, isTerminal) and not isString(expression, isTerminal):
        raise SemanticException("No es un tipo valido para la operacion +=")
    subexpressions[0] = {"value": "+=" + expression["value"], "type": expression["type"],"isPlusEqual" :True}

def p_d_decrement(subexpressions):
    'd : DECREMENT'

    subexpressions[0] = {"value": "--", "type": ""}

def p_c_minequal(subexpressions):
    'c : MINEQUAL expression'

    expression = subexpressions[2]
    isTerminal = False
    if not isNumerical(expression, isTerminal):
        raise SemanticException("No es un tipo valido para la operacion -=")

    subexpressions[0] = {"value": "-=" + expression["value"], "type": expression["type"], "isPlusEqual" :False}

def p_c_mulequal(subexpressions):
    'c : MULEQUAL expression'

    expression = subexpressions[2]

    isTerminal = False
    if not isNumerical(expression, isTerminal):
        raise SemanticException("No es un tipo valido para la operacion *=")

    subexpressions[0] = {"value": "*=" + expression["value"], "type": expression["type"], "isPlusEqual" :False}

def p_c_divequal(subexpressions):
    'c : DIVEQUAL expression'

    expression = subexpressions[2]

    isTerminal = False
    if not isNumerical(expression, isTerminal):
        raise SemanticException("No es un tipo valido para la operacion /=")

    subexpressions[0] = {"value": "/=" + expression["value"], "type": expression["type"], "isPlusEqual" :False}

def p_value_minus_paren_num(subexpressions):
    'value : MINUS LPAREN num RPAREN'

    num = subexpressions[3]

    subexpressions[0] = {"value": "-("+ num["value"]+ ")", "type": num["type"]}



def p_value_minus_paren_function_with_return(subexpressions):
    'value : MINUS LPAREN function_with_return RPAREN'

    function_with_return = subexpressions[3]

    isTerminal = False
    if not(isNumerical(function_with_return, isTerminal)):
        raise SemanticException("No puede agregarle un - a un tipo que no es numerico")


    subexpressions[0] = {"value": "-("+ function_with_return["value"] + ")", "type": function_with_return["type"]}



def p_value_minus_paren_array(subexpressions):
    'value :  MINUS LPAREN VAR s RPAREN'

    s = subexpressions[4]
    var = subexpressions[3]
    isTerminal = True

    isTerminal = True
    typ = getTypeRecursivo(var["value"] + s["stringInterno"])

    subexpressions[0] = {"value":  "-(" + var["value"] + s["value"] + ")", "type": typ}



def p_value_minus_function_with_return(subexpressions):
    'value : MINUS function_with_return'

    function_with_return = subexpressions[2]

    isTerminal = False


    if not(isNumerical(function_with_return, isTerminal)):
        raise SemanticException("No puede agregarle un - a un tipo que no es numerico")


    subexpressions[0] = {"value": "-"+ function_with_return["value"] , "type": function_with_return["type"]}

def p_value_minus_array(subexpressions):
    'value :  MINUS VAR s'

    s = subexpressions[3]
    var = subexpressions[2]
    isTerminal = True

    isTerminal = True
    typ = getTypeRecursivo(var["value"] + s["stringInterno"])


    subexpressions[0] = {"value":  "-" + var["value"] + s["value"], "type": typ}

def p_value_string(subexpressions):
    'value : STRING'

    string = subexpressions[1]

    subexpressions[0] = {"value": string["value"], "type": {"tipo": "string", "tipoInterno": None}}


def p_value_bool(subexpressions):
    'value : bool'

    bool1 = subexpressions[1]

    subexpressions[0] = {"value":  bool1["value"], "type": {"tipo": "bool", "tipoInterno": None}}

def p_value_num(subexpressions):
    'value : num'

    num = subexpressions[1]

    subexpressions[0] = {"value": num["value"], "type": num["type"]}


def p_value_function_with_return(subexpressions):
    'value : function_with_return'

    function_with_return = subexpressions[1]
    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}


def p_s_array(subexpressions):
    's : LBRACKET expression RBRACKET s'

    expression = subexpressions[2]
    s = subexpressions[4]

    isTerminal = False
    if not isNatural(expression, isTerminal):
        raise SemanticException("El valor para acceder a un array debe ser natural")

    stringInterno  =  ".[]" + s["stringInterno"]
    subexpressions[0] = {"value":  "[" + expression["value"] + "]" + s["value"], "type": {"tipo": "",  "tipoInterno": None}, "stringInterno" : stringInterno}

def p_s_lambda(subexpressions):
    's : '

    typ =  {"tipo": "",  "tipoInterno": None}
    subexpressions[0] = {"value":  "", "type": typ, "stringInterno" : ""}



def p_value_var_array(subexpressions):
    'value : VAR s'

    s = subexpressions[2]
    var = subexpressions[1]

    isTerminal = True
    typ = getTypeRecursivo(var["value"] + s["stringInterno"])

    subexpressions[0] = {"value":  var["value"]  + s["value"] , "type": typ}


def p_value_list_values(subexpressions):
    'value : LBRACKET expression list_values RBRACKET'

    expression = subexpressions[2]
    list_values2 = subexpressions[3]
    isTerminal = False
    value1 = ''

    if list_values2["value"] == "":
        typ = getType(expression, isTerminal)
    else:
        if isArrayNumerical(list_values2, isTerminal) and isArrayNumerical(expression, isTerminal):
            if EsSubtipo(list_values2["type"]["tipoInterno"], expression["type"]["tipoInterno"]):
                typ = getType(list_values2, isTerminal)
            else:
                typ = getType(expression, isTerminal)

            if typ["tipoInterno"]["tipo"] == "negativo" and  (list_values2["type"]["tipoInterno"]["tipo"] == "natural" or list_values2["type"]["tipoInterno"]["tipo"] == "natural"):
                typ = {"tipo":"natural", "tipoInterno": None}
        else:
            if isNumerical(list_values2, isTerminal) and isNumerical(expression, isTerminal):

                if EsSubtipo(list_values2["type"], expression["type"]):
                    typ = getType(list_values2, isTerminal)
                else:
                    typ = getType(expression, isTerminal)

                if typ["tipo"] == "negativo" and  (list_values2["type"]["tipo"] == "natural" or list_values2["type"]["tipo"] == "natural"):
                    typ = {"tipo":"natural", "tipoInterno": None}
            else:
                typ = getType(list_values2, isTerminal)


    if list_values2["value"] != "":
        if not (isArrayNumerical(list_values2, isTerminal) and isArrayNumerical(expression, isTerminal)) and (not isNumerical(list_values2, isTerminal) and isNumerical(expression, isTerminal)):
            if (not TienenElMismoTipo(list_values2["type"],typ)) :
                raise SemanticException("El tipo del valor no coincide con el tipo de la lista")

    subexpressions[0] = {"value": "[" + expression["value"] + list_values2["value"] + "]", "type": {"tipo":"array", "tipoInterno": typ }}


def p_list_registers(subexpressions):
    'list_registers : VAR COLON expression l'

    var = subexpressions[1]
    exp = subexpressions[3]
    l = subexpressions[4]
    dict = l["dict"]
    dict.update({ var["value"] : getType(exp,False ) })
    subexpressions[0] = {"value": var["value"] + " : " + exp["value"] + l["value"], "dict": dict}

def p_l_list_registers(subexpressions):
    'l : COMMA list_registers'

    list_registers = subexpressions[2]
    subexpressions[0] = {"value": "," + list_registers["value"], "dict": list_registers["dict"] }

def p_l_lambda(subexpressions):
    'l : '

    subexpressions[0] = {"value": "", "dict": {}}


def p_list_values_comma(subexpressions):
    'list_values : COMMA expression list_values'

    expression = subexpressions[2]
    list_values2 = subexpressions[3]
    isTerminal = False
    tipoRes = {}

    if list_values2["value"] == "":
        typ = getType(expression, isTerminal)
    else:
        if isArrayNumerical(list_values2, isTerminal) and isArrayNumerical(expression, isTerminal):
            if EsSubtipo(list_values2["type"]["tipoInterno"], expression["type"]["tipoInterno"]):
                typ = getType(list_values2, isTerminal)
            else:
                typ = getType(expression, isTerminal)

            if typ["tipoInterno"]["tipo"] == "negativo" and  (list_values2["type"]["tipoInterno"]["tipo"] == "natural" or list_values2["type"]["tipoInterno"]["tipo"] == "natural"):
                typ = {"tipo":"natural", "tipoInterno": None}
        else:
            if isNumerical(list_values2, isTerminal) and isNumerical(expression, isTerminal):
                if EsSubtipo(list_values2["type"], expression["type"]):
                    typ = getType(list_values2, isTerminal)
                else:
                    typ = getType(expression, isTerminal)

                if typ["tipo"] == "negativo" and  (list_values2["type"]["tipo"] == "natural" or list_values2["type"]["tipo"] == "natural"):
                    typ = {"tipo":"natural", "tipoInterno": None}
            else:
                typ = getType(list_values2, isTerminal)


    if list_values2["value"] != "":
        if not (isArrayNumerical(list_values2, isTerminal) and isArrayNumerical(expression, isTerminal)) and (not isNumerical(list_values2, isTerminal) and isNumerical(expression, isTerminal)):
            if (not TienenElMismoTipo(list_values2["type"],typ)) :
                raise SemanticException("El tipo del valor no coincide con el tipo de la lista")


    subexpressions[0] = {"value": "," + expression["value"] + list_values2["value"], "type":typ}

def p_list_values_lambda(subexpressions):
    'list_values : '

    values = []
    subexpressions[0] = {"value": ""}

def p_value_list_registers(subexpressions):
    'value : LKEY list_registers RKEY'

    list_registers = subexpressions[2]
    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": {"tipo": "register", "tipoInterno": list_registers["dict"] }}

def p_expression_conditional(subexpressions):
    'expression : t QUESTIONMARK expression COLON expression'

    m = subexpressions[1]
    expression1 = subexpressions[3]
    expression2 = subexpressions[5]
    isTerminal = False
    if not isNumerical(expression1, isTerminal) or not isNumerical(expression2, isTerminal):
        if not TienenElMismoTipo(getType(expression1, isTerminal), getType(expression2, isTerminal)):
            raise SemanticException("Los tipos de las expresiones del condicional deben ser iguales")
        typ = expression1["type"]
    else:
        if isDecimal(expression1, isTerminal) or isDecimal(expression2, isTerminal):
            typ = {"tipo" : "decimal", "tipoInterno" : None}
        else:
            if isNatural(expression1, isTerminal) or isNatural(expression2, isTerminal):
                typ = {"tipo" : "natural", "tipoInterno" : None}
            else:
                typ = {"tipo" : "negativo", "tipoInterno" : None}

    if not isBoolean(m, isTerminal):
        raise SemanticException("La condicion del condicional debe ser booleana")
    subexpressions[0] = {"value": m["value"] + " ? " + expression1["value"] + " : " + expression2["value"], "type": typ}

def p_expression_t(subexpressions):
    'expression : t'

    m  = subexpressions[1]
    subexpressions[0] = {"value": m["value"] , "type": m["type"]}

def p_t_or(subexpressions):
    't : term OR t'

    left  = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False
    if (not isBoolean(left, isTerminal) or not isBoolean(right, isTerminal)):
        raise SemanticException("Los tipos para operar con OR deben ser booleanos")

    subexpressions[0] = {"value": left["value"] + " OR " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_t_term(subexpressions):
    't : term'

    term  = subexpressions[1]
    subexpressions[0] = {"value": term["value"], "type": term["type"]}

def p_term_factor_and_term(subexpressions):
    'term : factor AND term'

    left = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False

    if (not isBoolean(left, isTerminal) or not isBoolean(right, isTerminal)):
        raise SemanticException("Los tipos para operar con AND deben ser booleanos")

    subexpressions[0] = {"value": left["value"] + " AND " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_term_factor(subexpressions):
    'term : factor'

    factor = subexpressions[1]
    subexpressions[0] = {"value": factor["value"], "type": factor["type"]}

def p_term_factor_pow_x(subexpressions):
    'factor : factor POW x'

    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False

    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a multiplicar deben ser numericos")

    if isDecimal(left, isTerminal) or isDecimal(right, isTerminal):
        typ = 'decimal'
    else:
        typ = 'natural'

    typ = {"tipo":typ, "tipoInterno":None}
    subexpressions[0] = {"value": left["value"] + " ^ " + right["value"], "type": typ}


def p_factor_x(subexpressions):
    'factor : x'

    x = subexpressions[1]
    subexpressions[0] = {"value": x["value"], "type": x["type"]}

def p_x_y_equal_x(subexpressions):
    'x : y EQUAL x'

    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " == " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_x_y_unequal_x(subexpressions):
    'x : y UNEQUAL x'

    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " != " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_x_y(subexpressions):
    'x : y'

    y = subexpressions[1]
    subexpressions[0] = {"value": y["value"], "type": y["type"]}

def p_y_z_greater_y(subexpressions):
    'y : z GREATER y'

    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " > " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_y_z_less_y(subexpressions):
    'y : z LESS y'

    left = subexpressions[1]
    right = subexpressions[3]
    subexpressions[0] = {"value": left["value"] + " < " + right["value"], "type": {"tipo":"bool", "tipoInterno":None}}

def p_y_z(subexpressions):
    'y : z'

    z = subexpressions[1]
    subexpressions[0] = {"value": z["value"], "type": z["type"]}

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
        if isDecimal(left, isTerminal) or isDecimal(right, isTerminal):
            typ = 'decimal'
        else:
            typ = 'natural'


    tipoRes = {"tipo":typ, "tipoInterno":None}
    subexpressions[0] = {"value": left["value"] + " + " + right["value"], "type": tipoRes}

def p_z_zminus(subexpressions):
    'z : z MINUS h'

    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a restar deben ser numericos")

    if isDecimal(left, isTerminal) or isDecimal(right, isTerminal):
        typ = 'decimal'
    else:
        typ = 'natural'


    tipoRes = {"tipo": typ, "tipoInterno": None}

    subexpressions[0] = {"value": left["value"] + " - " + right["value"], "type": tipoRes}

def p_z_h(subexpressions):
    'z : h'

    h = subexpressions[1]
    subexpressions[0] = {"value": h["value"], "type": h["type"]}

def p_h_times(subexpressions):
    'h : h TIMES r'

    left = subexpressions[1]
    right = subexpressions[3]
    isTerminal = False

    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a multiplicar deben ser numericos")

    if isDecimal(left, isTerminal) or isDecimal(right, isTerminal):
        typ = 'decimal'
    else:
        typ = 'natural'



    tipoRes = {"tipo": typ, "tipoInterno": None}
    subexpressions[0] = {"value": left["value"] + " * " + right["value"], "type": tipoRes}

def p_h_divide(subexpressions):
    'h : h DIVIDE r'

    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False
    if (not isNumerical(left, isTerminal) or not isNumerical(right, isTerminal)):
        raise SemanticException("Los elementos a dividir deben ser numericos")

    typ = 'decimal'

    tipoRes = {"tipo": typ, "tipoInterno": None}
    subexpressions[0] = {"value": left["value"] + " / " +  right["value"], "type": tipoRes}

def p_h_modulo(subexpressions):
    'h : h MODULE r'

    left = subexpressions[1]
    right = subexpressions[3]

    isTerminal = False

    if (not isNatural(left, isTerminal) and not isNegativo(left, isTerminal)) or (not isNatural(right, isTerminal) and not isNegativo(right, isTerminal)):
        raise SemanticException("Los elementos a aplicarle modulo deben ser numericos")

    typ = "natural"

    tipoRes = {"tipo": typ, "tipoInterno": None}

    subexpressions[0] = {"value": left["value"] + " % " + right["value"], "type": tipoRes}

def p_h_r(subexpressions):
    'h : r'

    r = subexpressions[1]
    subexpressions[0] = {"value": r["value"], "type": r["type"]}

def p_r_not_value(subexpressions):
    'r : NOT value'

    value = subexpressions[2]

    isTerminal = False
    if not isBoolean(value, isTerminal):
        raise SemanticException("Solo se pueden negar booleanos")

    subexpressions[0] = {"value": "NOT " + value["value"], "type": {"tipo": "bool", "tipoInterno": None}}

def p_r_not_expression(subexpressions):
    'r : NOT LPAREN expression RPAREN'

    expression = subexpressions[3]

    isTerminal = False
    if not isBoolean(expression, isTerminal):
        raise SemanticException("Solo se pueden negar booleanos")

    subexpressions[0] = {"value": "NOT (" + expression["value"] + ")", "type": {"tipo": "bool", "tipoInterno": None}}

def p_r_value(subexpressions):
    'r : value'

    value = subexpressions[1]
    subexpressions[0] = {"value": value["value"], "type": value["type"]}

def p_r_lparen_expression_rparen(subexpressions):
    'r : LPAREN expression RPAREN'

    expression = subexpressions[2]

    subexpressions[0] = {"value": "(" + expression["value"] + ")", "type": expression["type"]}

def p_func_func_wr(subexpressions):
    'function : function_with_return'

    function_with_return = subexpressions[1]
    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}

def p_func_print(subexpressions):
    'function : PRINT LPAREN expression RPAREN'

    expression = subexpressions[3]
    subexpressions[0] = {"value": "print(" + expression["value"] + ")"}

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'

    param_me = subexpressions[3]
    tipoRes = {"tipo": "array", "tipoInterno": param_me["type"]}

    subexpressions[0] = {"value":"multiplicacionEscalar("+ param_me["value"] + ")", "type": tipoRes }

def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN expression RPAREN'

    expression = subexpressions[3]

    isTerminal = False
    if not(isString(expression, isTerminal)):
        raise SemanticException("Capitalizar recibe solo strings")

    subexpressions[0] = {"value": "capitalizar(" + expression["value"] + ")", "type": {"tipo": "string", "tipoInterno": None}}

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN expression COMMA expression  RPAREN'

    expression1 = subexpressions[3]
    expression2 = subexpressions[5]
    isTerminal = False
    if not isArrayNumerical(expression1, isTerminal) or not isArrayNumerical(expression2, isTerminal):
        raise SemanticException("colineales solo puede recibir arrays de numeros")
    subexpressions[0] = {"value": "colineales(" + expression1["value"] + ", " + expression2["value"] + ")", "type": {"tipo": "bool", "tipoInterno": None}}

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN expression RPAREN'

    expression = subexpressions[3]
    isTerminal = False
    if not(isString(expression, isTerminal) or isArray(expression, isTerminal)):
        raise SemanticException("length solo puede recibir un string o un array")
    subexpressions[0] = {"value": "length(" + expression["value"] + ")", "type": {"tipo": "natural", "tipoInterno": None}}

def p_param_me_var(subexpressions):
    'param_me : expression COMMA expression n'

    expression1 = subexpressions[1]
    comma = subexpressions[2]
    expression2 = subexpressions[3]
    n = subexpressions[4]
    isTerminal = False
    if not isNumerical(expression2, isTerminal) :
        raise SemanticException("El segundo parametro de multiplicacionEscalar debe ser un numero")

    if not isArrayNumerical(expression1, isTerminal) :
        raise SemanticException("El primer parametro de multiplicacionEscalar debe ser un array de numeros")
    typ = getType(expression1, isTerminal)

    if typ == "decimal" and n["isTrue"] :
        typ = typ = {"tipo":"decimal", "tipoInterno":None}

    subexpressions[0] = {"value": expression1["value"] + "," + expression2["value"] + n["value"], "type": typ}

def p_n_bool(subexpressions):
    'n : COMMA expression'

    expression = subexpressions[2]
    isTerminal = False
    if not(isBoolean(expression, isTerminal)):
        raise SemanticException("El tercer parametro de multiplicacionEscalar debe ser un booleano")
    subexpressions[0] = {"value": ", " + expression["value"], "isTrue": expression["value"] == True}

def p_n_lambda(subexpressions):
    'n : '

    subexpressions[0] = {"value": "", "isTrue": False}

def p_num_decimal(subexpressions):
    'num : DECIMAL '

    dec = subexpressions[1]
    subexpressions[0] = {"value": str(dec["value"]), "type":   {"tipo":dec["type"],"tipoInterno":None}}

def p_num_natural(subexpressions):
    'num : NATURAL'
    nat = subexpressions[1]
    subexpressions[0] = {"value": str(nat["value"]), "type": {"tipo":nat["type"],"tipoInterno":None}}

def p_num_ngeativo(subexpressions):
    'num : NEGATIVO'

    neg = subexpressions[1]
    subexpressions[0] = {"value": str(neg["value"]), "type": {"tipo":neg["type"],"tipoInterno":None}}

def p_bool_true(subexpressions):
    'bool : TRUE '

    true = subexpressions[1]
    subexpressions[0] = {"value": true["value"], "type":{"tipo":"bool","tipoInterno":None}}

def p_bool_false(subexpressions):
    'bool : FALSE '

    false = subexpressions[1]
    subexpressions[0] = {"value": false["value"], "type":{"tipo":"bool","tipoInterno":None}}

def p_error(subexpressions):
    print("The element '", subexpressions.value["value"], "' wasn't expected.", "Line:", subexpressions.value["line"])
    raise Exception
