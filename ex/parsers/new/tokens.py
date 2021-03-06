from .tokens_base import *


class TokenEof(Token):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_EOF, '__EOF__', *args, **kwargs)


class TokenOfRange(Token):
    pass


class TokenDollar(TokenOfRange):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_DOLLAR, '$', *args, **kwargs)


class TokenComma(TokenOfRange):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_COMMA, ',', *args, **kwargs)


class TokenSemicolon(TokenOfRange):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_SEMICOLON, ';', *args, **kwargs)


class TokenOffset(TokenOfRange):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_OFFSET, content, *args, **kwargs)


class TokenPercent(TokenOfRange):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_PERCENT, '%', *args, **kwargs)


class TokenDot(TokenOfRange):
    def __init__(self, *args, **kwargs):
        super().__init__(TOKEN_DOT, '.', *args, **kwargs)


class TokenSearchForward(TokenOfRange):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_SEARCH_FORWARD, content, *args, **kwargs)


class TokenSearchBackward(TokenOfRange):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_SEARCH_BACKWARD, content, *args, **kwargs)


class TokenDigits(TokenOfRange):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_DIGITS, content, *args, **kwargs)


class TokenMark(TokenOfRange):
    def __init__(self, content, *args, **kwargs):
        super().__init__(TOKEN_MARK, content, *args, **kwargs)

    def __str__(self):
        return "'{}".format(self.content)

    def __repr__(self):
        return "<[{0}]('{1})>".format(self.__class__.__name__, self.content)
