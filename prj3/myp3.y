%{
    #include <stdio.h>
    #include <stdlib.h>
    extern yylex();
    extern yytext[];
    extern FILE *yyin;
%}

%start start
%token LT
%token GT
%token LTGT
%token LTE 
%token GTE 
%token EQ 
%token NUM 
%token LBRC 
%token RBRC 
%token LBRK 
%token RBRK 
%token LP 
%token RP 
%token CMMA 
%token RENAME 
%token AS 
%token WHERE 
%token CNO 
%token CITY 
%token CNAME 
%token SNO 
%token PNO 
%token TQTY 
%token SNAME 
%token QUOTA 
%token PNAME 
%token COST 
%token AVQTY 
%token SS 
%token STATUS 
%token PP 
%token COLOR 
%token WEIGHT 
%token QTY 
%token S 
%token P 
%token SP 
%token PRDCT 
%token CUST
%token ORDERS
%token UNION
%token INTERSECT
%token MINUS
%token TIMES
%token JOIN
%token DIVIDEBY
%%

start : expression {};
expression  : oneRelationExpression {};
            | twoRelationExpression {};
oneRelationExpression   : renaming {};
                        | restriction {};
                        | projection {};
renaming : term RENAME attribute AS attribute {};
term  : relation {};
      | LP expression RP
restriction : term WHERE comparison {};
projection  : term {};
            | LBRK attributeCommalist RBRK
attributeCommalist   : attribute {};
                     | attribute CMMA attributeCommalist {};
twoRelationExpression   : projection binaryOperation expression {};
binaryOperation   : UNION
                  | INTERSECT
                  | MINUS
                  | TIMES
                  | JOIN
                  | DIVIDEBY
comparison  : attribute compare number {};
compare  : LT
         | GT
         | LTE
         | GTE
         | EQ
         | LTGT
number   : val
         | val number {};
val   : NUM
attribute   : CNO
            | CITY
            | CNAME
            | SNO
            | PNO
            | TQTY
            | SNAME
            | QUOTA
            | PNAME
            | COST
            | AVQTY
            | SS
            | STATUS
            | PP
            | COLOR
            | WEIGHT
            | QTY
relation : S
         | P
         | SP
         | PRDCT
         | CUST
         | ORDERS
%%
int main(int argc, char *argv[])
{
   yyin = fopen(argv[1], "r");
   if (!yyin)
   {
      printf("no file\n");
      exit(0);
   }
   yyparse();
   printf("\nACCEPT\n");
}
yyerror()
{
   printf("error from yyerror\n");
   exit(0);
}
yywrap()
{
   printf("\nin yywrap\n");
   exit(0);
}
