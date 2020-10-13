import sympy as sp


class Parser:
    def __init__(self, expr, symbols):
        for symbol in symbols.split():
            exec(symbols + " = " + "sp.Symbol('{}')".format(symbol))
        self.expr = eval(expr)

    @property
    def latex(self):
        return sp.latex(self.expr)

    def __eq__(self, other):
        return self.expr.equals(other.expr)
