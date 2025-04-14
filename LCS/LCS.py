def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Finds the longest common subsequence of two strings using dynamic
    programming (tabular method).

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        The longest common subsequence as a string.
    """
    n = len(str1)
    m = len(str2)

    # Initialize a 2D array (table) of size (n+1) x (m+1) with zeros
    memoTable = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                # print(i , j, memoTable[i - 1][j - 1], memoTable[i])
                memoTable[i + 1][j + 1] = memoTable[i][j] + 1
            else:
                memoTable[i + 1][j + 1] = max(memoTable[i][j + 1], memoTable[i + 1][j])

    print(*memoTable, sep="\n")

    lcs = ""
    i = len(str1)
    j = len(str2)
    while i and j:
        if str1[i-1] == str2[j-1]:
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        else:
            if memoTable[i - 1][j] == memoTable[i][j]:
                i -= 1
            else:
                j -=1
    return lcs

s1 = "ACADB"
s2 = "CBDAKJHJHGCKJHKJHASDWERB"

print("longest common subsequence:", longest_common_subsequence(s1, s2))
