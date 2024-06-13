import collections

vote = []

def mem():
    print("1.Candidate1\n2.Candidate2\n3.Candidate3\n4.Candidate4\n5.Candidate5\n")

def get_member_choice(member_number):
    print(f"Member {member_number} voting")
    mem()
    choice = int(input("Vote for: "))
    return choice

def get_votes(num_members):
    votes = []
    for i in range(num_members):
        choice = get_member_choice(i+1)
        votes.append(choice)
    return votes

n = int(input("Enter no.of members: "))
votes = get_votes(n)


vote_counts = collections.Counter(votes)



winner_candidate, max_votes = vote_counts.most_common(1)[0]
# print(votes)
print(vote_counts)

if len(vote_counts) > 1 and vote_counts.most_common(2)[0][1] == vote_counts.most_common(2)[1][1]:
    print("There is a tie between the following candidates:")
    # print(vote_counts.items())
    # print(max(vote_counts.items()))
    tied_candidates = [candidate for candidate, count in vote_counts.items() if count == max_votes]
    # print(tied_candidates)
else:
    print(f"The winner is Candidate {winner_candidate} with {max_votes} votes.")