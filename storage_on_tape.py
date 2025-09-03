def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] ,arr[j]

def optimal_storage_on_tape():
    n = int(input("Enter the number of programs: "))
    programs = []

    print("Enter the lengths of the programs:")
    for i in range(n):
        length = int(input(f"Program {i + 1} length: "))
        programs.append(length)

    bubble_sort(programs)

    print("\nSorted program lengths:")
    print(programs)

    total_retrieval_time = 0
    cumulative_time = 0

    print("\nProgram\tlength\tRT")
    for i in range(n):
        cumulative_time += programs[i]
        total_retrieval_time += cumulative_time
        print(f"{i + 1}\t{programs[i]}\t{cumulative_time}")

    average_retrieval_time = total_retrieval_time / n

    print(f"\nTotal Retrieval Time: {total_retrieval_time}")
    print(f"Average Retrieval Time: {average_retrieval_time:.2f}")

if __name__ == "__main__":
    optimal_storage_on_tape()
