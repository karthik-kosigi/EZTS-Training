n=5  
k=2  
arr = [1,2,3,4,5]
summ_arr = [(arr[i]*(i+1)) for i in range(len(arr)) ]
maximum = 0
for i in range(n-k+1):
    summation = sum(summ_arr[i:k+i])
    # for j in range(i,k+i):
    #     sum +=summ_arr[j]
    maximum = max(maximum,summation)
print(maximum)

# def max_possible_score(N, K, A):
#     # Calculate scores array
#     scores = [(i + 1) * A[i] for i in range(N)]
    
#     # Use a sliding window to find the maximum sum of any contiguous subarray of size K
#     max_sum = float('-inf')
#     current_sum = sum(scores[:K])
#     max_sum = current_sum
    
#     for i in range(K, N):
#         current_sum = current_sum - scores[i - K] + scores[i]
#         max_sum = max(max_sum, current_sum)
    
#     return max_sum

# # Sample Input
# N = 5
# K = 2
# A = [1, 2, 3, 4, 5]

# # Sample Output
# print(max_possible_score(N, K, A))