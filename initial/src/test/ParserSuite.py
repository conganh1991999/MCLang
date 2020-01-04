import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_var_declare_1(self):
        # test case 1: không chấp nhận biến kiểu 'void'
        ip = """
        int std_id;
        float sem_score;
        boolean isStudent;
        string myString;
        void nothing;
        """
        expect = "Error on line 6 col 20: ;"
        self.assertTrue(TestParser.checkParser(ip, expect, 201))

    def test_var_declare_2(self):
        # test case 2: khai báo biến thiếu tên biến, đây không phải là 1 khai báo, chương trình MC chỉ chứa các khai báo.
        ip = """
        int alpha;
        int beta;
        int alpha, beta, gama;
        int ;
        """
        expect = "Error on line 5 col 12: ;"
        self.assertTrue(TestParser.checkParser(ip, expect, 202))

    def test_var_declare_3(self):
        # test case 3: long, short, char chỉ là những định danh
        ip = """
        int long, short, char;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 203))

    def test_var_declare_4(self):
        # test case 4: tương tự, double cũng chỉ là định danh, nhưng 'int' thì không.
        ip = """
        float double  ;
        float double_double;
        float int;
        """
        expect = "Error on line 4 col 14: int"
        self.assertTrue(TestParser.checkParser(ip, expect, 204))

    def test_var_declare_5(self):
        # test case 5: có 2 kiểu khai báo biến, nhưng không thể thiếu ';' khi kết thúc khai báo
        ip = """
        float math_score;
        float math_score, phys_score, chem_score;
        float math_score[5], phys_score, chem_score;
        float math_score, phys_score[5], chem_score;
        float math_score, phys_score, chem_score[5];
        float math_score[5], phys_score[5], chem_score[5];
        float average, average[3]
        float average ;
        """
        expect = "Error on line 9 col 8: float"
        self.assertTrue(TestParser.checkParser(ip, expect, 205))

    def test_var_declare_6(self):
        # test case 6: biến có thể là biến thông thường, không được khởi tạo giá trị cho biến
        ip = """
        boolean isStudent;
        boolean isBKer = true ;
        """
        expect = "Error on line 3 col 23: ="
        self.assertTrue(TestParser.checkParser(ip, expect, 206))

    def test_var_declare_7(self):
        # test case 7: biến cũng có thể là biến mảng 1 chiều, không được khởi tạo giá trị cho biến
        ip = """
        int my_Arr[0], my_Arr[1], my_Arr[2];
        int my_Arr[3] = {1, 2, 3};
        """
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.checkParser(ip, expect, 207))

    def test_var_declare_8(self):
        # test case 8: nếu là biến mảng 1 chiều, kích thước mảng phải rõ ràng
        ip = """
        int N;
        int ARR[ 5 ];
        boolean isTrue, isFalse, ARR[ ] ;
        """
        expect = "Error on line 4 col 38: ]"
        self.assertTrue(TestParser.checkParser(ip, expect, 208))

    def test_var_declare_9(self):
        # test case 9: chương trình MC chỉ gồm các khai báo biến và khai báo hàm, định danh không đứng một mình như một khai báo.
        ip = """
        int i; float j; string k;
        alpha , beta , gama;
        """
        expect = "Error on line 3 col 8: alpha"
        self.assertTrue(TestParser.checkParser(ip, expect, 209))

    def test_var_declare_10(self):
        # test case 10: các định danh cách nhau bởi dấu ','
        ip = """
        int a, b, c, d[4], e[5], f[6];
        int a b ;
        """
        expect = "Error on line 3 col 14: b"
        self.assertTrue(TestParser.checkParser(ip, expect, 210))

    def test_func_declare_1(self):
        # test case 11:
        ip = """
        void main(){}
        int main1(){}
        float main2(){}
        boolean main3(){}
        string main4(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 211))

    def test_func_declare_2(self):
        # test case 12:
        ip = """
        int[] main1() {}
        float[] main2() {}
        boolean[] main3() {}
        string[] main4() {}
        void[] main(){}
        """
        expect = "Error on line 6 col 12: ["
        self.assertTrue(TestParser.checkParser(ip, expect, 212))

    def test_func_declare_3(self):
        # test case 13:
        ip = """
        void main(int a, int b, int c){}
        int[] main(int a[], int b[], int c){}
        float average(){};
        """
        expect = "Error on line 4 col 25: ;"
        self.assertTrue(TestParser.checkParser(ip, expect, 213))

    def test_func_declare_4(self):
        # test case 14:
        ip = """
        void main()
        {
            \t
        }
        boolean checksum(boolean etc, boolean check[5])
        {
            \t
        }
        """
        expect = "Error on line 6 col 52: 5"
        self.assertTrue(TestParser.checkParser(ip, expect, 214))

    def test_func_declare_5(self):
        # test case 15:
        ip = """
        float main(float main, float main){}
        int main()
        """
        expect = "Error on line 4 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(ip, expect, 215))

    def test_func_declare_6(self):
        # test case 16:
        ip = """
        float main(float main, float main){}
        int main{}
        """
        expect = "Error on line 3 col 16: {"
        self.assertTrue(TestParser.checkParser(ip, expect, 216))

    def test_func_declare_7(self):
        # test case 17:
        ip = """
        int[] foo(int a, string b){
        }boolean isEmpty(int members[]){
        }float myFloat(float array[], ){}
        """
        expect = "Error on line 4 col 38: )"
        self.assertTrue(TestParser.checkParser(ip, expect, 217))

    def test_func_declare_8(self):
        # test case 18:
        ip = """
        int[] float(string[] members){}
        """
        expect = "Error on line 2 col 14: float"
        self.assertTrue(TestParser.checkParser(ip, expect, 218))

    def test_if_stmt_1(self):
        # test case 19: // else thuộc về if thứ hai
        ip = """
        void main(){
            if ( a && b )
                if( a || b )
                    a || b ;
            else
                a && b ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 219))

    def test_if_stmt_2(self):
        # test case 20: else thuộc về if thứ nhất
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b )
                    a || b ;
            }
            else
                a && b ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 220))

    def test_if_stmt_3(self):
        # test case 21: if else đầy đủ
        ip = """
        void main(){
            if ( a && b )
            {
                if( a || b ){a || b ;}
                else
                {}
            }
            else{a && b ;}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 221))

    def test_if_stmt_4(self):
        # test case 22:
        ip = """
        void main(){
            if (a && b)
            if( a || b )
            a || b;
            else a && b;
            if (a != b)
            a == b;
            else
        }
        """
        expect = "Error on line 10 col 8: }"
        self.assertTrue(TestParser.checkParser(ip, expect, 222))

    def test_if_stmt_5(self):
        # test case 23:
        ip = """
        void main(){
            if (a && b)
            if (a || b)
            if (a == b)
            if (a != b)
            if (a > b)
            if (a < b){}
            else
            {if (a >= b){}}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 223))

    def test_if_stmt_6(self):
        # test case 24:
        ip = """
        void main(){
            if (a && b)
            if (a || b)
            if (a == b)
            if (a != b)
            if (a > b)
            if (a < b)
            if (a >= b)
        {}
        """
        expect = "Error on line 11 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(ip, expect, 224))

    def test_if_stmt_7(self):
        # test case 25:
        ip = """
        int main(){
            if (a == b){
                if((a == b)){
                    if(((a == b))){ return 1; }
                    else{
                        return 0;
                    }
                }
            }
            else{
                if(a != b)
                {
                    return 0; 
                }
                else
                    return 1;
                else{}
            }
        }
        """
        expect = "Error on line 18 col 16: else"
        self.assertTrue(TestParser.checkParser(ip, expect, 225))

    def test_do_while_stmt_1(self):
        # test case 26:
        ip = """
        void main(){
        do {} {} {} {} {} {}
        {} 
        while a == b ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 226))

    def test_do_while_stmt_2(self):
        # test case 27:
        ip = """
        void main(){
        do {
            do {//\n} while ( a < 0);
            if ( a && b )
            {
                if( a || b ){a || b ;}
                else
                {}
            }
            else{a && b ;}
        } {}
        while a == b ;
        while a != b ;
        }
        """
        expect = "Error on line 15 col 8: while"
        self.assertTrue(TestParser.checkParser(ip, expect, 227))

    def test_do_while_stmt_3(self):
        # test case 28:
        ip = """
        void main(){
        do {
            do {} while (a<0);
            do {{{int i;}}} while b<0;
        } {} {} {} {} do {{if(a){}}} while 5 == 0 ;
        while 5 >= 10 ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 228))

    def test_do_while_stmt_4(self):
        # test case 29:
        ip = """
        void main(){
        do
            {int a;}
            a = 0;
            a = a + 1;
            do
                {boolean b;}
                b = true;
                b = false; 
                do
                    do{}
                    while b == 1;
                while b != 1;
            while a == 0;
        while a != 0;
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 229))

    def test_do_while_stmt_5(self):
        # test case 30:
        ip = """
        void main(){
            int i[5];
            boolean check;
            do{
                int count;
                count = 0;
                if(count != 0)
                    break;
                count = count*count;
                {}
            } while count == 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 230))

    def test_for_stmt_1(self):
        # test case 31:
        ip = """
        int main(){
            for ( i = 0; i < alpha; i = i + 1){}
            for ( i; j; k) {}
            for (i = 0 ; i < 10 ; i++) {}
            return 0;
        }
        """
        expect = "Error on line 5 col 36: +"
        self.assertTrue(TestParser.checkParser(ip, expect, 231))

    def test_for_stmt_2(self):
        # test case 32:
        ip = """
        int main(){
            for (i = 1; j = 1; k = 1){
                i = i + 2;
                if ( i > j )
                    print(i);
                else
                    print(j);
            }
            for ( int i = 0; i < 10; i+=1){}
        }
        """
        expect = "Error on line 10 col 18: int"
        self.assertTrue(TestParser.checkParser(ip, expect, 232))

    def test_for_stmt_3(self):
        # test case 33:
        ip = """
        void main(){
            for(changeA = 0; changeA < MATRIX/n_pros; changeA = changeA + 1)
            {
                for(i = 0; i < MATRIX; i = i + 1)
                {
                    matA[i] = rand() % 2;
                }
                for(changeB = 0; changeB < MATRIX; changeB = changeB +1)
                {
                    for(j = 0; j < MATRIX; j = j + 1){
                        matB[j] = rand() % 2;
                    }
                    tem_val = 0;
                    for(offset = 0; offset < MATRIX; offset = offset + 1){
                        tem_val = tem_val + matA[offset] * matB[offset];
                    }
                }
            }
            return;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 233))

    def test_for_stmt_4(self):
        # test case 34:
        ip = """
        boolean isPrime(int n)
        { 
            // Corner case 
            if (n <= 1) 
                return false; 

            // Check from 2 to n-1
            int i; 
            for (i = 2; i < n; i = i + 1) 
                if (n % i == 0) 
                    return false;
            return true; 
        }

        void printPrime(int n)
        {
            int i;
            for (i = 2; i <= n; i = i + 1) { 
                if (isPrime(i)) 
                    print(i); 
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 234))

    def test_for_stmt_5(self):
        # test case 35:
        ip = """
        int main(){
            for (i = 0; i <  r; i = i + 1) 
                for (j = 0; j < c; j = j + 1) 
                    for (i = 0; i <  r; i = i + 1) 
                        for (j = 0; j < c; j = j + 1) 
                            print("i"); // for
                            print("i"); // main
                            print("i"); // main
                            print("i"); // main
                            print("i"); // main
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 235))

    def test_stmt_1(self):
        # test case 36:
        ip = """
        int main() { 
            int i;
            i = 20; 
            if (i < 15) 
                printf("i is smaller than 15"); 
            else
                printf("i is greater than 15");      
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 236))

    def test_stmt_2(self):
        # test case 37:
        ip = """
        void findElement(int arr[], int size, int key)  
        {  
            int i;
            // loop to traverse array and search for key  
            for (i = 0; i < size; i = i + 1)
                if (arr[i] == key)
                    printf("Element found at position: %d", (i + 1));  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 237))

    def test_stmt_3(self):
        # test case 38:
        ip = """
        int main() { 
            // loop from 1 to 10
            int i;
            for (i = 1; i <= 10; i = i + 1) {    
                if (i == 6)
                    continue;  
                else
                    //
                    printf("%d ", i);
            }
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 238))

    def test_stmt_4(self):
        # test case 39:
        ip = """
        void printNumbers() 
        {
            int n; n = 1;
            label
                printf("%d ",n); 
                n++; 
                if (n <= 10) 
                    goto label;
        }
        """
        expect = "Error on line 6 col 16: printf"
        self.assertTrue(TestParser.checkParser(ip, expect, 239))

    def test_stmt_5(self):
        # test case 40:
        ip = """
        int main()
        {
            int i, j;
            do{
                j = 1;
                do{
                    j = j + 1;
                } while ( j <= 10 );
                i = i + 1;
            } while ( i <= 10 );
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 240))

    def test_stmt_6(self):
        # test case 41:
        ip = """
        int main(){
            int i;
            i = 1;
            do {
            int j;
            for (j=1; j<=i; j = j + 1)
            {
                Write(i + " ");
            }
                WriteLine();
                i = i + 1;
            }
            while (i<=5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 241))

    def test_stmt_7(self):
        # test case 42:
        ip = """
        int main(){
            for(; i < 10 ; i = i + 1)
                continue;
        }
        """
        expect = "Error on line 3 col 16: ;"
        self.assertTrue(TestParser.checkParser(ip, expect, 242))

    def test_stmt_8(self):
        # test case 43:
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                int j;
                j = 1;
                for(j = 0; j < 10 ; j = j + 1){
                int k;
                k = 1;
                }
        }
        """
        expect = "Error on line 4 col 16: int"
        self.assertTrue(TestParser.checkParser(ip, expect, 243))

    def test_stmt_9(self):
        # test case 44:
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                j = 1; int j;
                for(j = 0; j < 10 ; j = j + 1){
                int k;
                k = 1;
                }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 244))

    def test_stmt_10(self):
        # test case 45:
        ip = """
        int main(){
            for(i = 0; i < 10 ; i = i + 1)
                if( i == 0)
            break ;
            else
                continue;
                int j;
                j = 10;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 245))

    def test_statement_11(self):
        # test case 46
        ip = """
        void main() {
            if (a == b)
                if (c == d)
                    foo();
                else
                    foo();
            else
                foo();
            else {
                //comment
            }
        }
        """
        expect = "Error on line 10 col 12: else"
        self.assertTrue(TestParser.checkParser(ip, expect, 246))

    def test_statement_12(self):
        # test case 47
        ip = """
        int main(int argc){
            int a;
            { 
                int b;
                {
                    int c;
                } 
            }
            return;
            return 0;
            return 0 + 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 247))

    def test_statement_13(self):
        # test case 48
        ip = """
        int main(int argc){
            return;
            return a = a + 0;
            return a;
            return main;
            return "nothing";
            return return;
        }
        """
        expect = "Error on line 8 col 19: return"
        self.assertTrue(TestParser.checkParser(ip, expect, 248))

    def test_statement_14(self):
        # test case 49
        ip = """
        int main(int argc){
            int argc;
            int argv[10];
            {
                if (argv[1] == argc){
                    return 0;
                }
                return 1;
            }
            boolean check() {
                // checking
            }
        }
        """
        expect = "Error on line 11 col 25: ("
        self.assertTrue(TestParser.checkParser(ip, expect, 249))

    def test_statement_15(self):
        # test case 50
        ip = """
        int main(int argc){
            int a, b, c; // variable declaration
            a=b=c=5; // assignment statement
            float f[5]; // variable declaration
            if ( a==b ) f[0] = 1.0; // if statement
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 250))

    def test_expr_1(self):
        # test case 51
        ip = """
        int main(){
            arr[5]; //pass
            (arr)[5]; //pass
            arr[5][10]; //fail
        }
        """
        expect = "Error on line 5 col 18: ["
        self.assertTrue(TestParser.checkParser(ip, expect, 251))

    def test_expr_2(self):
        # test case 52
        ip = """
        int main(){
            foo()[5]; //pass
            (foo())[5]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 252))

    def test_expr_3(self):
        # test case 53
        ip = """
        int main(){
            foo(2)[5]; //pass
            foo(1,2,3)[5]; //pass
            float(1,2,3); //fail
        }
        """
        expect = "Error on line 5 col 17: ("
        self.assertTrue(TestParser.checkParser(ip, expect, 253))

    def test_expr_4(self):
        # test case 54
        ip = """
        int main(){
            (foo(1,2,3))[5]; //pass
            int[5]; //fail
        }
        """
        expect = "Error on line 4 col 15: ["
        self.assertTrue(TestParser.checkParser(ip, expect, 254))

    def test_expr_5(self):
        # test case 55
        ip = """
        int main(){
            func(1+2, a[5], a < 5)[5]; //pass
            func(func(1), a, a == b)[10]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 255))

    def test_expr_6(self):
        # test case 56
        ip = """
        int main(){
            ()[5]; //fail
        }
        """
        expect = "Error on line 3 col 13: )"
        self.assertTrue(TestParser.checkParser(ip, expect, 256))

    def test_expr_7(self):
        # test case 57
        ip = """
        int main(){
            ((arr))[5]; //pass
            ((foo()))[5]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 257))

    def test_expr_8(self):
        # test case 58
        ip = """
        int main(){
            foo(2)[3+x] = a[b[2]] +3; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 258))

    def test_expr_9(self):
        # test case 59
        ip = """
        void goo(float x[]) {
            float y[10];
            int z [10];
            foo(x) ;
            foo(y) ;
            foo(z) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 259))

    def test_expr_10(self):
        # test case 60
        ip = """
        void goo(float x[]) {
            arr[func()]; //pass
            arr[func(1)]; //pass
            arr[func(1,2,3, another_arr[4])]; //pass
        }        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 260))

    def test_expr_11(self):
        # test case 61
        ip = """
        int main(){
            arr[(func())]; //pass
            arr[((func(1)))]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 261))

    def test_expr_12(self):
        # test case 62
        ip = """
        int main(){
            arr[arr[5]]; //pass
            arr1[arr2[arr3[5]]]; //pass
            arr[arr[[5]]]; //fail
        }
        """
        expect = "Error on line 5 col 20: ["
        self.assertTrue(TestParser.checkParser(ip, expect, 262))

    def test_expr_13(self):
        # test case 63
        ip = """
        int main(){
            arr [ ( arr[5] ) ]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 263))

    def test_expr_14(self):
        # test case 64
        ip = """
        int main(){
            arr[i]; //pass
            arr[1 + 2 - 3 * 4 / 5 % 6]; //pass
            arr[----------3]; //pass
            arr[ a = b ]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 264))

    def test_expr_15(self):
        # test case 65
        ip = """
        int main(){
            arr[(i)]; //pass
            arr[(1 + 2 - 3 * 4 / 5 % 6)]; //pass
            arr[(----------3)]; //pass
            arr[ (a = b) ]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 265))

    def test_expr_16(self):
        # test case 66
        ip = """
        int main(){
            arr[((i))]; //pass
            arr[((a + b - c * d / e % f))]; //pass
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 266))

    def test_expr_17(self):
        # test case 67
        ip = """
        int main(){
            func();
            func(()); //fail
        }
        """
        expect = "Error on line 4 col 18: )"
        self.assertTrue(TestParser.checkParser(ip, expect, 267))

    def test_expr_18(self):
        # test case 68
        ip = """
        int main(){
            func(1 + 2 - 3 * 4 / 5 % 6);
            func((1 + 2 - 3 * 4 / 5 % 6));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 268))

    def test_expr_19(self):
        # test case 69
        ip = """
        int main(){
            func(a < b, 1 >= b, a <= 2, 1 < 2);
            func(a || b && c, -a-b, !a !b);
        }
        """
        expect = "Error on line 4 col 39: !"
        self.assertTrue(TestParser.checkParser(ip, expect, 269))

    def test_expr_20(self):
        # test case 70
        ip = """
        int main(){
            func(arr[num], arr[num + 1], arr[num + 2]);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 270))

    def test_expr_21(self):
        # test case 71
        ip = """
        int main(){
            func(foo(1), foo(2), foo(3));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 271))

    def test_expr_22(self):
        # test case 72
        ip = """
        int main(){
            func(foo(1), arr[5], i, a + 5, a < 5);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 272))

    def test_expr_23(self):
        # test case 73
        ip = """
        int main(){
            a = 5;
            a = (5 + 5) - 5;
            a[5] = a * (5 / b);
            func(5)[--3] = --3;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 273))

    def test_expr_24(self):
        # test case 74
        ip = """
        int main(){
            a = arr[a+a] = func(a);
            a = b = c = 5 + (a + b) + c;
            a = b && c || d;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 274))

    def test_expr_25(self):
        # test case 75
        ip = """
        int main(){
            (a > a) > 5;
            a == (a != b);
            (a >= ((b >= c) >= d));
            a != b != c == d;
        }
        """
        expect = "Error on line 6 col 19: !="
        self.assertTrue(TestParser.checkParser(ip, expect, 275))

    def test_expr_26(self):
        # test case 76
        ip = """
        int main(){
            a = !(((--3 - 4) --5) -- 6 - 7 - 8);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 276))

    def test_combine_1(self):
        # test case 77
        ip = """
        int a;
        float b[3];
        int[] foo(int a, float b[]) {
            int c[3];
            if (a>0)
                foo(a-1, b);
            return c;
        }
        void foo(int a) {
            float f;
            int child_of_foo(float f) {} //fail
        }
        """
        expect = "Error on line 12 col 28: ("
        self.assertTrue(TestParser.checkParser(ip, expect, 277))

    def test_combine_2(self):
        # test case 78
        ip = """
        int foo(int a, float b[])
        {
            boolean c;
            int i;
            i = a + 3 ;
            if (i > 0) {
                int d;
                d = i + 3;
                putInt( d );
            }
            return i;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 278))

    def test_combine_3(self):
        # test case 79
        ip = """
        int i;
        int f() {
            return 200;
        }
        void main () {
            int main ;
            main = f() ;
            putIntLn( main ) ;
            {
                int i ;
                int main ;
                int f ;
                main = f = i = 100;
                putIntLn( i ) ;
                putIntLn( main ) ;
                putIntLn ( f ) ;
            }
            putIntLn( main ) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 279))

    def test_combine_4(self):
        # test case 80
        ip = """
        int main() {
            // printf() displays the string inside quotation
            printf("Hello, World!");
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 280))

    def test_combine_5(self):
        # test case 81
        ip = """
        int main()
        {
            int number;
            //printf() displays the formatted output 
            printf("Enter an integer: ");

            //scanf() reads the formatted input and stores them
            scanf("%d", &number);

            //printf() displays the formatted output
            printf("You entered: %d", number);
            return 0;
        }
        """
        expect = "&"
        self.assertTrue(TestParser.checkParser(ip, expect, 281))

    def test_combine_6(self):
        # test case 82
        ip = """
        int main()
        {
            float firstNumber, secondNumber, product;
            firstNumber = 90e-1;
            secondNumber = 85e-1;

            // Performs multiplication and stores the result in variable productOfTwoNumbers
            product = firstNumber * secondNumber;  
            // Result up to 2 decimal point is displayed using %.2lf
            printf("Product = %.2lf\\n", product);

            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 282))

    def test_combine_7(self):
        # test case 83
        ip = """
        int main()
        {
            int integerType;
            float floatType;

            // Sizeof operator is used to evaluate the size of a variable
            printf("Size of int: %ld bytes\\n",sizeof(integerType));
            printf("Size of float: %ld bytes\\n",sizeof(floatType));
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 283))

    def test_combine_8(self):
        # test case 84
        ip = """
        int main()
        {
            int number; number = 15;
            // True if the number is perfectly divisible by 2
            if(number % 2 == 0)
                printf("%d is even.", number);
            else
                printf("%d is odd.", number);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 284))

    def test_combine_9(self):
        # test case 85
        ip = """
        int main()
        {
            float n1, n2, n3;
            n1 = n2 = n3 = 109.0e-1; 
            if (n1>=n2)
            {
                if(n1>=n3)
                    printf("%.2lf is the largest number.", n1);
                else
                    printf("%.2lf is the largest number.", n3);
            }
            else
            {
                if(n2>=n3)
                    printf("%.2lf is the largest number.", n2);
                else
                    printf("%.2lf is the largest number.",n3);
            }
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 285))

    def test_combine_10(self):
        # test case 86
        ip = """
        int main()
        {
            int n, i, sum;
            sum = 0;
            n = 100;
            for(i = 1; i <= n; i = i + 1)
            {
                sum = sum + i;
            }
            printf("Sum = %d",sum);
            return 0;
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 286))

    def test_combine_11(self):
        # test case 87
        ip = """
        int main()
        {
            int n, i;
            int factorial;
            factorial = 1;
            n = 19;
            printf("integer: %d \\n", n);
            // show error if the user enters a negative integer
            if (n < 0)
                printf("Error! Factorial of a negative number doesn't exist.");
            else
            {
                for(i=1; i<=n; i=i+1)
                {
                    factorial = factorial * i;
                }
                printf("Factorial of %d = %ld", n, factorial);
            }
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 287))

    def test_combine_12(self):
        # test case 88
        ip = """
        int main()
        {
            int i, n, t1, t2, nextTerm;
            t1 = 0; t2 = 1;
            N = 100;
            printf("Fibonacci Series: ");
            for (i = 1; i <= n; i = i + 1)
            {
                printf("%d, ", t1);
                nextTerm = t1 + t2;
                t1 = t2;
                t2 = nextTerm;
            }
            return 0 + 0 + 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 288))

    def test_combine_13(self):
        # test case 89
        ip = """
        int main()
        {
            int number, i;
            printf("Factors of %d are: ", number);
            for(i=1; i <= number; i = i + 1)
            {
                if (number%i == 0)
                {
                    printf("%d ",i);
                }
            }
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 289))

    def test_combine_14(self):
        # test case 90
        ip = """
        int checkPrimeNumber(int n)
        {
            int j, flag;
            flag = 1;
            for(j = 2; j <= n/2; j = j + 1)
            {
                if (n%j == 0)
                {
                    flag =0 ;
                    break;
                }
            }
            return flag;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 290))

    def test_combine_15(self):
        # test case 91
        ip = """
        int main()
        {
            int n;
            printf("Enter a positive integer: ");
            n = 20;
            printf("Factorial of %d = %ld", n, multiplyNumbers(n));
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 291))

    def test_combine_16(self):
        # test case 92
        ip = """
        int main()
        {
            int i, n;
            float arr[100];
            printf("Enter total number of elements(1 to 100): ");
            n = 100;
            printf("\\n");
            // Stores number entered by the user
            for(i = 0; i < n; i = i + 1)
            {
                arr[i] = rand() ;
            }
            // Loop to store largest number to arr[0]
            for(i = 1; i < n; i = i + 1)
            {
                // Change < to > if you want to find the smallest element
                if(arr[0] < arr[i])
                    arr[0] = arr[i];
            }
            printf("Largest element = %.2f", arr[0]);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 292))

    def test_combine_17(self):
        # test case 93
        ip = """
        float calculateSD(float data[])
        {
            float sum, mean, standardDeviation;
            sum = 0.0;
            standardDeviation = 0.0;
            int i;
            for(i=0; i<10; i=i+1)
            {
                sum = sum + data[i];
            }
            mean = sum/10;
            for(i = 0; i < 10; i = i + 1)
            standardDeviation = standardDeviation + pow(data[i] - mean, 2);
            return sqrt(standardDeviation/10);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 293))

    def test_combine_18(self):
        # test case 94
        ip = """
        int main()
        {
            string str;
            int i, frequency; frequency = 0;
            printf("Enter a string: ");
            gets(str);
            for(i = 0; str[i] != "\0"; i = i + 1)
            {
                if("a" == str[i])
                    frequency = frequency + 1;
            }
            printf("Frequency of %c = %d", "a", frequency);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 294))

    def test_combine_19(self):
        # test case 95
        ip = """
        int main()
        {
            string s;
            int i;
            printf("Enter a string: ");
            gets(s);
            for(i = 0; s[i] != "\0"; i = i + 1)
                printf("Length of string: %d", i);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 295))

    def test_combine_20(self):
        # test case 96
        ip = """
        int main()
        {
            string s1, s2, i;
            printf("Enter string s1: ");
            gets(s1);
            for(i = 0; s1[i] != "\0"; i = i + 1)
            {
                s2[i] = s1[i];
            }
            s2[i] = "\0";
            printf("String s2: %s", s2);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 296))

    def test_combine_21(self):
        # test case 97
        ip = """
        int main()
        {
            string s1, s2, i, j;
            printf("Enter first string: ");
            gets(s1);
            printf("Enter second string: ");
            gets(s2);
            // calculate the length of string s1
            // and store it in i
            for(i = 0; s1[i] != "\0"; i = i + 1)
                for(j = 0; s2[j] != "\0"; j = j + 1)
                {
                    s1[i] = s2[j];
                }
            s1[i] = "\0";
            printf("After concatenation: %s", s1);
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 297))

    def test_combine_22(self):
        # test case 98
        ip = """
        int hcf(int n1, int n2)
        {
            if (n2 != 0)
                return hcf(n2, n1%n2);
            else 
                return n1;
        }
        int main()
        {
            int n1, n2;
            printf("Enter two positive integers: ");
            n1 = 8; n2 = 73;
            printf("G.C.D of %d and %d is %d.", n1, n2, hcf(n1,n2));
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 298))

    def test_combine_23(self):
        # test case 99
        ip = """
        int main() 
        { 
            // Calculate the time taken by fun() 
            // clock_t t;
            t = clock(); 
            fun(); 
            t = clock() - t; 
            float time_taken;
            time_taken = (double)(t/CLOCKS_PER_SEC); // in seconds 

            printf("fun() took %f seconds to execute \\n", time_taken); 
            return 0;
        } 
        """
        expect = "Error on line 10 col 33: ("
        self.assertTrue(TestParser.checkParser(ip, expect, 299))

    def test_combine_24(self):
        # test case 100
        ip = """
        void printRandoms(int lower, int upper, int count)
        {
            int i;
            for (i = 0; i < count; i = i + 1) { 
                int num;
                num = rand() % (upper - lower + 1) + lower; 
                printf("%d ", num);
            }
        }  
        int main() 
        {
            int lower, upper, count;
            lower = 5; upper = 7; count = 1;  
            // Use current time as 
            // seed for random generator 
            srand(time(0));
            printRandoms(lower, upper, count);  
            return 0;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(ip, expect, 300))
