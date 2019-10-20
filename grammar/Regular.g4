grammar Regular;

// PARSER RULES
language
        : term (OR term)*
        ;

term
        : (symbol | parenthesizedLanguage | kleeneClosure)+
        ;

symbol
        : ALPHABET
        ;

parenthesizedLanguage
        : L_PARENTHESIS language R_PARENTHESIS
        ;

kleeneClosure
        : (symbol | parenthesizedLanguage) KLEENE_STAR
        ;

// LEXER RULES
// Alphabet
ALPHABET
	: [a-zA-Z0-9];

// Operators
OR
        : '|';

KLEENE_STAR
        : '*';

// Structural symbols
L_PARENTHESIS
        : '(';

R_PARENTHESIS
        : ')';

// Whitespace
WS
        :  [ \t\r\n\u000C]+ -> skip
        ;
