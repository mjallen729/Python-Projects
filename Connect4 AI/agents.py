import random
import math

BOT_NAME = "ConnectBot"


class RandomAgent:
    """Agent that picks a random available move.  You should be able to beat it."""
    def __init__(self, sd=None):
        if sd is None:
            self.st = None
        else:
            random.seed(sd)
            self.st = random.getstate()

    def get_move(self, state):
        if self.st is not None:
            random.setstate(self.st)
        return random.choice(state.successors())


class HumanAgent:
    """Prompts user to supply a valid move."""
    def get_move(self, state, depth=None):
        move__state = dict(state.successors())
        prompt = "Kindly enter your move {}: ".format(sorted(move__state.keys()))
        move = None
        while move not in move__state:
            try:
                move = int(input(prompt))
            except ValueError:
                continue
        return move, move__state[move]


class MinimaxAgent:
    """Artificially intelligent agent that uses minimax to optimally select the best move."""

    def get_move(self, state):
        """Select the best available move, based on minimax value."""
        nextp = state.next_player()
        best_util = -math.inf if nextp == 1 else math.inf
        best_move = None
        best_state = None

        for move, state in state.successors():
            util = self.minimax(state)
            if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
                best_util, best_move, best_state = util, move, state
        return best_move, best_state

    def minimax(self, state):
        """Determine the minimax utility value of the given state.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the exact minimax utility value of the state
        """
        if state.is_full():  # if terminal node
            return state.utility()

        # player1 (1) = max, player2 (-1) = min
        # evals to true if p == 1, false otherwise
        isMaximizingPlayer = lambda p: p == 1

        if isMaximizingPlayer(state.next_player()):
            best = -math.inf

            for _, state in state.successors():
                val = self.minimax(state)
                best = max(best,val)

            return best

        else: # if player is the minimizing player
            best = math.inf

            for _, state in state.successors():
                val = self.minimax(state)
                best = min(best,val)

            return best

class MinimaxHeuristicAgent(MinimaxAgent):
    """Artificially intelligent agent that uses depth-limited minimax to select the best move."""

    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def minimax(self, state):
        """Determine the heuristically estimated minimax utility value of the given state.

        The depth data member (set in the constructor) determines the maximum depth of the game
        tree that gets explored before estimating the state utilities using the evaluation()
        function.  If depth is 0, no traversal is performed, and minimax returns the results of
        a call to evaluation().  If depth is None, the entire game tree is traversed.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        if self.depth_limit >= 0: # depth limit >= 0, call to recursive look-ahead func
            return self._UsingDepth(state, self.depth_limit)

        else: # depth limit is none, perform default minimax
            if state.is_full():  # if terminal node
                return state.utility()

            # player1 (1) = max, player2 (-1) = min
            # evals to true if p == 1, false otherwise
            isMaximizingPlayer = lambda p: p == 1

            if isMaximizingPlayer(state.next_player()):
                best = -math.inf

                for _, state in state.successors():
                    val = self.minimax(state)
                    best = max(best,val)

                return best

            else: # if player is the minimizing player
                best = math.inf

                for _, state in state.successors():
                    val = self.minimax(state)
                    best = min(best,val)

                return best

    def _UsingDepth(self, state, depth):
        """Internal helper method for recursive depth tracking.

        It makes my life much easier to just do this instead of more complicated way.
        Method counts down so edge case of 0 depth limit can use it also.

        Args:
            state: a connect383.GameState object representing the current board
            depth: a integer variable tracking current depth in game tree

        Returns: the minimax utility value of the state
        """
        if state.is_full() or depth == 0:  # if terminal node or lookahead reached
            return self.evaluation(state)

        # player1 (1) = max, player2 (-1) = min
        # evals to true if p == 1, false otherwise
        isMaximizingPlayer = lambda p: p == 1

        if isMaximizingPlayer(state.next_player()):
            best = -math.inf

            for _, state in state.successors():
                val = self._UsingDepth(state, depth - 1)
                best = max(best,val)

            return best

        else: # if player is the minimizing player
            best = math.inf

            for _, state in state.successors():
                val = self._UsingDepth(state, depth - 1)
                best = min(best,val)

            return best

    def evaluation(self, state):
        """Estimate the utility value of the game state based on features.

        N.B.: This method must run in O(1) time!

        Args:
            state: a connect383.GameState object representing the current board

        Returns: a heusristic estimate of the utility value of the state
        """
        board = state.board

        one_score = 0
        zero_score = 0

        # check up,upleft,upright,left (already visited)
        for arr in range(1, len(board) - 1):
            for val in range(1, len(board[arr]) - 1):
                cur = board[arr][val]
                
                if cur == 0:
                    if board[arr-1][val] == 0:  #up
                        zero_score += 1

                    if board[arr-1][val-1] == 0:  #upleft
                        zero_score += 1

                    if board[arr-1][val+1] == 0:  #upright
                        zero_score += 1

                    if board[arr][val-1] == 0:  #left
                        zero_score += 1

                if cur == 1:
                    if board[arr-1][val] == 0:  #up
                        one_score += 1

                    if board[arr-1][val-1] == 0:  #upleft
                        one_score += 1

                    if board[arr-1][val+1] == 0:  #upright
                        one_score += 1

                    if board[arr][val-1] == 0:  #left
                        one_score += 1

        return one_score - zero_score

class MinimaxHeuristicPruneAgent(MinimaxHeuristicAgent):
    """Smarter computer agent that uses minimax with alpha-beta pruning to select the best move."""

    def minimax(self, state):
        """Determine the minimax utility value the given state using alpha-beta pruning.

        The value should be equal to the one determined by MinimaxAgent.minimax(), but the
        algorithm should do less work.  You can check this by inspecting the value of the class
        variable GameState.state_count, which keeps track of how many GameState objects have been
        created over time.  This agent should also respect the depth limit like HeuristicAgent.

        N.B.: When exploring the game tree and expanding nodes, you must consider the child nodes
        in the order that they are returned by GameState.successors().  That is, you cannot prune
        the state reached by moving to column 4 before you've explored the state reached by a move
        to to column 1.

        Args:
            state: a connect383.GameState object representing the current board

        Returns: the minimax utility value of the state
        """
        return self._pruning(state,-math.inf,math.inf)

    def _pruning(self, state, alpha, beta):
        if state.is_full():  # if terminal node
            return state.utility()

        # player1 (1) = max, player2 (-1) = min
        # evals to true if p == 1, false otherwise
        isMaximizingPlayer = lambda p: p == 1

        if isMaximizingPlayer(state.next_player()):
            best = -math.inf

            for _, state in state.successors():
                val = self._pruning(state,alpha,beta)
                best = max(best,val)
                alpha = max(best,alpha)

                if alpha >= beta:
                    break

            return best

        else: # if player is the minimizing player
            best = math.inf

            for _, state in state.successors():
                val = self._pruning(state,alpha,beta)
                best = min(best,val)
                beta = min(best,beta)

                if alpha >= beta:
                    break

            return best
