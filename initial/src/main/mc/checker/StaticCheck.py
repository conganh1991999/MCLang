# 1710477

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype # List[Type]
        self.rettype = rettype # Type

    def __str__(self):
        return "(" + "[" + ",".join(str(i) for i in self.partype) + "]" + "," + str(self.rettype) + ")"

class Symbol:
    def __init__(self, name, mtype, called = None, value = None):
        self.name = name # string
        self.mtype = mtype # biến: Type, hàm: MType
        self.called = called # biến: None, hàm: bool
        self.value = value

    def __str__(self):
        return self.name + "," + str(self.mtype) + "," + " called = " + str(self.called)

def checkUnaryOp(tree, op, right):
    if op == "!":
        if right[0] == "BoolType":
            return ["BoolType"]
        else:
            raise TypeMismatchInExpression(tree)
    elif op == "-":
        if right[0] == "IntType":
            return ["IntType"]
        elif right[0] == "FloatType":
            return ["FloatType"]
        else:
            raise TypeMismatchInExpression(tree)

def checkBinaryOp(tree, op, left, right):
    if op == "=":
        if left[0] in ["VoidType", "ArrayType", "ArrayPointerType"]:
            raise TypeMismatchInExpression(tree)
        elif left[0] in ["BoolType", "IntType", "FloatType", "StringType"]:
            if (right[0] == left[0]) or (left[0] == "FloatType" and right[0] == "IntType"):
                return left
            else:
                raise TypeMismatchInExpression(tree)

    if left[0] == "BoolType" and right[0] == "BoolType":
        if op in ["==", "!=", "&&", "||"]:
            return ["BoolType"]
        else:
            raise TypeMismatchInExpression(tree)
    elif left[0] == "IntType":
        if op == "%":
            if right[0] == "IntType":
                return ["IntType"]
            else:
                raise TypeMismatchInExpression(tree)
        elif op in ["==", "!="]:
            if right[0] == "IntType":
                return ["BoolType"]
            else:
                raise TypeMismatchInExpression(tree)
        elif op in ["+", "-", "*", "/"]:
            if right[0] == "IntType":
                return ["IntType"]
            elif right[0] == "FloatType":
                return ["FloatType"]
            else:
                raise TypeMismatchInExpression(tree)
        elif op in ["<", "<=", ">", ">="]:
            if right[0] in ["IntType", "FloatType"]:
                return ["BoolType"]
            else:
                raise TypeMismatchInExpression(tree)
        else:
            raise TypeMismatchInExpression(tree)
    elif left[0] == "FloatType":
        if op in ["+", "-", "*", "/"]:
            if right[0] in ["IntType", "FloatType"]:
                return ["FloatType"]
            else:
                raise TypeMismatchInExpression(tree)
        elif op in ["<", "<=", ">", ">="]:
            if right[0] in ["IntType", "FloatType"]:
                return ["BoolType"]
            else:
                raise TypeMismatchInExpression(tree)
        else:
            raise TypeMismatchInExpression(tree)
    else:
        raise TypeMismatchInExpression(tree)

class StaticChecker(BaseVisitor, Utils):

    global_envi = [
    Symbol("getInt", MType([], IntType()), False),
    Symbol("putInt", MType([IntType()], VoidType()), False),
    Symbol("putIntLn", MType([IntType()], VoidType()), False),
    Symbol("getFloat", MType([], FloatType()), False),
    Symbol("putFloat", MType([FloatType()], VoidType()), False),
    Symbol("putFloatLn", MType([FloatType()], VoidType()), False),
    Symbol("putBool", MType([BoolType()], VoidType()), False),
    Symbol("putBoolLn", MType([BoolType()], VoidType()), False),
    Symbol("putString", MType([StringType()], VoidType()), False),
    Symbol("putStringLn", MType([StringType()], VoidType()), False),
    Symbol("putLn", MType([], VoidType()), False)
    ]

    def __init__(self, ast):
        # print(ast)
        # print(ast)
        # print()
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        global_decl = c[:]
        decl_start = len(c)
        # lấy tất cả các khai báo toàn cục bỏ vào global_decl
        for decl in ast.decl:
            if isinstance(decl, VarDecl):
                for i in range(len(global_decl)): # kiểm tra redeclared variable
                    if decl.variable == global_decl[i].name:
                        raise Redeclared(Variable(), decl.variable)
                global_decl.append(Symbol(decl.variable, decl.varType))
            elif isinstance(decl, FuncDecl):
                for i in range(len(global_decl)): # kiểm tra redeclared function
                    if decl.name.name == global_decl[i].name:
                        raise Redeclared(Function(), decl.name.name)
                global_decl.append(Symbol(decl.name.name, MType([x.varType for x in decl.param], decl.returnType), False))
        # kiểm tra chương trình đã có hàm main hay chưa
        main_exs = False
        for i in range(len(global_decl)):
            if global_decl[i].name == "main" and global_decl[i].called == False:
                main_exs = True
                break
        if main_exs == False:
            raise NoEntryPoint()
        # visit các khai báo
        visit_declarations = [self.visit(x, global_decl) for x in ast.decl]
        # kiểm tra các hàm đã được gọi từ hàm khác chưa (ngoại trừ main)
        for i in range(decl_start, len(global_decl)):
            if global_decl[i].called == False:
                if global_decl[i].name != "main":
                    raise UnreachableFunction(global_decl[i].name)
        # return visitProgram
        return None

    def visitFuncDecl(self, ast, c):
        local_scope = []
        inside = False # biến kiểm tra break, continue có ở trong for hay dowhile không.
        func_return = False # biến kiểm tra khả năng return của hàm
        func_name = ast.name.name # tên hàm, kiểm tra lời gọi hàm có trùng tên hàm không
        func_rtype = self.visit(ast.returnType, c) # kiểu trả về của hàm, dùng kiểm tra kiểu trong return.
        # kiểm tra redeclared parameter
        for vardecl in ast.param:
            for i in range(len(local_scope)):
                if vardecl.variable == local_scope[i].name:
                    raise Redeclared(Parameter(), vardecl.variable)
            local_scope.append(Symbol(vardecl.variable, vardecl.varType))
        # visit xuống block của function, lấy về cờ return
        func_return = self.visit(ast.body, [func_rtype, func_name, inside, c, local_scope])
        # kiểm tra cờ return
        if (func_return == False) and (func_rtype[0] != "VoidType"):
            raise FunctionNotReturn(ast.name.name)
        return None

    def visitVarDecl(self, ast, c):
        return None

    def visitBlock(self, ast, c):
        memb_return = []  # các member của block này có return được hay không?
        # visit các member
        for member in ast.member:
            if isinstance(member, VarDecl):
                for i in range(len(c[-1])):
                    if member.variable == c[-1][i].name:
                        raise Redeclared(Variable(), member.variable)
                c[-1].append(Symbol(member.variable, member.varType))
            elif isinstance(member, Block):
                new_c = c[:]
                new_c.append([]) # block mở trong block thì tạo tầm vực mới
                memb_return.append(self.visit(member, new_c))
            elif isinstance(member, (If, Dowhile, Return)):
                memb_return.append(self.visit(member, c))
            elif isinstance(member, Id):
                flag = self.visit(member, c)
                if flag == False:
                    raise Undeclared(Identifier(), member.name)
            elif isinstance(member, (Stmt, Expr)):
                ignore = self.visit(member, c)
            else:
                pass
        # end visit
        # trả về khả năng return của block
        for returnable in memb_return:
            if returnable == True:
                return True
        return False

    def visitIf(self, ast, c):
        thenelse_return = []
        stmts = []
        if ast.elseStmt:
            stmts = [ast.thenStmt, ast.elseStmt]
        else:
            stmts = [ast.thenStmt]
        # kiểm tra kiểu của biểu thức
        expr_type = self.visit(ast.expr, c)
        if expr_type[0] != "BoolType":
            raise TypeMismatchInStatement(ast)
        # visit stmt
        for stmt in stmts:
            if isinstance(stmt, Block):
                new_c = c[:]
                new_c.append([]) # block mở trong if|else thì tạo tầm vực mới
                thenelse_return.append(self.visit(stmt, new_c))
            elif isinstance(stmt, (If, Dowhile, Return)):
                thenelse_return.append(self.visit(stmt, c))
            elif isinstance(stmt, Id):
                flag = self.visit(stmt, c)
                if flag == False:
                    raise Undeclared(Identifier(), stmt.name)
            elif isinstance(stmt, (Stmt, Expr)):
                ignore = self.visit(stmt, c)
            else:
                pass
        # kiểm tra khả năng trả về
        if len(thenelse_return) <= 1: # if không else, hoặc không có phát biểu nào có khả năng trả về
            return False
        else: # if có else
            for returnable in thenelse_return:
                if returnable == False:
                    return False
            return True

    def visitFor(self, ast, c):
        new_c = c[:]
        new_c[2] = True # break và continue từ đây sẽ hợp lệ
        # kiểm tra kiểu của các biểu thức
        expr1_type = self.visit(ast.expr1, new_c)
        expr2_type = self.visit(ast.expr2, new_c)
        expr3_type = self.visit(ast.expr3, new_c)
        if expr1_type[0] != "IntType":
            raise TypeMismatchInStatement(ast)
        if expr2_type[0] != "BoolType":
            raise TypeMismatchInStatement(ast)
        if expr3_type[0] != "IntType":
            raise TypeMismatchInStatement(ast)
        # visit loop
        if isinstance(ast.loop, Block):
            newnew_c = new_c[:]
            newnew_c.append([]) # block mở trong for thì tạo tầm vực mới
            ignore = self.visit(ast.loop, newnew_c)
        elif isinstance(ast.loop, Id):
            flag = self.visit(ast.loop, new_c)
            if flag == False:
                raise Undeclared(Identifier(), ast.loop.name)
        elif isinstance(ast.loop, (Stmt, Expr)):
            ignore = self.visit(ast.loop, new_c)
        else:
            pass
        # trả về khả năng return
        return False

    def visitDowhile(self, ast, c):
        new_c = c[:]
        new_c[2] = True # break và continue từ đây sẽ hợp lệ
        mem_return = []
        # kiểm tra kiểu của biểu thức
        expr_type = self.visit(ast.exp, new_c)
        if expr_type[0] != "BoolType":
            raise TypeMismatchInStatement(ast)
        # visit
        for stmt in ast.sl:
            if isinstance(stmt, Block):
                newnew_c = new_c[:]
                newnew_c.append([]) # block mở trong dowhile thì tạo tầm vực mới
                mem_return.append(self.visit(stmt, newnew_c))
            elif isinstance(stmt, (If, Dowhile, Return)):
                mem_return.append(self.visit(stmt, new_c))
            elif isinstance(stmt, Id):
                flag = self.visit(stmt, new_c)
                if flag == False:
                    raise Undeclared(Identifier(), stmt.name)
            elif isinstance(stmt, (Stmt, Expr)):
                ignore = self.visit(stmt, new_c)
            else:
                pass
        # trả về khả năng return
        for returnable in mem_return:
            if returnable == True:
                return True
        return False

    def visitBreak(self, ast, c):
        if c[2] == False:
            raise BreakNotInLoop()
        else:
            pass
        return False

    def visitContinue(self, ast, c):
        if c[2] == False:
            raise ContinueNotInLoop()
        else:
            pass
        return False

    def visitReturn(self, ast, c):
        if c[0][0] == "VoidType":
            if ast.expr:
                raise TypeMismatchInStatement(ast)
            else:
                pass
        else:
            if ast.expr:
                return_type = self.visit(ast.expr, c)
                if len(c[0]) == 1:
                    if (return_type[0] == c[0][0]) or (c[0][0] == "FloatType" and return_type[0] == "IntType"):
                        pass
                    else:
                        raise TypeMismatchInStatement(ast)
                elif len(c[0]) == 2:
                    if return_type[0] in ["ArrayType", "ArrayPointerType"]:
                        if return_type[1] == c[0][1]:
                            pass
                        else:
                            raise TypeMismatchInStatement(ast)
                    else:
                        raise TypeMismatchInStatement(ast)
                else:
                    pass
            else:
                raise TypeMismatchInStatement(ast)
        # khả năng trả về
        return True

    def visitBinaryOp(self, ast, c):
        # kiểm tra not left value
        this_op = ast.op
        if this_op == "=":
            if isinstance(ast.left, LHS):
                pass
            else:
                raise NotLeftValue(ast.left)
        # kiểm tra tên của vế trái
        left_type = self.visit(ast.left, c)
        if left_type == False:
            raise Undeclared(Identifier(), ast.left.name)
        elif left_type[-1] == True:
            raise TypeMismatchInExpression(ast)
        else:
            pass
        # kiểm tra tên của vế phải
        right_type = self.visit(ast.right, c)
        if right_type == False:
            raise Undeclared(Identifier(), ast.right.name)
        elif right_type[-1] == True:
            raise TypeMismatchInExpression(ast)
        else:
            pass
        # get type:
        expr_type = checkBinaryOp(ast, this_op, left_type, right_type)
        return expr_type

    def visitUnaryOp(self, ast, c):
        this_op = ast.op
        right_type = self.visit(ast.body, c)
        if right_type == False:
            raise Undeclared(Identifier(), ast.body.name)
        elif right_type[-1] == True:
            raise TypeMismatchInExpression(ast)
        else:
            pass
        # get type:
        expr_type = checkUnaryOp(ast, this_op, right_type)
        return expr_type

    def visitCallExpr(self, ast, c):
        expr_type = []
        func_types = self.visit(ast.method, c)
        arg_types = []
        for expr in ast.param:
            atype = self.visit(expr, c)
            if atype == False:
                raise Undeclared(Identifier(), expr.name)
            elif atype[-1] == True:
                raise TypeMismatchInExpression(ast)
            else:
                arg_types.append(atype)
        # kiểm tra ràng buộc tên hàm
        if func_types == False:
            raise Undeclared(Function(), ast.method.name) # không tìm thấy hàm
        elif func_types[-1] != True:
            raise TypeMismatchInExpression(ast)
        else:
            expr_type = func_types[0]
            del func_types[-1]
            del func_types[0]
        # so trùng kiểu
        if len(func_types) != len(arg_types):
            raise TypeMismatchInExpression(ast)
        else:
            for i in range(len(func_types)):
                if func_types[i][0] == "ArrayPointerType":
                    if arg_types[i][0] in ["ArrayType", "ArrayPointerType"]:
                        if arg_types[i][1] == func_types[i][1]:
                            pass
                        else:
                            raise TypeMismatchInExpression(ast)
                    else:
                        raise TypeMismatchInExpression(ast)
                elif func_types[i][0] in ["BoolType", "IntType", "FloatType", "StringType"]:
                    if (arg_types[i][0] == func_types[i][0]) or (arg_types[i][0] == "IntType" and func_types[i][0] == "FloatType"):
                        pass
                    else:
                        raise TypeMismatchInExpression(ast)
                else:
                    pass
        # trả về kiểu của lời gọi hàm
        return expr_type

    def visitArrayCell(self, ast, c):
        # kiểm tra tên biểu thức ngoài
        outer_type = self.visit(ast.arr, c)
        if outer_type == False:
            raise Undeclared(Identifier(), ast.arr.name)
        elif outer_type[-1] == True:
            raise TypeMismatchInExpression(ast) # ??
        else:
            pass
        # kiểm tra tên biểu thức trong
        inner_type = self.visit(ast.idx, c)
        if inner_type == False:
            raise Undeclared(Identifier(), ast.idx.name)
        elif inner_type[-1] == True:
            raise TypeMismatchInExpression(ast)
        else:
            pass
        # so trùng kiểu
        if inner_type[0] != "IntType":
            raise TypeMismatchInExpression(ast)
        if outer_type[0] in ["ArrayType", "ArrayPointerType"]:
            expr_type = [outer_type[1]]
            return expr_type
        else:
            raise TypeMismatchInExpression(ast)

    def visitId(self, ast, c):
        decls = c[3:][::-1]
        for scope in decls:
            for symb in scope:
                if symb.name == ast.name: # tìm thấy tên khai báo
                    if symb.called == None: # là khai báo biến
                        return self.visit(symb.mtype, c) # với c[-1] là một string
                    else: # là khai báo hàm
                        if ast.name != c[1]:
                            symb.called = True
                        func_types  = []
                        func_types.append(self.visit(symb.mtype.rettype, c)) # [[return type]]
                        for paratype in symb.mtype.partype:
                            func_types.append(self.visit(paratype, c)) # [[return type], [para type], [para type], ...]
                        func_types.append(True) # [[return type], [para type], [para type], ..., True]
                        return func_types # với c[-1] là một giá trị bool = True
        return False

    def visitIntLiteral(self, ast, c):
        return ["IntType"]

    def visitFloatLiteral(self, ast, c):
        return ["FloatType"]

    def visitBooleanLiteral(self, ast, c):
        return ["BoolType"]

    def visitStringLiteral(self, ast, c):
        return ["StringType"]

    def visitIntType(self, ast, c):
        return [str(ast)] # trả về ["IntType"]

    def visitFloatType(self, ast, c):
        return [str(ast)] # trả về ["FloatType"]

    def visitBoolType(self, ast, c):
        return [str(ast)] # trả về ["BoolType"]

    def visitStringType(self, ast, c):
        return [str(ast)] # trả về ["StringType"]

    def visitVoidType(self, ast, c):
        return [str(ast)] # trả về ["VoidType"]

    def visitArrayType(self, ast, c):
        return ["ArrayType"] + self.visit(ast.eleType, c) # trả về ["ArrayType", "EleType"]

    def visitArrayPointerType(self, ast, c):
        return ["ArrayPointerType"] + self.visit(ast.eleType, c) # trả về ["ArrayPointerType", "EleType"]