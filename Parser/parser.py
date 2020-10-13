import sympy as sp


class Parser:
    def __init__(self, expr, symbols):
        try:
            for symbol in symbols.split():
                exec(symbols + " = " + "sp.Symbol('{}')".format(symbol))
            self.expr = eval(expr)
            self.is_expr = str(type(self.expr)) != "<class 'int'>"
        except (SyntaxError, NameError):
            self.expr = None
            self.is_expr = False

    @property
    def latex(self):
        return sp.latex(self.expr)

    def __eq__(self, other):
        if self.is_expr:
            return self.expr.equals(other.expr)
        return self.expr == other.expr
