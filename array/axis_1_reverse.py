import numpy as np

# 2차원 배열 열 축 기준 거꾸로 정렬
arr = np.array([[2, 1, 6],
                [0, 7, 4],
                [5, 3, 2]])  # 2차원 배열 정의

arr_sort_axis_1_reverse = np.sort(arr, axis=1)[::-1]
# 열 축을 기준으로 정렬한 것 뒤집기


print("열 축 기준 거꾸로 정렬\n", arr_sort_axis_1_reverse)
