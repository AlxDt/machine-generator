from antlr4 import FileStream

from evaluator import RegularEvaluator
from gen.RegularLexer import RegularLexer, CommonTokenStream
from gen.RegularParser import RegularParser


def main():
    # Set the input to the file with the specified file name
    input_stream = FileStream('test.txt')

    # Split the input stream into its component tokens using the lexer
    lexer = RegularLexer(input_stream)
    stream = CommonTokenStream(lexer)

    # Make sense of the structure of the component tokens using a parse tree generated by the parser
    parser = RegularParser(stream)

    # Set the start rule of the language to the parse tree
    tree = parser.language()

    # Begin traversing the parse tree
    visitor = RegularEvaluator()

    # Get the machine
    machine = visitor.visit(tree)

    # Get the DFA version of the machine
    dfa = machine.dfa()

    print('Initial state:\n\t' + str(dfa.init_state))
    print('Final states:')

    for state in dfa.final_states:
        print('\t' + str(state))

    print('Transitions:')

    for state, transitions in dfa.state_table.items():
        print('\t' + ('>' if state == dfa.init_state else '') + str(state) + ('*' if state in dfa.final_states else ''))

        for stimulus, destination in transitions.items():
            print('\t\t' + stimulus + ' -> ' + str(destination))

    # Test the machine with input
    string = str(input('\nTest the machine (\'-\' to finish testing): '))

    while string != '-':
        current_state = dfa.init_state
        latest_stimulus = ''

        try:
            for symbol in string:
                latest_stimulus = symbol
                current_state = dfa.state_table[current_state][symbol]

            if current_state in dfa.final_states:
                print('\tAccepted.')
            else:
                print('\tNot accepted - terminated unaccepted @ state ' + str(current_state) + ' on stimulus \'' + str(
                    latest_stimulus) + '\'.')
        except KeyError:
            print('\tNot accepted - rejected @ state ' + str(current_state) + ' on stimulus \'' + str(latest_stimulus)
                  + '\'.')

        string = str(input('Test the machine (enter to finish testing): '))


main()
