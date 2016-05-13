import itertools

from pundit.base import PunditBase
from pundit.condition import ConditionGroup

__version__ = "0.0.6"

'''
Pundit class where structure is defined and
inherited features of pundit base and condition groups
'''


class Pundit(PunditBase, ConditionGroup):
    def __init__(self, pundit, conditions):
        self.pundit = pundit
        self.condition_val = conditions
        self.conditions = conditions.conditions
        self.response = []
        self.set_input = []

    def evaluate(self, arg1, arg2=None):
        arg_one = arg1.lower() if type(arg1) == str else arg1
        arg_two = arg2.lower() if type(arg2) == str else arg2

        # appending to a sample dump with the struture
        self.set_input = []
        self.response = []
        self.set_input.append({self.pundit.arg1: arg_one, self.pundit.arg2: arg_two})

        # checking for the conditions
        for yme in self.conditions:

            if yme['optn'] == 'IN':
                self.response.append(True) if True in [
                    yme['l1'] in self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'NOT_IN':
                self.response.append(False) if True in [
                    yme['l1'] in self.set_input[0][yme['arg']]] else self.response.append(True)
            elif yme['optn'] == 'NOT_IS':
                pass
            elif yme['optn'] == 'EQ':
                self.response.append(True) if True in [
                    yme['l1'] == self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'NOT_EQ':
                self.response.append(True) if True in [
                    yme['l1'] != self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'GT':
                self.response.append(True) if True in [
                    yme['l1'] < self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'LT':
                self.response.append(True) if True in [
                    yme['l1'] > self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'GTE':
                self.response.append(True) if True in [
                    yme['l1'] <= self.set_input[0][yme['arg']]] else self.response.append(False)
            elif yme['optn'] == 'LTE':
                self.response.append(True) if True in [
                    yme['l1'] >= self.set_input[0][yme['arg']]] else self.response.append(False)
            else:
                return "unsupported operation"

        return self.condition_val.success if True in self.response else self.condition_val.failed


class MathRuler():
    """Mathemaical rule operatons"""

    def __init__(self, for_this, then_that):
        self.condition = for_this;
        self.then = then_that

    def math(self, con):
        then_that = self.then
        for_this = self.condition
        exp_converter = then_that.replace(for_this, str(con))
        return eval(exp_converter)


class ListRuler():
    def __init__(self, arg_list):
        self.list = arg_list
        self.reduced = []
        for li in self.list:
            if type(li) == list:
                for cc in list(itertools.chain(li)):
                    self.reduced.append(cc)
            else:
                self.reduced.append(li)

    def fullfill(self, arg):
        return True if arg in self.reduced else False
