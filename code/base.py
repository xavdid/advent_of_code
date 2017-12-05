# Base class for other solutions
import os

class InputTypes(object):
    TEXT, INTEGER, TSV, ARRAY = range(4)

class BaseSolution(object):
    def __init__(self, number):
        self.number = number
        self.input = self.read_input(self.input_type())

    def input_type(self):
        return InputTypes.TEXT

    def read_input(self, input_type):
        with open(os.path.join(os.path.dirname(__file__), '../inputs/{}.txt'.format(self.number))) as file:
            if input_type == InputTypes.TEXT:
                # one solid block of text
                return file.read()

            elif input_type == InputTypes.INTEGER:
                # a single int
                i = file.read()
                return int(i.strip())

            elif input_type == InputTypes.TSV:
                import csv
                reader = csv.reader(file, delimiter='\t')
                input_ = []
                for row in reader:
                    input_.append([int(i) for i in row])
                return input_

            elif input_type == InputTypes.ARRAY:
                # an array, where each line is a new item
                f = file.read()
                return f.strip().split('\n')

    def print_solutions(self):
        print '= Solutions for Day {}'.format(self.number)
        for i in [1, 2, 3]:  # might be more than 2 parts?
            if hasattr(self, 'part_{}'.format(i)):
                solve_func = getattr(self, 'part_{}'.format(i))
                res = solve_func()
                # have to double check now that there's defaults for the methods
                if res:
                    print '\n== Part {}'.format(i)
                    print '=== {}'.format(res)
