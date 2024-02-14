N = int(input())
vote_array = list()
max_supporter =""
max_vote = 0
for i in range(N):
    vote_array.append(input())
vote_set = list(set(vote_array))

for supporter in vote_set:
    now_number = vote_array.count(supporter)
    if(max_vote < now_number):
        max_vote = now_number
        max_supporter = supporter

print(max_supporter)