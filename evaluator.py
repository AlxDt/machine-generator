from gen.RegularParser import RegularParser
from gen.RegularVisitor import RegularVisitor
from machine import Machine


class RegularEvaluator(RegularVisitor):
    def visitLanguage(self, ctx: RegularParser.LanguageContext):
        # Construct the final NFA by connecting the terms to single start and final states
        # Take note of each concatenated machine
        concatenated_machines = []

        for termComponent in ctx.getChildren():
            if type(termComponent) is RegularParser.TermContext:
                concatenated_machines.append(self.visitTerm(termComponent))

        # Create a new initial state
        new_init_state = Machine.assign_state_name()

        # Create a new final state
        new_final_state = Machine.assign_state_name()

        # Create a new state table, merging all the state tables of the concatenated machines, then connecting the new
        # initial state to all the old initial states of the concatenated machines, then finally connecting the old
        # final states of the machines to the new final state
        new_state_table = {
            new_init_state: {},
            new_final_state: {}
        }

        for concatenated_machine in concatenated_machines:
            # Merge its state table with the new state table
            new_state_table.update(concatenated_machine.state_table)

            # Create an epsilon transition from the new initial state to the old initial state of the concatenated
            # machine
            new_state_table[new_init_state][Machine.assign_epsilon_transition()] = concatenated_machine.init_state

            # Create an epsilon transition from the old final state of the concatenated machine to the new final state
            new_state_table[concatenated_machine.final_states[0]][Machine.assign_epsilon_transition()] = new_final_state

        return Machine(concatenated_machines[0].alphabet, new_state_table, new_init_state, [new_final_state])

    def visitTerm(self, ctx: RegularParser.TermContext):
        # Concatenate potential symbols, parenthesized expressions, and Kleene closures into a term
        # Build a machine out of the simpler machines from the components
        concatenated_machine = None

        first_pass = True

        for component in ctx.getChildren():
            if type(component) is RegularParser.SymbolContext:
                machine = self.visitSymbol(component)
            elif type(component) is RegularParser.ParenthesizedLanguageContext is not None:
                machine = self.visitParenthesizedLanguage(component)
            else:
                machine = self.visitKleeneClosure(component)

            if not first_pass:
                # Concatenate the current machine to the previous machine if there was already a previous machine
                concatenated_machine = concatenated_machine.concatenate(machine)
            else:
                # If no machines were constructed to now, consider this new machine from now on
                concatenated_machine = machine
                first_pass = False

        return concatenated_machine

    def visitSymbol(self, ctx: RegularParser.SymbolContext):
        # Construct a simple machine out of the symbol from the base case
        init_state = Machine.assign_state_name()
        final_state = Machine.assign_state_name()

        state_table = {
            init_state: {ctx.ALPHABET().getText(): final_state},
            final_state: {}
        }

        simple_machine = Machine([str(num) for num in list(range(2))], state_table, init_state, [final_state])

        return simple_machine

    def visitParenthesizedLanguage(self, ctx: RegularParser.ParenthesizedLanguageContext):
        # Construct an NFA out of the expression in the parenthesis
        return self.visitLanguage(ctx.language())

    def visitKleeneClosure(self, ctx: RegularParser.KleeneClosureContext):
        # Get the operand of the Kleene closure
        # And take note of its machine form
        if ctx.symbol() is not None:
            # Get the symbol's corresponding machine
            machine = self.visitSymbol(ctx.symbol())
        else:
            # Get the parenthesized language's corresponding machine
            machine = self.visitParenthesizedLanguage(ctx.parenthesizedLanguage())

        # Then construct the appropriate Kleene closure form from the given machine
        # Get the machine's state table
        state_table = machine.state_table

        # Construct a new initial state
        new_init_state = Machine.assign_state_name()

        # Construct a new final state
        new_final_state = Machine.assign_state_name()

        # Construct a new state table for what would be the Kleene closure form of the machine
        new_state_table = {
            new_init_state: {},
            new_final_state: {}
        }

        # Merge the operand state table with the new state table
        new_state_table.update(state_table)

        # Create an epsilon transition from the final state to the initial state of the operand machine
        new_state_table[machine.final_states[0]][Machine.assign_epsilon_transition()] = machine.init_state

        # Create an epsilon transition from the new initial state to the old initial state
        new_state_table[new_init_state][Machine.assign_epsilon_transition()] = machine.init_state

        # Create an epsilon transition from the old final state to the new final state
        new_state_table[machine.final_states[0]][Machine.assign_epsilon_transition()] = new_final_state

        # Finally, create an epsilon transition from the new initial state to the new final state
        new_state_table[new_init_state][Machine.assign_epsilon_transition()] = new_final_state

        return Machine(machine.alphabet, new_state_table, new_init_state, [new_final_state])
