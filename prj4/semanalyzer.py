import sys
import re as re
import scanner
import os

# call scanner to generate token list
scanner.scanner()
#print("- - - - - - - - - - - - - - - - - - - - - - -")
# keep track of current token being evaluated
global i
i = 0
# keep track of current scope (each function declaration is new scope)
global x
x = 0

# expressions can be of any size any form, so they are created dynamically during semantic analysis
global expression
expression = ""

# search within different scopes using dictionary key values i.e. sym_name = func name && sym_attr is function
sym_table = []

# list of tokens' value
token_list_value = []
# list of token types (same size as token_value_list)
token_list_type = []
try:
    with open("tokens.txt", "r") as f2:
        tokens = f2.readlines()
        for token in tokens:
            # ex. KW: while, KW: int, ID: aaa
            if(len(token.split(" ")) == 2):
                # token value
                token_value = token.split(" ")[1]
                # token type (ID --> [a-zA-Z]+, INT --> [0-9]+)
                token_type = token.split(" ")[0]
            else:
                token_value = token
                token_type = token
            token_value = token_value.strip()
            token_type = token_type.strip()

            # rebuild list of tokens without the token identifier i.e. remove "KW:" from "KW: while"
            token_list_value.append(token_value)
            token_list_type.append(token_type)
    # add "end of file" symbol
    token_list_value.append("$")
    token_list_type.append("$")
except:
    exit()
#print(len(token_list_type))
#print(len(token_list_value))
#print(token_list_value)
#print(token_list_type)

def exitProgram():
    global i
    global x
    #print(i)
    print("REJECT")
    # identify token type that caused the error (for testing)
    #print("error at " + token_list_value[i])
    exit()

# program() -> declaration() declarationList()
def program():
    global i
    global x
    #print(i)
    declaration()
    declarationList()

# declaration() -> int ID declarationPrime() | void ID declarationPrime()
def declaration():
    global i
    global x
    #print(i)
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
            # consume
            i = i + 1
            declarationPrime()
    elif token_list_value[i] == "void":
        # consume "void"
        i = i + 1
        #print(i)
        if token_list_type[i] == "ID:":
            # symbol name is value of token ID
            # consume ID
            i = i + 1
            declarationPrime()
        else:
            exitProgram()
    else:
        exitProgram()

# declarationPrime() -> funDeclaration() | varDeclaration()
def declarationPrime():
    global i
    global x
    #print(i)
    ## function declaration
    if token_list_value[i] == "(":

        ## if the length of the symbol table is greater than 0, check each scope for function being called

        if len(sym_table) > 0:
            ## check symbol table to see if this function already exists
            for val in sym_table:
                ## if the function being called/declared already exists in the symbol table
                if val['sym_name'][0] == token_list_value[i-1]:
                    print("function already exists")
                ## if function does not already exist in the symbol table, create it
                else:
                    ### check for duplicate function declarations
                    print("function does not exist in symbol table")

                    sym_table.append([{'sym_name': [token_list_value[i-1]], 'sym_type': [token_list_value[i-2]], 'sym_attr': ["function declaration"]}])

                break
        #print("empty symbol table")

        # if the symbol table does not have any entries, create the first

        else:
            sym_table.append({'sym_name': [token_list_value[i-1]], 'sym_type': [token_list_value[i-2]], 'sym_attr': ["function declaration"]})
        funDeclaration()

    # var declaration
    elif token_list_value[i] in [";", "["]:

        sym_table[x]['sym_name'].append(token_list_value[i-1])
        sym_table[x]['sym_type'].append(token_list_value[i-2])
        sym_table[x]['sym_attr'].append(None)
        varDeclaration()
    else:
        exitProgram()

# declarationList() -> declaration() declarationList() | EPSILON
def declarationList():
    global i
    if token_list_value[i] in ["int", "void"]:
        declaration()
        declarationList()
    # if rule contains empty, check first of follow sets e.g. first of follow set of declarationList is "$"
    # if we hit dollar sign we accept
    elif token_list_value[i] in "$":
        for val in sym_table:
            print(val)
        print("ACCEPT")
        exit()
    else:
        exitProgram()

# funDeclaration() -> ( params() ) compoundStmt()
def funDeclaration():
    global i
    global x
    if token_list_value[i] == "(":
        # consume "("
        i = i + 1
        params()
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
            compoundStmt()
            x = x + 1
    else:
        exitProgram()

# varDeclaration() -> ; | [ NUM ] ;
def varDeclaration():
    global i
    if token_list_value[i] == ";":
        sym_table[x]['sym_type'].append(token_list_value[i-1])
        sym_table[x]['sym_name'].append(token_list_value[i])
        sym_table[x]['sym_attr'].append('local declaration')
        # consume ";"
        i = i + 1
    elif token_list_value[i] == "[":
        sym_table[x]['sym_type'].append(token_list_value[i-1] + "[" + token_list_value[i+2] + "]")
        sym_table[x]['sym_name'].append(token_list_value[i])
        sym_table[x]['sym_attr'].append('local declaration')
        # consume "["
        i = i + 1
        if token_list_type[i] == "INT:":
            sym_table[x]['sym_type'].update()
            # consume NUM
            i = i + 1
            sym_table[x]['sym_type'].append[x]
        if token_list_value[i] == "]":
            # consume "]"
            i = i + 1
        if token_list_value[i] == ";":
            # consume ";"
            i = i + 1
    else:
        exitProgram()

# params() -> void paramsPrime() | int paramsPrime()
def params():
    global i
    global x
    if token_list_value[i] == "void":
        # consume "void"
        i = i + 1
        paramsPrime()
    elif token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        paramsPrime()
    else:
        #print("error here")
        exitProgram()

# paramsPrime() -> ID param() paramList() | EPSILON
def paramsPrime():
    global i
    global x
    if token_list_type[i] == "ID:":
        sym_table[x]['sym_name'].append(token_list_value[i])
        sym_table[x]['sym_type'].append(token_list_value[i-1])
        sym_table[x]['sym_attr'].append('parameter')
        # consume ID:
        i = i + 1
        param()
        paramList()
    # elif next token in follow(paramsPrime())
    elif token_list_value[i] == ")":
        return
    else:
        exitProgram()

# paramList() -> , paramListPrime() | EPSILON
def paramList():
    global i
    global x
    if token_list_value[i] == ",":
        # consume ","
        # add another parameter to symbol table
        i = i + 1
        paramListPrime()
    # follow of paramList is in follow of paramsPrime()
    elif token_list_value[i] == ")":
        return
    else:
        exitProgram()

# paramListPrime() -> int ID param() paramList() | void ID param() paramList()
def paramListPrime():
    global i
    global x
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
            # add parameter to symbol table
            sym_table[x]['sym_type'].append('int')
            sym_table[x]['sym_name'].append(token_list_value[i])
            sym_table[x]['sym_attr'].append('parameter')
            # consume ID
            i = i + 1
        else:
            exitProgram()
        param()
        paramList()
    elif token_list_value[i] == "void":
        # consume void
        i = i + 1
        if token_list_type[i] == "ID:":
            # add parameter to symbol table
            sym_table[x]['sym_type'].append('int')
            sym_table[x]['sym_name'].append(token_list_value[i])
            sym_table[x]['sym_attr'].append('parameter')
            # consume ID
            i = i + 1
        else:
            exitProgram()
        param()
        paramList()
    else:
        exitProgram()

# param() -> [ ] | EPSILON
def param():
    global i
    global x
    if token_list_value[i] == "[":
        # consume "["
        sym_table[x]['sym_type'][-1].append("[")
        i = i + 1
        if token_list_value[i] == "]":
            sym_table[x]['sym_type'][-1].append("]")
            # consume "]"
            i = i + 1
        else:
            exitProgram()
    # check follow set because of epsilon --> first(paramList()) in follow(param())
    elif token_list_value[i] in [",", ")"]:
        return
    else:
        exitProgram()

# compoundStmt() -> { localDeclarations() statementList() }
def compoundStmt():
    global i
    global x
    if token_list_value[i] == "{":

        # consume "{"
        i = i + 1
        #print("I am in compoundStmt() and my token is: " + token_list_value[i])
        localDeclarations()
        #print("I am in compoundStmt() and my token is: " + token_list_value[i])
        statementList()
        #print("I am in compoundStmt() and my token is: " + token_list_value[i])

        if token_list_value[i] == "}":
            #print("I am in compoundStmt() and my token is: " + token_list_value[i])
            # consume "}"
            i = i + 1
    else:
        exitProgram()

# localDeclarations() -> int ID varDeclaration() localDeclarations() | void ID varDeclaration() localDeclarations() | EPSILON
def localDeclarations():
    global i
    #print(token_list_type[i])
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
            # consume ID
            i = i + 1
            varDeclaration()
            localDeclarations()
    elif token_list_value[i] == "void":
        # consume "void"
        i = i + 1
        if token_list_type[i] == "ID:":
            # consume ID
            i = i + 1
            varDeclaration()
            localDeclarations()
    # check follow set cause of epsilon --> first(statementList()) in  follow(localDeclarations())
    elif token_list_value[i] in [";", "(", "if", "return", "{", "while", "}"] or token_list_type[i] in ["INT:", "ID:"]:
        return
    else:
        exitProgram()

# statementList() -> statement() statementList() | EPSILON
def statementList():
    global i
    # first(statement())
    if token_list_value[i] in [";", "(", "if", "return", "{", "while"] or token_list_type[i] in ["INT:", "ID:"]:
        #print("I am in statementList() and my token is: " + token_list_type[i])
        statement()
        statementList()
    # elif next token is in follow(statementList())
    elif token_list_value[i] == "}":
        return
    else:
        exitProgram()

# statement() -> expressionStmt() | compoundStmt() | selectionStmt() | iterationStmt() | returnStmt()
def statement():
    global i
    global expression
    if token_list_value[i] in [";", "("] or token_list_type[i] in ["INT:", "ID:"]:
        expressionStmt()
    elif token_list_value[i] == "{":
        compoundStmt()
    elif token_list_value[i] == "if":
        selectionStmt()
    elif token_list_value[i] == "while":
        iterationStmt()
    elif token_list_value[i] == "return":
        returnStmt()
    else:
        exitProgram()

# expressionStmt() -> expression() ; | ;
def expressionStmt():
    global i
    if token_list_value[i] == "(" or token_list_type[i] in ["INT:", "ID:"]:
        expression()
        if token_list_value[i] == ";":
            # consume ";"
            i = i + 1
        else:
            exitProgram()
    elif token_list_value[i] == ";":
        # consume ";"
        i = i + 1
    else:
        exitProgram()

# selectionStmt() -> if ( expression() ) statement() selectionStmtPrime() *********
def selectionStmt():
    global i
    if token_list_value[i] == "if":
        # consume "if"
        i = i + 1
        if token_list_value[i] == "(":
            # consume "("
            i = i + 1
            expression()
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
            statement()
            selectionStmtPrime()
    else:
        exitProgram()

# selectionStmtPrime() -> else statement() | EPSILON
def selectionStmtPrime():
    global i
    if token_list_value[i] == "else":
        # consume "else"
        i = i + 1
        statement()
    # check follow set cause of epsilon [else, ;, ID, (, NUM, if, return, {, while, }]
    elif token_list_value[i] in ["else", ";", "(", "if", "return", "{", "while", "}"] or token_list_type[i] in ["INT:", "ID:"]:
        return
    else:
        exitProgram()

# iterationStmt() -> while ( expression() ) statement() *******
def iterationStmt():
    global i
    if token_list_value[i] == "while":
        # consume "while"
        i = i + 1
        if token_list_value[i] == "(":
            # consume "("
            i = i + 1
            expression()
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
            statement()
    else:
        exitProgram()

# returnStmt() -> return returnStmtPrime()
def returnStmt():
    global i
    #print("I am in returnStmt() and my token is: " + token_list_value[i])
    if token_list_value[i] == "return":
        # consume "return"
        i = i + 1
        returnStmtPrime()
    else:
        exitProgram()

# returnStmtPrime() -> ; | expression() ;
def returnStmtPrime():
    global i
    if token_list_value[i] == ";":
        # consume ";"
        i = i + 1
    elif token_list_value[i] == "(" or token_list_type[i] in ["ID:", "INT:"]:
        expression()
        # consume ";"
        i = i + 1
    else:
        exitProgram()

# expression() -> ID expressionPrime() | simpleExpression()
def expression():
    global i
    global expression
    if token_list_type[i] == "ID:":
        expression = expression + token_list_value[i]
        
        ### check if variable exists in scope
        for val in sym_table:
            if val["sym_name"] == token_list_value[i]:
                print("found " + token_list_value[i] + "!")
            else:
                print("token not found in scope")
                exitProgram()
        
        # consume ID
        i = i + 1
        expressionPrime()
        if token_list_value[i] in [",", ")", "]", ";"]:
            return
        # if token_list_value[i] in ["[", "(", "=", "*", "/", "<=", "<", ">", ">=", "==", "!=", "+", "-"]:
        # elif token_list_value[i] in [",", ")", "]", ";"]:
        #     return
    # elif next token is in first(simpleExpression())
    elif token_list_value[i] == "(" or token_list_type[i] == "INT:":
        simpleExpression()
    else:
        exitProgram()

# expressionPrime() -> var() expressionPrimePrime() | factorPrime() term() additiveExpressionPrime() simpleExpressionPrime() ******
def expressionPrime():
    global i
    global expression
    # if token in first(var())
    if token_list_value[i] in ["[", "=", "*", "/", "<=", "<", ">", ">=", "==", "!=", "+", "-"]:
        var()
        expressionPrimePrime()
    elif token_list_value[i] == "(":
        factorPrime()
        term()
        additiveExpressionPrime()
        simpleExpressionPrime()
    #
    # temp fix
    #
    elif token_list_value[i] in [",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# expressionPrimePrime() -> = expression() | term() additiveExpressionPrime() simpleExpressionPrime()
def expressionPrimePrime():
    global i
    global expression
    #print("I am in expressionPrimePrime() and my token is: " + token_list_value[i])
    if token_list_value[i] == "=":
        expression = expression + "="
        # consume "="
        i = i + 1
        expression()
    # if next token is in first(term())
    elif token_list_value[i] in ["*", "/", "+", "-", "<=", "<", ">", ">=", "==", "!="]:
        term()
        additiveExpressionPrime()
        simpleExpressionPrime()
    # elif next token is in follow(expressionPrimePrime())
    elif token_list_value[i] in [",", ")", "]", ";"]:
        return
    else:
        #print("error in expressionPrimePrime()")
        exitProgram()

# var() -> [ expression() ] | EPSILON ***
def var():
    global i
    global expression
    if token_list_value[i] == "[":
        expression = expression + "["
        # consume "["
        i = i + 1
        expression()
        # consume "]"
        i = i + 1
    # elif next token in follow(var())
    elif token_list_value[i] in ["*", "/", "+", "-", "=", "<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# simpleExpression() -> additiveExpression() simpleExpressionPrime()
def simpleExpression():
    global i
    additiveExpression()
    simpleExpressionPrime()

# simpleExpressionPrime() -> relop() simpleExpressionPrimePrime() | EPSILON
def simpleExpressionPrime():
    global i
    # first(relop)
    if token_list_value[i] in ["<=", "<", ">", ">=", "==", "!="]:
        relop()
        simpleExpressionPrimePrime()
    # follow(simpleExpressionPrime())
    elif token_list_value[i] in [",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# simpleExpressionPrimePrime() -> additiveExpression() | ID simpleExpressionPrimePrimePrime()
def simpleExpressionPrimePrime():
    global i
    # first(additiveExpression())
    if token_list_value[i] == "(" or token_list_type[i] == "INT:":
        additiveExpression()
    elif token_list_type[i] == "ID:":
        # consume ID
        i = i + 1
        simpleExpressionPrimePrimePrime()
    else:
        exitProgram()

# simpleExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
def simpleExpressionPrimePrimePrime():
    global i
    if token_list_value[i] == "(":
        factorPrime()
        term()
        additiveExpressionPrime()
    elif token_list_value[i] in ["[", "*", "/", "+", "-"]:
        var()
        term()
        additiveExpressionPrime()
    elif token_list_value[i] in [",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# relop() -> <= | < | > | >= | == | !=
def relop():
    global i
    if token_list_value[i] in ["<=", "<", ">", ">=", "==", "!="]:
        # consume the token
        i = i + 1
    else:
        exitProgram()

# additiveExpression() -> factor() term() additiveExpressionPrime()
def additiveExpression():
    global i
    if token_list_value[i] == "(" or token_list_type[i] == "INT:":
        factor()
        term()
        additiveExpressionPrime()
    else:
        exitProgram()

# additiveExpressionPrime() -> addop() additiveExpressionPrimePrime() | EPSILON
def additiveExpressionPrime():
    global i
    if token_list_value[i] in ["+", "-"]:
        addop()
        additiveExpressionPrimePrime()
    # next token in follow(additiveExpressionPrime())
    elif token_list_value[i] in ["<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        #print("please work")
        exitProgram()

# additiveExpressionPrimePrime() -> factor() term() additiveExpressionPrime() | ID additiveExpressionPrimePrimePrime()
def additiveExpressionPrimePrime():
    global i
    if token_list_value[i] == "(" or token_list_type[i] == "INT:":
        factor()
        term()
        additiveExpressionPrime()
    elif token_list_type[i] == "ID:":
        # consume ID
        i = i + 1
        additiveExpressionPrimePrimePrime()
    # elif token_list_value[i] in ["(", "[", "+", "-", "*", "/"]:
    #     additiveExpressionPrimePrimePrime()
    else:
        exitProgram()

# additiveExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime() ****
def additiveExpressionPrimePrimePrime():
    global i
    # if next token in first(factorPrime())
    if token_list_value[i] == "(":
        factorPrime()
        term()
        additiveExpressionPrime()
    elif token_list_value[i] in ["[", "*", "/", "+", "-"]:
        var()
        term()
        additiveExpressionPrime()
    # include epsilon transition because var(), term(), and addExpPrime() can be null <=, <, >, >=, ==, !=, ,, ), ], ;
    elif token_list_value[i] in ["<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# addop() -> + | -
def addop():
    global i
    if token_list_value[i] == "+":
        # consume "+"
        i = i + 1
    elif token_list_value[i] == "-":
        # consume "-"
        i = i + 1
    else:
        exitProgram()

# term() -> mulop() termPrime() | EPSILON
# A butt lives here
def term():
    global i
    # if next token in first(mulop())
    if token_list_value[i] in ["*", "/"]:
        mulop()
        termPrime()
    # elif next token in follow(term()) +, -, <=, <, >, >=, ==, !=, ,, ), ], ;
    elif token_list_value[i] in ["+", "-", "<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        #print("please work")
        exitProgram()

# termPrime() -> factor() term() | ID termPrimePrime()
def termPrime():
    global i
    # if next token in first(factor())
    if token_list_value[i] == "(" or token_list_type[i] == "INT:":
        factor()
        term()
    elif token_list_type[i] == "ID:":
        # consume ID
        i = i + 1
        termPrimePrime()
    else:
        exitProgram()

# termPrimePrime() -> factorPrime() term() | var() term()
def termPrimePrime():
    global i
    if token_list_value[i] == "(":
        factorPrime()
        term()
    elif token_list_value[i] in ["[", "*", "/"]:
        var()
        term()
    # include follow(termPrimePrime()) +, -, <=, <, >, >=, ==, !=, ,, ), ], ;
    elif token_list_value in ["+", "-", "<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        exitProgram()

# mulop() -> * | /
def mulop():
    global i
    if token_list_value[i] == "*":
        # consume "*"
        i = i + 1
    elif token_list_value[i] == "/":
        # consume "/"
        i = i + 1
    else:
        exitProgram()

# factor() -> ( expression() ) | NUM ****
def factor():
    global i
    if token_list_value[i] == "(":
        # consume "("
        i = i + 1
        expression()
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
    elif token_list_type[i] == "INT:":
        # consume NUM
        i = i + 1
    else:
        exitProgram()

# factorPrime() -> ( args() )
def factorPrime():
    global i
    if token_list_value[i] == "(":
        # consume "("
        i = i + 1
        args()
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
    else:
        exitProgram()

# args() -> expression() argList() | EPSILON
def args():
    global i
    if token_list_value[i] == "(" or token_list_type[i] in ["ID:", "INT:"]:
        expression()
        argList()
    # elif next token in follow(args())
    elif token_list_value[i] == ")":
        return
    else:
        exitProgram()

# argList() -> , expression() argList() | EPSILON
def argList():
    global i
    if token_list_value[i] == ",":
        i = i + 1
        expression()
        argList()
    elif token_list_value[i] == ")":
        return
    else:
        exitProgram()

# start parser
program()

# program only accepted in declarationList() everywhere else returns ($ is in follow set)

# program() -> declaration() declarationList()
# declaration() -> int ID declarationPrime() | void ID declarationPrime()
# declarationPrime() -> funDeclaration() | varDeclaration()
# declarationList() -> declaration() declarationList() | EPSILON
# funDeclaration() -> ( params() ) compoundStmt()
# varDeclaration() -> ; | [ NUM ] ;
# params() -> void paramsPrime() | int paramsPrime()
# paramsPrime() -> ID param() paramList() | EPSILON
# paramList() -> , paramListPrime() | EPSILON
# paramListPrime() -> int ID param() paramList() | void ID param() paramList()
# param() -> [ ] | EPSILON
# compoundStmt() -> { localDeclarations() statementList() }
# localDeclarations() -> int ID varDeclaration() localDeclarations() | void ID varDeclaration() localDeclarations() | EPSILON
# statementList() -> statement() statementList() | EPSILON
# statement() -> expressionStmt() | compoundStmt() | selectionStmt() | iterationStmt() | returnStmt()
# expressionStmt() -> expression() ; | ;
# selectionStmt() -> if ( expression() ) statement() selectionStmtPrime()
# selectionStmtPrime() -> else statement() | EPSILON
# iterationStmt() -> while ( expression() ) statement()
# returnStmt() -> return returnStmtPrime()
# returnStmtPrime() -> ; | expression() ;
# expression() -> ID expressionPrime() | simpleExpression()
# expressionPrime() -> var() expressionPrimePrime() | factorPrime() term() additiveExpressionPrime() simpleExpressionPrime()
# expressionPrimePrime() -> = expression() | term() additiveExpressionPrime() simpleExpressionPrime()
# var() -> [ expression() ] | EPSILON
# simpleExpression() -> additiveExpression() simpleExpressionPrime()
# simpleExpressionPrime() -> relop() simpleExpressionPrimePrime() | EPSILON
# simpleExpressionPrimePrime() -> additiveExpression() | ID simpleExpressionPrimePrimePrime()
# simpleExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# relop() -> <= | < | > | >= | == | !=
# additiveExpression() -> factor() term() additiveExpressionPrime()
# additiveExpressionPrime() -> addop() additiveExpressionPrimePrime() | EPSILON
# additiveExpressionPrimePrime() -> factor() term() additiveExpressionPrime() | ID additiveExpressionPrimePrimePrime()
# additiveExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# addop() -> + | -
# term() -> mulop() termPrime() | EPSILON
# termPrime() -> factor() term() | ID termPrimePrime()
# termPrimePrime() -> factorPrime() term() | var() term()
# mulop() -> * | /
# factor() -> ( expression() ) | NUM
# factorPrime() -> ( args() )
# args() -> expression() argList() | EPSILON
# argList() -> , expression() argList() | EPSILON