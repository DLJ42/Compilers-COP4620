
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     LT = 258,
     GT = 259,
     LTGT = 260,
     LTE = 261,
     GTE = 262,
     EQ = 263,
     NUM = 264,
     LBRC = 265,
     RBRC = 266,
     LBRK = 267,
     RBRK = 268,
     LP = 269,
     RP = 270,
     CMMA = 271,
     RENAME = 272,
     AS = 273,
     WHERE = 274,
     CNO = 275,
     CITY = 276,
     CNAME = 277,
     SNO = 278,
     PNO = 279,
     TQTY = 280,
     SNAME = 281,
     QUOTA = 282,
     PNAME = 283,
     COST = 284,
     AVQTY = 285,
     SS = 286,
     STATUS = 287,
     PP = 288,
     COLOR = 289,
     WEIGHT = 290,
     QTY = 291,
     S = 292,
     P = 293,
     SP = 294,
     PRDCT = 295,
     CUST = 296,
     ORDERS = 297,
     UNION = 298,
     INTERSECT = 299,
     MINUS = 300,
     TIMES = 301,
     JOIN = 302,
     DIVIDEBY = 303
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


