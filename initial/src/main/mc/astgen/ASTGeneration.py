from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
from functools import *

def repr(self):
    return self.__str__()
setattr(AST, '__repr__', repr)

class ASTGeneration(MCVisitor):

    # Program(decl: list(Decl))
    # return "Program([" + ','.join(str(i) for i in self.decl) + "])"
    def visitProgram(self, ctx: MCParser.ProgramContext):
        return Program(
            reduce(lambda lst, decl: lst + decl, [self.visit(decl) for decl in ctx.declaration()], [])
        )

    # pass
    def visitDeclaration(self, ctx: MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # VarDecl(variable: string, varType: Type)
    # return "VarDecl(" + str(self.variable) + "," + str(self.varType) + ")"
    def visitVar_declaration(self, ctx: MCParser.Var_declarationContext):
        def detach(var: MCParser.VarContext):
            var_ctx = self.visit(var)
            if var_ctx.getChildCount() == 1:
                return VarDecl(
                    var_ctx.IDENTIFIER().getText(), self.visit(ctx.primi_type())
                )
            else:
                return VarDecl(
                    var_ctx.IDENTIFIER().getText(), ArrayType(int(var_ctx.INTLIT().getText()), self.visit(ctx.primi_type()))
                )
        return list(map(detach, ctx.var()))

    def visitVar(self, ctx: MCParser.VarContext):
        return ctx

    def visitPrimi_type(self, ctx: MCParser.Primi_typeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()

    # FuncDecl(name: Id, param: list(VarDecl), returnType: Type, body: Block)
    # return "FuncDecl(" + str(self.name) + ",[" + ','.join(str(i) for i in self.param) + "]," + str(self.returnType) + "," + str(self.body) + ")"
    def visitFunc_declaration(self, ctx: MCParser.Func_declarationContext):
        return [FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.para_list()) if ctx.para_list() else [], self.visit(ctx.func_type()), self.visit(ctx.block_stmt()))]

    def visitFunc_type(self, ctx: MCParser.Func_typeContext):
        if ctx.getChildCount() == 1:
            if ctx.primi_type():
                return self.visit(ctx.primi_type())
            else:
                return VoidType()
        else:
            return ArrayPointerType(self.visit(ctx.primi_type()))

    def visitPara_list(self, ctx: MCParser.Para_listContext):
        return list(map(lambda para_decl: self.visit(para_decl), ctx.para_declaration()))

    def visitPara_declaration(self, ctx: MCParser.Para_declarationContext):
        if ctx.getChildCount() == 2:
            return VarDecl(ctx.IDENTIFIER().getText(), self.visit(ctx.primi_type()))
        else:
            return VarDecl(ctx.IDENTIFIER().getText(), ArrayPointerType(self.visit(ctx.primi_type())))

    # Block(decl: list(BlockMember))
    # return "Block([" + ','.join(str(i) for i in self.member) + "])"
    def visitBlock_stmt(self, ctx: MCParser.Block_stmtContext):
        return Block(self.visit(ctx.body())) if ctx.body() else Block([])

    def visitBody(self, ctx: MCParser.BodyContext):
        members = list(map(lambda block_mem: self.visit(block_mem), ctx.getChildren()))

        def join(mems):
            lst_of_mem = []
            for item in mems:
                if isinstance(item, list):
                    lst_of_mem += item
                else:
                    lst_of_mem.append(item)
            return lst_of_mem

        return join(members)

    def visitStmt(self, ctx: MCParser.StmtContext):
        return self.visit(ctx.getChild(0))

    # If(expr:Expr, thenStmt:Stmt, elseStmt:Stmt)
    # return "If(" + str(self.expr) + "," + str(self.thenStmt) + ("" if (self.elseStmt is None) else "," + str(self.elseStmt)) + ")"
    def visitIf_stmt(self, ctx: MCParser.If_stmtContext):
        if ctx.getChildCount() == 5:
            return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))
        else:
            return If(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))

    # DoWhile(sl:list(Stmt), exp: Expr)
    # return "Dowhile([" + ','.join(str(i) for i in self.sl) + "]," + str(self.exp) + ")"
    def visitDowhile_stmt(self, ctx: MCParser.Dowhile_stmtContext):
        return Dowhile([self.visit(stmt) for stmt in ctx.stmt()], self.visit(ctx.expr()))

    # For(expr1, expr2, expr3: Expr, loop:Stmt)
    # return "For(" + str(self.expr1) + ";" + str(self.expr2) + ";" + str(self.expr3) + ";" + str(self.loop) + ")"
    def visitFor_stmt(self, ctx: MCParser.For_stmtContext):
        return For(self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))

    # return "Break()"
    def visitBreak_stmt(self, ctx: MCParser.Break_stmtContext):
        return Break()

    # return "Continue()"
    def visitContinue_stmt(self, ctx: MCParser.Continue_stmtContext):
        return Continue()

    # Return(expr:Expr)
    # return "Return(" + ("" if (self.expr is None) else str(self.expr)) + ")"
    def visitReturn_stmt(self, ctx: MCParser.Return_stmtContext):
        return Return(self.visit(ctx.expr())) if ctx.expr() else Return()

    # BinaryOp(op:string, left:Expr, right:Expr)
    # return "BinaryOp(" + self.op + "," + str(self.left) + "," + str(self.right) + ")"
    def visitExpr(self, ctx: MCParser.ExprContext):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.ASSIGN().getText(), self.visit(ctx.expr1()), self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr1())

    def visitExpr1(self, ctx: MCParser.Expr1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.OROP().getText(), self.visit(ctx.expr1()), self.visit(ctx.expr2()))
        else:
            return self.visit(ctx.expr2())

    def visitExpr2(self, ctx: MCParser.Expr2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.ANDOP().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return self.visit(ctx.expr3())

    def visitExpr3(self, ctx: MCParser.Expr3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4(0)), self.visit(ctx.expr4(1)))
        else:
            return self.visit(ctx.expr4(0))

    def visitExpr4(self, ctx: MCParser.Expr4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr5(0)), self.visit(ctx.expr5(1)))
        else:
            return self.visit(ctx.expr5(0))

    def visitExpr5(self, ctx: MCParser.Expr5Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr5()), self.visit(ctx.expr6()))
        else:
            return self.visit(ctx.expr6())

    def visitExpr6(self, ctx: MCParser.Expr6Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr6()), self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr7())

    # UnaryOp(op: string, body: Expr)
    # return "UnaryOp(" + self.op + "," + str(self.body) + ")"
    def visitExpr7(self, ctx: MCParser.Expr7Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr7()))
        else:
            return self.visit(ctx.expr8())

    # ArrayCell(arr:Expr, idx:Expr)
    # return "ArrayCell(" + str(self.arr) + "," + str(self.idx) + ")"
    def visitExpr8(self, ctx: MCParser.Expr8Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expr9()), self.visit(ctx.expr()))
        else:
            return self.visit(ctx.expr9())

    def visitExpr9(self, ctx: MCParser.Expr9Context):
        if ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.call_expr():
            return self.visit(ctx.call_expr())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.expr())

    def visitLiteral(self, ctx: MCParser.LiteralContext):
        if ctx.BOOLLIT():
            return BooleanLiteral(True) if ctx.BOOLLIT().getText() == "true" else BooleanLiteral(False)
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        else:
            return StringLiteral(ctx.STRLIT().getText())

    # CallExpr(method:Id, param:list(Expr))
    # return "CallExpr(" + str(self.method) + ",[" + ','.join(str(i) for i in self.param) + "])"
    def visitCall_expr(self, ctx: MCParser.Call_exprContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), [] if ctx.getChildCount() == 3 else [self.visit(expr) for expr in ctx.expr()])
