# Generated from C:/Users/user/PycharmProjects/MachineGenerator\Regular.g4 by ANTLR 4.7.2
# encoding: utf-8
import sys
from io import StringIO

from antlr4 import *
from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\3\3\3\3\3\6\3\30\n\3\r")
        buf.write("\3\16\3\31\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\5\6$\n\6\3")
        buf.write("\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\'\2\f\3\2\2\2\4\27\3")
        buf.write("\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n#\3\2\2\2\f\21\5\4\3")
        buf.write("\2\r\16\7\4\2\2\16\20\5\4\3\2\17\r\3\2\2\2\20\23\3\2\2")
        buf.write("\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2")
        buf.write("\2\2\24\30\5\6\4\2\25\30\5\b\5\2\26\30\5\n\6\2\27\24\3")
        buf.write("\2\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27")
        buf.write("\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\34\7\3\2\2\34\7")
        buf.write("\3\2\2\2\35\36\7\6\2\2\36\37\5\2\2\2\37 \7\7\2\2 \t\3")
        buf.write("\2\2\2!$\5\6\4\2\"$\5\b\5\2#!\3\2\2\2#\"\3\2\2\2$%\3\2")
        buf.write("\2\2%&\7\5\2\2&\13\3\2\2\2\6\21\27\31#")
        return buf.getvalue()


class RegularParser(Parser):
    grammarFileName = "Regular.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "'|'", "'*'", "'('", "')'"]

    symbolicNames = ["<INVALID>", "ALPHABET", "OR", "KLEENE_STAR", "L_PARENTHESIS",
                     "R_PARENTHESIS", "WS"]

    RULE_language = 0
    RULE_term = 1
    RULE_symbol = 2
    RULE_parenthesizedLanguage = 3
    RULE_kleeneClosure = 4

    ruleNames = ["language", "term", "symbol", "parenthesizedLanguage",
                 "kleeneClosure"]

    EOF = Token.EOF
    ALPHABET = 1
    OR = 2
    KLEENE_STAR = 3
    L_PARENTHESIS = 4
    R_PARENTHESIS = 5
    WS = 6

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class LanguageContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegularParser.TermContext)
            else:
                return self.getTypedRuleContext(RegularParser.TermContext, i)

        def OR(self, i: int = None):
            if i is None:
                return self.getTokens(RegularParser.OR)
            else:
                return self.getToken(RegularParser.OR, i)

        def getRuleIndex(self):
            return RegularParser.RULE_language

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLanguage"):
                return visitor.visitLanguage(self)
            else:
                return visitor.visitChildren(self)

    def language(self):

        localctx = RegularParser.LanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_language)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.term()
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == RegularParser.OR:
                self.state = 11
                self.match(RegularParser.OR)
                self.state = 12
                self.term()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegularParser.SymbolContext)
            else:
                return self.getTypedRuleContext(RegularParser.SymbolContext, i)

        def parenthesizedLanguage(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegularParser.ParenthesizedLanguageContext)
            else:
                return self.getTypedRuleContext(RegularParser.ParenthesizedLanguageContext, i)

        def kleeneClosure(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(RegularParser.KleeneClosureContext)
            else:
                return self.getTypedRuleContext(RegularParser.KleeneClosureContext, i)

        def getRuleIndex(self):
            return RegularParser.RULE_term

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitTerm"):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)

    def term(self):

        localctx = RegularParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.symbol()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.parenthesizedLanguage()
                    pass

                elif la_ == 3:
                    self.state = 20
                    self.kleeneClosure()
                    pass

                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == RegularParser.ALPHABET or _la == RegularParser.L_PARENTHESIS):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SymbolContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHABET(self):
            return self.getToken(RegularParser.ALPHABET, 0)

        def getRuleIndex(self):
            return RegularParser.RULE_symbol

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitSymbol"):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)

    def symbol(self):

        localctx = RegularParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(RegularParser.ALPHABET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParenthesizedLanguageContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PARENTHESIS(self):
            return self.getToken(RegularParser.L_PARENTHESIS, 0)

        def language(self):
            return self.getTypedRuleContext(RegularParser.LanguageContext, 0)

        def R_PARENTHESIS(self):
            return self.getToken(RegularParser.R_PARENTHESIS, 0)

        def getRuleIndex(self):
            return RegularParser.RULE_parenthesizedLanguage

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParenthesizedLanguage"):
                return visitor.visitParenthesizedLanguage(self)
            else:
                return visitor.visitChildren(self)

    def parenthesizedLanguage(self):

        localctx = RegularParser.ParenthesizedLanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parenthesizedLanguage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(RegularParser.L_PARENTHESIS)
            self.state = 28
            self.language()
            self.state = 29
            self.match(RegularParser.R_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KleeneClosureContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KLEENE_STAR(self):
            return self.getToken(RegularParser.KLEENE_STAR, 0)

        def symbol(self):
            return self.getTypedRuleContext(RegularParser.SymbolContext, 0)

        def parenthesizedLanguage(self):
            return self.getTypedRuleContext(RegularParser.ParenthesizedLanguageContext, 0)

        def getRuleIndex(self):
            return RegularParser.RULE_kleeneClosure

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitKleeneClosure"):
                return visitor.visitKleeneClosure(self)
            else:
                return visitor.visitChildren(self)

    def kleeneClosure(self):

        localctx = RegularParser.KleeneClosureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_kleeneClosure)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RegularParser.ALPHABET]:
                self.state = 31
                self.symbol()
                pass
            elif token in [RegularParser.L_PARENTHESIS]:
                self.state = 32
                self.parenthesizedLanguage()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 35
            self.match(RegularParser.KLEENE_STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
