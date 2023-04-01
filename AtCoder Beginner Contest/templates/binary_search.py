
def binary_search(sorted_list: int, search_value: int) -> bool:
    """
    二分探索を実施し、検索対象の値がリスト内に含まれるかどうかの
    真偽値を取得する。

    Parameters
    ----------
    sorted_list : list of int
        ソート済みの整数値を格納したリスト。
    search_value : int
        検索対象の値。

    Returns
    -------
    value_exists : bool
        値がリスト内に含まれるかどうか。
    """
    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]

        if search_value < middle_value:
            right_index = middle_index - 1
            continue
        if search_value > middle_value:
            left_index = middle_index + 1
            continue

        return True

    return False
