class Machine:
    # This is simply a constant value for an epsilon
    EPSILON = 'epsilon'

    # This is an epsilon counter so that all epsilon transitions are 'unique" in the eyes of the Python dict
    __epsilon_counter = 0

    # This state counter is for uniquely naming states
    __state_counter = 0

    def __init__(self, alphabet, state_table, init_state, final_state_list):
        # Assign the alphabet
        self.alphabet = alphabet

        # Setup then validate the state table
        self.state_table = state_table

        for transitions in state_table.values():
            # Check each outgoing edge of the transition
            for transition in transitions.items():
                # Complain if a stimulus is not in the alphabet and is not an epsilon transition
                if transition[0] not in self.alphabet and Machine.EPSILON not in transition[0]:
                    raise Exception('Stimuli \'' + str(transition[0]) + '\' not in alphabet.')

                # Complain if a destination state is not in the state list
                if transition[1] not in self.state_table.keys():
                    raise Exception('Destination state \'' + str(transition[1]) + '\' not in state table.')

        # Assign the initial state
        if init_state in state_table.keys():
            self.init_state = init_state
        else:
            # Initial state does not exist, so this is an invalid machine
            raise Exception('Initial state \'' + str(init_state) + '\' not in state table.')

        # Mark the final states
        self.final_states = []

        for state in final_state_list:
            # Final state does not exist, so this is an invalid machine
            if state not in state_table.keys():
                raise Exception('Final state \'' + str(state) + '\' not in state table.')
            else:
                self.final_states.append(state)

    # Concatenate another machine into this machine, with this machine coming first
    # This returns a new machine
    def concatenate(self, other_machine):
        # Get the final state of this machine
        final_state = self.final_states[0]

        # Get the initial state of the other machine
        init_state_other = other_machine.init_state

        # Connect this machine's final state and the other machine's initial state with an epsilon transition
        # Do this by merging the two state tables of the two machines
        self.state_table.update(other_machine.state_table)
        new_state_table = self.state_table

        # Then modifying the (empty) transition from the final state to point to the initial state of the other machine
        # Get the transition from the final state of the original machine
        new_state_table[final_state][Machine.assign_epsilon_transition()] = init_state_other

        # Assign the new final state
        new_final_state = other_machine.final_states[0]

        # Return the concatenated machine
        return Machine(self.alphabet, new_state_table, self.init_state, [new_final_state])

    # Return the DFA representation of this NFA machine
    def dfa(self):
        # Get the epsilon closure of the current state (with respect to the internal state table)
        def __epsilon_closure(state_provided):
            # Only ever compute for the epsilon closure of a state if it hasn't already been computed
            # Else, just recycle the old result
            if state_provided not in epsilon_closures_cache:
                result = {state_provided}

                # If the current state responds to an epsilon stimulus (other than to itself), the epsilon closure of
                # this state is this state union the epsilon closures of the destination states when the current state
                # is given an epsilon
                epsilon_transitions_exclusive = []

                for given_stimulus, given_destination in self.state_table[state_provided].items():
                    # If an epsilon stimulus is found, take not of it
                    if Machine.EPSILON in given_stimulus:
                        epsilon_transitions_exclusive.append(given_destination)

                if len(epsilon_transitions_exclusive) != 0:
                    # Gather all next epsilon closure sets in a list
                    next_epsilon_closures = [__epsilon_closure(next_state) for next_state in
                                             epsilon_transitions_exclusive]

                    # Then compute the union of the current state with each of the sets in the next epsilon closure list
                    for next_epsilon_closure in next_epsilon_closures:
                        result = result.union(next_epsilon_closure)

                # Else, the epsilon closure of this state is just itself
                # Also, remember the result for future computations
                frozen_result = frozenset(result)

                epsilon_closures_cache[state_provided] = frozen_result

                return frozen_result
            else:
                return epsilon_closures_cache[state_provided]

        # See which states a state set leads to given a stimulus
        def __move(state_set, given_stimulus):
            destination_states = set()

            for individual_state in state_set:
                # See where this individual state leads to
                # If this state leads to nowhere given the stimulus, return nothing
                # If this state, given the stimulus, leads to somewhere, return the union of all possible destinations
                transitions = self.state_table[individual_state]

                # If there are no transitions at all, then there is no point in checking where it leads to
                if len(transitions) == 0:
                    continue
                else:
                    # Check whether the current state leads to anywhere when given the provided stimulus
                    for sample_stimulus, destination_state in transitions.items():
                        # This means there is a transition of this state on the provided stimulus
                        if given_stimulus == sample_stimulus:
                            # Then append the epsilon closure of the destination state
                            destination_states = destination_states.union(__epsilon_closure(destination_state))

            return destination_states

        init_state_dfa = None
        final_states_dfa = []

        # Get all the epsilon closures of the NFA states
        epsilon_closures = []
        epsilon_closures_cache = {}

        state_list = self.state_table.keys()

        for state in state_list:
            # Compute for the epsilon closure of the current state
            epsilon_closure = __epsilon_closure(state)

            # Mark the starting state set because we would start there
            if self.init_state in epsilon_closure:
                init_state_dfa = epsilon_closure

            epsilon_closures.append(epsilon_closure)

        # Starting from the state represented by the epsilon closure with the initial state, iteratively discover new
        # states (which would be DFA states) and then see where each transition leads to
        dfa_state_table = {
        }

        states_undiscovered = [init_state_dfa]
        states_discovered = []

        # While there are still DFA states to be discovered, continue discovering new moves and states
        while len(states_undiscovered) != 0:
            current_state = states_undiscovered.pop()
            dfa_state_table[current_state] = {}

            # Add the current state to the discovered states
            states_discovered.append(current_state)

            # For each possible stimulus, see where the state set collectively leads to
            for stimulus in self.alphabet:
                destination_state_set = __move(current_state, stimulus)

                # If the destination state is not empty, and if the destination state has not been discovered yet, add
                # it to the undiscovered states
                if len(destination_state_set) != 0:
                    destination_state_set = frozenset(destination_state_set)

                    # If the state has not been discovered yet, add it to the list of undiscovered states
                    if destination_state_set not in states_discovered:
                        states_undiscovered.append(destination_state_set)

                    # Construct the new state table accordingly
                    dfa_state_table[current_state][stimulus] = destination_state_set

        # Also take note of the final states
        for state in states_discovered:
            if self.final_states[0] in state:
                final_states_dfa.append(state)

        # Convert all the state names to more understandable names
        reference = {state: None for state in states_discovered}

        # Create a new state table to hold all the new state names
        new_dfa_state_table = {}

        # First, assign unique state numbers for all the state sets
        for state in dfa_state_table.keys():
            # Take note of the new name of this state
            reference[state] = self.assign_state_name()

            # Transfer the contents of the old state table to a new key
            new_dfa_state_table[reference[state]] = dfa_state_table[state]

        # Then convert all the old state set names in the transitions to their new names
        for transition in new_dfa_state_table.values():
            for stimulus, destination in transition.items():
                transition[stimulus] = reference[destination]

        # Return the constructed DFA machine
        return Machine(self.alphabet, new_dfa_state_table, reference[init_state_dfa],
                       [reference[final_state_dfa] for final_state_dfa in final_states_dfa])

    # Assign unique epsilon transitions every time
    @staticmethod
    def assign_epsilon_transition():
        name = Machine.EPSILON + '-' + str(Machine.__epsilon_counter)
        Machine.__epsilon_counter += 1

        return name

    # Assign unique state names every time
    @staticmethod
    def assign_state_name():
        name = str(Machine.__state_counter)
        Machine.__state_counter += 1

        return name
