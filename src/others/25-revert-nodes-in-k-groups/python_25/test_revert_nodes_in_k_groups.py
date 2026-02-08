from .revert_nodes_in_k_groups import Solution, ListNode


def test_revert_nodes_in_k_groups_example_case_1():
    # Input: head = [1,2,3,4,5], k = 2
    # Output: [2,1,4,3,5]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    solution = Solution()
    result = solution.reverseKGroup(n1, 2)
    resultList = [result.val]
    while result.next is not None:
        result = result.next
        resultList.append(result.val)
    assert resultList == [2, 1, 4, 3, 5]


def test_revert_nodes_in_k_groups_example_case_2():
    # Input: head = [1,2,3,4,5], k = 3
    # Output: [3,2,1,4,5]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    solution = Solution()
    result = solution.reverseKGroup(n1, 3)
    resultList = [result.val]
    while result.next is not None:
        result = result.next
        resultList.append(result.val)
    assert resultList == [3, 2, 1, 4, 5]
