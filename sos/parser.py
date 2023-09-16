# type: ignore
# ruff: noqa
from __future__ import annotations

from sly import Parser
from sly.yacc import YaccProduction
from sos.lexer import SOSLexer


class SOSParser(Parser):
    tokens = SOSLexer.tokens

    # Grammar rules and actions
    @_("expr PLUS term")
    def expr(self, p: YaccProduction) -> int | float:
        return p.expr + p.term

    @_("expr MINUS term")
    def expr(self, p: YaccProduction) -> int | float:
        return p.expr - p.term

    @_("term")
    def expr(self, p: YaccProduction) -> int | float:
        return p.term

    @_("term TIMES factor")
    def term(self, p: YaccProduction) -> int | float:
        return p.term * p.factor

    @_("term DIVIDE factor")
    def term(self, p: YaccProduction) -> int | float:
        return p.term / p.factor

    @_("factor")
    def term(self, p: YaccProduction) -> int | float:
        return p.factor

    @_("NUMBER")
    def factor(self, p: YaccProduction) -> int | float:
        return p.NUMBER

    @_("LPAREN expr RPAREN")
    def factor(self, p: YaccProduction) -> int | float:
        return p.expr


if __name__ == "__main__":
    lexer = SOSLexer()
    parser = SOSParser()
    while True:
        try:
            text = input("sos > ")
        except EOFError:
            break
        if text:
            result = parser.parse(lexer.tokenize(text))
            print(result)
