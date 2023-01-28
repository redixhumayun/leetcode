def matrix_chain_multiplication(n, arr):
    def dp(i, j) -> int:
        if i >= j:
            return 0

        ans = float("inf")
        for k in range(i, j):
            left_chain = dp(i, k)
            right_chain = dp(k + 1, j)
            combine_cost = arr[i-1] * arr[k] * arr[j]
            ans = min(ans, left_chain + right_chain + combine_cost)
        return ans

    ans = dp(1, n - 1)
    print(ans)

if __name__ == "__main__":
    matrix_chain_multiplication(5, [50, 20, 1, 10, 100])