import sys
import re as re
import scanner
import os

# elif token_list_value[i] == ";":
#     return

# added to expressionPrime() and additiveExpressionPrimePrimePrime()
# seems to fix issue with expressions -> semicolons were rejected
# rejects "=" in expressions -> ex. a + b = c;

# call scanner to generate token list
scanner.scanner()
#print("- - - - - - - - - - - - - - - - - - - - - - -")
# keep track of current token being evaluated
global i
i = 0
# list of tokens' value
token_list_value = []
# list of token types (same size as token_value_list)
token_list_type = []
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
#print(len(token_list_type))
#print(len(token_list_value))
#print(token_list_value)
#print(token_list_type)

def exitProgram():
    global i
    #print(i)
    print("REJECT")
    # identify token type that caused the error (for testing)
    print("error at " + token_list_value[i])
    exit()

# program() -> declaration() declarationList()
def program():
    global i
    #print(i)
    declaration()
    declarationList()

# declaration() -> int ID declarationPrime() | void ID declarationPrime()
def declaration():
    global i
    #print(i)
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
            # consume 
            print("I am in declaration() and my token is: " + token_list_value[i])
            i = i + 1
            print("I am in declaration() and my token is: " + token_list_value[i])
            declarationPrime()
    elif token_list_value[i] == "void":
        # consume "void"
        i = i + 1
        #print(i)
        if token_list_type[i] == "ID:":
            print("I am in declaration() and my token is: " + token_list_value[i])
            # consume ID
            i = i + 1
            print("I am in declaration() and my token is: " + token_list_value[i])
            declarationPrime()
        else:
            exitProgram()
    else:
        exitProgram()

# declarationPrime() -> funDeclaration() | varDeclaration()  
def declarationPrime():
    global i
    #print(i)
    # look 1 symbol ahead to decide which function to call
    if token_list_value[i] == "(":
        funDeclaration()
    elif token_list_value[i] in [";", "["]:
        print("I am in declarationPrime() and my token is: " + token_list_value[i])
        varDeclaration()
    else:
        exitProgram()

# declarationList() -> declaration() declarationList() | EPSILON
def declarationList():
    global i
    print("I am in declarationList() and my token is: " + token_list_value[i])
    if token_list_value[i] in ["int", "void"]:
        declaration()
        declarationList()
    # if rule contains empty, check first of follow sets e.g. first of follow set of declarationList is "$"
    # if we hit dollar sign we accept
    elif token_list_value[i] in "$":
        print("ACCEPT")
        exit()
    else:
        exitProgram()

# funDeclaration() -> ( params() ) compoundStmt() 
def funDeclaration():
    global i
    if token_list_value[i] == "(":
        # consume "("
        i = i + 1
        print("I am in funDeclaration() and my token is: " + token_list_value[i])
        params()
        print("I am in funDeclaration() and my token is: " + token_list_value[i])
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
            print("I am in funDeclaration() and my token is: " + token_list_value[i])
            compoundStmt()
    else:
        exitProgram()

# varDeclaration() -> ; | [ NUM ] ;
def varDeclaration():
    global i
    print("I am in varDeclaration() and my token is: " + token_list_value[i])
    if token_list_value[i] == ";":
        # consume ";"
        i = i + 1
    elif token_list_value[i] == "[":
        # consume "["
        i = i + 1
        if token_list_type[i] == "INT:":
            # consume NUM
            i = i + 1
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
    #print("I am in params() and my token is: " + token_list_value[i])
    if token_list_value[i] == "void":
        # consume "void"
        i = i + 1
        paramsPrime()
    elif token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        print("I am in params() and my token is: " + token_list_value[i])
        paramsPrime()
    else:
        print("error here")
        exitProgram()

# paramsPrime() -> ID param() paramList() | EPSILON
def paramsPrime():
    global i
    print("I am in paramsPrime() and my token type is: " + token_list_type[i])
    if token_list_type[i] == "ID:": 
        # consume ID:
        i = i + 1
        print("I am in paramsPrime() and my token is: " + token_list_value[i])
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
    if token_list_value[i] == ",":
        # consume ","
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
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
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
    if token_list_value[i] == "[":
        # consume "["
        i = i + 1
        if token_list_value[i] == "]":
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
    if token_list_value[i] == "{":
        # consume "{"
        i = i + 1
        print("I am in compoundStmt() and my token is: " + token_list_value[i])
        localDeclarations()
        print("I am in compoundStmt() and my token is: " + token_list_value[i])
        statementList()
        print("I am in compoundStmt() and my token is: " + token_list_value[i])

        if token_list_value[i] == "}":
            #print("I am in compoundStmt() and my token is: " + token_list_value[i])
            # consume "}"
            i = i + 1
    else:
        exitProgram()

# localDeclarations() -> int ID varDeclaration() localDeclarations() | void ID varDeclaration() localDeclarations() | EPSILON
def localDeclarations():
    global i
    print(token_list_type[i])
    if token_list_value[i] == "int":
        # consume "int"
        i = i + 1
        if token_list_type[i] == "ID:":
            # consume ID
            i = i + 1
            varDeclaration()
            print("I am in localDeclarations() and my token is: " + token_list_value[i])
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
        print("I am in statementList() and my token is: " + token_list_type[i])
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
    if token_list_value[i] in [";", "("] or token_list_type[i] in ["INT:", "ID:"]:
        print("I am in statement() and my token is: " + token_list_type[i])
        expressionStmt()
        print("I am in statement() and my token is: " + token_list_value[i])
    elif token_list_value[i] == "{":
        print("I am in statement() and my token is: " + token_list_value[i])
        compoundStmt()
    elif token_list_value[i] == "if":
        #print("I am in statement() and my token is: " + token_list_value[i])
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
    #print("I am in expressionStmt() and my token is: " + token_list_type[i])
    if token_list_value[i] == "(" or token_list_type[i] in ["INT:", "ID:"]:
        print("I am in expressionStmt() and my token is: " + token_list_value[i])
        expression()
        # consume ";"
        i = i + 1
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
            print("usybecukby")
            expression()
        #print("I am in selectionStmt() and my token is: " + token_list_value[i])
        print("I am in selectionStmt() and my token is: " + token_list_value[i])
        if token_list_value[i] == ")":
            # consume ")"
            i = i + 1
            statement()
            selectionStmtPrime()
    else:
        print("this is where the error is")
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
    print("I am in expression() and my token is: " + token_list_type[i])
    if token_list_type[i] == "ID:":
        # consume ID
        i = i + 1
        print("I am in expression() and my token is: " + token_list_value[i])
        expressionPrime()
    # elif next token is in first(simpleExpression())
    elif token_list_value[i] == "(" or token_list_type[i] == "INT:":
        simpleExpression()
    else:
        exitProgram()

# expressionPrime() -> var() expressionPrimePrime() | factorPrime() term() additiveExpressionPrime() simpleExpressionPrime() ******
def expressionPrime():
    global i
    print("I am in expressionPrime() and my token value is: " + token_list_value[i])
    # if token in first(var())
    #print("I am in expressionPrime() and my token is: " + token_list_value[i])
    if token_list_value[i] in ["[", "=", "*", "/", "<=", "<", ">", ">=", "==", "!=", "+", "-"]:
        var()
        print("I am in expressionPrime() and my token is: " + token_list_value[i])
        expressionPrimePrime()
        print("I am in expressionPrime() and my token is: " + token_list_value[i])
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
    print("I am in expressionPrimePrime() and my token is: " + token_list_value[i])
    if token_list_value[i] == "=":
        # consume "="
        i = i + 1
        expression()
    # if next token is in first(term())
    elif token_list_value[i] in ["*", "/", "+", "-", "<=", "<", ">", ">=", "==", "!="]:
        term()
        print("I have just left term() and my token is " + token_list_value[i])
        additiveExpressionPrime()
        print("I have just left additiveExpressionPrime() " + token_list_value[i])
        simpleExpressionPrime()
        print("I have just left simpleExpressionPrime() " + token_list_value[i])
    else:
        print("error in expressionPrimePrime()")
        exitProgram() 

# var() -> [ expression() ] | EPSILON ***
def var():
    global i
    #print("I am in var() and my token is: " + token_list_value[i])
    if token_list_value[i] == "[":
        # consume "["
        i = i + 1
        print("I am in var() and my token is: " + token_list_value[i])
        expression()
        print(token_list_value[i])
        # consume "]"
        i = i + 1
        print(token_list_value[i])
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
        print("I am in simpleExpressionPrimePrime() and my token is " + token_list_value[i])
        simpleExpressionPrimePrimePrime()
        print("I am in simpleExpressionPrimePrime() and my token is " + token_list_value[i])
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
        print("I am in additiveExpressionPrime() and my token is " + token_list_value[i])
        addop()
        print("I am in additiveExpressionPrime() and my token is " + token_list_value[i])
        additiveExpressionPrimePrime()
        print("I have just left additiveExpressionPrimePrime and my token is: " + token_list_value[i])
    # next token in follow(additiveExpressionPrime())
    elif token_list_value[i] in ["<=", "<", ">", ">=", "==", "!=", ",", ")", "]", ";"]:
        return
    else:
        #print("please work")
        exitProgram()
    
# additiveExpressionPrimePrime() -> factor() term() additiveExpressionPrime() | ID additiveExpressionPrimePrimePrime()
def additiveExpressionPrimePrime():
    global i
    print("I am in addExpPrimePrime() and my token is " + token_list_type[i])
    if token_list_value[i] == "(" or token_list_type[i] == "INT:":
        factor()
        term()
        additiveExpressionPrime()
    elif token_list_type[i] == "ID:":
        # consume ID
        i = i + 1
        print("I am in addExpPrimePrime() and my token is " + token_list_value[i])
        additiveExpressionPrimePrimePrime()
    # elif token_list_value[i] in ["(", "[", "+", "-", "*", "/"]:
    #     additiveExpressionPrimePrimePrime()
    else:
        exitProgram()

# additiveExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime() ****
def additiveExpressionPrimePrimePrime():
    global i
    print("I am in addExprPrimePrimePrime() and my token is " + token_list_value[i])
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
        print("error in additiveExpressionPrimePrimePrime()")
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

## HE CHANGED THE GRAMMER ##
## adding empty transition in the rule for testing ##
# expression() -> ID expressionPrime() | simpleExpression()
## tried adding an empty transition production in the rule ##

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