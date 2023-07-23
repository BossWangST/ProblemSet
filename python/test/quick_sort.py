def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r) # pivot INDEX
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]  # Pivot
    i = p - 1  # A[p, i] < x
    for j in range(p, r):
        if A[j] <= x:
            i += 1  # First element >x
            A[i], A[j] = A[j], A[i]
    # swap first element >x with x
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


a = [2, 8, 7, 1, 3, 5, 6, 4]
quick_sort(a, 0, len(a) - 1)
for i in a:
    print(i)
