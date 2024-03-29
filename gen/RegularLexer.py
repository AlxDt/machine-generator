# Generated from C:/Users/user/PycharmProjects/MachineGenerator\Regular.g4 by ANTLR 4.7.2
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write(" \b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\33\n")
        buf.write("\7\r\7\16\7\34\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\3\2\4\5\2\62;C\\c|\5\2\13\f\16\17\"\"\2 \2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\3\17\3\2\2\2\5\21\3\2\2\2\7\23\3\2\2\2\t\25\3")
        buf.write("\2\2\2\13\27\3\2\2\2\r\32\3\2\2\2\17\20\t\2\2\2\20\4\3")
        buf.write("\2\2\2\21\22\7~\2\2\22\6\3\2\2\2\23\24\7,\2\2\24\b\3\2")
        buf.write("\2\2\25\26\7*\2\2\26\n\3\2\2\2\27\30\7+\2\2\30\f\3\2\2")
        buf.write("\2\31\33\t\3\2\2\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36\37\b\7\2\2\37\16\3")
        buf.write("\2\2\2\4\2\34\3\b\2\2")
        return buf.getvalue()


class RegularLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    ALPHABET = 1
    OR = 2
    KLEENE_STAR = 3
    L_PARENTHESIS = 4
    R_PARENTHESIS = 5
    WS = 6

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'|'", "'*'", "'('", "')'"]

    symbolicNames = ["<INVALID>",
                     "ALPHABET", "OR", "KLEENE_STAR", "L_PARENTHESIS", "R_PARENTHESIS",
                     "WS"]

    ruleNames = ["ALPHABET", "OR", "KLEENE_STAR", "L_PARENTHESIS", "R_PARENTHESIS",
                 "WS"]

    grammarFileName = "Regular.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
