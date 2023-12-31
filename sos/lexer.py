# type: ignore
# ruff: noqa
from __future__ import annotations

from sly import Lexer
from sly.lex import Token


class SOSLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {
        NAME,
        NUMBER,
        STRING,
        IF,
        ELSE,
        WHILE,
        PRINT,
        RETURN,
        FUN,
        TO,
        ARROW,
        EQEQ,
        NE,
        LE,
        GE,
        AND,
        OR,
        NOT,
        ASSIGN,
        PLUS,
        MINUS,
        TIMES,
        DIVIDE,
        MOD,
        LPAREN,
        RPAREN,
        LBRACE,
        RBRACE,
        COMMA,
        SEMI,
        COLON,
    }

    # String containing ignored characters between tokens
    ignore = " \t"

    # Regular expression rules for tokens
    NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
    IF = r"if"
    ELSE = r"else"
    WHILE = r"while"
    PRINT = r"print"
    RETURN = r"return"
    FUN = r"fun"
    TO = r"to"
    ARROW = r"->"
    EQEQ = r"=="
    NE = r"!="
    LE = r"<="
    GE = r">="
    AND = r"&&"
    OR = r"\|\|"
    NOT = r"!"
    ASSIGN = r"="
    PLUS = r"\+"
    MINUS = r"-"
    TIMES = r"\*"
    DIVIDE = r"/"
    MOD = r"%"
    LPAREN = r"\("
    RPAREN = r"\)"
    LBRACE = r"\{"
    RBRACE = r"\}"
    COMMA = r","
    SEMI = r";"
    COLON = r":"

    # Number rule for both integers and floats
    @_(r"\d*\.\d+", r"\d+")
    def NUMBER(self, t: Token) -> Token:
        if t.value.count(".") == 1:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    @_(r'"[^"]*"')
    def STRING(self, t: Token) -> Token:
        t.value = str(t.value)
        return t

    # Ignored text
    ignore_comment = r"\#.*"

    # Line number tracking
    @_(r"\n+")
    def ignore_newline(self, t: Token) -> None:
        self.lineno += t.value.count("\n")


if __name__ == "__main__":
    data = "x = 3.21231 + 42 * (s - t)"
    lexer = SOSLexer()
    for tok in lexer.tokenize(data):
        print(f"type={tok.type!r}, value={tok.value!r}")
