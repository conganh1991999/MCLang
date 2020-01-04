// 1710477

grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text[1:]);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    elif tk == self.STRLIT:
        result = super().emit();
        result.text = result.text[1:-1];
        return result;
    else:
        return super().emit();
}

options{
	language=Python3;
}
//-----------------------------------------------------------------------------------------
/* Parser Rules */
//-----------------------------------------------------------------------------------------

// program
program: declaration+ EOF;

declaration: var_declaration | func_declaration ;

// variable declaration
var_declaration: primi_type var (COMMA var)* SEMI ;

primi_type: BOOLTYPE | INTTYPE | FLOATTYPE | STRTYPE ;

var: IDENTIFIER | (IDENTIFIER LSB INTLIT RSB) ;

// function declaration
func_declaration: func_type IDENTIFIER LB para_list? RB block_stmt ;

func_type: primi_type | VOIDTYPE | primi_type LSB RSB ;

para_list: para_declaration (COMMA para_declaration)* ;

para_declaration: primi_type IDENTIFIER (LSB RSB)? ;

// statements
stmt: block_stmt | if_stmt | dowhile_stmt | for_stmt | (expr SEMI) | break_stmt | continue_stmt | return_stmt ;

block_stmt: LP body? RP ;

body: (var_declaration | stmt)+ ;

if_stmt: IF LB expr RB stmt (ELSE stmt)? ;

dowhile_stmt: DO stmt+ WHILE expr SEMI ;

for_stmt: FOR LB expr SEMI expr SEMI expr RB stmt ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN expr? SEMI ;

// expressions

expr: expr1 ASSIGN expr
    | expr1;

expr1: expr1 OROP expr2
    | expr2;

expr2: expr2 ANDOP expr3
    | expr3;

expr3: expr4 ( EQUAL | NOTEQUAL ) expr4
    | expr4;

expr4: expr5 ( LT | LE | GT | GE ) expr5
    | expr5;

expr5: expr5 ( ADDOP | SUBOP ) expr6
    | expr6;

expr6: expr6 ( DIVOP | MULOP | MODOP ) expr7
    | expr7;

expr7: ( SUBOP | NOTOP ) expr7
    | expr8;

expr8: expr9 LSB expr RSB
    | expr9;

expr9: literal | call_expr | IDENTIFIER | LB expr RB ;

literal: BOOLLIT | INTLIT | FLOATLIT | STRLIT ;

call_expr: IDENTIFIER LB ( expr ( COMMA expr )* )? RB ;

//-----------------------------------------------------------------------------------------
/* Lexer Rules */
//-----------------------------------------------------------------------------------------

// keywords
BOOLTYPE: 'boolean' ;
INTTYPE: 'int' ;
FLOATTYPE: 'float' ;
STRTYPE: 'string' ;
VOIDTYPE: 'void' ;

IF: 'if' ;
ELSE: 'else' ;
FOR: 'for' ;
DO: 'do' ;
WHILE: 'while' ;
BREAK: 'break' ;
CONTINUE: 'continue' ;
RETURN: 'return' ;

// operators
ADDOP: '+' ;
MULOP: '*' ;
SUBOP: '-' ;
DIVOP: '/' ;
MODOP: '%' ;
NOTOP: '!' ;
ANDOP: '&&' ;
OROP: '||' ;
EQUAL: '==' ;
NOTEQUAL: '!=' ;
LT: '<' ;
GT: '>' ;
LE: '<=' ;
GE: '>=' ;
ASSIGN: '=' ;

// separators
LSB: '[' ;
RSB: ']' ;
LB: '(' ;
RB: ')' ;
LP: '{' ;
RP: '}' ;
SEMI: ';' ;
COMMA: ',' ;

// literals
BOOLLIT: 'true' | 'false' ;
INTLIT: [0-9]+ ;

fragment DOT: '.' ;
fragment EXP: ( 'e' | 'E' ) '-'? INTLIT ;
FLOATLIT: ( INTLIT? DOT INTLIT EXP? ) | ( INTLIT DOT INTLIT? EXP? ) | ( INTLIT EXP ) ;

fragment QUOTE: '"' ;
fragment IN_STRING: '\\' ('b'|'t'|'r'|'f'|'n'|'\\'|'"') ;
STRLIT: QUOTE ((~[\b\t\r\f\n"\\]) | (IN_STRING))* QUOTE ;

// identifier
fragment DIGIT: [0-9] ;
fragment LOWCASE: [a-z] ;
fragment UPCASE: [A-Z] ;
fragment IDSTART: LOWCASE | UPCASE | '_' ;

IDENTIFIER: IDSTART (IDSTART | DIGIT)* ;

// white spaces
WS: [ \t\r\f\n]+ -> skip ; // skip whitespace characters
NEWLINE: '\n' ;

// comments
fragment BLOCK_COMMENT: '/*' .*? '*/' ;
fragment LINE_COMMENT: '//' (~[\n])* ;

COMMENT: (BLOCK_COMMENT | LINE_COMMENT) -> skip ; //skip comments

//-----------------------------
ERROR_CHAR: ~ ([0-9] | [a-z] | [A-Z] | '_' | '+' | '-' | '*' | '/' | '%' | '!' | '=' | '>' | '<' | '{' | '}' | '[' | ']' | '(' | ')' | ',' | ';' | '"');
UNCLOSE_STRING: QUOTE ((~[\b\t\r\f\n"\\]) | (IN_STRING))* ;
ILLEGAL_ESCAPE: QUOTE ((~[\b\t\r\f\n"\\]) | (IN_STRING))* '\\' ~[btrfn\\"] ;