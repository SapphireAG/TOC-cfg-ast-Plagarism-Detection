# Generated from MiniPy.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniPyParser import MiniPyParser
else:
    from MiniPyParser import MiniPyParser

# This class defines a complete generic visitor for a parse tree produced by MiniPyParser.

class MiniPyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniPyParser#program.
    def visitProgram(self, ctx:MiniPyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#statement.
    def visitStatement(self, ctx:MiniPyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniPyParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#ifStmt.
    def visitIfStmt(self, ctx:MiniPyParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#whileStmt.
    def visitWhileStmt(self, ctx:MiniPyParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MiniPyParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#AtomExpr.
    def visitAtomExpr(self, ctx:MiniPyParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniPyParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniPyParser#atom.
    def visitAtom(self, ctx:MiniPyParser.AtomContext):
        return self.visitChildren(ctx)



del MiniPyParser