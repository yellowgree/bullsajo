def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # 왼쪽 자식이 루트보다 큰 경우
        if left < n and arr[left] > arr[largest]:
            largest = left

        # 오른쪽 자식이 현재 최대값보다 큰 경우
        if right < n and arr[right] > arr[largest]:
            largest = right

        # 최대값이 루트가 아닌 경우 교환 후 재귀 호출
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙에서 요소 하나씩 꺼내 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 루트(최대값)와 마지막 원소 교환
        heapify(arr, i, 0)

    return arr


def bubble_sort(arr):
    if not arr:
        return arr

    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True

        if not swapped:
            break

    return sorted_arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    # 삽입 정렬 알고리즘
    n = len(arr)
    # 두 번째 원소부터 시작하여 배열을 순회
    for i in range(1, n):
        # 현재 삽입할 원소를 선택
        key = arr[i]
        # key의 앞 원소부터 역순으로 비교
        j = i - 1

        # key보다 큰 원소들을 오른쪽으로 한 칸씩 이동
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # 올바른 위치에 key를 삽입
        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr):
    """
    반복(스택) 기반 퀵정렬: 최악의 재귀 깊이 회피, 반환은 새 리스트.
    - 피벗: median-of-three (lo, mid, hi)
    - 파티션: Hoare
    """
    n = len(arr)
    if n <= 1:
        return arr[:]

    a = arr[:]  # 원본 보존
    stack = [(0, n - 1)]

    def median_of_three(lo, hi):
        mid = (lo + hi) // 2
        x = [(a[lo], lo), (a[mid], mid), (a[hi], hi)]
        x.sort(key=lambda t: t[0])
        return x[1][1]  # 인덱스 반환

    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue

        # ---- Hoare partition ----
        pidx = median_of_three(lo, hi)
        pivot = a[pidx]
        i, j = lo - 1, hi + 1
        while True:
            i += 1
            while a[i] < pivot:
                i += 1
            j -= 1
            while a[j] > pivot:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]

        # 다음 구간 push (작은 구간 먼저 넣어 스택 깊이 최소화)
        left = (lo, j)
        right = (j + 1, hi)
        if left[1] - left[0] < right[1] - right[0]:
            stack.append(right)
            stack.append(left)
        else:
            stack.append(left)
            stack.append(right)

    return a


if __name__ == "__main__":
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read().strip()
        data = [int(x.strip()) for x in content.split(",") if x.strip().isdigit()]

    print("원본 데이터:", data)

    # 각 정렬 알고리즘 테스트
    print("\n[버블 정렬 결과]")
    print(bubble_sort(data.copy()))

    print("\n[선택 정렬 결과]")
    print(selection_sort(data.copy()))

    print("\n[삽입 정렬 결과]")
    print(insertion_sort(data.copy()))

    print("\n[병합 정렬 결과]")
    print(merge_sort(data.copy()))

    print("\n[퀵 정렬 결과]")
    print(quick_sort(data.copy()))

    print("\n[힙 정렬 결과]")
    print(heap_sort(data.copy()))
