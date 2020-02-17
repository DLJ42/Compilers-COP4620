# program() -> declaration() declarationList()
# declarationList() -> declaration() declarationList() | ϵ
# declaration() -> int ID declarationPrime() | void ID declarationPrime()
# declarationPrime() -> funDeclaration() | varDeclaration()
# varDeclaration() -> ; | [ NUM ] ;
# funDeclaration() -> ( params() ) compoundStmt()
# params() -> void paramsPrime() | int paramsPrime()
# paramsPrime() -> ID param() paramList() | ϵ
# paramList() -> , paramListPrime() | ϵ
# paramListPrime() -> int ID param() paramList() | void ID param() paramList()
# param() -> [ ] | ϵ
# compoundStmt() -> { localDeclarations() statementList() }
# localDeclarations() -> int ID varDeclaration() localDeclarations() | void ID varDeclaration() localDeclarations() | ϵ
# statementList() -> statement() statementList() | ϵ
# statement() -> expressionStmt() | compoundStmt() | selectionStmt() | iterationStmt() | returnStmt()
# expressionStmt() -> expression() ; | ;
# selectionStmt() -> if ( expression() ) statement() selectionStmtPrime()
# selectionStmtPrime() -> else statement() | ϵ
# iterationStmt() -> while ( expression() ) statement()
# returnStmt() -> return returnStmtPrime()
# returnStmtPrime() -> ; | expression() ;
# expression() -> ID expressionPrime() | simpleExpression()
# expressionPrime() -> var() expressionPrimePrime() | factorPrime() term() additiveExpressionPrime() simpleExpressionPrime()
# expressionPrimePrime() -> = expression() | term() additiveExpressionPrime() simpleExpressionPrime()
# var() -> [ expression() ] | ϵ
# simpleExpression() -> additiveExpression() simpleExpressionPrime()
# simpleExpressionPrime() -> relop() simpleExpressionPrimePrime() | ϵ
# simpleExpressionPrimePrime() -> additiveExpression() | ID simpleExpressionPrimePrimePrime()
# simpleExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# relop() -> <= | < | > | >= | == | !=
# additiveExpression() -> factor() term() additiveExpressionPrime()
# additiveExpressionPrime() -> addop() additiveExpressionPrimePrime() | ϵ
# additiveExpressionPrimePrime() -> factor() term() additiveExpressionPrime() | ID additiveExpressionPrimePrimePrime()
# additiveExpressionPrimePrimePrime() -> factorPrime() term() additiveExpressionPrime() | var() term() additiveExpressionPrime()
# addop() -> + | -
# term() -> mulop() termPrime() | ϵ
# termPrime() -> factor() term() | ID termPrimePrime()
# termPrimePrime() -> factorPrime() term() | var() term()
# mulop() -> * | /
# factor() -> ( expression() ) | NUM
# factorPrime() -> ( args() )
# args() -> expression() argList() | ϵ
# argList() -> , expression() argList() | ϵ