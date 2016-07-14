from lexer_rules import tokens
import pdb;

class SemanticException(Exception):
    pass

table = {}

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

def isArray(name):
	#pregunta si una variable almacenada en la tabla es o no un arreglo
    isArray = False
    if (table.has_key(name)!= False):
        datos =table[name]
        isArray = datos[1]
    return isArray

def getType(name):
	#obtiene el tipo de una variable a partir de la informacion de la tabla
    type = ""
    if (table.has_key(name)!= False):
        datos =table[name]
        type = datos[0]
    return type

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
        if sentence[0] == 'd' and sentence[1] == 'o' and sentence["line"] == a["line"]:
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

def p_e_ecomparable(subexpressions):
    'e : ecomparable'
    #{E.value = ECOMPARABLE.value}
    ecomparable = subexpressions[1]
    subexpressions[0] = {"value": ecomparable["value"]}

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

def p_ecomparable_expression(subexpressions):
    'ecomparable : expression'
    #{ECOMPARABLE.value = EXPRESSION.value, ECOMPARABLE.type = EXPRESSION.type, ECOMPARABLE.isArray = EXPRESSION.isArray}
    expression = subexpressions[1]
    subexpressions[0] = {"value": expression["value"], "type": expression["type"], "isArray": expression["isArray"]}

def p_ecomparable_condition(subexpressions):
    'ecomparable : condition'
    #{ECOMPARABLE.value = CONDITION.value, ECOMPARABLE.type = CONDITION.type, ECOMPARABLE.isArray = "False"}
    condition = subexpressions[1]
    subexpressions[0] = {"value": condition["value"], "type": condition["type"], "isArray": False}

def p_ecomparable_conditional(subexpressions):
    'ecomparable : conditional'
    #{ECOMPARABLE.value = CONDITIONAL.value, ECOMPARABLE.type = CONDITIONAL.type, ECOMPARABLE.isArray = "False"}
    conditional = subexpressions[1]
    subexpressions[0] = {"value": conditional["value"], "type": conditional["type"], "isArray": False}

def p_comment_list_append(subexpressions):
    'comment_list : COMMENT comment_list'
    #{COMMENT_LIST1.value = comment.value + '\n' + COMMENT_LIST2.value}
    comment = subexpressions[1]
    comment_list2 = subexpressions[2]
    subexpressions[0] = {"value": comment["value"] + "\n" + comment_list2["value"]}

def p_comment_list_newline(subexpressions):
    'comment_list :  comment_list'
    #{COMMENT_LIST1.value = '\n' + COMMENT_LIST2}
    comment_list2 = subexpressions[2]
    subexpressions[0] = {"value":  "\n" + comment_list2["value"]}

def p_comment_list_lambda(subexpressions):
    'comment_list : '
    #{COMMENT LIST.value = ''}
    subexpressions[0] = {"value": ""}

def p_while(subexpressions):
    'while : WHILE LPAREN condition RPAREN keys'
    #{WHILE.value = 'while (' + CONDITION.value + ') ' + '\n' + KEYS.value}
    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "while(" + condition["value"] + ")" + new}

def p_if_else(subexpressions):
    'if_else : if possibleelse'
    #{IF_ELSE.value = IF.value + POSSIBLEELSE.value}
    if1 = subexpressions[1]
    possibleelse = subexpressions[2]
    subexpressions[0] = {"value": if1["value"] + possibleelse["value"]}

def p_possibleelse_else(subexpressions):
    'possibleelse : ELSE keys'
    #{POSSIBLEELSE.value = 'else' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    keys = subexpressions[2]
    lastElementLine = subexpressions[1]["line"]
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value":  " else " + new}

def p_possibleelse_lambda(subexpressions):
    'possibleelse : '
    #{POSSIBLEELSE.value = ''}
    subexpressions[0] = {"value":  ""}

def p_if(subexpressions):
    'if : IF LPAREN condition RPAREN keys'
    #{IF.value = 'if (' + CONDITION.value + ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    condition = subexpressions[3]
    keys = subexpressions[5]
    lastElementLine = subexpressions[4]["line"]
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "if(" + condition["value"] + ")" + new}

def p_conditional_paren(subexpressions):
    'conditional : LPAREN condition RPAREN QUESTIONMARK ecomparable COLON expression'
    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + ECOMPARABLE.value + ':' + EXPRESSION2.value, CONDITIONAL.type = ECOMPARABLE.type}
    condition = subexpressions[2]
    expression1 = subexpressions[5]
    expression2 = subexpressions[7]
    subexpressions[0] = {"value": "(" + condition["value"] + ")?" + expression1["value"] + ":" + expression2["value"], "type": expression1["type"]}

def p_conditional(subexpressions):
    'conditional : condition QUESTIONMARK ecomparable COLON expression'
    #{CONDITIONAL.value = '(' + CONDITION.value + ')?' + ECOMPARABLE.value + ':' + EXPRESSION2.value, CONDITIONAL.type = ECOMPARABLE.type}
    condition = subexpressions[1]
    expression1 = subexpressions[3]
    expression2 = subexpressions[5]
    subexpressions[0] = {"value": condition["value"] + "?" + expression1["value"] + ":" + expression2["value"], "type": expression1["type"]}

def p_for(subexpressions):
    'for : FOR LPAREN assignationorlambda SEMICOLON condition SEMICOLON advancefor RPAREN keys'
    #{FOR.value ='for (' + ASSIGNATIONORLAMBDA.value + ';' + CONDITION.value + ';' + ADVANCE.value ') ' + POSSIBLECOMMENT.value + '\n' + KEYS.value}
    assignationorlamba = subexpressions[3]
    condition = subexpressions[5]
    advancefor = subexpressions[7]
    keys = subexpressions[9]
    lastElementLine = subexpressions[8]["line"]
    if keys["value"][0] == '#' and lastElementLine == keys["line"]:
        new = "\n"
    new = new + keys["value"]
    subexpressions[0] = {"value": "for(" + assignationorlamba["value"] + "; "+condition["value"]+ "; " +advancefor["value"]+ ")" + new}

def p_do_while(subexpressions):
    'do_while : DO keys_do WHILE LPAREN condition RPAREN SEMICOLON'
    #{DO_WHILE.value = 'do' + '\n' + KEYS_DO.value + ' while(' + CONDITION.value + '); ' + POSSIBLECOMMENT.value + '\n'}
    keysdo = subexpressions[2]
    condition = subexpressions[5]
    subexpressions[0] = {"value": "do \n" + keysdo["value"] + "while(" + condition["value"] + ");", "line": subexpressions[7]["line"]}

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
    #{B.value = '=' + ECOMPARABLE.value, B.type = ECOMPARABLE.type, B.isArray = ECOMPARABLE.isArray}
    ecomparable =  subexpressions[2]
    subexpressions[0] = {"value": "= " + ecomparable["value"] , "type": ecomparable["type"], "isArray": ecomparable["isArray"]}

def p_b_registers(subexpressions):
    'b : COLON ecomparable'
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

def p_advance_var(subexpressions):
    'advance : VAR c'
    #{COND(table.getType(var.value) == 'natural' || table.getType(var.value)  == 'decimal' || table.getType(var.value)  == 'string'), ADVANCE.value = var.value + C.value}
    var = subexpressions[1]
    c = subexpressions[2]
    if (not(getType(var) == "natural" or getType(var) == "decimal" or getType(var) == "string")) :
        raise SemanticException("El tipo a avanzar no es un numero")
    subexpressions[0] = {"value":  var + c["value"]}

def p_c_increment(subexpressions):
    'c : INCREMENT'
    #{C.value = '++'}
    subexpressions[0] = {"value": "++"}

def p_c_plus(subexpressions):
    'c : PLUSEQUAL value'
    #{C.value = '+=' + value.value}
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
    #{COND(VALUE.type != "natural" && VALUE.type != "decimal" && VALUE.type != "string"), C.value = '-=' + VALUE.value}
    value = subexpressions[2]
    if value["type"] != 'natural' and value["type"] != 'decimal' and value["type"] != 'string':
        raise SemanticException("No es un tipo valido para la operacion -=")
    subexpressions[0] = {"value": "-=" + value["value"]}

def p_condition_or(subexpressions):
    'condition : condition OR x'
    #{COND(CONDITION2.type != "bool" || X.type != "bool"), CONDITION1.value = CONDITION2 + 'or' + X.value, CONDITION1.type = "bool"}
    condition1 = subexpressions[1]
    x = subexpressions[3]
    if (condition1["type"] != "bool") or (x["type"]!="bool"):
        raise SemanticException("Solo puede operar con booleanos")
    subexpressions[0] = {"value": condition1["value"] + " or " + x["value"], "type": "bool"}

def p_condition_x(subexpressions):
    'condition : x'
    #{CONDITION_X.value = X.value, CONDITION_X.type = X.type}
    x = subexpressions[1]
    subexpressions[0] = {"value": x["value"], "type": x["type"]}

def p_y_and(subexpressions):
    'x : x AND y'
    #{COND(X2.type != "bool" || Y.type != "bool")X1.value = X2.value + 'and' + Y.value, X1.type = X2.type}
    x = subexpressions[1]
    y = subexpressions[3]
    if (x["type"] != "bool" or y["type"]!= "bool"):
        raise SemanticException("Solo puede operar con booleanos")
    subexpressions[0] = {"value": x["value"] + " and " + y["value"], "type": x["type"]}

def p_x_y(subexpressions):
    'x : y'
    #{X.value = Y.value, X.type = Y.type}
    y = subexpressions[1]
    subexpressions[0] = {"value": y["value"], "type": y["type"]}

def p_y_not(subexpressions):
    'y : NOT y'
    #{Y1.value = 'not' + Y2.value, Y1.type = Y2.type}
    y = subexpressions[2]
    if  y["type"] != 'bool':
        raise SemanticException("Solo puede operar con booleanos")
    subexpressions[0] = {"value": " not " + y["value"], "type": y["type"]}

def p_y_parent(subexpressions):
    'y : LPAREN condition RPAREN'
    #{Y.value = '(' + CONDITION.value + ')', Y.type = CONDITION.type}
    condition = subexpressions[2]
    subexpressions[0] = {"value": " ( " + condition["value"] + " ) ", "type": condition["type"]}

def p_y_logical_condition(subexpressions):
    'y : logical_condition'
    #{Y.value = LOGICAL_CONDITION.value, Y.type = LOGICAL_CONDITION.type}
    logical_condition = subexpressions[1]
    subexpressions[0] = {"value": logical_condition["value"], "type": logical_condition["type"]}

def p_y_value(subexpressions):
    'y : value'
    #{Y.value = VALUE.value, Y.type = VALUE.type}
    value = subexpressions[1]
    subexpressions[0] = {"value": value["value"], "type": value["type"] }

def p_logical_condition(subexpressions):
    'logical_condition : ecomparable i'
    #{LOGICAL_CONDITION.value = ECOMPARABLE.value + I.value, LOGICAL_CONDITION.type = "bool"}
    ecomparable = subexpressions[1]
    i = subexpressions[2]
    subexpressions[0] = {"value": ecomparable["value"] + i["value"], "type": "bool"}

def p_logical_condition_less(subexpressions):
    'i : LESS possibleparen'
    #{I.value = '<' + ECOMPARABLE.value, I.type = "bool"}
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": " < " + ecomparable["value"], "type": "bool"}

def p_logical_condition_greater(subexpressions):
    'i : GREATER possibleparen'
    #{I.value = '>' + ECOMPARABLE.value, I.type = "bool"}
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": " > " + ecomparable["value"], "type": "bool"}

def p_logical_condition_equal(subexpressions):
    'i : EQUAL possibleparen'
	#{I.value = '==' + ECOMPARABLE.value, I.type = "bool"}
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": " == " +  ecomparable["value"], "type": "bool"}

def p_logical_condition_unequal(subexpressions):
    'i : UNEQUAL possibleparen'
    #{I.value = '!=' + ECOMPARABLE.value, I.type = "bool"}
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": " != " +  ecomparable["value"], "type": "bool"}

def p_possibleparen_paren(subexpressions):
    'possibleparen : LPAREN ecomparable RPAREN'
    #{POSSIBLEPAREN.value = "(" +  ecomparable["value"] + ")", POSSIBLEPAREN.type = "bool"}
    ecomparable = subexpressions[2]
    subexpressions[0] = {"value": "(" +  ecomparable["value"] + ")", "type": "bool"}

def p_possibleparen_ecomparable(subexpressions):
    'possibleparen : ecomparable'
    #{POSSIBLEPAREN.value = ECOMPARABLE.value, POSSIBLEPAREN.type = "bool"}
    ecomparable = subexpressions[1]
    subexpressions[0] = {"value": ecomparable["value"], "type": "bool"}

def p_value_string(subexpressions):
    'value : STRING'
    #{VALUE.value = string.value, VALUE.type = 'string', VALUE.isArray = "False"}
    string = subexpressions[1]
    subexpressions[0] = {"value": string, "type": "string", "isArray": False}

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

def p_value_list_registers(subexpressions):
    'value : LKEY list_registers RKEY'
    #{VALUE.value = '{' + LIST_REGISTERS.value + '}', VALUE.type = 'register', VALUE.isArray = "True"}
    list_registers = subexpressions[2]
    subexpressions[0] = {"value": "{" + list_registers["value"] + "}", "type": "register", "isArray": True}

def p_value_var_array(subexpressions):
    'value : VAR j'
    #{VALUE.value = var.value + J.value, VALUE.type = table.getType(var.value), VALUE.isArray = J.isArray}
    j = subexpressions[2]
    var = subexpressions[1]
    typ = getType(var)
    subexpressions[0] = {"value":  var + j["value"], "type": typ, "isArray": j["isArray"]}

def p_j_array(subexpressions):
    'j : LBRACKET expression RBRACKET'
    #{COND(EXPRESSION.type == 'natural'), J.value = '[' + EXPRESSION.value + ']', J.isArray = EXPRESSION.isArray}
    expression = subexpressions[2]
    if expression["type"] != 'natural':
        raise SemanticException("El valor para acceder a un array debe ser natural")
    subexpressions[0] = {"value": "[" + expression["value"] + "]", "isArray": expression["isArray"]}

def p_j_lambda(subexpressions):
    'j : '
    #{J.value = '', J.isArray = "False"}
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
    list_registers = subexpressions[2]
    subexpressions[0] = {"value": ", " + list_registers["value"]}

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
    subexpressions[0] = {"value": ""}

def p_l_lambda(subexpressions):
    'l : '
    #{L.value = '' }
    subexpressions[0] = {"value": ""}

def p_expression_expression_w(subexpressions):
	'expression : expression w'
	expression = subexpressions[1]
	w = subexpressions[2]
	if w["operator"] == "minus":
		if not ((expression["type"] == 'natural' or expression["type"] == 'decimal') and (w["type"] == 'natural' or w["type"] == 'decimal')):
			raise SemanticException("No puede utilizar el - si ambos tipos no son numericos")
	if w["operator"] == "plus":
		if not(((expression["type"] == 'natural' or expression["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')) or (expression["type"] == 'string' and term["type"] == 'string')):
			raise SemanticException("No puede utilizar el + si ambos tipos no son numericos o strings")
	typ = 'string'
	if  expression["type"] == 'decimal' or w["type"] == 'decimal':
		typ = 'decimal'
	else:
		if expression["type"] == 'natural' and w["type"] == 'natural':
			typ = 'natural'
	subexpressions[0] = {"value": expression["value"] + w["value"], "type": typ, "isArray": False}

def p_w_plus(subexpressions):
    'w : PLUS term'
    #{EXPRESSION1.value = EXPRESSION2.value + '+' + TERM.value, EXPRESSION1.type = IF(EXPRESSION2.type == 'decimal' || TERM.type == 'decimal', 'decimal', IF(EXPRESSION2.type == 'natural' and TERM.type == 'natural', 'natural', 'string')), EXPRESSION1.isArray = "False"}
    term  = subexpressions[2]
    subexpressions[0] = {"value": expression["value"] + " + " + term["value"], "type": term["type"], "operator": "plus", "isArray": False}

def p_w_minus(subexpressions):
    'w : MINUS term'
    #{EXPRESSION1.value = EXPRESSION2.value + '-' + TERM.value, EXPRESSION1.type = IF(EXPRESSION2.type == 'decimal' || TERM.type == 'decimal', 'decimal', EXPRESSION2.type), EXPRESSION1.isArray = "False"}
    term  = subexpressions[2]
    subexpressions[0] = {"value": expression["value"] + " - " + term["value"], "type": term["type"], "operator": "minus", "isArray": False}

def p_expression_term(subexpressions):
    'expression : term'
    #{EXPRESSION.value = TERM.value, EXPRESSION.type = TERM.type, EXPRESSION.isArray = TERM.isArray}
    term = subexpressions[1]
    subexpressions[0] = {"value": term["value"], "type": term["type"], "isArray": term["isArray"]}

def p_pow_ops(subexpressions):
	'term : term ops'
	term = subexpressions[1]
	value = subexpressions[2]
	if not((value["type"] == 'natural' or value["type"] == 'decimal') and (term["type"] == 'natural' or term["type"] == 'decimal')):
		raise SemanticException("No puede operar con tipos que no son numericos")
	typ = 'natural'
	if  value["type"] == 'decimal' or term["type"] == 'decimal':
		typ = 'decimal'
	subexpressions[0] = {"value": term["value"] + value["value"], "type": typ, "isArray": False}


def p_ops_pow(subexpressions):
    'ops : POW factor'
    #{TERM.value = TERM1.value +'^' + FACTOR.value, TERM.type = IF(FACTOR.type == 'decimal' || TERM1.type == 'decimal', 'decimal', TERM1.type), TERM.isArray = "False"}
    term = subexpressions[1]
    value = subexpressions[2]
    subexpressions[0] = {"value": " ^ " + value["value"], "type": value["type"], "isArray": False}

def p_ops_times(subexpressions):
    'ops : TIMES factor'
    #{TERM.value = TERM1.value +'*'+ FACTOR.value, TERM.type = IF(FACTOR.type == 'decimal' || TERM1.type == 'decimal', 'decimal', TERM1.type), TERM.isArray = "False"}
    term = subexpressions[1]
    value = subexpressions[2]
    subexpressions[0] = {"value": " * " + value["value"], "type": value["type"], "isArray": False}

def p_ops_divide(subexpressions):
    'ops : DIVIDE factor'
    #{COND(FACTOR.value != 0), COND(TERM1.type != 'string' && FACTOR.type != 'string'), TERM.value = TERM1.value + '/' + FACTOR.value, TERM.type = 'decimal', TERM.isArray = "False"}
    term = subexpressions[1]
    value = subexpressions[2]
    subexpressions[0] = {"value": " / " + value["value"], "type": value["type"], "isArray": False}

def p_ops_module(subexpressions):
    'ops : MODULE factor'
    #{COND(TERM1.type != 'string' && FACTOR.type != 'string'), TERM.value = TERM1.value + '%' + FACTOR.value, TERM.type = IF(TERM1.type == 'decimal', 'decimal', 'natural'), TERM.isArray = "False"}
    term = subexpressions[1]
    value = subexpressions[2]
    subexpressions[0] = {"value": " % " + value["value"], "type": value["type"], "isArray": False}

def p_factor_paren(subexpressions):
    'factor : LPAREN expression RPAREN'
    #{FACTOR.value = '(' + EXPRESSION.value + ')', FACTOR.type = TERM.type, FACTOR.isArray = TERM.isArray}
    term = subexpressions[2]
    subexpressions[0] = {"value": "(" + term["value"] + ")", "type": term["type"], "isArray": term["isArray"]}

def p_factor_value(subexpressions):
    'factor : value'
    #{FACTOR.value = TERM.value, FACTOR.type = TERM.type, FACTOR.isArray = TERM.isArray}
    value = subexpressions[1]
    subexpressions[0] = {"value":  value["value"] , "type": value["type"], "isArray": value["isArray"]}

def p_term_value(subexpressions):
    'term : factor'
    #{TERM.value = FACTOR.value, TERM.type = FACTOR.type, TERM.isArray = FACTOR.isArray}
    value = subexpressions[1]
    subexpressions[0] = {"value": value["value"], "type": value["type"], "isArray": value["isArray"]}

def p_func_func_wr(subexpressions):
    'function : function_with_return'
    #{FUNCTION.value = FUNCTION_WITH_RETURN.value, FUNCTION.type = FUNCTION_WITH_RETURN.type}
    function_with_return = subexpressions[1]
    subexpressions[0] = {"value": function_with_return["value"], "type": function_with_return["type"]}

def p_func_print(subexpressions):
    'function : PRINT LPAREN ecomparable RPAREN'
    #{FUNCTION.value = '(' + ECOMPARABLE.value + ')'}
    expression = subexpressions[3]
    subexpressions[0] = {"value": "(" + expression["value"] + ")"}

def p_func_wr_mult(subexpressions):
    'function_with_return : MULTIPLICACIONESCALAR LPAREN param_me RPAREN'
    #{FUNCTION_WITH_RETURN.value = "multiplicacionEscalar(" + PARAM_ME.value + ')', FUNCTION_WITH_RETURN.type = PARAM_ME.type, FUNCTION_WITH_RETURN.isArray = "False"}
    param_me = subexpressions[3]
    subexpressions[0] = {"value":"multiplicacionEscalar("+ param_me["value"] + ")", "type": param_me["type"], "isArray": False}

def p_func_wr_capi(subexpressions):
    'function_with_return : CAPITALIZAR LPAREN ecomparable RPAREN'
    #{COND(ECOMPARABLE.type == 'string'), FUNCTION_WITH_RETURN.value = "capitalizar(" + ECOMPARABLE.value + ')', FUNCTION_WITH_RETURN.type = "string", FUNCTION_WITH_RETURN.isArray = "False"}
    ecomp = subexpressions[3]
    if not(ecomp["type"] == "string"):
        raise SemanticException("Capitalizar recibe solo strings")
    subexpressions[0] = {"value": "capitalizar( " + ecomp["value"] + " )", "type": "string", "isArray": False}

def p_func_wr_coli(subexpressions):
    'function_with_return : COLINEALES LPAREN VAR COMMA VAR  RPAREN'
    #{FUNCTION_WITH_RETURN.value = "colineales(" + var.value + "," + var2.value + ')', FUNCTION_WITH_RETURN.type = "bool", FUNCTION_WITH_RETURN.isArray = "False"}
    var1 = subexpressions[3]
    var2 = subexpressions[5]
    subexpressions[0] = {"value": "colineales( " + var1 + ", " + var2 + " )", "type": "bool", "isArray": False}

def p_func_wr_length(subexpressions):
    'function_with_return : LENGTH LPAREN param_length RPAREN'
    #{FUNCTION_WITH_RETURN.value = "length(" + pl.value + ')', FUNCTION_WITH_RETURN.type = "natural", FUNCTION_WITH_RETURN.isArray = "False"}
    pl = subexpressions[3]
    subexpressions[0] = {"value": "length( " + pl["value"] + " )", "type": "natural", "isArray": False}

def p_param_me_var(subexpressions):
    'param_me : VAR COMMA value n'
    #{COND(VALUE.type == 'natural' || VALUE.type == 'decimal'), COND(var.type == 'natural' || var.type == 'decimal'), PARAM_ME.value = var.value + "," + VALUE.value + N.value, PARAM_ME.type = IF(var.type == 'decimal' && N.isTrue, 'decimal', 'var1.type')}
    var1 = subexpressions[1]
    comma = subexpressions[2]
    var2 = subexpressions[3]
    n = subexpressions[4]
    if not(var2["type"] == "natural" or var2["type"] == "decimal"):
        raise SemanticException("El tercer parametro de multiplicacionEscalar debe ser un numero")
    table_var1_type = getType(var1)
    if not((table_var1_type == "natural" or table_var1_type == "decimal")):
        raise SemanticException("El primer parametro de multiplicacionEscalar debe ser un numero")
    if table_var1_type == "decimal" and n["isTrue"] :
        typ = "decimal"
    else:
        typ = table_var1_type

    subexpressions[0] = {"value": var1 + "," + var2["value"] + n["value"], "type": typ}

def p_n_bool(subexpressions):
    'n : COMMA bool'
    #{N.value = string.value, PARAM_LENGTH.type = 'string', PARAM_LENGTH.isArray = "False"}
    booleano = subexpressions[2]
    subexpressions[0] = {"value": ", " + booleano["value"], "isTrue": booleano["value"] == "true"}


def p_n_lambda(subexpressions):
    'n : '
    #{N.value = "", N.isArray = "False"}
    subexpressions[0] = {"value": "", "isTrue": False}

def p_param_l_var(subexpressions):
    'param_length : VAR '
    #{PARAM_LENGTH.value = var.value, PARAM_LENGTH.isArray = "False"}
    var = subexpressions[1]
    subexpressions[0] = {"value": var, "isArray": False}

def p_param_l_fwr(subexpressions):
    'param_length : function_with_return '
    #{COND(FUNCTION_WITH_RETURN.type == "string"), PARAM_LENGTH.value = FUNCTION_WITH_RETURN.value, PARAM_LENGTH.type = FUNCTION_WITH_RETURN.type, PARAM_LENGTH.isArray = FUNCTION_WITH_RETURN.isArray}
    func = subexpressions[1]
    if not(func["type"] == "string"):
        raise SemanticException("Length recibe funciones a string o a arreglos")
    subexpressions[0] = {"value": func["value"], "type": func["type"], "isArray": func["isArray"]}

def p_param_l_vector(subexpressions):
    'param_length : LBRACKET value list_values RBRACKET '
    #{PARAM_LENGTH.value = '[' + VALUE.value + LIST_VALUES.value + ']', PARAM_LENGTH.type = IF(LIST_VALUES.value == "", VALUE.type, IF(LIST_VALUES.type == 'decimal' && VALUE.type == 'natural', 'decimal', IF(LIST_VALUES.type == 'natural' && VALUE.type == 'natural','decimal', VALUE.type))), PARAM_LENGTH.isArray = "True"}
    val = subexpressions[2]
    list_val = subexpressions[3]
    if list_val["value"] == "":
        tp = value["type"]
    elif (val["type"] == "natural" and list_val["type"] == "decimal"):
        tp = "decimal"
    elif (val["type"] == "decimal" and list_val["type"] == "natural"):
        tp = "decimal"
    else:
        tp = value["type"]
    subexpressions[0] = {"value": "["+ val["value"] + list_val["value"] + "]", "type": tp, "isArray": True}

def p_param_l_string(subexpressions):
    'param_length : STRING '
    #{PARAM_LENGTH.value = string.value, PARAM_LENGTH.type = 'string', PARAM_LENGTH.isArray = "False"}
    subexpressions[0] = {"value": subexpressions[1], "type": "string", "isArray": False}

def p_num_decimal(subexpressions):
    'num : DECIMAL '
    #{NUM.value = decimal.value, NUM.type = 'decimal'}
    dec = subexpressions[1]
    subexpressions[0] = {"value": str(dec), "type": "decimal"}

def p_num_natural(subexpressions):
    'num : NATURAL'
    #{NUM.value = natural.value, NUM.type = 'natural'}
    nat = subexpressions[1]
    subexpressions[0] = {"value": str(nat), "type": "natural"}

def p_bool_true(subexpressions):
    'bool : TRUE '
    #{BOOL.value = "True", BOOL.type = 'bool'}
    subexpressions[0] = {"value": "true", "type":"bool"}

def p_bool_false(subexpressions):
    'bool : FALSE '
   	#{BOOL.value = "False", BOOL.type = 'bool'}
    subexpressions[0] = {"value": "false", "type":"bool"}

def p_error(subexpressions):
    print subexpressions
    raise Exception("Syntax error.")

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
