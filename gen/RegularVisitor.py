# Generated from C:/Users/user/PycharmProjects/MachineGenerator\Regular.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RegularParser import RegularParser
else:
    from RegularParser import RegularParser


# This class defines a complete generic visitor for a parse tree produced by RegularParser.

class RegularVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RegularParser#language.
    def visitLanguage(self, ctx: RegularParser.LanguageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RegularParser#term.
    def visitTerm(self, ctx: RegularParser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RegularParser#symbol.
    def visitSymbol(self, ctx: RegularParser.SymbolContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RegularParser#parenthesizedLanguage.
    def visitParenthesizedLanguage(self, ctx: RegularParser.ParenthesizedLanguageContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RegularParser#kleeneClosure.
    def visitKleeneClosure(self, ctx: RegularParser.KleeneClosureContext):
        return self.visitChildren(ctx)


del RegularParser
