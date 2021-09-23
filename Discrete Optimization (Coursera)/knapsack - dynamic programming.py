
"""
Given weights and values of n items, put these items in a knapsack of
 capacity W to get the maximum total value in the knapsack.
Note that only the integer weights 0-1 knapsack problem is solvable
 using dynamic programming.
"""

def knapsack(W, wt, val, n):
    dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W], dp


def knapsack_with_example_solution(W: int, wt: list, val: list):
    """
    Solves the integer weights knapsack problem returns one of
    the several possible optimal subsets.
    Parameters
    ---------
    W: int, the total maximum weight for the given knapsack problem.
    wt: list, the vector of weights for all items where wt[i] is the weight
    of the i-th item.
    val: list, the vector of values for all items where val[i] is the value
    of the i-th item
    Returns
    -------
    optimal_val: float, the optimal value for the given knapsack problem
    example_optional_set: set, the indices of one of the optimal subsets
    which gave rise to the optimal value.
    Examples
    -------
    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4])
    Traceback (most recent call last):
        ...
    ValueError: The number of weights must be the same as the number of values.
    But got 4 weights and 3 values
    """
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Both the weights and values vectors must be either lists or tuples"
        )

    num_items = len(wt)
    if num_items != len(val):
        raise ValueError(
            "The number of weights must be the "
            "same as the number of values.\nBut "
            f"got {num_items} weights and {len(val)} values"
        )
    for i in range(num_items):
        if not isinstance(wt[i], int):
            raise TypeError(
                "All weights must be integers but "
                f"got weight of type {type(wt[i])} at index {i}"
            )

    optimal_val, dp_table = knapsack(W, wt, val, num_items)
    example_optional_set: set = set()
    _construct_solution(dp_table, wt, num_items, W, example_optional_set)

    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights
    Parameters
    ---------
    dp: list of list, the table of a solved integer weight dynamic programming problem
    wt: list or tuple, the vector of weights of the items
    i: int, the index of the  item under consideration
    j: int, the current possible maximum weight
    optimal_set: set, the optimal subset so far. This gets modified by the function.
    Returns
    -------
    None
    """
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)


"""
Adding test case for knapsack
"""
val = [1, 1, 1, 10, 10, 13, 7]
wt = [2, 2, 2, 5, 5, 8, 3]
n = len(val)
w = 10
optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
print('The value for the optimal solituon is: ' + str(optimal_solution))
print('An optional choice would be: ' + str(optimal_subset))