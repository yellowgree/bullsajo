# main.py

def bubble_sort(arr):
    pass  # 버블 정렬 구현 예정


def selection_sort(arr):
    pass  # 선택 정렬 구현 예정


def insertion_sort(arr):
    pass  # 삽입 정렬 구현 예정


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
    pass  # 퀵 정렬 구현 예정


def heap_sort(arr):
    pass  # 선택 구현: 힙 정렬


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
