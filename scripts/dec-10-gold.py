"""
Solution is based on such idea:
- define task as a system of linear eq.
- transform matrix to a row echelon form via sympy
- brute force valid solution that will produce min number of steps 

Way too slow solution, it took 7h to solve test case.

Thanks to a numerous reddit post that help me think in a right direction:
- https://www.reddit.com/r/adventofcode/s/PxAeNeXnFC
"""

import numpy as np

from sympy import Matrix
from sympy.matrices.dense import matrix2numpy

from itertools import product


def run_if_true(bool_run, func, *args, **kwargs):
    if bool_run:
        func(*args, **kwargs)


class SolutionSet:
    _solutions: list[int]
    _min_steps: int

    def __init__(self, max_steps):
        self._solutions = []
        self._min_steps = max_steps

    def add_solution(self, vec):
        vec = vec.astype(int).tolist()
        steps = int(sum(vec))

        if self._min_steps >= steps:
            self._solutions.append(vec)
            self._min_steps = steps

    def get_min_steps(self) -> int:
        return self._min_steps

    def get_min_step_solution(self) -> list[int] | None:
        if self._solutions:
            return self._solutions[-1] # pyright: ignore


def main():
    fn = "inputs/aoc-25-dec-10.txt"
    # fn = "inputs/aoc-25-dec-10-test.txt"

    with open(fn, "r") as f:
        lines = f.readlines()
        lines = [s[:-1] for s in lines]

    sum_of_presses = 0

    for machine_idx, machine in enumerate(lines[:35]):
        run_if_true(True, print, f"Cur machine idx: {machine_idx+1}")

        # parse input buttons and state
        blocks = machine.split(" ")
        _ = blocks.pop(0)
        state = blocks.pop(-1)
        state = state.replace("{", "").replace("}", "")
        state = [int(ch) for ch in state.split(",")]
        btns = [b.replace("(", "").replace(")", "")  for b in blocks]
        btns = [list(map(int, b.split(",")))  for b in btns]

        # compose linear system (matrix) based on inputs values
        # rows correspond to state positions
        # columns correspond to buttons
        A = np.zeros((len(state), len(btns)))
        for btn_idx in range(len(btns)):
            A[btns[btn_idx], btn_idx] = 1

        # transform matrix to a row echelon form
        A_augm = np.hstack((A, np.array(state).reshape(-1, 1)))
        A_augm = Matrix(A_augm)
        A_ref = A_augm.echelon_form()
        A_ref = matrix2numpy(A_ref).astype(float)[::-1]

        # caclculate max possible value of presses per button 
        #   based on a required state
        max_per_btn = [max([state[i] for i in b]) for b in btns]

        solutions = SolutionSet(sum(max_per_btn))
        defined = np.full(len(btns), False)
        vec = np.full(len(btns), -1)

        # walk through a nullspace of A and search for a min step solution
        # that is integer and not negative
        def brute_force_solutions(row_idx, defined, vec):

            if row_idx >= A_ref.shape[0]: # pyright: ignore
                solutions.add_solution(vec)
                return

            row = A_ref[row_idx][:-1]
            y = A_ref[row_idx][-1]

            # skip linearly dependent rows
            if (row == 0).all():
                brute_force_solutions(row_idx+1, defined, vec)
                return


            # detect not zero entries that should be defined
            m = (row != 0.0) & ~defined
            var_idx = np.where(m)[0]


            # go through all possible values of those detected variables
            for var_values in product(*[
                range(0, max_per_btn[i]+1)
                for i in var_idx
            ]): # pyright: ignore

                # put already defined variables
                sug_vec = np.zeros(len(btns))
                sug_vec[defined] = vec[defined] # pyright: ignore

                # put new defined variables
                for pos_idx, pos_v in zip(var_idx, var_values):
                    sug_vec[pos_idx] = pos_v


                # check if suggested vector is compliant with current row
                if row @ sug_vec.reshape(-1, 1) == y:
                    if sug_vec.sum() <= solutions.get_min_steps():

                        new_defined = defined.copy()
                        new_defined[var_idx] = True

                        brute_force_solutions(
                            row_idx+1,
                            new_defined,
                            sug_vec
                        )

        brute_force_solutions(0, defined, vec)

        run_if_true(
            True,
            print,
            f"Solution: {solutions.get_min_step_solution()} " \
            f"steps: {solutions.get_min_steps()}"
        )
        sum_of_presses += solutions.get_min_steps()

    run_if_true(True, print, f"Total sum of presses: {sum_of_presses}")


if __name__ == "__main__":
    main()


# Simple brute force solution, too slow
# from itertools import combinations_with_replacement
# seq_len = 0
# is_found = False
# while True:
#     seq_len += 1

#     # print(f"Current sequence len: {seq_len}")
#     for selected_btns in combinations_with_replacement(
#         range(len(btns)),
#         seq_len
#     ):
#         # print(selected_btns)
#         state_to_check = [0, ] * len(state)
#         for btn in [btns[b] for b in selected_btns]:
#             for item in btn:
#                 state_to_check[item] += 1
#         # print(f"{state} {state_to_check}")
#         # exit(0)
#         # time.sleep(0.5)
#         if state_to_check == state:
#             # print([btns[b] for b in selected_btns])
#             print(selected_btns)
#             print(f"Btn sequence found with len {seq_len}")
#             is_found = True
#             sum_of_presses += seq_len

#         if is_found:
#             break

#     if is_found:
#         break
# exit(0)
