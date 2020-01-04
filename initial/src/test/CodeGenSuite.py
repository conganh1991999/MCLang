import unittest
from TestUtils import TestCodeGen
from AST import *

class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

class CheckCodeGenSuite(unittest.TestCase):

    def test_print_5(self):
        input = "void main () {putIntLn(5);}"
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

    def test_print_125(self):
        input = "void main () {putIntLn(125);}"
        expect = "125"
        self.assertTrue(TestCodeGen.test(input, expect, 502))

    def test_print_0(self):
        input = "void main () {putIntLn(000);}"
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 503))

    def test_simple_global_variable(self):
        input = "int a,b; float c; void main () {putIntLn(000);}"
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 504))

    def test_global_array_variable(self):
        input = "int a[5],b[2];string d[2]; float c; void main () {int a;{int b;} { float c;putIntLn(000);}}"
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 505))

    def test_another_print_0(self):
        input = "void print(){putIntLn(000);} void main () {print();}"
        expect = "0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))

    def test_print_float(self):
        input = "void main () {putFloatLn(0.1);}"
        expect = "0.1"
        self.assertTrue(TestCodeGen.test(input, expect, 507))

    def test_print_another_float(self):
        input = "void main () {putFloatLn(0.242);}"
        expect = "0.242"
        self.assertTrue(TestCodeGen.test(input, expect, 508))

    def test_print_1_add_5(self):
        input = Program(List(
            FuncDecl(Id("main"), List(), VoidType,
                     Block(List(VarDecl(Id("a"), IntType)),
                           List(CallExpr(Id("putIntLn"), List(BinaryOp("+", IntLiteral(1), IntLiteral(5)))))))))
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 509))

    def test_print_value_AddOP(self):
        input = Program(List(
            FuncDecl(Id("main"), List(), VoidType,
                     Block(List(VarDecl(Id("a"), IntType), VarDecl(Id("b"), FloatType)),
                           List(CallExpr(Id("putIntLn"), List(BinaryOp("+", IntLiteral(1), IntLiteral(5)))))))))
        expect = "6"
        self.assertTrue(TestCodeGen.test(input, expect, 510))

    def test_print_parameter_int_value(self):
        input = "void print(int a,float c){putIntLn(a);} void main () {print(1,2.5);}"
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 511))

    def test_print_parameter_float_value(self):
        input = "void print(int a,float c){putFloatLn(c);} void main () {print(1,2.5);}"
        expect = "2.5"
        self.assertTrue(TestCodeGen.test(input, expect, 512))

    def test_print_parameter_boolean_value(self):
        input = """void print(int a,boolean c){putBoolLn(c);} void main () {print(1,true);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 513))

    def test_print_MODOP_of_2_digits(self):
        input = """void print(boolean c){putIntLn(5%10);} void main () {print(true);}"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 514))

    def test_print_with_gt_operator(self):
        input = """void main () {putBoolLn(5>10);}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 515))

    def test_print_with_ge_operator(self):
        input = """void main () {putBoolLn(9<10.0);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 516))

    def test_print_with_eq_operator(self):
        input = """void main () {putBoolLn(5==10);}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 517))

    def test_print_with_not_eq_operator(self):
        input = """void main () {putBoolLn(false!=false);}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 518))

    def test_print_with_not_eq_operator_and_2_operand_is_var(self):
        input = """void checkBool(boolean a,boolean b){putBoolLn(a!=b);}void main () {checkBool(true,false);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 519))

    def test_print_value_of_local_variable(self):
        input = """void main () {float a;a=1.2;putFloatLn(a);}"""
        expect = "1.2"
        self.assertTrue(TestCodeGen.test(input, expect, 520))

    def test_print_value_of_local_variable_float_and_int(self):
        input = """void main () {float a;a=1; putFloatLn(a);}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 521))

    def test_print_value_of_local_variable_int_type_by_float_function(self):
        input = """void main () {int a;a=1; putFloatLn(a);}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 522))

    def test_print_value_of_local_variable_array(self):
        input = """void main () {int a[5];float b[10];boolean c[2]; a[1]=1; b[2]=22; c[1] = true; putFloatLn(b[2]);}"""
        expect = "22.0"
        self.assertTrue(TestCodeGen.test(input, expect, 523))

    def test_print_value_of_parameter_array(self):
        input = """void print(int b[],boolean c,int a){putFloatLn(b[2]);} void main () {int a[5];a[2]=1;print(a,true,a[2]);}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 524))

    def test_print_with_assigns_array(self):
        input = """void print(int b[],boolean c,int a){putFloatLn(b[2]);} void main () {int a[5];int b; a[2]=a[0]=b=a[3]=25;print(a,true,b);}"""
        expect = "25.0"
        self.assertTrue(TestCodeGen.test(input, expect, 525))

    def test_print_with_assigns_variable(self):
        input = """void print(int a){putFloatLn(a);} void main () {int a;int b; print(a=b=100);}"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 526))

    def test_print_with_assigns_variable_extra(self):
        input = """void print(float a){putFloatLn(a);} void main () {float a;int b[4]; print(a=b[3]=100);}"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 527))

    def test_print_with_value_of_and_operator(self):
        input = """void main () {float a;int b[4]; putBoolLn(true&&false);}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 528))

    def test_print_with_value_of_and_operator_and_variable_array(self):
        input = """void main () {float a;boolean b[4];b[3]=true; putBoolLn(true&&b[3]);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 529))

    def test_print_with_value_of_and_operator_and_variable_simple(self):
        input = """void main () {float a;boolean b;b=false; putBoolLn(b&&true&&b);}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 530))

    def test_print_with_value_of_or_operator_and_variable_simple(self):
        input = """void main () {float a;boolean b;b=false;a=2; putBoolLn((b=a>1) || a<=10);}"""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 531))

    def test_print_with_value_of_var_in_block_of_block(self):
        input = """void main () {float a;boolean b;int c;c=10;{int c; c=1;}{int c;int b;float d; c=100; } {float c;c=1;putFloatLn(c);}}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))

    def test_print_with_value_of_global_var(self):
        input = """int a; void main () {a=10;putIntLn(a);}"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 533))

    def test_print_with_value_of_global_var_in_block_of_block(self):
        input = """float a; void main () {int b; {int c; a=1;}{float d; a=100; } {putFloatLn(a);}}"""
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 534))

    def test_print_with_value_of_local_var_has_same_name_with_global_var(self):
        input = """boolean a; void main () {float a;{int c; a=100;}{float d; a=20; } {float c;c=1;putFloatLn(a);}}"""
        expect = "20.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))

    def test_print_with_value_of_operator_with_global_var(self):
        input = """int a;float b; void main () {float c;a=1;b=2;c=3;putFloatLn(a/13+b+3-c/22*144);}"""
        expect = "-14.636364"
        self.assertTrue(TestCodeGen.test(input, expect, 536))

    def test_print_with_value_of_operator_with_global_var_is_parameter(self):
        input = """
        int a;float b;
        void printf(int a,float b,float c){putFloatLn(a/13+b+3-c/22*144);}
        void main () {float c;a=1;b=2;c=3;printf(a,b,c);}
        """
        expect = "-14.636364"
        self.assertTrue(TestCodeGen.test(input, expect, 537))

    def test_print_with_value_of_assign_with_global_var(self):
        input = """int a;float b; void main () {float c;putFloatLn(c=b=a=1);}"""
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))

    def test_print_with_value_of_assign_with_local_var_array_is_parameter(self):
        input = """int a;void print(int a[]){putFloatLn(a[2]);} void main () {int c[10];c[2]=124; print(c);}"""
        expect = "124.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))

    def test_print_with_value_of_add_with_two_local_var_array(self):
        input = """
        void print(float b) {putFloatLn(b);}
        void get(int a[]){a[1]=1;}
        void main () {
            int c[10];
            get(c);
            c[2]=c[1]+124;
            print(c[2]);
        }
        """
        expect = "125.0"
        self.assertTrue(TestCodeGen.test(input, expect, 540))

    def test_print_with_value_of_variable_in_else_stmt(self):
        input = """
        void main () {
            int c[10];
            c[1] = 1;
            c[2]= c[1] + 1;
            if(false) putIntLn(c[1]);
            else putIntLn(c[2]);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 541))

    def test_print_with_value_of_variable_in_else_stmt_and_exp_is_gt(self):
        input = """
        void main () {
            int c[10];
            c[1] = 1;
            c[2]= c[1] + 1;
            if(c[1]>100) putIntLn(c[1]);
            else putIntLn(c[2]);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 542))

    def test_print_with_value_of_variable_in_then_stmt_and_no_else(self):
        input = """
        void main () {
            int c[10];
            c[1] = 1;
            c[2]= c[1] + 1;
            if(c[1]>0.1) putIntLn(c[1]);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 543))

    def test_print_with_value_of_variable_in_complex_case(self):
        input = """
        void main () {
            float a;
            int c[10];
            a = c[1] = 1;
            c[2]= c[1] + 1;
            if(c[1]>0.1){
                int b;
                if(c[2]<1){
                int d;
                putIntLn(c[1]);
                }
                else
                    if(a<10 && a > 0) putBoolLn(true);
                    else putBoolLn(false);
                }
            else{
                putFloatLn(1000);
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 544))

    def test_print_with_value_of_parameter_in_complex_case(self):
        input = """
        void print(int x,float y, boolean d){
            float a;
            int c[10];
            y = a = c[1] = 1;
            x = c[2]= c[1] + 1;
            if(c[1]>0.1){
                int b;
                if(c[2]>1){
                    int d;
                    putIntLn(x);
                }
            }
            else
            {}
        }
        void main () {
            print(1,2,true);
        }
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input, expect, 545))

    def test_print_with_value_of_variable_after_do_stmt(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                c[2]= c[1] + 1;
            } while(c[2] < 10);
            putIntLn(c[2]);
        }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 546))

    def test_print_with_value_of_variable_other_exp(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                c[2]= c[1] + 1;
            } while(c[2] < 10 && false);
            putIntLn(c[2]);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 547))

    def test_another_print_with_value_of_variable_in_complex_case(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                c[2]= c[1] + 1;
            }
            {
                int b[2];
                float c[3];
                c[2] = 100;
            }
            while(c[2] < 10);
            putIntLn(c[2]);
        }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 548))

    def test_print_with_value_of_variable_do_stmt_and_if_stmt(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                if(c[2]<10) c[2] = c[2]+10;
                else
                    c[2]= c[1] + 1;
            } while(c[2] < 10);
            putIntLn(c[2]);
        }
        """
        expect = "17"
        self.assertTrue(TestCodeGen.test(input, expect, 549))

    def test_print_with_value_of_variable_do_stmt_and_no_else_if(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                if(c[2]-3<10) {}
                c[2]=c[2]-1;
            } while(c[2] > 10);
            putIntLn(c[2]);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 550))

    def test_do_while_statement_has_continue_stmt_print_with_value(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                if(c[2]-3<10) {c[2]=c[2]-5; continue;}
                c[2]=c[2]-1;
            } while(c[2] > 10);
            putIntLn(c[2]);
        }
        """
        expect = "7"
        self.assertTrue(TestCodeGen.test(input, expect, 551))

    def test_do_while_statement_has_break_stmt_print_with_value(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                if(c[2]-3<10) {break;}
                c[2]=c[2]-1;
            } while(c[2] > 10);
            putIntLn(c[2]);
        }
        """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input, expect, 552))

    def test_another_do_while_statement_has_break_stmt_print_with_value(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                do if(c[2]-3<10) {break;} c[2]=c[2]-2; while(c[2]>11);
                c[2]=c[2]-1;
            } while(c[2] > 10);
            putIntLn(c[2]);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 553))

    def test_do_while_statement_has_continue_stmt_print_with_value_complex_case(self):
        input = """
        void main () {
            int c[10];
            c[2] = 100;
            c[1] = 1;
            do{
                c[1] = c[1]+5;
                if(c[2]<10) break;
                do if(c[2]-3<10) {c[2]=1; continue;} c[2]=c[2]-2; while(c[2]>11);
                {
                    continue;
                }
                c[2]=c[2]-1;
            } while(c[2] > 10);
            putIntLn(c[2]);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 554))

    def test_do_while_statements_print_with_value_in_next_do_while(self):
        input = """
        void main () {
            int c[10];
            int a;
            do{
                a=10;
                c[2]=1;
                if(c[2]<10)
                {
                    a=a-9;
                    continue;
                    putIntLn(2);
                }
                c[2]=c[2]-1;
            } while(c[2] > 10);
            do{continue; c[2]=100;}while(false);
            if(a==1) do{putIntLn(c[2]);a=a-1;}while(false);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 555))

    def test_for_statement_print_with_value_after_for_stmt(self):
        input = """
        void main () {
            int c[10];
            int a;
            for(a=1;a<10;a=a+1)
            {
                if(a==5) break;
            }
            putIntLn(a);
        }
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input, expect, 556))

    def test_for_statement_print_with_value_with_for_in_for_stmt(self):
        input = """"
        void main () {
            int c[10];
            int a;
            for(a=1;a<10;a=a+1)
            {
                if(a==5)
                    for(a=1;a<10;a=a+1)
                    {
                        if(a==10) break;
                    }
            }
            putIntLn(a);
        }
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 557))

    def test_for_statement_print_with_value_with_do_in_for_stmt(self):
        input = """
        void main () {
            int c[10];
            int a;
            for(a=1;a<10;a=a+1)
            {
                do{
                    if(a==5) break;
                    a=a+2;
                } while(false);
            }
            putIntLn(a);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 558))

    def test_for_statements_print_with_value_for_stmts(self):
        input = """"
        void main () {
            int c[10];
            int a;
            for(a=1;a<10;a=a+1)
            {
                if(a==5) break;
            }
            for(a=100;a<10;a=a+1)
            {
                if(a==5) break;
            }
            putIntLn(a);
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 559))

    def test_for_statement_print_with_value_with_complex_case(self):
        input = """
        void main () {
            int c[10];
            int a;
            for(a=1;a<10;a=a+1)
            {
                int a;
                a=5;
                if(a==5) break;
                for(a=100;a<10;a=a+1)
                {
                    if(a==5) break;
                }
            }
            do{
                putIntLn(a);
                for(a=1;a<10;a=a+1)
                {
                    if(a==5) break;
                }
            } while(false);
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 560))

    def test_return_statement_print_with_value_return_int_type(self):
        input = """
        int print(){return 1;}
        void main () {
            putIntLn(print());
        }
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input, expect, 561))

    def test_return_statement_print_with_value_return_void_type(self):
        input = """
        void print(){return;putIntLn(1);}
        void main () {
            print();
            putFloatLn(1);
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 562))

    def test_return_statement_print_with_value_return_float_type(self):
        input = """
        float print(){return 2;}
        void main () {
            putFloatLn(print());
        }
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))

    def test_return_statement_print_with_value_return_boolean_type(self):
        input = """
        boolean print(){return true;}
        void main () {
            putBoolLn(print());
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 564))

    def test_return_statement_print_with_value_return_value_of_element_array_pointer_type(self):
        input = """
        int print(){int a[10]; a[5]=100; return a[5];}
        void main () {
            int a;
            a = print();
            putIntLn(a);
        }
        """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input, expect, 565))

    def test_return_statement_print_with_value_return_float_array_pointer_type(self):
        input = """
        float[] print(float a[]){return a;}
        void main () {
            float a[10];
            a[5]=100;
            {
                putFloatLn(print(a)[5]);
            }
        }
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 566))

    def test_return_statement_print_with_value_return_boolean_array_pointer_type(self):
        input = """
        boolean print(boolean a[]){return a[5];}
        void main () {
            boolean a[10];
            a[5]=true;
            {
                putBoolLn(print(a));
            }
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 567))

    def test_return_statement_print_with_value_return_array_pointer_type(self):
        input = """
        float[] print(float a[]){a[5]=100; return a;}
        void main () {
            float a[10];
            a = print(a);
            {
                putFloatLn(a[5]);
            }
        }
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 568))

    def test_return_statement_print_with_value_return_array_with_operators(self):
        input = """
        float print(float a[]){ return a[5];}
        void main () {
            float a[10];
            int i;
            for(i=0;i<10;i=i+1)
            {
                a[i] = i;
            }
            {
                putFloatLn(print(a));
            }
        }
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))

    def test_return_statement_print_with_value_return_complex_case(self):
        input = """
        float print(){
            float a[10];
            int i;
            for(i=0;i<10;i=i+1)
            {
                a[i] = i;
                return 100;
                if(false) break;
            }
            {
                return 0;
            }
                return a[5];}
        void main () {
            putFloatLn(print());
        }
        """
        expect = "100.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))

    def test_print_out_value_of_global_var_string_type(self):
        input = """
        string a;
        void main () {
            string b;
            int i;
            b = "ABcdef";
            for(i=0;i<2;i=i+1)
                b = "ABcdef";
            a = b;
            putStringLn(a);
        }
        """
        expect = "ABcdef"
        self.assertTrue(TestCodeGen.test(input, expect, 571))

    def test_print_out_value_of_local_var_string_type(self):
        input = """
        string a;
        void main () {
            string b;
            int i;
            b = "ABcdef";
            for(i=0;i<1;i=i+1)
                b = "ABcdef";
            a = "ABcdef";
            putStringLn(b);
        }
        """
        expect = "ABcdef"
        self.assertTrue(TestCodeGen.test(input, expect, 572))

    def test_print_out_value_of_local_var_string_array_type(self):
        input = """
        void main () {
            string b[5];
            int i;
            for(i=0;i<2;i=i+1)
                b[4] = "ABcdef";
            putStringLn(b[4]);
        }
        """
        expect = "ABcdef"
        self.assertTrue(TestCodeGen.test(input, expect, 573))

    def test_print_with_assigns_variable_extra_array_and_simple(self):
        input = """void print(float c){putFloatLn(c);} void main () {float a[5];int b;b=0;print(1+(a[2]=4*b+2.4-20/100));}"""
        expect = "3.4"
        self.assertTrue(TestCodeGen.test(input, expect, 574))

    def test_print_value_of_string(self):
        input = """void main () {string a; a="abc"; putStringLn(a);}"""
        expect = "abc"
        self.assertTrue(TestCodeGen.test(input, expect, 575))

    def test_print_out_value_of_global_var_string_after_assigns(self):
        input = """
        string a;
        void main () {
            string b[2];
            int i;
            for(i=0;i<2;i=i+1)
                b[i] = "ABcdef";
            a = b[1];
            putStringLn(a);
        }
        """
        expect = "ABcdef"
        self.assertTrue(TestCodeGen.test(input, expect, 576))

    def test_print_out_value_of_global_var_with_unary_op_int_type(self):
        input = """
        int a;
        void main () {
            a = 1525;
            putIntLn(-a);
        }
        """
        expect = "-1525"
        self.assertTrue(TestCodeGen.test(input, expect, 577))

    def test_print_out_value_of_global_var_with_unary_op_float_type(self):
        input = """
        float a;
        void main () {
            int b;
            b = 15111;
            a = -b;
            putFloatLn(a);
        }
        """
        expect = "-15111.0"
        self.assertTrue(TestCodeGen.test(input, expect, 578))

    def test_print_out_value_of_global_var_with_unary_op_boolean_type(self):
        input = """
        int a;
        float c;
        void main () {
            int b;
            b = 15111;
            c=1;
            -b;
            a = -b;
            putBoolLn(!(a > -b||a == b+122|| false != false|| b+1>=123--a));
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 579))

    def test_print_out_value_of_var_with_value_in_call_function(self):
        input = """
        int a;
        float c;
        int print(int a){ a = 1; return a;}
        void main () {
            int b[3];
            print(print(print(b[1])));
            a = -b[2];
            putBoolLn(!(a > -b[1]||a == b[1]+122|| false != false|| b[1]+1>=123--a));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 580))

    def test_print_out_value_global_array_var_with_value_in_call_function(self):
        input = """
        int a[5];
        float c;
        int print(int a){ a = 1; return a;}
        void main () {
            int b[3];
            b[1] = -print(print(print(a[1])));
            putBoolLn(!(a[1] > -b[1]||a[1] == b[1]+122|| false != false || b[1]+1>=123--a[1]));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 581))

    def test_print_out_value_of_global_array_var_with_value_of_other_var(self):
        input = """
        int a[10];
        float c;
        int print(int a){ a = 1; return a;}
        void main () {
            int b[3];
            a[2] = print(print(print(b[1])));
            a[1] = a[2];
            putBoolLn(!(a[1] > -b[1]||a[1] == b[1]+122|| false != false));
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 582))

    def test_print_out_value_of_global_array_var_function_array_type(self):
        input = """
        int a[10];
        float c;
        int[] print(int a[]){ a[2] = 1; return a;}
        void main () {
            int b[3];
            a = print(print(print(b)));
            a[1] = a[2]+100/10-10;
            putBoolLn(!((a[1] > -b[1] && false != false)|| b[1]+1>=123--a[1]));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test_print_out_value_of_global_array_var_local_array_type(self):
        input = """
        int a[3];
        float c;
        int print(int a){ a = 1; return a;}
        void main () {
            int b[3];
            int i;
            for(i=0;i<3;i=i+1)
                print(print(print(b[i])));
            a = b;
            a[1] = a[2]+100/10-10;
            putBoolLn(!(a[1] > -b[1]));
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 584))

    def test_print_out_value_of_global_array_var_is_string_type(self):
        input = """
        string a[3];
        float c;
        void main () {
            string b[3];
            int i;
            for(i=0;i<3;i=i+1)
                b[i]="abc";
            for(i=0;i<3;i=i+1)
                a[i]=b[i];
            for(i=0;i<3;i=i+1)
                putString(a[i]);
        }
        """
        expect = "abcabcabc"
        self.assertTrue(TestCodeGen.test(input, expect, 585))

    def test_print_out_value_of_global_array_var_string_type_with_assign(self):
        input = """
        string a[3];
        void main () {
            string b[3];
            int i;
            for(i=0;i<3;i=i+1)
                b[i]="DZ";
            for(i=0;i<3;i=i+1)
                a[i]="DA";
            for(i=0;i<3;i=i+1){
                putString(a[i]);
                putString(b[i]);
            }
        }
        """
        expect = "DADZDADZDADZ"
        self.assertTrue(TestCodeGen.test(input, expect, 586))

    def test_print_out_value_of_global_array_var_float_type_with_assign(self):
        input = """
        float a[3];
        float c;
        void main () {
            float b[3];
            int i;
            c = 1000;
            for(i=0;i<3;i=i+1)
                b[i]=c+30-12/424*545--5325+-1+10.e32+-10E12;
            for(i=0;i<3;i=i+1)
                a[i]=b[i]+10000;
            for(i=0;i<3;i=i+1){
                putFloat(a[i]+b[i]);
            }
        }
        """
        expect = "2.0E332.0E332.0E33"
        self.assertTrue(TestCodeGen.test(input, expect, 587))

    def test_print_out_value_of_global_array_var_boolean_type_with_assign(self):
        input = """
        boolean a[3];
        float c;
        void main () {
            float b[3];
            int i;
            c = 1000;
            for(i=0;i<3;i=i+1)
                b[i]=c+30-12/424*545--5325+-1+10.e32+-10E12;
            for(i=0;i<3;i=i+1)
                a[i]=(b[i]+10000-i*1000 < c*2/14);
            for(i=0;i<3;i=i+1){
                putBool(!a[i]);
            }
        }
        """
        expect = "truetruetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 588))

    def test_print_out_value_of_with_simple_case_of_variable(self):
        input = """
        boolean a[3];
        float c;
        void main () {
            {
                boolean b; // local boolean variable
                int i ; // local int variable
                i =3;
                if (i >0) putInt(i);
            }
        }
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input, expect, 589))

    def test_print_out_value_of_global_array_var_with_do_while_stmt(self):
        input = """
        boolean a[3];
        float d[10];
        float c;
        void main () {
            {
                // start declaration part
                int a ,b, c ;
                float f[5];
                int i;
                //end declaration part
                // start statement part
                i = 5;
                d[9]=d[8]=d[7]=d[6]=d[5]=a=b=2;
                if(a==b) f[0]=1.0;
                do{
                    putFloat(d[i]);
                    i=i+1;
                } while(i<10);
                //end statement part
            }
        }
        """
        expect = "2.02.02.02.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 590))

    def test_print_out_value_of_global_array_types_element(self):
        input = """
        float a[5];
        float print(float a[]){ putFloat(a[1]); return 1;}
        void main () {
            float b[2];
            a = b;
            b[1] = 10.22e12;
            a[1]=1;
            print(a);
        }
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 591))

    def test_print_with_value_of_local_var_has_same_name_with_global_var_array(self):
        input = """boolean a[10]; void main () {int b;boolean a; {int c; a=true; putBool(!a);}}"""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 592))

    def test_print_out_value_of_global_array_var_int_type(self):
        input = """
        int a[5];
        int put(int a){return a;}
        void main () {
            int i;
            int b[2];
            b[1]=1;
            b[1];
            put(b[1]);
            putInt(put(b[1]));
            for(i=0;i<2;i=i+1)
                b[i] = i;
            a[3] = put(b[1]);
            putInt(a[3]);
        }
        """
        expect = "11"
        self.assertTrue(TestCodeGen.test(input, expect, 593))

    def test_print_out_value_of_var_check_and_symbol(self):
        input = """
        void main () {
            boolean a;
            a=false;
            true&&false&&true&&(a=true);
            putBool(a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 594))

    def test_print_out_value_of_var_check_or_symbol(self):
        input = """
        int a[5];
        void main () {
            boolean a;
            a=false;
            true||false||true||(a=true);
            putBool(a);
        }
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 595))

    def test_print_out_value_of_var_check_and_or_with_complex_case(self):
        input = """
        int a[5];
        void main () {
            boolean a;
            a=false;
            if(false||false&&true && 12<5325.2 || (a!=false) ||(a=true)) {}
            putBool(a);
        }
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 596))

    def test_print_out_value_of_var_check_and_or_with_function_return(self):
        input = """
        int a[5];
        boolean check(int a){a = 100; return true;}
        void main () {
            a[1] = 10;
            if(false||false&&true && 12<5325.2 || (check(a[1])!=false) ||(check(a[3])==true)) {}
            putInt(a[1]);
        }
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input, expect, 597))

    def test_print_out_value_in_complex_case(self):
        input = """
        float a[5];
        float print(float a[]){ putFloat(a[1]); return 1;}
        boolean check(int a){a = 100; return true;}
        void main () {
            float b[2];
            a = b;
            b[1] = 10.22e12;
            a[1]=1;
            print(a);
            {
                int a[5];
                a[1] = 10;
                if(false||false&&true && 12<5325.2 || (check(a[1])!=false) ||(check(a[3])==true)) {}
                putInt(a[1]);
            }
            {
                int a;
                float c;
                int b;
                b = 15111;
                c=1;
                -b;
                a = -b;
                putBool(!(a > -b||a == b+122|| false != false|| b+1>=123--a));
            }
        }
        """
        expect = "1.010false"
        self.assertTrue(TestCodeGen.test(input, expect, 598))

    def test_MC_program_check_the_same_name_variable(self):
        input = """
        int i;
        int f(){
            return 200;
        }
        void main () {
            int main;
            main = f();
            putInt(main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putInt(i);
                putInt(main);
                putInt(f);
            }
            putInt(main);
        }
        """
        expect = "200100100100200"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
