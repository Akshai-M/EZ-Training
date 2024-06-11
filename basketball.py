def max_possible_score(N,K,A):
    scores = [(i+1)*A[i] for i in range(N)]

    current_sum = sum(scores[:K])

    max_sum = current_sum

    for i in range(K,N):
        current_sum+=scores[i]
        max_sum = max(max_sum,current_sum)

    return max_sum

max_possible_score()