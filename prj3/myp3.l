%{
#include "myp3.tab.h"
extern int yylval;
%}
num     [0-9]
%%
{num} return(NUM);
"\<" return(LT);
"\>" return(GT);
"\<\>" return(LTGT);
"\<\=" return(LTE);
"\>\=" return(GTE);
"\=" return(EQ);
"\[" return(LBRK);
"\]" return(RBRK);
"\(" return(LP);
"\)" return(RP);
"," return(CMMA);
"RENAME" return(RENAME);
"AS"    return(AS);
"WHERE"  return(WHERE);
"CNO" return(CNO);
"CITY" return(CITY);
"CNAME" return(CNAME);
"SNO" return(SNO);
"PNO" return(PNO);
"TQTY" return(TQTY);
"SNAME" return(SNAME);
"QUOTA" return(QUOTA);
"PNAME" return(PNAME);
"COST" return(COST);
"AVQTY" return(AVQTY);
"S\#" return(SS);
"STATUS" return(STATUS);
"P\#" return(PP);
"COLOR" return(COLOR);
"WEIGHT" return(WEIGHT);
"QTY" return(QTY);
"S" return(S);
"P" return(P);
"SP" return(SP);
"PRDCT" return(PRDCT);
"CUST" return(CUST);
"ORDERS" return(ORDERS);
"UNION" return(UNION);
"INTERSECT" return(INTERSECT);
"MINUS" return(MINUS);
"TIMES" return(TIMES);
"JOIN" return(JOIN);
"DIVIDEBY" return(DIVIDEBY);
. return;
%%
