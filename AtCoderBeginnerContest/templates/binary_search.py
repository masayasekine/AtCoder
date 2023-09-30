
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

def find_smallest_satisfying_value():
    # 二分探索の初期設定
    lower_bound = 0  # 下限
    upper_bound = 1000000  # 上限（適切な大きな値を設定）

    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2  # 中間値を計算

        if is_condition_satisfied(mid):
            upper_bound = mid  # 条件を満たす場合、上限を中間値に設定
        else:
            lower_bound = mid + 1  # 条件を満たさない場合、下限を中間値の次の値に設定

    return lower_bound