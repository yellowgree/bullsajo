# main.py

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
    pass  # 선택 정렬 구현 예정


def insertion_sort(arr):
    pass  # 삽입 정렬 구현 예정


def merge_sort(arr):
    pass  # 병합 정렬 구현 예정


def quick_sort(arr):
    pass  # 퀵 정렬 구현 예정


def heap_sort(arr):
    pass  # 선택 구현: 힙 정렬


if __name__ == "__main__":
    # data.txt 읽기 (각 줄에 숫자가 있다고 가정)
    with open("data.txt", "r", encoding="utf-8") as f:
        data = [int(line.strip()) for line in f if line.strip().isdigit()]

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
