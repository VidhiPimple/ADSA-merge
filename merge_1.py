def merge(A, B, lb, mid, ub):
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
        B[k] = A[i]
        i += 1
        k += 1
    while j <= ub:
        B[k] = A[j]
        j += 1
        k += 1
    for k in range(lb, ub + 1):
        A[k] = B[k]

def merge_sort(A, B, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(A, B, lb, mid)
        merge_sort(A, B, mid + 1, ub)
        merge(A, B, lb, mid, ub)

def main():
    Size = int(input("Enter number of elements: "))
    A = [0] * Size
    B = [0] * Size

    print(f"Enter {Size} elements:")
    for i in range(Size):
        A[i] = int(input(f"Element[{i}]: "))

    merge_sort(A, B, 0, Size - 1)

    print("Sorted array:")
    print(" ".join(str(x) for x in A))

if __name__ == "__main__":
    main()
