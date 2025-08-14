# bullsajo
불사조의 역사가 시작된다

# Sorting Algorithms

파이썬으로 구현한 **6가지 정렬 알고리즘**의 동작을 비교하는 코드입니다.  
`data.txt`에 입력된 숫자 데이터를 읽어 각 정렬 알고리즘을 적용한 결과를 출력합니다.

---

##  프로젝트 구조

 main.py # 정렬 알고리즘 구현 및 실행 스크립트
 data.txt # 정렬 대상 데이터 (쉼표 또는 줄바꿈 구분)
 README.md # 프로젝트 설명


---

##  구현된 정렬 알고리즘
| 함수명            | 알고리즘     | 특징 |
|------------------|-------------|------|
| `bubble_sort`    | 버블 정렬   | 인접 요소를 비교·교환 |
| `selection_sort` | 선택 정렬   | 가장 작은 요소 선택 후 제자리 교환 |
| `insertion_sort` | 삽입 정렬   | 이미 정렬된 부분에 삽입 |
| `merge_sort`     | 병합 정렬   | 분할 후 병합 (재귀) |
| `quick_sort`     | 퀵 정렬     | median-of-three + 반복문 기반 |
| `heap_sort`      | 힙 정렬     | 최대 힙 구성 후 정렬 |

---

##  실행 방법

```bash
git clone https://github.com/사용자명/bullsajo.git
cd bullsajo
./main.py
