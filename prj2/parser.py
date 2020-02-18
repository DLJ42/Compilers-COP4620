import sys
import re as re
import scanner
import os

scanner.scanner()
print("- - - - - - - - - - - - - - - - - - - - - - -")
i = 0
token_list = []
with open("tokens.txt", "r") as f2:
    tokens = f2.readlines()
    for token in tokens:
        if(len(token.split(" ")) == 2):
            token = token.split(" ")[1]
        token = token.strip()
        token_list.append(token)
token_list.append("$")
print(token_list)

def exitProgram():
    global i
    print("REJECT")
    print("error at " + token_list[i])
    exit()

# program() -> declaration() declarationList()
def program():
    global i
    declaration()
    declarationList()

# declaration() -> int ID declarationPrime() | void ID declarationPrime()
def declaration():
    global i
    if token_list[i] == "int":
        i = i + 1
        # skip over ID
        i = i + 1
        declarationPrime()
    elif token_list[i] == "void":
        i = i + 1
        # skip ID
        i = i + 1
        declarationPrime()
    else:
        exitProgram()

# declarationPrime() -> funDeclaration() | varDeclaration()  
def declarationPrime():
    print("we made it")

# declarationList() -> declaration() declarationList() | EPSILON
def declarationList():
    global i
    if token_list[i] in ["int", "void"]:
        declaration()
        declarationList()
    elif token_list[i] is "$":
        print("ACCEPT")
        exit()
    else:
        exitProgram()

# start parser
program()

# program only accepted in declarationList() everywhere else returns ($ is in follow set)

# program() -> declaration() declarationList()
# declaration() -> int ID declarationPrime() | void ID declarationPrime()
# declarationPrime() -> funDeclaration() | varDeclaration()
# declarationList() -> declaration() declarationList() | EPSILON
# varDeclaration() -> ; | [ NUM ] ;
# funDeclaration() -> ( params() ) compoundStmt()
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