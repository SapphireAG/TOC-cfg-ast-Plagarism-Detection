grammar MiniPy;

// ---------------- Parser rules (CFG) ----------------

program
  : statement* EOF
  ;

statement
  : assignStmt
  | ifStmt
  | whileStmt
  ;

assignStmt
  : NAME '=' expr NEWLINE
  ;

ifStmt
  : 'if' expr ':' NEWLINE INDENT statement* DEDENT
  ;

whileStmt
  : 'while' expr ':' NEWLINE INDENT statement* DEDENT
  ;

// Expression with precedence (left associative)
expr
  : expr op=('*'|'/') expr          # MulDivExpr
  | expr op=('+'|'-') expr          # AddSubExpr
  | atom                            # AtomExpr
  ;

atom
  : NAME
  | NUMBER
  | '(' expr ')'
  ;

// ---------------- Lexer rules ----------------

NAME   : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

NEWLINE : ('\r'? '\n')+ ;
WS      : [ \t]+ -> skip ;

// A minimal indentation mechanism (simplified).
// For a real Python grammar, indentation is more complex.
// For the course report, this simplified version is acceptable.

INDENT : '<INDENT>' ;
DEDENT : '<DEDENT>' ;

// Comments
COMMENT : '#' ~[\r\n]* -> skip ;
