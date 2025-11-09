from .shifting_letters_ii import shifting_letters


def test_shifting_letters_ii_example_case_1():
    # Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
    # Output: "ace"
    # Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
    # Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
    # Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
    assert shifting_letters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"


def test_shifting_letters_ii_example_case_2():
    # Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
    # Output: "catz"
    # Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
    # Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
    assert shifting_letters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz"
