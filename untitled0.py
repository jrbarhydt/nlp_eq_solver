# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:08:14 2019

@author: Johnathon
"""
from sympy import Eq, Symbol, solve, add
from fractions import Fraction

class EquationParser:
    def __init__(self, equation_string: str = '2x+3+1x=0'):
        eq_list = equation_string.split('=')
        self.y = Symbol('y')
        self.x = Symbol('x')
        self.vars = {'x': self.x, 'y': self.y}
        self.lhs = eq_list[0]
        self.rhs = eq_list[1]
        self.equation = None
        self.solution = None
        
    def __str__(self):
        return str([str(self._fraction(sol)) for sol in self.solution])
    
    def _build(self):
        self.equation = Eq(self.lhs, self.rhs)
        
    def _solve(self):
        self.solution = solve(self.equation)
        
    def _parse(self, input_string):
        output_eq = 0
        hold = ''
        for idx, atom in enumerate(list(input_string)):
            if atom.isalpha() or (atom == '+' and hold) or (atom=='-' and '-' in hold):
                if hold:
                    coef = float(hold)
                else:
                    coef = 1
                if atom.isalpha():
                    val = self.vars[atom]
                else:
                    val = 1
                output_eq = add.Add(output_eq, coef * val)
                hold = ''
                
            elif atom in ['-', '.'] or atom.isnumeric():
                hold += atom
        if hold:
            output_eq = add.Add(output_eq, float(hold))
        return output_eq
    
    @staticmethod
    def _fraction(float_vals, max_den: int = 1000):
        if type(float_vals) is list:
            return [Fraction(str(val)).limit_denominator(max_den) for val in float_vals]
        else:
            return Fraction(str(float_vals)).limit_denominator(max_den)
    
    def parse(self, outside_string: str = None):
        if outside_string is not None:
            self.lhs = outside_string.split('=')[0]
            self.rhs = outside_string.split('=')[1]
        self.lhs = self._parse(self.lhs)
        self.rhs = self._parse(self.rhs)
        

if __name__ == '__main__':
    eq = EquationParser()
    eq.parse('2.5x+5.12=0')
    eq._build()
    eq._solve()
    soln = eq.solution
    print(eq)
    #print('x = {}'.format(eq._fraction(soln[0])))    