# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var_declaration.
    def visitVar_declaration(self, ctx:MCParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#primi_type.
    def visitPrimi_type(self, ctx:MCParser.Primi_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#var.
    def visitVar(self, ctx:MCParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_declaration.
    def visitFunc_declaration(self, ctx:MCParser.Func_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#func_type.
    def visitFunc_type(self, ctx:MCParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_list.
    def visitPara_list(self, ctx:MCParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para_declaration.
    def visitPara_declaration(self, ctx:MCParser.Para_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#stmt.
    def visitStmt(self, ctx:MCParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block_stmt.
    def visitBlock_stmt(self, ctx:MCParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#body.
    def visitBody(self, ctx:MCParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_stmt.
    def visitIf_stmt(self, ctx:MCParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#dowhile_stmt.
    def visitDowhile_stmt(self, ctx:MCParser.Dowhile_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_stmt.
    def visitFor_stmt(self, ctx:MCParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_stmt.
    def visitBreak_stmt(self, ctx:MCParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MCParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_stmt.
    def visitReturn_stmt(self, ctx:MCParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr1.
    def visitExpr1(self, ctx:MCParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr2.
    def visitExpr2(self, ctx:MCParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr3.
    def visitExpr3(self, ctx:MCParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr4.
    def visitExpr4(self, ctx:MCParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr5.
    def visitExpr5(self, ctx:MCParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr6.
    def visitExpr6(self, ctx:MCParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr7.
    def visitExpr7(self, ctx:MCParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr8.
    def visitExpr8(self, ctx:MCParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr9.
    def visitExpr9(self, ctx:MCParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#literal.
    def visitLiteral(self, ctx:MCParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#call_expr.
    def visitCall_expr(self, ctx:MCParser.Call_exprContext):
        return self.visitChildren(ctx)



del MCParser