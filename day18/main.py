from copy import deepcopy
class Expression:
    def __init__(self, literal):
        self.literals = []
        self.sub_expression_pointer = None
        self.open = True
        if literal == "(":
            exp = Expression(None)
            self.sub_expression_pointer = exp
            self.literals.append(exp)
        elif literal != None:
            self.literals.append(litteral)
    def add_literal(self, literal):
        if literal == ")":
            self.close_expression()
        elif literal == "(":
            self.add_sub_expression()
        elif self.sub_expression_pointer != None and self.sub_expression_pointer.open:
            self.sub_expression_pointer.add_literal(literal)
        else:
            self.literals.append(literal)
    def add_sub_expression(self):
        if self.sub_expression_pointer != None and self.sub_expression_pointer.open:
            self.sub_expression_pointer.add_sub_expression()
        else:
            exp = Expression(None)
            self.sub_expression_pointer = exp
            self.literals.append(exp)
    def close_expression(self):
        if self.sub_expression_pointer != None and self.sub_expression_pointer.open:
            self.sub_expression_pointer.close_expression()
        else:
            self.open = False
    def print(self):
        for literal in self.literals:
            if type(literal) == Expression:
                print("(")
                literal.print()
                print(")")
            else:
                print(literal)
    def evaluate(self):
        # PART ONE 
        
        #result = 0
        #current_operation = None
        #for literal in self.literals:
        #    if type(literal) == Expression:
        #        if current_operation == None:
        #            result = literal.evaluate()
        #        else:
        #            result = self.calculate(current_operation, result, literal.evaluate())
        #    elif literal == "+":
        #        current_operation = "+"
        #    elif literal == "*":
        #        current_operation = "*"
        #    else:
        #        if current_operation == None:
        #            result = int(literal)
        #        else:
        #            result = self.calculate(current_operation, result, int(literal))
        #return result

        tmp_result = 0
        tmp_literals = []
        current_operation = None
        for literal in self.literals:
            if type(literal) == Expression:
                if current_operation == None:
                    tmp_literals.append(literal.evaluate())
                else:
                    last = tmp_literals.pop(-1)
                    tmp_literals.append(last + literal.evaluate())
            elif literal == "+":
                current_operation = "+"
            elif literal == "*":
                current_operation = None
                tmp_literals.append("*")
            else:
                if current_operation == None:
                    tmp_literals.append(int(literal))
                else:
                    last = tmp_literals.pop(-1)
                    tmp_literals.append(last + int(literal))
        result = 0
        current_operation = None
        for literal in tmp_literals:
            if literal == "*":
                current_operation = "*"
            else:
                if current_operation == None:
                    result = int(literal)
                else:
                    result *= int(literal)
        return result
    def calculate(self, operation, tmp_result, literal):
        if operation == "+":
            return tmp_result + literal
        elif operation == "*":
            return tmp_result * literal

if __name__ == "__main__":
    results = []
    with open("puzzle", "r") as f:
        for line in f.readlines():
            exp = Expression(None)
            for character in line.strip():
                if not character.strip():
                    continue
                exp.add_literal(character)
            results.append(exp.evaluate())
    print(sum(results))

