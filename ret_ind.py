# def return_indices(S,P):
#     indices = []

#     for i in range(len(S) - len(P) + 1):
#         if P == S[i:i+len(P)]:
#             indices.append(i)
#     return indices

# S = "AJEBFABABCASNSNABABCAMGPPOTK"
# P = "ABABCA"

# print(return_indices(S,P))

def kmp_search(S, P):
    def compute_lps(P):
        lps = [0] * len(P)
        length = 0
        i = 1
        while i < len(P):
            if P[i] == P[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(P)
    indices = []
    i = 0
    j = 0

    while i < len(S):
        if P[j] == S[i]:
            i += 1
            j += 1

        if j == len(P):
            indices.append(i - j)
            j = lps[j - 1]
        elif i < len(S) and P[j] != S[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return indices

S = "AJEBFABABCASNSNABABCAMGPPOTK"
P = "ABABCA"

print(kmp_search(S, P))
