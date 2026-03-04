# Generated from MiniPy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPyParser import MiniPyParser
else:
    from MiniPyParser import MiniPyParser

# This class defines a complete listener for a parse tree produced by MiniPyParser.
class MiniPyListener(ParseTreeListener):

    # Enter a parse tree produced by MiniPyParser#program.
    def enterProgram(self, ctx:MiniPyParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniPyParser#program.
    def exitProgram(self, ctx:MiniPyParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniPyParser#statement.
    def enterStatement(self, ctx:MiniPyParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniPyParser#statement.
    def exitStatement(self, ctx:MiniPyParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniPyParser#assignStmt.
    def enterAssignStmt(self, ctx:MiniPyParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MiniPyParser#assignStmt.
    def exitAssignStmt(self, ctx:MiniPyParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MiniPyParser#ifStmt.
    def enterIfStmt(self, ctx:MiniPyParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MiniPyParser#ifStmt.
    def exitIfStmt(self, ctx:MiniPyParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MiniPyParser#whileStmt.
    def enterWhileStmt(self, ctx:MiniPyParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MiniPyParser#whileStmt.
    def exitWhileStmt(self, ctx:MiniPyParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MiniPyParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MiniPyParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MiniPyParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MiniPyParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MiniPyParser#AtomExpr.
    def enterAtomExpr(self, ctx:MiniPyParser.AtomExprContext):
        pass

    # Exit a parse tree produced by MiniPyParser#AtomExpr.
    def exitAtomExpr(self, ctx:MiniPyParser.AtomExprContext):
        pass


    # Enter a parse tree produced by MiniPyParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MiniPyParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniPyParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MiniPyParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniPyParser#atom.
    def enterAtom(self, ctx:MiniPyParser.AtomContext):
        pass

    # Exit a parse tree produced by MiniPyParser#atom.
    def exitAtom(self, ctx:MiniPyParser.AtomContext):
        pass



del MiniPyParser