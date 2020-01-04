import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_no_entry_point(self):
        ip = """
        int a;
        int b;
        int c;
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(ip, expect, 400))

    def test_has_entry_point_void_main(self):
        ip = """
        int a;
        void foo(){}
        int b;
        void main(){
            foo();
        }
        int c;
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 401))

    def test_has_entry_point_int_main_with_parameters(self):
        ip = """
        int a, b, c;
        void foo(){}
        int main(int a, boolean b, float c, string d){
            foo();
            return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 402))

    def test_redeclare_global_var_after_var(self):
        ip = """
        void main(){
            foo();
        }
        int a; int b; int c;
        void foo(){}
        int a;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(ip, expect, 403))

    def test_redeclare_global_var_after_func(self):
        ip = """
        void foo(){}
        int main(){
            foo();
            return 0;
        }
        float foo;
        int a;
        """
        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(ip, expect, 404))

    def test_redeclare_func_after_var(self):
        ip = """
        int mul; int div; int add;
        void main(){}
        void add(){}
        int foo;
        """
        expect = "Redeclared Function: add"
        self.assertTrue(TestChecker.test(ip, expect, 405))

    def test_redeclare_func_after_func(self):
        ip = """
        int a;
        int main(){
            return 1;
        }
        int b;
        void main(){
            return ;
        }
        """
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(ip, expect, 406))

    def test_global_scope(self):
        ip = """
        void main(){
            mul();
        }
        int a; int b; int c;
        int mul(){
            div();
            return 0;
        }
        float d;
        float div(){
            add();
            return 0.0;
        }
        boolean e; string f;
        string add(){
            return "nothing";
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 407))

    def test_redeclare_parameter(self):
        ip = """
        int main(int a, int b, int a){
            int local;
            putInt(5);
            local = getInt();
            return local;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(ip, expect, 408))

    def test_does_not_redeclare_parameter(self):
        ip = """
        int a; int b;
        int add(int a, int b){
            return a + b;
        }
        int sub(int a, int b){
            return a - b;
        }
        int main(){
            int mul;
            a = 5;
            b = 10;
            mul = add(a, b) * sub(a, b);
            return mul;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 409))

    def test_redeclare_local_var_in_1st_scope(self):
        ip = """
        void main(){
            int a, b;
            a = 1;
            b = 1;
            foo(a, b);
        }
        int foo(int a, int b){
            int foo;
            int a;
            int c;
            return 0;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(ip, expect, 410))

    def test_redeclare_local_var_in_2nd_scope(self):
        ip = """
        int a; int b; int c;
        void main(){
            a = 7;
            b = 8;
            c = 9;
            foo(a, b, c);
        }
        void foo(int a, int b, int c){
            int d; int e;
            { int d; }
            { int d; int e;}
            { int d; int e; int d;}
            int f;
        }
        """
        expect = "Redeclared Variable: d"
        self.assertTrue(TestChecker.test(ip, expect, 411))

    def test_does_not_redeclare_local_var_in_parallel_scope(self):
        ip = """
        void main(){
            int a, b, c;
            a = b = c = 1;
            foo(a, b, c);
        }
        void foo(int a, int b, int c){
            int d; int e;
            { int f; {}}
            { int e; int f; { int f; { int e; int f; } } }
            { int e; int f; { int f; { int e; int f; } } }
            int f;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 412))

    def test_undeclared_identifier(self):
        ip = """
        int a;
        void main(){
            float b;
            b = 10.0;
            a = b + c;
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(ip, expect, 413))

    def test_does_not_undeclared_identifier_by_founding_in_outer_scope(self):
        ip = """
        int a;
        void main(int b){
            int c;
            {
                int d;
                {
                    int e;
                    {
                        int f;
                        a = 1;
                        b = 2;
                        c = 3;
                        d = 4;
                        e = 5;
                        f = 6;
                    }
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 414))

    def test_undeclared_function(self):
        ip = """
        void main(int a, int b){
            int c;
            foo();
        }
        """
        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(ip, expect, 415))

    def test_does_not_undeclared_function(self):
        ip = """
        int pow(int num){
            int exp;
            exp = num * num;
            return exp;
        }
        int main(){
            int a; int b;
            putInt(5);
            a = getInt();
            b = pow(a);
            return b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 416))

    def test_type_match_in_if_stmt(self):
        ip = """
        void main(){
            int i;
            i = 5;
            if (i < 10)
                putStringLn("i < 10");
            else
                putStringLn("i >= 10");
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 417))

    def test_type_mismatch_in_if_stmt(self):
        ip = """
        void main(){
            int i;
            i = 5;
            if (i + 10)
                putString("i < 10");
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(i),IntLiteral(10)),CallExpr(Id(putString),[StringLiteral(i < 10)]))"
        self.assertTrue(TestChecker.test(ip, expect, 418))

    def test_type_mismatch_in_another_if_stmt(self):
        ip = """
        float a;
        float main(){
            float b;
            a = b = 10.5;
            if (a >= b)
                return a;
            else
                if (a * b){}
                else {}
            return 0.0;
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,Id(a),Id(b)),Block([]),Block([]))"
        self.assertTrue(TestChecker.test(ip, expect, 419))

    def test_type_match_in_for_stmt(self):
        ip = """
        void main(){
            int i;
            for(i = 1; i < 10; i = i + 1){
                putIntLn(i);
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 420))

    def test_type_mismatch_in_expr1_in_for_stmt(self):
        ip = """
        void main(){
            float i;
            for(i = 1; i < 10; i = i + 1){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(10));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));Block([]))"
        self.assertTrue(TestChecker.test(ip, expect, 421))

    def test_type_mismatch_in_expr2_in_for_stmt(self):
        ip = """
        void main(){
            int i;
            for(i = 1; i = i + 1; i = i + 2){}
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(1)));BinaryOp(=,Id(i),BinaryOp(+,Id(i),IntLiteral(2)));Block([]))"
        self.assertTrue(TestChecker.test(ip, expect, 422))

    def test_type_mismatch_in_dowhile_stmt(self):
        ip = """
        void main(){
            int i;
            i = 10;
            do {} while (i);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(i))"
        self.assertTrue(TestChecker.test(ip, expect, 423))

    def test_type_match_in_dowhile_stmt(self):
        ip = """
        void main(){
            boolean i;
            do {} while (i = true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 424))

    def test_type_match_in_if_for_and_dowhile_stmt(self):
        ip = """
        int i;
        void main(){
            float max;
            max = 100;
            for (i = 0; i < max; i = i + 1){
                if(i == 100){
                    float precision;
                    precision = max - i;
                    do {putFloatLn(precision);} while(false);
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 425))

    def test_type_mismatch_in_return_stmt_for_void_type(self):
        ip = """
        void main(){
            return 1;
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(1))"
        self.assertTrue(TestChecker.test(ip, expect, 426))

    def test_type_mismatch_in_return_stmt_for_int_type(self):
        ip = """
        int main(){
            return ;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(ip, expect, 427))

    def test_type_match_in_return_stmts1(self):
        ip = """
        void main(){
            isbool(); add(); div(); print();
            return ;
        }
        boolean isbool(){
            return true;
        }
        int add(){
            return 1;
        }
        float div(){
            return 1;
        }
        string print(){
            return "1";
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 428))

    def test_type_mismatch_in_return_stmt_for_float_arraypointer_type(self):
        ip = """
        void main(){
            int a[5];
            float b[5];
            int_pointer(a, b);
            float_pointer_1(a, b);
            float_pointer_2(a, b);
        }
        int[] int_pointer(int a[], float b[]){
            return a; // OK
        }
        float[] float_pointer_1(int a[], float b[]){
            return b; // OK
        }
        float[] float_pointer_2(int a[], float b[]){
            return a; // error
        }
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(ip, expect, 429))

    def test_type_match_in_return_stmts2(self):
        ip = """
        void main(){
            int_pointer();
            float_pointer();
        }
        int[] int_pointer(){
            int a[5]; float b[5];
            return a; // OK
        }
        float[] float_pointer(){
            int a[5]; float b[5];
            return b; // OK
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 430))

    def test_type_mismatch_in_return_callexpr_for_int_type(self):
        ip = """
        int main(){
            return foo(); // error
        }
        float foo(){
            int a; float b;
            a = 1;
            b = 1.1;
            return a; // OK
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(ip, expect, 431))

    def test_type_match_in_return_stmts3(self):
        ip = """
        void main(){
            d_checker();
            return ;
        }
        boolean[] s_checker(){
            boolean bool_list[10];
            return bool_list;
        }
        boolean[] d_checker(){
            return s_checker();
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 432))

    def test_type_mismatch_in_unaryop_with_int_op(self):
        ip = """
        int a;
        int b;
        void main(boolean c){
            boolean d;
            a = 1; b = 1; c = true; d = false;
            a = a + b;
            c = !c;
            d = !c;
            a = !a;
            return ;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,Id(a))"
        self.assertTrue(TestChecker.test(ip, expect, 433))

    def test_type_mismatch_in_unaryop_with_bool_op_and_callexpr(self):
        ip = """
        int a; float b;
        int foo(){
            return 1;
        }
        boolean boo(){
            return true;
        }
        void main(boolean c){
            a = 2;
            b = -(foo() + a);
            c = -boo();
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,CallExpr(Id(boo),[]))"
        self.assertTrue(TestChecker.test(ip, expect, 434))

    def test_type_mismatch_in_unaryop_with_bool_op_and_var(self):
        ip = """
        int a; float b; boolean c;
        void main(){
            a = 1; b = 1.0; c = false;
            c = !!!!!!!!!!!c;
            a = -----------a;
            b = -----------b;
            c = -----------c;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(c))"
        self.assertTrue(TestChecker.test(ip, expect, 435))

    def test_type_mismatch_in_unaryop_with_string_op_and_var(self):
        ip = """
        void main(){
            string name;
            name = "Nguyen Cong Anh";
            putStringLn(name);
            putString(-name);
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(name))"
        self.assertTrue(TestChecker.test(ip, expect, 436))

    def test_type_mismatch_in_unaryop_with_arraytype(self):
        ip = """
        void main(){
            int a[5];
            int b[10];
            a = -b;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(ip, expect, 437))

    def test_type_mismatch_in_unaryop_with_int_op_and_arraycell(self):
        ip = """
        void main(){
            int a; float b; boolean c;
            int alpha[5]; float beta[5]; boolean theta[5];
            alpha[0] = 1; beta[0] = 1.0; theta[0] = true;
            a = -alpha[0];
            b = -beta[0];
            b = -alpha[0];
            c = !theta[0];
            a = !alpha[0];
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,ArrayCell(Id(alpha),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(ip, expect, 438))

    def test_type_mismatch_when_assign_int_to_bool(self):
        ip = """
        int a; int b;
        void main(boolean c){
            b = 1;
            a = b; a = -b;
            a = a + b; a = a - b; a = a * b; a = a / b; a = a % b;
            c = a == b; c = a != b; c = a >= b; c = a <= b; c = a > b; c = a < b;
            c = a + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(c),BinaryOp(+,Id(a),Id(b)))"
        self.assertTrue(TestChecker.test(ip, expect, 439))

    def test_type_mismatch_in_binaryop_when_inttype_add_booltype(self):
        ip = """
        int a; float b; boolean c;
        void main(){
            a = 1; b = 1.0; c = false;
            c = boo();
            b = a + b + foo() + doo();
            b = foo() + boo() + doo();
        }
        int foo(){
            return 1;
        }
        float doo(){
            return 1.0;
        }
        boolean boo(){
            return true;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(foo),[]),CallExpr(Id(boo),[]))"
        self.assertTrue(TestChecker.test(ip, expect, 440))

    def test_type_match_in_all_expr1(self):
        ip = """
        int a; float b; boolean c;
        void main(){
            a = 1; b = 1.0; c = false;
            b = a + b + foo() + doo();
            c = boo() && boo() && !boo();
        }
        int foo(){
            return 1;
        }
        float doo(){
            return 1.0;
        }
        boolean boo(){
            return true;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 441))

    def test_type_mismatch_in_binaryop_when_inttype_sub_booltype(self):
        ip = """
        int a; float b;
        void main(boolean c, boolean d){
            a = 1; b = 1; c = true; d = false;
            c = ((c && d) != (c || d)) == c;
            c = c = c = d;
            c = c && d && c;
            c = d || c || d;
            b = a - c;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(a),Id(c))"
        self.assertTrue(TestChecker.test(ip, expect, 442))

    def test_type_mismatch_when_assign_float_cell_to_int_cell(self):
        ip = """
        int a; float b;
        void main(boolean c[], string d[]){
            int a[5];
            a[0] = 1; a[1] = 1; a[2] = 1; a[3] = 1; a[4] = 1;
            float b[5];
            c[0] = true; c[1] = true; c[2] = true; c[3] = true; c[4] = true;
            d[0] = "a"; d[1] = "a";
            b[0] = a[0] = a[1] + a[2] + a[3] + a[4];
            c[0] = c[1] && c[2] && c[3] && c[4];
            d[0] = d[1];
            a[0] = b[0];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(Id(a),IntLiteral(0)),ArrayCell(Id(b),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(ip, expect, 443))

    def test_type_mismatch_when_assign_array_type(self):
        ip = """
        int a; float b;
        void main(){
            int a[5]; a[0] = 1;
            float b[5];
            b[0] = a[0];
            b = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(ip, expect, 444))

    def test_type_mismatch_in_mod_op_with_different_type(self):
        ip = """
        void main(int a, float b, boolean c){
            a = 1;
            b = a;
            b = b + a; b = b - a; b = b * a; b = b / a;
            c = b > a; c = b < a; c = b >= a; c = b <= a;
            b = b % a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(ip, expect, 445))

    def test_type_mismatch_in_equal_op_with_different_type(self):
        ip = """
        void main(int a, float b, boolean c, string d){
            a = 1; b = 1.0;
            d = "a % b";
            c = b == a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,Id(b),Id(a))"
        self.assertTrue(TestChecker.test(ip, expect, 446))

    def test_type_mismatch_in_call_by_variable(self):
        ip = """
        int foo(){
            return 1;
        }
        void main(int foo){
            int a; float b;
            b = doo();
            foo = 1;
            foo = foo + 1;
            a = foo();
            return ;
        }
        float doo(){
            int a;
            a = foo();
            return 1.0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(ip, expect, 447))

    def test_type_mismatch_in_assign_variable_by_function(self):
        ip = """
        int foo(){
            return 1;
        }
        void main(){
            int a; float b;
            a = foo();
            b = doo();
            return ;
        }
        float doo(){
            foo = 1;
            return 1.0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(foo),IntLiteral(1))"
        self.assertTrue(TestChecker.test(ip, expect, 448))

    def test_type_match_in_all_expr2(self):
        ip = """
        void main(){
            int a; int b; int c;
            b = 1; c = 2;
            a = foo(b, c);
        }
        int foo(int a, int b){
            return a + b;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 449))

    def test_type_match_in_all_expr3(self):
        ip = """
        int a; float b; boolean c; string d;
        void main(){
            int a; float b; boolean c; string d;
            a = 10; b = 10.0; c = true; d = "Nguyen Cong Anh has PPL average score = ";
            foo(a, a, c, d);
        }
        void foo(int a, float b, boolean c, string d){
            putString(d);
            putFloat(b);
            putString(" with final score = ");
            putIntLn(a);
            putBoolLn(c);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 450))

    def test_type_mismatch_in_call_expr_which_not_enough_argument(self):
        ip = """
        void main(){
            float a; a = 10;
            foo();
            return ;
        }
        int foo(int a){
            return a;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[])"
        self.assertTrue(TestChecker.test(ip, expect, 451))

    def test_type_mismatch_in_call_expr_which_does_not_match_type_of_arguments(self):
        ip = """
        void main(){
            float a; a = 10;
            foo(a);
        }
        int foo(int a){
            return a;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(a)])"
        self.assertTrue(TestChecker.test(ip, expect, 452))

    def test_type_mismatch_in_call_expr_which_more_expected_argument(self):
        ip = """
        void main(){
            int b[10]; b[0] = 1;
            foo(b[0]);
        }
        int foo(int a){
            float b[10]; b[0] = 1.0;
            doo(b[0]);
            return a;
        }
        float doo(float a){
            boolean b[10]; b[0] = true;
            boo(b[0]);
            return a;
        }
        boolean boo(boolean a){
            string b[10]; b[0] = "a"; b[1] = "b";
            soo(b[0], b[1]);
            return a;
        }
        string soo(string a){
            return a;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(soo),[ArrayCell(Id(b),IntLiteral(0)),ArrayCell(Id(b),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(ip, expect, 453))

    def test_type_mismatch_in_call_expr_which_does_not_match_array_pointer_type_argument(self):
        ip = """
        void main(){
            int a[5]; a[0] = 1; a[1] = 1; a[2] = 1; a[3] = 1; a[4] = 1;
            float b[5]; b[0] = 1.0;
            doo(a[0], a[1], a[2], a[3], a[4]);
            foo(b[0]);
        }
        void foo(int a){}
        void doo(float a, float b, float c, float d, float e){}
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(b),IntLiteral(0))])"
        self.assertTrue(TestChecker.test(ip, expect, 454))

    def test_type_mismatch_in_call_expr_which_does_not_match_bool_type_argument(self):
        ip = """
        void boo(boolean a){}
        void soo(string a, string b, string c){}
        void main(){
            int a[5]; a[0] = 1;
            string b[5]; b[0] = "a"; b[1] = "a"; b[2] = "a";
            soo(b[0], b[1], b[2]);
            boo(a[0]);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(boo),[ArrayCell(Id(a),IntLiteral(0))])"
        self.assertTrue(TestChecker.test(ip, expect, 455))

    def test_type_match_in_all_expr4(self):
        ip = """
        void foo(int a[], float b[], boolean c[], string d[]){}
        void main(){
            int a[10]; float b[10]; boolean c[10]; string d[10];
            foo(a, b, c, d);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 456))

    def test_type_match_in_all_expr5(self):
        ip = """
        void foo(int a[], float b[], boolean c[], string d[]){}
        int[] foo1(int a[]){ return a; }
        float[] foo2(float b[]){ return b; }
        boolean[] foo3(boolean c[]){ return c; }
        string[] foo4(string d[]){ return d; }
        void main(){
            int a[10]; float b[10]; boolean c[10]; string d[10];
            foo(foo1(a), foo2(b), foo3(c), foo4(d));
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 457))

    def test_type_mismatch_when_pass_int_type_to_array_type(self):
        ip = """
        void foo(int a[], float b[], boolean c[], string d[]){}
        void main(){
            int a[10]; float b[10]; boolean c[10]; string d[10]; a[0] = 1;
            foo(a[0], b, c, d);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(0)),Id(b),Id(c),Id(d)])"
        self.assertTrue(TestChecker.test(ip, expect, 458))

    def test_type_mismatch_when_pass_array_type_to_int_type(self):
        ip = """
        void foo(int a, float b, boolean c, string d){}
        void main(){
            int a[10]; float b[10]; boolean c[10]; string d[10];
            a[0] = 1; b[0] = 1.0; c[0] = true;
            foo(a[0], b[0], c[0], d);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[ArrayCell(Id(a),IntLiteral(0)),ArrayCell(Id(b),IntLiteral(0)),ArrayCell(Id(c),IntLiteral(0)),Id(d)])"
        self.assertTrue(TestChecker.test(ip, expect, 459))

    def test_type_mismatch_when_pass_wrong_call_expr_type(self):
        ip = """
        int foo(){ return 1; }
        int foofoo(int a){ return a; }
        void doo(int a[]){}
        void main(){
            int a[1]; a[0] = 10;
            doo(a); // OK
            a[1] = foofoo(foo()); // OK
            doo(foo()); // error
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(doo),[CallExpr(Id(foo),[])])"
        self.assertTrue(TestChecker.test(ip, expect, 460))

    def test_type_mismatch_when_use_function_type_as_variable_type(self):
        ip = """
        int foo(){
            return 1;
        }
        void main(){
            int a;
            a = foo();
            a = foo[10];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(ip, expect, 461))

    def test_type_mismatch_when_use_int_type_as_array_type(self):
        ip = """
        void main(int foo){
            int a;
            a = foo[10];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(foo),IntLiteral(10))"
        self.assertTrue(TestChecker.test(ip, expect, 462))

    def test_type_match_in_all_expr6(self):
        ip = """
        int func(){ return 1; }
        void main(int foo[]){
            int a;
            foo[10] = 1; foo[1] = 10;
            a = foo[10];
            a = foo[func()];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 463))

    def test_type_mismatch_when_assign_string_to_int(self):
        ip = """
        int[] foo1(int a[]){ return a; }
        float[] foo2(float b[]){ return b; }
        boolean[] foo3(boolean c[]){ return c; }
        string[] foo4(string d[]){ return d; }
        void main(){
            int a[5]; float b[5]; boolean c[5]; string d[5];
            a[0] = 1; b[0] = 1.0; c[0] = true; d[0] = "a";
            foo1(a)[0] = a[0];
            foo2(b)[0] = b[0];
            foo3(c)[0] = c[0];
            foo1(a)[0] = d[0];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,ArrayCell(CallExpr(Id(foo1),[Id(a)]),IntLiteral(0)),ArrayCell(Id(d),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(ip, expect, 464))

    def test_type_mismatch_in_inner_expr_in_array_cell(self):
        ip = """
        void main(){
            int a[10]; float b[10]; boolean c[10];
            a[0] = 1; a[1] = 1; b[0] = 1.0; b[1] = 1.0; c[0] = true; c[1] = true;
            b[0] = a[a[0]];
            b[0] = b[a[0]];
            c[0] = c[b[0]];
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c),ArrayCell(Id(b),IntLiteral(0)))"
        self.assertTrue(TestChecker.test(ip, expect, 465))

    def test_type_match_in_all_expr7(self):
        ip = """
        int[] foo(int a[]){ return a; }
        void main(){
            int a[5]; float b[5]; boolean c[5]; string d[5];
            a[0] = 1; a[1] = 1; b[0] = 1.0; b[1] = 1.0; c[0] = true; c[1] = true; d[0] = "a"; d[1] = "a";
            a[0] = a[foo(a)[0]];
            b[0] = b[foo(a)[0]];
            c[0] = c[foo(a)[0]];
            d[0] = d[foo(a)[0]];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 466))

    def test_function_not_return_in_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a;
            a = 5;
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(ip, expect, 467))

    def test_function_return_in_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            {
                {
                    int a;
                    a = 5;
                    return a;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 468))

    def test_function_not_return_in_if_and_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 10;
            if (a == 0){
                a = 10;
                return a;
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(ip, expect, 469))

    def test_function_return_in_if(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 10;
            if (a == 0){
                {
                    a = 10;
                }
                return a;
            }
            else {
                int a; a = 10;
                {
                    return a;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 470))

    def test_function_not_return_in_if_but_return_in_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 10;
            if (a == 0){
                putStringLn("do nothing");
                return a;
            }
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 471))

    def test_function_not_return_in_for_and_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int i;
            for(i = 0; i < 100; i = i + 1){
                int j;
                for(j = 0; j < i/2; j = j + 1){
                    if(j % i == 0)
                        return j;
                    else
                        continue;
                }
            }
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(ip, expect, 472))

    def test_function_return_in_inner_block_if(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 100;
            if(a < 100){
                if(a < 50){
                    return a;
                }
                else {
                    a = 50;
                    return a;
                }
            }
            else{
                if(a > 150){
                    return a;
                }
                else {
                    a = 150;
                    return a;
                }
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 473))

    def test_function_not_return_in_dowhile_and_block(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 100;
            int b; b = 3;
            do {
                int c;
                c = a % b;
                b = b + 1;
            }
            while(b < 100);
        }
        """
        expect = "Function foo Not Return "
        self.assertTrue(TestChecker.test(ip, expect, 474))

    def test_function_return_in_dowhile(self):
        ip = """
        void main(){
            foo();
        }
        string foo(){
            int a; a = 100;
            int b; b = 3;
            do {
                int c;
                c = a % b;
                if(c == 1) {
                    return "true";
                }
                else
                    return "false";
            }
            while(b < 100);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 475))

    def test_function_return_in_inner_block_dowhile(self):
        ip = """
        void main(){
            foo();
        }
        int foo(){
            int a; a = 100;
            int b; b = 3;
            do
            a = a - 1;
            b = b + 1;
            {
                {
                    {
                        return b - a;
                    }
                }
            }
            while(b < 100);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 476))

    def test_break_not_in_loop_but_in_block(self):
        ip = """
        void main(){
            break;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(ip, expect, 477))

    def test_continue_not_in_loop_but_in_else(self):
        ip = """
        void main(){
            int a; a = 0;
            if(a != 0){
                return ;
            }
            else{
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(ip, expect, 478))

    def test_break_and_continue_in_for_loop(self):
        ip = """
        int main(){
            int a; a = 0;
            for(a = 0; a < 100; a = a + 1)
                if(a % 13 == 0){
                    break;
                }
                else{
                    continue;
                }
            return a;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 479))

    def test_break_in_dowhile_loop(self):
        ip = """
        void main(){
            do {
                { { break; } }
            }
            while(true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 480))

    def test_break_not_in_loop_but_in_if(self):
        ip = """
        int main(){
            int a; a = 100;
            do { { {
                if(a % 13 == 0){
                    return a;
                }
                else{
                    a = a + 1;
                    continue;
                }
            } } } while(true);
            if(a % 13 == 0){
                break;
            }
            else{
                a = a + 1;
            }
            return 0;
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(ip, expect, 481))

    def test_unreachable_function(self):
        ip = """
        int a;
        void main(){}
        int b;
        int foo(){ return 1; }
        int c;
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(ip, expect, 482))

    def test_unreachable_another_function(self):
        ip = """
        int a, b, c;
        void main(){}
        void foo(){ soo(); }
        void boo(){}
        void doo(){ boo(); }
        void soo(){ foo(); }
        """
        expect = "Unreachable Function: doo"
        self.assertTrue(TestChecker.test(ip, expect, 483))

    def test_unreachable_function_when_self_call(self):
        ip = """
        void main(){}
        void foo(){ foo(); doo(); soo(); boo(); }
        void boo(){}
        void doo(){}
        void soo(){}
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(ip, expect, 484))

    def test_binary_op_is_not_left_value(self):
        ip = """
        void main(){
            int a; int b; int c;
            int alpha[5]; int beta[5]; int gama[5];
            a = b = c = 1;
            alpha[2] = 3;
            beta[1] = 2;
            gama[0] = 1;
            foo(alpha)[foo(beta)[foo(gama)[0]]] = 1;
            (a + 1) = a + 1;
        }
        int[] foo(int a[]){
            return a;
        }
        """
        expect = "Not Left Value: BinaryOp(+,Id(a),IntLiteral(1))"
        self.assertTrue(TestChecker.test(ip, expect, 485))

    def test_call_expr_is_not_left_value(self):
        ip = """
        void main(){
            int alpha[5]; alpha[0] = 1;
            foo(alpha) = 1;
        }
        int foo(int a[]){
            return a[0];
        }
        """
        expect = "Not Left Value: CallExpr(Id(foo),[Id(alpha)])"
        self.assertTrue(TestChecker.test(ip, expect, 486))

    def test_literal_is_not_left_value(self):
        ip = """
        void main(){
            -1 = 1;
        }
        """
        expect = "Not Left Value: UnaryOp(-,IntLiteral(1))"
        self.assertTrue(TestChecker.test(ip, expect, 487))

    def test_all_program1(self):
        ip = """
        int a;
        float b[3];
        int[] foo(int a, float b[]) {
            a = 5;
            int c[3];
            if (a > 0)
                foo(a-1, b);
            return c;
        }
        void main(int a) {
            float f;
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(ip, expect, 488))

    def test_all_program2(self):
        ip = """
        int i;
        int foo(){
            return 200;
        }
        void main (){
            int main;
            main = foo();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 489))

    def test_all_program3(self):
        ip = """
        int main()
        {
            float firstNumber, secondNumber, product;
            firstNumber = 90e-1;
            secondNumber = 85e-1;
            product = firstNumber * secondNumber;
            printf("Product = %.2lf\\n", product);
            return 0;
        }
        """
        expect = "Undeclared Function: printf"
        self.assertTrue(TestChecker.test(ip, expect, 490))

    def test_all_program4(self):
        ip = """
        int printf(string s, int a){
            putString(s);
            putIntLn(a);
            return ;
        }
        void main()
        {
            int n, i, sum;
            sum = 0;
            n = 100;
            for(i = 1; i <= n; i = i + 1)
            {
                sum = sum + i;
            }
            printf("Sum = %d", sum);
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(ip, expect, 491))

    def test_all_program5(self):
        ip = """
        void main(){
            checkPrimeNumber(n);
        }
        int checkPrimeNumber(int n){
            int j, flag;
            flag = 1;
            for(j = 2; j <= n/2; j = j + 1)
            {
                if (n % j == 0)
                {
                    flag = 0;
                    break;
                }
            }
            return flag;
        }
        """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(ip, expect, 492))

    def test_all_program6(self):
        ip = """
        void printf(string s){
            putStringLn(s);
        }
        int main()
        {
            int n;
            printf("Enter a positive integer: ");
            n = 20;
            multiplyNumbers(n);
            return 0;
        }
        int multiplyNumbers(int n)
        {
            if (n >= 1)
                return n*multiplyNumbers(n-1);
            else
                return 1;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(ip, expect, 493))

    def test_all_program7(self):
        ip = """
        float pow(float a, int b){ return 1.0; }
        float sqrt(float a){ return 1.0; }
        void main(){
            float a; int b; float data[10];
            a = 4.0; b = 3;
            calculateSD(pow);
        }
        float calculateSD(float data[])
        {
            int i; float sum, mean, standardDeviation;
            sum = 0.0; standardDeviation = 0.0;
            for(i = 0; i < 10; i = i + 1)
            {
                sum = sum + data[i];
            }
            mean = sum/10;
            for(i = 0; i < 10; i = i + 1)
                standardDeviation = standardDeviation + pow(data[i] - mean, 2);
            return sqrt(standardDeviation/10);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(calculateSD),[Id(pow)])"
        self.assertTrue(TestChecker.test(ip, expect, 494))

    def test_all_program8(self):
        ip = """
        int main()
        {
            string s[5];
            s[0] = "a"; s[1] = "a"; s[2] = "a"; s[3] = "a"; s[4] = "a";
            int i;
            putStringLn("Enter a string: ");
            for(i = 0; s[i] != "a"; i = i + 1){
                putString("Length of string: ");
                putIntLn(i);
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(!=,ArrayCell(Id(s),Id(i)),StringLiteral(a))"
        self.assertTrue(TestChecker.test(ip, expect, 495))

    def test_all_program9(self):
        ip = """
        int hcf(int n1, int n2)
        {
            if (n2 != 0)
                return hcf(n2, n1 % n2);
            else
                return n1;
        }
        int main()
        {
            int n1; int n2; { int n2; }
            n1 = 8; n2 = 73;
            result = hcf(n1, n2);
            int result;
            return 0;
        }
        """
        expect = "Undeclared Identifier: result"
        self.assertTrue(TestChecker.test(ip, expect, 496))

    def test_all_program10(self):
        ip = """
        int hcf(int n1, int n2)
        {
            if (n2 != 0)
                return hcf(n2, n1 % n2);
            else
                return n1;
        }
        int main()
        {
            int result;
            int n1; { int n2; }
            n1 = 8; n2 = 73;
            result = hcf(1, 2);
            return 0;
        }
        """
        expect = "Undeclared Identifier: n2"
        self.assertTrue(TestChecker.test(ip, expect, 497))

    def test_all_program11(self):
        ip = """
        int foo(int a, int b, int c){
            return a + b % c;
        }
        void main(int a, int b){
            a = 2; b = 3; c = 4;
            foo(a, b, c);
        }
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(ip, expect, 498))

    def test_all_program12(self):
        ip = """
        int foo(int a, int b, int c){
            return a + b + c;
        }
        int main()
        {
            int a, b, c; a = 1; b = 2; c = 3;
            foo(foo(a + b + c, a + b + c, a + b + c), foo(c % a % b, c % a % b, c % a % b), foo(b - a - c));
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[BinaryOp(-,BinaryOp(-,Id(b),Id(a)),Id(c))])"
        self.assertTrue(TestChecker.test(ip, expect, 499))
