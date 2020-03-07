%{
#include "myp3.tab.h"
extern int yyval;
%}
cmp     ["<"|">"|"<>"|"<="|">="|"="]
num     [0-9]
kw      ["CNO"|"CITY"|"CNAME"|"SNO"|"PNO"|"TQTY"|"SNAME"|"QUOTA"|"PNAME"|"COST"|"AVQTY"|"S#"|"STATUS"|"P#"|"COLOR"|"WEIGHT"|"QTY"|"S"|"P"|"SP"|"PRDCT"|"CUST"|"ORDERS"|"UNION"|"INTERSECT"|"MINUS"|"TIMES"|"JOIN"|"DIVIDEBY"]
sc      ["\{"|"\}"|"\["|"\]"|"\("|"\)"|","]
%%
"CNO" {return(CNO);}
"CITY"
"CNAME"
"SNO"
"PNO"
"TQTY"
"SNAME"
"QUOTA"
"PNAME"
"COST"
"AVQTY"
"S#"
"STATUS"
"P#"
"COLOR"
"WEIGHT"
"QTY"
"S"
"P"
"SP"
"PRDCT"
"CUST"
"ORDERS"
"UNION"
"INTERSECT"
"MINUS"
"TIMES"
"JOIN"
"DIVIDEBY"
{cmp}   {return(CMP);}
{num}   {return(NUM);}
{kw}   {return(KW);}
{sc}   {return(SC);}
