# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0125\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\6\2@\n\2\r\2\16\2A\3\2\3\2\3\3\3\3\5\3")
        buf.write("H\n\3\3\4\3\4\3\4\3\4\7\4N\n\4\f\4\16\4Q\13\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\\\n\6\3\7\3\7\3\7\3\7")
        buf.write("\5\7b\n\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bm\n\b")
        buf.write("\3\t\3\t\3\t\7\tr\n\t\f\t\16\tu\13\t\3\n\3\n\3\n\3\n\5")
        buf.write("\n{\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\5\13\u0087\n\13\3\f\3\f\5\f\u008b\n\f\3\f\3\f\3\r")
        buf.write("\3\r\6\r\u0091\n\r\r\r\16\r\u0092\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u009c\n\16\3\17\3\17\6\17\u00a0\n")
        buf.write("\17\r\17\16\17\u00a1\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\5\23\u00ba\n\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\5\24\u00c3\n\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u00cb\n\25\f\25\16\25\u00ce\13\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\7\26\u00d6\n\26\f\26\16\26\u00d9")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\5\27\u00e0\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u00e7\n\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\7\31\u00ef\n\31\f\31\16\31\u00f2\13\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\7\32\u00fa\n\32\f\32\16\32\u00fd")
        buf.write("\13\32\3\33\3\33\3\33\5\33\u0102\n\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u010a\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0113\n\35\3\36\3\36\3\37\3\37\3\37\3")
        buf.write("\37\3\37\7\37\u011c\n\37\f\37\16\37\u011f\13\37\5\37\u0121")
        buf.write("\n\37\3\37\3\37\3\37\2\6(*\60\62 \2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<\2\t\3\2\3\6")
        buf.write("\3\2\30\31\3\2\32\35\4\2\20\20\22\22\4\2\21\21\23\24\4")
        buf.write("\2\22\22\25\25\3\2\'*\2\u012a\2?\3\2\2\2\4G\3\2\2\2\6")
        buf.write("I\3\2\2\2\bT\3\2\2\2\n[\3\2\2\2\f]\3\2\2\2\16l\3\2\2\2")
        buf.write("\20n\3\2\2\2\22v\3\2\2\2\24\u0086\3\2\2\2\26\u0088\3\2")
        buf.write("\2\2\30\u0090\3\2\2\2\32\u0094\3\2\2\2\34\u009d\3\2\2")
        buf.write("\2\36\u00a7\3\2\2\2 \u00b1\3\2\2\2\"\u00b4\3\2\2\2$\u00b7")
        buf.write("\3\2\2\2&\u00c2\3\2\2\2(\u00c4\3\2\2\2*\u00cf\3\2\2\2")
        buf.write(",\u00df\3\2\2\2.\u00e6\3\2\2\2\60\u00e8\3\2\2\2\62\u00f3")
        buf.write("\3\2\2\2\64\u0101\3\2\2\2\66\u0109\3\2\2\28\u0112\3\2")
        buf.write("\2\2:\u0114\3\2\2\2<\u0116\3\2\2\2>@\5\4\3\2?>\3\2\2\2")
        buf.write("@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\2\2\3D\3")
        buf.write("\3\2\2\2EH\5\6\4\2FH\5\f\7\2GE\3\2\2\2GF\3\2\2\2H\5\3")
        buf.write("\2\2\2IJ\5\b\5\2JO\5\n\6\2KL\7&\2\2LN\5\n\6\2MK\3\2\2")
        buf.write("\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2PR\3\2\2\2QO\3\2\2\2R")
        buf.write("S\7%\2\2S\7\3\2\2\2TU\t\2\2\2U\t\3\2\2\2V\\\7+\2\2WX\7")
        buf.write("+\2\2XY\7\37\2\2YZ\7(\2\2Z\\\7 \2\2[V\3\2\2\2[W\3\2\2")
        buf.write("\2\\\13\3\2\2\2]^\5\16\b\2^_\7+\2\2_a\7!\2\2`b\5\20\t")
        buf.write("\2a`\3\2\2\2ab\3\2\2\2bc\3\2\2\2cd\7\"\2\2de\5\26\f\2")
        buf.write("e\r\3\2\2\2fm\5\b\5\2gm\7\7\2\2hi\5\b\5\2ij\7\37\2\2j")
        buf.write("k\7 \2\2km\3\2\2\2lf\3\2\2\2lg\3\2\2\2lh\3\2\2\2m\17\3")
        buf.write("\2\2\2ns\5\22\n\2op\7&\2\2pr\5\22\n\2qo\3\2\2\2ru\3\2")
        buf.write("\2\2sq\3\2\2\2st\3\2\2\2t\21\3\2\2\2us\3\2\2\2vw\5\b\5")
        buf.write("\2wz\7+\2\2xy\7\37\2\2y{\7 \2\2zx\3\2\2\2z{\3\2\2\2{\23")
        buf.write("\3\2\2\2|\u0087\5\26\f\2}\u0087\5\32\16\2~\u0087\5\34")
        buf.write("\17\2\177\u0087\5\36\20\2\u0080\u0081\5&\24\2\u0081\u0082")
        buf.write("\7%\2\2\u0082\u0087\3\2\2\2\u0083\u0087\5 \21\2\u0084")
        buf.write("\u0087\5\"\22\2\u0085\u0087\5$\23\2\u0086|\3\2\2\2\u0086")
        buf.write("}\3\2\2\2\u0086~\3\2\2\2\u0086\177\3\2\2\2\u0086\u0080")
        buf.write("\3\2\2\2\u0086\u0083\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\25\3\2\2\2\u0088\u008a\7#\2\2\u0089")
        buf.write("\u008b\5\30\r\2\u008a\u0089\3\2\2\2\u008a\u008b\3\2\2")
        buf.write("\2\u008b\u008c\3\2\2\2\u008c\u008d\7$\2\2\u008d\27\3\2")
        buf.write("\2\2\u008e\u0091\5\6\4\2\u008f\u0091\5\24\13\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0090\3\2\2\2\u0092\u0093\3\2\2\2\u0093\31\3\2\2\2\u0094")
        buf.write("\u0095\7\b\2\2\u0095\u0096\7!\2\2\u0096\u0097\5&\24\2")
        buf.write("\u0097\u0098\7\"\2\2\u0098\u009b\5\24\13\2\u0099\u009a")
        buf.write("\7\t\2\2\u009a\u009c\5\24\13\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\33\3\2\2\2\u009d\u009f\7\13\2\2\u009e")
        buf.write("\u00a0\5\24\13\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\7\f\2\2\u00a4\u00a5\5&\24\2\u00a5")
        buf.write("\u00a6\7%\2\2\u00a6\35\3\2\2\2\u00a7\u00a8\7\n\2\2\u00a8")
        buf.write("\u00a9\7!\2\2\u00a9\u00aa\5&\24\2\u00aa\u00ab\7%\2\2\u00ab")
        buf.write("\u00ac\5&\24\2\u00ac\u00ad\7%\2\2\u00ad\u00ae\5&\24\2")
        buf.write("\u00ae\u00af\7\"\2\2\u00af\u00b0\5\24\13\2\u00b0\37\3")
        buf.write("\2\2\2\u00b1\u00b2\7\r\2\2\u00b2\u00b3\7%\2\2\u00b3!\3")
        buf.write("\2\2\2\u00b4\u00b5\7\16\2\2\u00b5\u00b6\7%\2\2\u00b6#")
        buf.write("\3\2\2\2\u00b7\u00b9\7\17\2\2\u00b8\u00ba\5&\24\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\7%\2\2\u00bc%\3\2\2\2\u00bd\u00be\5(\25\2")
        buf.write("\u00be\u00bf\7\36\2\2\u00bf\u00c0\5&\24\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00c3\5(\25\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\'\3\2\2\2\u00c4\u00c5\b\25\1\2\u00c5")
        buf.write("\u00c6\5*\26\2\u00c6\u00cc\3\2\2\2\u00c7\u00c8\f\4\2\2")
        buf.write("\u00c8\u00c9\7\27\2\2\u00c9\u00cb\5*\26\2\u00ca\u00c7")
        buf.write("\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cd\3\2\2\2\u00cd)\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf")
        buf.write("\u00d0\b\26\1\2\u00d0\u00d1\5,\27\2\u00d1\u00d7\3\2\2")
        buf.write("\2\u00d2\u00d3\f\4\2\2\u00d3\u00d4\7\26\2\2\u00d4\u00d6")
        buf.write("\5,\27\2\u00d5\u00d2\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8+\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00da\u00db\5.\30\2\u00db\u00dc\t\3\2\2")
        buf.write("\u00dc\u00dd\5.\30\2\u00dd\u00e0\3\2\2\2\u00de\u00e0\5")
        buf.write(".\30\2\u00df\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0-")
        buf.write("\3\2\2\2\u00e1\u00e2\5\60\31\2\u00e2\u00e3\t\4\2\2\u00e3")
        buf.write("\u00e4\5\60\31\2\u00e4\u00e7\3\2\2\2\u00e5\u00e7\5\60")
        buf.write("\31\2\u00e6\u00e1\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7/\3")
        buf.write("\2\2\2\u00e8\u00e9\b\31\1\2\u00e9\u00ea\5\62\32\2\u00ea")
        buf.write("\u00f0\3\2\2\2\u00eb\u00ec\f\4\2\2\u00ec\u00ed\t\5\2\2")
        buf.write("\u00ed\u00ef\5\62\32\2\u00ee\u00eb\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\61\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f4\b\32\1\2\u00f4")
        buf.write("\u00f5\5\64\33\2\u00f5\u00fb\3\2\2\2\u00f6\u00f7\f\4\2")
        buf.write("\2\u00f7\u00f8\t\6\2\2\u00f8\u00fa\5\64\33\2\u00f9\u00f6")
        buf.write("\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fc\3\2\2\2\u00fc\63\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe")
        buf.write("\u00ff\t\7\2\2\u00ff\u0102\5\64\33\2\u0100\u0102\5\66")
        buf.write("\34\2\u0101\u00fe\3\2\2\2\u0101\u0100\3\2\2\2\u0102\65")
        buf.write("\3\2\2\2\u0103\u0104\58\35\2\u0104\u0105\7\37\2\2\u0105")
        buf.write("\u0106\5&\24\2\u0106\u0107\7 \2\2\u0107\u010a\3\2\2\2")
        buf.write("\u0108\u010a\58\35\2\u0109\u0103\3\2\2\2\u0109\u0108\3")
        buf.write("\2\2\2\u010a\67\3\2\2\2\u010b\u0113\5:\36\2\u010c\u0113")
        buf.write("\5<\37\2\u010d\u0113\7+\2\2\u010e\u010f\7!\2\2\u010f\u0110")
        buf.write("\5&\24\2\u0110\u0111\7\"\2\2\u0111\u0113\3\2\2\2\u0112")
        buf.write("\u010b\3\2\2\2\u0112\u010c\3\2\2\2\u0112\u010d\3\2\2\2")
        buf.write("\u0112\u010e\3\2\2\2\u01139\3\2\2\2\u0114\u0115\t\b\2")
        buf.write("\2\u0115;\3\2\2\2\u0116\u0117\7+\2\2\u0117\u0120\7!\2")
        buf.write("\2\u0118\u011d\5&\24\2\u0119\u011a\7&\2\2\u011a\u011c")
        buf.write("\5&\24\2\u011b\u0119\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u0120\u0118\3\2\2\2\u0120\u0121\3")
        buf.write("\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123\7\"\2\2\u0123=")
        buf.write("\3\2\2\2\35AGO[alsz\u0086\u008a\u0090\u0092\u009b\u00a1")
        buf.write("\u00b9\u00c2\u00cc\u00d7\u00df\u00e6\u00f0\u00fb\u0101")
        buf.write("\u0109\u0112\u011d\u0120")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'boolean'", "'int'", "'float'", "'string'", 
                     "'void'", "'if'", "'else'", "'for'", "'do'", "'while'", 
                     "'break'", "'continue'", "'return'", "'+'", "'*'", 
                     "'-'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'='", "'['", 
                     "']'", "'('", "')'", "'{'", "'}'", "';'", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRTYPE", 
                      "VOIDTYPE", "IF", "ELSE", "FOR", "DO", "WHILE", "BREAK", 
                      "CONTINUE", "RETURN", "ADDOP", "MULOP", "SUBOP", "DIVOP", 
                      "MODOP", "NOTOP", "ANDOP", "OROP", "EQUAL", "NOTEQUAL", 
                      "LT", "GT", "LE", "GE", "ASSIGN", "LSB", "RSB", "LB", 
                      "RB", "LP", "RP", "SEMI", "COMMA", "BOOLLIT", "INTLIT", 
                      "FLOATLIT", "STRLIT", "IDENTIFIER", "WS", "NEWLINE", 
                      "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_var_declaration = 2
    RULE_primi_type = 3
    RULE_var = 4
    RULE_func_declaration = 5
    RULE_func_type = 6
    RULE_para_list = 7
    RULE_para_declaration = 8
    RULE_stmt = 9
    RULE_block_stmt = 10
    RULE_body = 11
    RULE_if_stmt = 12
    RULE_dowhile_stmt = 13
    RULE_for_stmt = 14
    RULE_break_stmt = 15
    RULE_continue_stmt = 16
    RULE_return_stmt = 17
    RULE_expr = 18
    RULE_expr1 = 19
    RULE_expr2 = 20
    RULE_expr3 = 21
    RULE_expr4 = 22
    RULE_expr5 = 23
    RULE_expr6 = 24
    RULE_expr7 = 25
    RULE_expr8 = 26
    RULE_expr9 = 27
    RULE_literal = 28
    RULE_call_expr = 29

    ruleNames =  [ "program", "declaration", "var_declaration", "primi_type", 
                   "var", "func_declaration", "func_type", "para_list", 
                   "para_declaration", "stmt", "block_stmt", "body", "if_stmt", 
                   "dowhile_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "literal", 
                   "call_expr" ]

    EOF = Token.EOF
    BOOLTYPE=1
    INTTYPE=2
    FLOATTYPE=3
    STRTYPE=4
    VOIDTYPE=5
    IF=6
    ELSE=7
    FOR=8
    DO=9
    WHILE=10
    BREAK=11
    CONTINUE=12
    RETURN=13
    ADDOP=14
    MULOP=15
    SUBOP=16
    DIVOP=17
    MODOP=18
    NOTOP=19
    ANDOP=20
    OROP=21
    EQUAL=22
    NOTEQUAL=23
    LT=24
    GT=25
    LE=26
    GE=27
    ASSIGN=28
    LSB=29
    RSB=30
    LB=31
    RB=32
    LP=33
    RP=34
    SEMI=35
    COMMA=36
    BOOLLIT=37
    INTLIT=38
    FLOATLIT=39
    STRLIT=40
    IDENTIFIER=41
    WS=42
    NEWLINE=43
    COMMENT=44
    ERROR_CHAR=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclarationContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.declaration()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 65
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self):
            return self.getTypedRuleContext(MCParser.Var_declarationContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(MCParser.Func_declarationContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.var_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.func_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primi_type(self):
            return self.getTypedRuleContext(MCParser.Primi_typeContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = MCParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.primi_type()
            self.state = 72
            self.var()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 73
                self.match(MCParser.COMMA)
                self.state = 74
                self.var()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primi_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRTYPE(self):
            return self.getToken(MCParser.STRTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primi_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimi_type" ):
                return visitor.visitPrimi_type(self)
            else:
                return visitor.visitChildren(self)




    def primi_type(self):

        localctx = MCParser.Primi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primi_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(MCParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(MCParser.IDENTIFIER)
                self.state = 86
                self.match(MCParser.LSB)
                self.state = 87
                self.match(MCParser.INTLIT)
                self.state = 88
                self.match(MCParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_type(self):
            return self.getTypedRuleContext(MCParser.Func_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def para_list(self):
            return self.getTypedRuleContext(MCParser.Para_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declaration" ):
                return visitor.visitFunc_declaration(self)
            else:
                return visitor.visitChildren(self)




    def func_declaration(self):

        localctx = MCParser.Func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.func_type()
            self.state = 92
            self.match(MCParser.IDENTIFIER)
            self.state = 93
            self.match(MCParser.LB)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRTYPE))) != 0):
                self.state = 94
                self.para_list()


            self.state = 97
            self.match(MCParser.RB)
            self.state = 98
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primi_type(self):
            return self.getTypedRuleContext(MCParser.Primi_typeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_func_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_type" ):
                return visitor.visitFunc_type(self)
            else:
                return visitor.visitChildren(self)




    def func_type(self):

        localctx = MCParser.Func_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_type)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.primi_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 102
                self.primi_type()
                self.state = 103
                self.match(MCParser.LSB)
                self.state = 104
                self.match(MCParser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Para_declarationContext)
            else:
                return self.getTypedRuleContext(MCParser.Para_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = MCParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.para_declaration()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 109
                self.match(MCParser.COMMA)
                self.state = 110
                self.para_declaration()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primi_type(self):
            return self.getTypedRuleContext(MCParser.Primi_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_declaration" ):
                return visitor.visitPara_declaration(self)
            else:
                return visitor.visitChildren(self)




    def para_declaration(self):

        localctx = MCParser.Para_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_para_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.primi_type()
            self.state = 117
            self.match(MCParser.IDENTIFIER)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 118
                self.match(MCParser.LSB)
                self.state = 119
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(MCParser.Dowhile_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.block_stmt()
                pass
            elif token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.if_stmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.dowhile_stmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.for_stmt()
                pass
            elif token in [MCParser.SUBOP, MCParser.NOTOP, MCParser.LB, MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT, MCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.expr()
                self.state = 127
                self.match(MCParser.SEMI)
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.break_stmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.continue_stmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.return_stmt()
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


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def body(self):
            return self.getTypedRuleContext(MCParser.BodyContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MCParser.LP)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRTYPE) | (1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.SUBOP) | (1 << MCParser.NOTOP) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 135
                self.body()


            self.state = 138
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declarationContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declarationContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.BOOLTYPE, MCParser.INTTYPE, MCParser.FLOATTYPE, MCParser.STRTYPE]:
                    self.state = 140
                    self.var_declaration()
                    pass
                elif token in [MCParser.IF, MCParser.FOR, MCParser.DO, MCParser.BREAK, MCParser.CONTINUE, MCParser.RETURN, MCParser.SUBOP, MCParser.NOTOP, MCParser.LB, MCParser.LP, MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT, MCParser.IDENTIFIER]:
                    self.state = 141
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 144 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLTYPE) | (1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.STRTYPE) | (1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.SUBOP) | (1 << MCParser.NOTOP) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT) | (1 << MCParser.IDENTIFIER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(MCParser.IF)
            self.state = 147
            self.match(MCParser.LB)
            self.state = 148
            self.expr()
            self.state = 149
            self.match(MCParser.RB)
            self.state = 150
            self.stmt()
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 151
                self.match(MCParser.ELSE)
                self.state = 152
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_dowhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stmt" ):
                return visitor.visitDowhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhile_stmt(self):

        localctx = MCParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dowhile_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MCParser.DO)
            self.state = 157 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self.stmt()
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.IF) | (1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.SUBOP) | (1 << MCParser.NOTOP) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT) | (1 << MCParser.IDENTIFIER))) != 0)):
                    break

            self.state = 161
            self.match(MCParser.WHILE)
            self.state = 162
            self.expr()
            self.state = 163
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MCParser.FOR)
            self.state = 166
            self.match(MCParser.LB)
            self.state = 167
            self.expr()
            self.state = 168
            self.match(MCParser.SEMI)
            self.state = 169
            self.expr()
            self.state = 170
            self.match(MCParser.SEMI)
            self.state = 171
            self.expr()
            self.state = 172
            self.match(MCParser.RB)
            self.state = 173
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MCParser.BREAK)
            self.state = 176
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(MCParser.CONTINUE)
            self.state = 179
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(MCParser.RETURN)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.SUBOP) | (1 << MCParser.NOTOP) | (1 << MCParser.LB) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 182
                self.expr()


            self.state = 185
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MCParser.Expr1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr)
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.expr1(0)
                self.state = 188
                self.match(MCParser.ASSIGN)
                self.state = 189
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.expr1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MCParser.Expr1Context,0)


        def OROP(self):
            return self.getToken(MCParser.OROP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 197
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 198
                    self.match(MCParser.OROP)
                    self.state = 199
                    self.expr2(0) 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MCParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(MCParser.ANDOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    self.match(MCParser.ANDOP)
                    self.state = 210
                    self.expr3() 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr4Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr4Context,i)


        def EQUAL(self):
            return self.getToken(MCParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(MCParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)




    def expr3(self):

        localctx = MCParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr3)
        self._la = 0 # Token type
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.expr4()
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==MCParser.EQUAL or _la==MCParser.NOTEQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.expr4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.expr4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr5Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr5Context,i)


        def LT(self):
            return self.getToken(MCParser.LT, 0)

        def LE(self):
            return self.getToken(MCParser.LE, 0)

        def GT(self):
            return self.getToken(MCParser.GT, 0)

        def GE(self):
            return self.getToken(MCParser.GE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MCParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.expr5(0)
                self.state = 224
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT) | (1 << MCParser.GT) | (1 << MCParser.LE) | (1 << MCParser.GE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 225
                self.expr5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.expr5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(MCParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(MCParser.Expr5Context,0)


        def ADDOP(self):
            return self.getToken(MCParser.ADDOP, 0)

        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 238
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 233
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADDOP or _la==MCParser.SUBOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.expr6(0) 
                self.state = 240
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MCParser.Expr6Context,0)


        def DIVOP(self):
            return self.getToken(MCParser.DIVOP, 0)

        def MULOP(self):
            return self.getToken(MCParser.MULOP, 0)

        def MODOP(self):
            return self.getToken(MCParser.MODOP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 249
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MULOP) | (1 << MCParser.DIVOP) | (1 << MCParser.MODOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 246
                    self.expr7() 
                self.state = 251
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def SUBOP(self):
            return self.getToken(MCParser.SUBOP, 0)

        def NOTOP(self):
            return self.getToken(MCParser.NOTOP, 0)

        def expr8(self):
            return self.getTypedRuleContext(MCParser.Expr8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MCParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUBOP, MCParser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==MCParser.SUBOP or _la==MCParser.NOTOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.expr7()
                pass
            elif token in [MCParser.LB, MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRLIT, MCParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.expr8()
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


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(MCParser.Expr9Context,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MCParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr8)
        try:
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.expr9()
                self.state = 258
                self.match(MCParser.LSB)
                self.state = 259
                self.expr()
                self.state = 260
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def call_expr(self):
            return self.getTypedRuleContext(MCParser.Call_exprContext,0)


        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = MCParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr9)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.call_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.match(MCParser.IDENTIFIER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.match(MCParser.LB)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(MCParser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def STRLIT(self):
            return self.getToken(MCParser.STRLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MCParser.IDENTIFIER, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_call_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_expr" ):
                return visitor.visitCall_expr(self)
            else:
                return visitor.visitChildren(self)




    def call_expr(self):

        localctx = MCParser.Call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MCParser.IDENTIFIER)
            self.state = 277
            self.match(MCParser.LB)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.SUBOP) | (1 << MCParser.NOTOP) | (1 << MCParser.LB) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRLIT) | (1 << MCParser.IDENTIFIER))) != 0):
                self.state = 278
                self.expr()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 279
                    self.match(MCParser.COMMA)
                    self.state = 280
                    self.expr()
                    self.state = 285
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 288
            self.match(MCParser.RB)
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
        self._predicates[19] = self.expr1_sempred
        self._predicates[20] = self.expr2_sempred
        self._predicates[23] = self.expr5_sempred
        self._predicates[24] = self.expr6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




