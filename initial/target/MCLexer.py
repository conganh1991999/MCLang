# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u017a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u00fc\n&\3\'\6\'\u00ff")
        buf.write("\n\'\r\'\16\'\u0100\3(\3(\3)\3)\5)\u0107\n)\3)\3)\3*\5")
        buf.write("*\u010c\n*\3*\3*\3*\5*\u0111\n*\3*\3*\3*\5*\u0116\n*\3")
        buf.write("*\5*\u0119\n*\3*\3*\3*\5*\u011e\n*\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\7-\u0128\n-\f-\16-\u012b\13-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\61\5\61\u0138\n\61\3\62\3\62\3\62")
        buf.write("\7\62\u013d\n\62\f\62\16\62\u0140\13\62\3\63\6\63\u0143")
        buf.write("\n\63\r\63\16\63\u0144\3\63\3\63\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\65\7\65\u014f\n\65\f\65\16\65\u0152\13\65\3\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\7\66\u015b\n\66\f\66\16\66")
        buf.write("\u015e\13\66\3\67\3\67\5\67\u0162\n\67\3\67\3\67\38\3")
        buf.write("8\39\39\39\79\u016b\n9\f9\169\u016e\139\3:\3:\3:\7:\u0173")
        buf.write("\n:\f:\16:\u0176\13:\3:\3:\3:\3\u0150\2;\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O\2Q\2S)U\2W\2Y*")
        buf.write("[\2]\2_\2a\2c+e,g-i\2k\2m.o/q\60s\61\3\2\13\3\2\62;\4")
        buf.write("\2GGgg\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^^\3\2c|\3\2C")
        buf.write("\\\5\2\13\f\16\17\"\"\3\2\f\f\f\2#$\'\'*/\61;=@C]__aa")
        buf.write("c}\177\177\2\u0186\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2S\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\3u\3\2\2\2\5}\3\2\2\2")
        buf.write("\7\u0081\3\2\2\2\t\u0087\3\2\2\2\13\u008e\3\2\2\2\r\u0093")
        buf.write("\3\2\2\2\17\u0096\3\2\2\2\21\u009b\3\2\2\2\23\u009f\3")
        buf.write("\2\2\2\25\u00a2\3\2\2\2\27\u00a8\3\2\2\2\31\u00ae\3\2")
        buf.write("\2\2\33\u00b7\3\2\2\2\35\u00be\3\2\2\2\37\u00c0\3\2\2")
        buf.write("\2!\u00c2\3\2\2\2#\u00c4\3\2\2\2%\u00c6\3\2\2\2\'\u00c8")
        buf.write("\3\2\2\2)\u00ca\3\2\2\2+\u00cd\3\2\2\2-\u00d0\3\2\2\2")
        buf.write("/\u00d3\3\2\2\2\61\u00d6\3\2\2\2\63\u00d8\3\2\2\2\65\u00da")
        buf.write("\3\2\2\2\67\u00dd\3\2\2\29\u00e0\3\2\2\2;\u00e2\3\2\2")
        buf.write("\2=\u00e4\3\2\2\2?\u00e6\3\2\2\2A\u00e8\3\2\2\2C\u00ea")
        buf.write("\3\2\2\2E\u00ec\3\2\2\2G\u00ee\3\2\2\2I\u00f0\3\2\2\2")
        buf.write("K\u00fb\3\2\2\2M\u00fe\3\2\2\2O\u0102\3\2\2\2Q\u0104\3")
        buf.write("\2\2\2S\u011d\3\2\2\2U\u011f\3\2\2\2W\u0121\3\2\2\2Y\u0124")
        buf.write("\3\2\2\2[\u012e\3\2\2\2]\u0130\3\2\2\2_\u0132\3\2\2\2")
        buf.write("a\u0137\3\2\2\2c\u0139\3\2\2\2e\u0142\3\2\2\2g\u0148\3")
        buf.write("\2\2\2i\u014a\3\2\2\2k\u0156\3\2\2\2m\u0161\3\2\2\2o\u0165")
        buf.write("\3\2\2\2q\u0167\3\2\2\2s\u016f\3\2\2\2uv\7d\2\2vw\7q\2")
        buf.write("\2wx\7q\2\2xy\7n\2\2yz\7g\2\2z{\7c\2\2{|\7p\2\2|\4\3\2")
        buf.write("\2\2}~\7k\2\2~\177\7p\2\2\177\u0080\7v\2\2\u0080\6\3\2")
        buf.write("\2\2\u0081\u0082\7h\2\2\u0082\u0083\7n\2\2\u0083\u0084")
        buf.write("\7q\2\2\u0084\u0085\7c\2\2\u0085\u0086\7v\2\2\u0086\b")
        buf.write("\3\2\2\2\u0087\u0088\7u\2\2\u0088\u0089\7v\2\2\u0089\u008a")
        buf.write("\7t\2\2\u008a\u008b\7k\2\2\u008b\u008c\7p\2\2\u008c\u008d")
        buf.write("\7i\2\2\u008d\n\3\2\2\2\u008e\u008f\7x\2\2\u008f\u0090")
        buf.write("\7q\2\2\u0090\u0091\7k\2\2\u0091\u0092\7f\2\2\u0092\f")
        buf.write("\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095\7h\2\2\u0095\16")
        buf.write("\3\2\2\2\u0096\u0097\7g\2\2\u0097\u0098\7n\2\2\u0098\u0099")
        buf.write("\7u\2\2\u0099\u009a\7g\2\2\u009a\20\3\2\2\2\u009b\u009c")
        buf.write("\7h\2\2\u009c\u009d\7q\2\2\u009d\u009e\7t\2\2\u009e\22")
        buf.write("\3\2\2\2\u009f\u00a0\7f\2\2\u00a0\u00a1\7q\2\2\u00a1\24")
        buf.write("\3\2\2\2\u00a2\u00a3\7y\2\2\u00a3\u00a4\7j\2\2\u00a4\u00a5")
        buf.write("\7k\2\2\u00a5\u00a6\7n\2\2\u00a6\u00a7\7g\2\2\u00a7\26")
        buf.write("\3\2\2\2\u00a8\u00a9\7d\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab")
        buf.write("\7g\2\2\u00ab\u00ac\7c\2\2\u00ac\u00ad\7m\2\2\u00ad\30")
        buf.write("\3\2\2\2\u00ae\u00af\7e\2\2\u00af\u00b0\7q\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7p\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6\7g\2\2\u00b6\32")
        buf.write("\3\2\2\2\u00b7\u00b8\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba")
        buf.write("\7v\2\2\u00ba\u00bb\7w\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd")
        buf.write("\7p\2\2\u00bd\34\3\2\2\2\u00be\u00bf\7-\2\2\u00bf\36\3")
        buf.write("\2\2\2\u00c0\u00c1\7,\2\2\u00c1 \3\2\2\2\u00c2\u00c3\7")
        buf.write("/\2\2\u00c3\"\3\2\2\2\u00c4\u00c5\7\61\2\2\u00c5$\3\2")
        buf.write("\2\2\u00c6\u00c7\7\'\2\2\u00c7&\3\2\2\2\u00c8\u00c9\7")
        buf.write("#\2\2\u00c9(\3\2\2\2\u00ca\u00cb\7(\2\2\u00cb\u00cc\7")
        buf.write("(\2\2\u00cc*\3\2\2\2\u00cd\u00ce\7~\2\2\u00ce\u00cf\7")
        buf.write("~\2\2\u00cf,\3\2\2\2\u00d0\u00d1\7?\2\2\u00d1\u00d2\7")
        buf.write("?\2\2\u00d2.\3\2\2\2\u00d3\u00d4\7#\2\2\u00d4\u00d5\7")
        buf.write("?\2\2\u00d5\60\3\2\2\2\u00d6\u00d7\7>\2\2\u00d7\62\3\2")
        buf.write("\2\2\u00d8\u00d9\7@\2\2\u00d9\64\3\2\2\2\u00da\u00db\7")
        buf.write(">\2\2\u00db\u00dc\7?\2\2\u00dc\66\3\2\2\2\u00dd\u00de")
        buf.write("\7@\2\2\u00de\u00df\7?\2\2\u00df8\3\2\2\2\u00e0\u00e1")
        buf.write("\7?\2\2\u00e1:\3\2\2\2\u00e2\u00e3\7]\2\2\u00e3<\3\2\2")
        buf.write("\2\u00e4\u00e5\7_\2\2\u00e5>\3\2\2\2\u00e6\u00e7\7*\2")
        buf.write("\2\u00e7@\3\2\2\2\u00e8\u00e9\7+\2\2\u00e9B\3\2\2\2\u00ea")
        buf.write("\u00eb\7}\2\2\u00ebD\3\2\2\2\u00ec\u00ed\7\177\2\2\u00ed")
        buf.write("F\3\2\2\2\u00ee\u00ef\7=\2\2\u00efH\3\2\2\2\u00f0\u00f1")
        buf.write("\7.\2\2\u00f1J\3\2\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7w\2\2\u00f5\u00fc\7g\2\2\u00f6\u00f7")
        buf.write("\7h\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7u\2\2\u00fa\u00fc\7g\2\2\u00fb\u00f2\3\2\2\2\u00fb\u00f6")
        buf.write("\3\2\2\2\u00fcL\3\2\2\2\u00fd\u00ff\t\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u00fe\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0101N\3\2\2\2\u0102\u0103\7\60\2\2\u0103")
        buf.write("P\3\2\2\2\u0104\u0106\t\3\2\2\u0105\u0107\7/\2\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\5M\'\2\u0109R\3\2\2\2\u010a\u010c\5M\'\2")
        buf.write("\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010e\5O(\2\u010e\u0110\5M\'\2\u010f\u0111")
        buf.write("\5Q)\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u011e")
        buf.write("\3\2\2\2\u0112\u0113\5M\'\2\u0113\u0115\5O(\2\u0114\u0116")
        buf.write("\5M\'\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0118\3\2\2\2\u0117\u0119\5Q)\2\u0118\u0117\3\2\2\2\u0118")
        buf.write("\u0119\3\2\2\2\u0119\u011e\3\2\2\2\u011a\u011b\5M\'\2")
        buf.write("\u011b\u011c\5Q)\2\u011c\u011e\3\2\2\2\u011d\u010b\3\2")
        buf.write("\2\2\u011d\u0112\3\2\2\2\u011d\u011a\3\2\2\2\u011eT\3")
        buf.write("\2\2\2\u011f\u0120\7$\2\2\u0120V\3\2\2\2\u0121\u0122\7")
        buf.write("^\2\2\u0122\u0123\t\4\2\2\u0123X\3\2\2\2\u0124\u0129\5")
        buf.write("U+\2\u0125\u0128\n\5\2\2\u0126\u0128\5W,\2\u0127\u0125")
        buf.write("\3\2\2\2\u0127\u0126\3\2\2\2\u0128\u012b\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012c\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012c\u012d\5U+\2\u012dZ\3\2\2\2")
        buf.write("\u012e\u012f\t\2\2\2\u012f\\\3\2\2\2\u0130\u0131\t\6\2")
        buf.write("\2\u0131^\3\2\2\2\u0132\u0133\t\7\2\2\u0133`\3\2\2\2\u0134")
        buf.write("\u0138\5]/\2\u0135\u0138\5_\60\2\u0136\u0138\7a\2\2\u0137")
        buf.write("\u0134\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0138b\3\2\2\2\u0139\u013e\5a\61\2\u013a\u013d\5a\61")
        buf.write("\2\u013b\u013d\5[.\2\u013c\u013a\3\2\2\2\u013c\u013b\3")
        buf.write("\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f")
        buf.write("\3\2\2\2\u013fd\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0143")
        buf.write("\t\b\2\2\u0142\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0146\u0147\b\63\2\2\u0147f\3\2\2\2\u0148\u0149\7\f\2")
        buf.write("\2\u0149h\3\2\2\2\u014a\u014b\7\61\2\2\u014b\u014c\7,")
        buf.write("\2\2\u014c\u0150\3\2\2\2\u014d\u014f\13\2\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u0151\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150\3\2\2\2")
        buf.write("\u0153\u0154\7,\2\2\u0154\u0155\7\61\2\2\u0155j\3\2\2")
        buf.write("\2\u0156\u0157\7\61\2\2\u0157\u0158\7\61\2\2\u0158\u015c")
        buf.write("\3\2\2\2\u0159\u015b\n\t\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("\u015e\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2")
        buf.write("\u015dl\3\2\2\2\u015e\u015c\3\2\2\2\u015f\u0162\5i\65")
        buf.write("\2\u0160\u0162\5k\66\2\u0161\u015f\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0164\b\67\2\2\u0164")
        buf.write("n\3\2\2\2\u0165\u0166\n\n\2\2\u0166p\3\2\2\2\u0167\u016c")
        buf.write("\5U+\2\u0168\u016b\n\5\2\2\u0169\u016b\5W,\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016dr\3\2\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016f\u0174\5U+\2\u0170\u0173\n\5\2\2\u0171")
        buf.write("\u0173\5W,\2\u0172\u0170\3\2\2\2\u0172\u0171\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\7")
        buf.write("^\2\2\u0178\u0179\n\4\2\2\u0179t\3\2\2\2\30\2\u00fb\u0100")
        buf.write("\u0106\u010b\u0110\u0115\u0118\u011d\u0127\u0129\u0137")
        buf.write("\u013c\u013e\u0144\u0150\u015c\u0161\u016a\u016c\u0172")
        buf.write("\u0174\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLTYPE = 1
    INTTYPE = 2
    FLOATTYPE = 3
    STRTYPE = 4
    VOIDTYPE = 5
    IF = 6
    ELSE = 7
    FOR = 8
    DO = 9
    WHILE = 10
    BREAK = 11
    CONTINUE = 12
    RETURN = 13
    ADDOP = 14
    MULOP = 15
    SUBOP = 16
    DIVOP = 17
    MODOP = 18
    NOTOP = 19
    ANDOP = 20
    OROP = 21
    EQUAL = 22
    NOTEQUAL = 23
    LT = 24
    GT = 25
    LE = 26
    GE = 27
    ASSIGN = 28
    LSB = 29
    RSB = 30
    LB = 31
    RB = 32
    LP = 33
    RP = 34
    SEMI = 35
    COMMA = 36
    BOOLLIT = 37
    INTLIT = 38
    FLOATLIT = 39
    STRLIT = 40
    IDENTIFIER = 41
    WS = 42
    NEWLINE = 43
    COMMENT = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'int'", "'float'", "'string'", "'void'", "'if'", 
            "'else'", "'for'", "'do'", "'while'", "'break'", "'continue'", 
            "'return'", "'+'", "'*'", "'-'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "';'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRTYPE", "VOIDTYPE", "IF", 
            "ELSE", "FOR", "DO", "WHILE", "BREAK", "CONTINUE", "RETURN", 
            "ADDOP", "MULOP", "SUBOP", "DIVOP", "MODOP", "NOTOP", "ANDOP", 
            "OROP", "EQUAL", "NOTEQUAL", "LT", "GT", "LE", "GE", "ASSIGN", 
            "LSB", "RSB", "LB", "RB", "LP", "RP", "SEMI", "COMMA", "BOOLLIT", 
            "INTLIT", "FLOATLIT", "STRLIT", "IDENTIFIER", "WS", "NEWLINE", 
            "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BOOLTYPE", "INTTYPE", "FLOATTYPE", "STRTYPE", "VOIDTYPE", 
                  "IF", "ELSE", "FOR", "DO", "WHILE", "BREAK", "CONTINUE", 
                  "RETURN", "ADDOP", "MULOP", "SUBOP", "DIVOP", "MODOP", 
                  "NOTOP", "ANDOP", "OROP", "EQUAL", "NOTEQUAL", "LT", "GT", 
                  "LE", "GE", "ASSIGN", "LSB", "RSB", "LB", "RB", "LP", 
                  "RP", "SEMI", "COMMA", "BOOLLIT", "INTLIT", "DOT", "EXP", 
                  "FLOATLIT", "QUOTE", "IN_STRING", "STRLIT", "DIGIT", "LOWCASE", 
                  "UPCASE", "IDSTART", "IDENTIFIER", "WS", "NEWLINE", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit();
            raise UncloseString(result.text[1:]);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text[1:]);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text);
        elif tk == self.STRLIT:
            result = super().emit();
            result.text = result.text[1:-1];
            return result;
        else:
            return super().emit();


