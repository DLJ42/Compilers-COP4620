import sys
import re as re
import scanner
import os

try:
    input_file = sys.argv[1]
except:
    print("no input file provided. Exiting...")
    exit()

scanner.scanner()
print("- - - - - - - - - - - - - - - - - - - - - - -")
with open("tokens.txt", "r") as f2:
    tokens = f2.readlines()
    for item in tokens:
        item = item.strip()
        print(item)


# program() -> declaration() declarationList()
# declarationList() -> declaraprint(tokens)tion() declarationList() | EMPTY
# declaration() -> int ID declarationPrime() | void ID declarationPrime()
# declarationPrime() -> funDeclaration() | varDeclaration()
# varDeclaration() -> ; | [ NUM ] ;
# funDeclaration() -> ( params() ) compoundStmt()
# params() -> void paramsPrime() | int paramsPrime()
# paramsPrime() -> ID param() paramList() | EMPTY
# paramList() -> , paramListPrime() | EMPTY
# paramListPrime() -> int ID param() paramList() | void ID param() paramList()
# param() -> [ ] | EMPTY
# compoundStmt() -> { localDeclarations() statementList() }
# localDeclarations() -> int ID varDeclaration() localDeclarations() | void ID varDeclaration() localDeclarations() | EMPTY
# statementList() -> statement() statementList() | EMPTY
# statement() -> expressionStmt() | compoundStmt() | selectionStmt() | iterationStmt() | returnStmt()
# expressionStmt() -> expression() ; | ;
# selectionStmt() -> if ( expression() ) statement() selectionStmtPrime()
# selectionStmtPrime() -> else statement() | EMPTY
# iterationStmt() -> while ( expression() ) statement()
# returnStmt() -> return returnStmtPrime()
# returnStmtPrime() -> ; | expression() ;
# expression() -> ID expressionPrime() | simpleExpression()
# expressionPrime() -> var() expressionPrimePrime() | factorPrime() term() additiveExpressionPrime() simpleExpressionPrime()
# expressionPrimePrime() -> = expression() | term() additiveExpressionPrime() simpleExpressionPrime()
# var() -> [ expression() ] | EMPTY
# simpleExpression() -> additiveExpression() simpleExpressionPrime()
# simpleExpressionPrime() -> relop() simpleExpressionPrimePrime() | EMPTY
# simpleExpressionPrimePrime() -> additiveExpression() | ID simpleExpressionPrimePrimePrime()
# simpleExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# relop() -> <= | < | > | >= | == | !=
# additiveExpression() -> factor() term() additiveExpressionPrime()
# additiveExpressionPrime() -> addop() additiveExpressionPrimePrime() | EMPTY
# additiveExpressionPrimePrime() -> factor() term() additiveExpressionPrime() | ID additiveExpressionPrimePrimePrime()
# additiveExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# addop() -> + | -
# term() -> mulop() termPrime() | EMPTY
# termPrime() -> factor() term() | ID termPrimePrime()
# termPrimePrime() -> factorPrime() term() | var() term()
# mulop() -> * | /
# factor() -> ( expression() ) | NUM
# factorPrime() -> ( args() )
# args() -> expression() argList() | EMPTY
# argList() -> , expression() argList() | EMPTY