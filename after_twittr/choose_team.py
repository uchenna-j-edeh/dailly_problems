

def teamFormation2(score, team_size, k):
    # Write your code here
    result = []
    for i in range(team_size):
        len_score = len(score)
        first_elem = score[0:k]
        last_elem = score[len_score-k:]
        
        max_first_elem = max(score[0:k])
        max_last_elem = max(score[len_score-k:])
        if max_first_elem >= max_last_elem:
            first_elem.remove(max_first_elem)
            result.append(max_first_elem)
        else:
            last_elem.remove(max_last_elem)
            result.append(max_last_elem)
        score = first_elem + score[k:len_score-k]+ last_elem
    return sum(result)

def teamFormation(score, team_size, k):  
    # Write your code here
    result = []
    # len_score = len(score)
    for i in range(team_size):
        # find the highest value with its, index
        highest = 0
        len_score = len(score)
        indx = 0
        if len(score) <= k:
            result.append(sum(score))
            break
        else:
            for j in range(k):
                if score[j] >= score[len_score-1 -j] and score[j] >= highest:
                    highest = score[j]
                    indx = j
                elif score[len_score-1 -j] >= score[j] and score[len_score-1 -j] >= highest:
                    highest = score[len_score-1 - j]
                    indx = len_score-1 - j
            score.pop(indx)
            result.append(highest)

    return sum(result)

score = [10,20,10,15,5,30,20]
teamSize = 2
k = 3

print(teamFormation(score, teamSize, k))


score = [6,
18,
8,
14,
10,
12,
18,
9]

team = 8
k = 3

print(teamFormation(score, team, k))