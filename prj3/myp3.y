%{
    #include <stdio.h>
    #include <stdlib.h>
    extern yylex();
    extern yytext[];
    extern FILE *yyin;
%}

%start start
%token LT GT LTGT LTE GTE EQ NUM LBRK RBRK LP RP CMMA RENAME AS WHERE CNO CITY CNAME SNO PNO TQTY SNAME QUOTA PNAME COST AVQTY SS STATUS PP COLOR WEIGHT QTY S P SP PRDCT CUST ORDERS UNION INTERSECT MINUS TIMES JOIN DIVIDEBY
%%

start : expression {return;};

expression  : oneRelationExpression
            | twoRelationExpression

oneRelationExpression   : renaming
                        | restriction
                        | projection

renaming : term RENAME attribute AS attribute

term  : relation {return};
      | LP expression RP

restriction : term WHERE comparison

projection  : term {return};
            | term LBRK attributeCommalist RBRK

attributeCommalist   : attribute
                     | attribute CMMA attributeCommalist

twoRelationExpression   : projection binaryOperation expression

binaryOperation   : UNION {return};
                  | INTERSECT
                  | MINUS
                  | TIMES
                  | JOIN
                  | DIVIDEBY

comparison  : attribute compare number

compare  : LT {return};
         | GT
         | LTE
         | GTE
         | EQ
         | LTGT

number   : val
         | val number

val   : NUM {return};

attribute   : CNO {return};
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

relation : S {return};
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
