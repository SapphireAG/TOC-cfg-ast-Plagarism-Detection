# Generated from MiniPy.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,39,8,3,10,3,12,3,
        42,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,68,8,5,10,5,12,
        5,71,9,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,79,8,6,1,6,0,1,10,7,0,2,4,6,
        8,10,12,0,2,1,0,5,6,1,0,7,8,82,0,17,1,0,0,0,2,25,1,0,0,0,4,27,1,
        0,0,0,6,32,1,0,0,0,8,45,1,0,0,0,10,58,1,0,0,0,12,78,1,0,0,0,14,16,
        3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,
        18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,0,0,0,22,26,3,4,
        2,0,23,26,3,6,3,0,24,26,3,8,4,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,
        1,0,0,0,26,3,1,0,0,0,27,28,5,11,0,0,28,29,5,1,0,0,29,30,3,10,5,0,
        30,31,5,13,0,0,31,5,1,0,0,0,32,33,5,2,0,0,33,34,3,10,5,0,34,35,5,
        3,0,0,35,36,5,13,0,0,36,40,5,15,0,0,37,39,3,2,1,0,38,37,1,0,0,0,
        39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,
        0,0,0,43,44,5,16,0,0,44,7,1,0,0,0,45,46,5,4,0,0,46,47,3,10,5,0,47,
        48,5,3,0,0,48,49,5,13,0,0,49,53,5,15,0,0,50,52,3,2,1,0,51,50,1,0,
        0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,56,1,0,0,0,55,53,
        1,0,0,0,56,57,5,16,0,0,57,9,1,0,0,0,58,59,6,5,-1,0,59,60,3,12,6,
        0,60,69,1,0,0,0,61,62,10,3,0,0,62,63,7,0,0,0,63,68,3,10,5,4,64,65,
        10,2,0,0,65,66,7,1,0,0,66,68,3,10,5,3,67,61,1,0,0,0,67,64,1,0,0,
        0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,11,1,0,0,0,71,69,
        1,0,0,0,72,79,5,11,0,0,73,79,5,12,0,0,74,75,5,9,0,0,75,76,3,10,5,
        0,76,77,5,10,0,0,77,79,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,78,74,
        1,0,0,0,79,13,1,0,0,0,7,17,25,40,53,67,69,78
    ]

class MiniPyParser ( Parser ):

    grammarFileName = "MiniPy.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'if'", "':'", "'while'", "'*'", 
                     "'/'", "'+'", "'-'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<INDENT>'", "'<DEDENT>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NAME", "NUMBER", 
                      "NEWLINE", "WS", "INDENT", "DEDENT", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignStmt = 2
    RULE_ifStmt = 3
    RULE_whileStmt = 4
    RULE_expr = 5
    RULE_atom = 6

    ruleNames =  [ "program", "statement", "assignStmt", "ifStmt", "whileStmt", 
                   "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    NAME=11
    NUMBER=12
    NEWLINE=13
    WS=14
    INDENT=15
    DEDENT=16
    COMMENT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniPyParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniPyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniPyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2068) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MiniPyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(MiniPyParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(MiniPyParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(MiniPyParser.WhileStmtContext,0)


        def getRuleIndex(self):
            return MiniPyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniPyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.assignStmt()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.ifStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MiniPyParser.NAME, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(MiniPyParser.NEWLINE, 0)

        def getRuleIndex(self):
            return MiniPyParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MiniPyParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MiniPyParser.NAME)
            self.state = 28
            self.match(MiniPyParser.T__0)
            self.state = 29
            self.expr(0)
            self.state = 30
            self.match(MiniPyParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(MiniPyParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(MiniPyParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(MiniPyParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniPyParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = MiniPyParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MiniPyParser.T__1)
            self.state = 33
            self.expr(0)
            self.state = 34
            self.match(MiniPyParser.T__2)
            self.state = 35
            self.match(MiniPyParser.NEWLINE)
            self.state = 36
            self.match(MiniPyParser.INDENT)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2068) != 0):
                self.state = 37
                self.statement()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(MiniPyParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def NEWLINE(self):
            return self.getToken(MiniPyParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(MiniPyParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(MiniPyParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniPyParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = MiniPyParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MiniPyParser.T__3)
            self.state = 46
            self.expr(0)
            self.state = 47
            self.match(MiniPyParser.T__2)
            self.state = 48
            self.match(MiniPyParser.NEWLINE)
            self.state = 49
            self.match(MiniPyParser.INDENT)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2068) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 56
            self.match(MiniPyParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniPyParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(MiniPyParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniPyParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniPyParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniPyParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniPyParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniPyParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 59
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiniPyParser.MulDivExprContext(self, MiniPyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = MiniPyParser.AddSubExprContext(self, MiniPyParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 65
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expr(3)
                        pass

             
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MiniPyParser.NAME, 0)

        def NUMBER(self):
            return self.getToken(MiniPyParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniPyParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniPyParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = MiniPyParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(MiniPyParser.NAME)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(MiniPyParser.NUMBER)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(MiniPyParser.T__8)
                self.state = 75
                self.expr(0)
                self.state = 76
                self.match(MiniPyParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




