SIZE = 9
A = [0] * SIZE
B = [0] * SIZE

def merge(lb, mid, ub):
    i, j, k = lb, mid + 1, lb
    while i <= mid and j <= ub:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    while i <= mid:
        B[k] = A[i]; i += 1; k += 1
    while j <= ub:
        B[k] = A[j]; j += 1; k += 1
    for k in range(lb, ub + 1):
        A[k] = B[k]

def merge_sort(lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(lb, mid)
        merge_sort(mid + 1, ub)
        merge(lb, mid, ub)

def main():
    print(f"Enter {SIZE} elements:")
    for i in range(SIZE):
        A[i] = int(input(f"Element[{i}]: "))
    merge_sort(0, SIZE - 1)
    print("Sorted array:")
    print(" ".join(str(x) for x in A))

if __name__ == "__main__":
    main()