from collections import Counter
def climbingLeaderboard(scores, alice):
    rank_array = []
    index = 0
    scores = Counter(scores)
    scores = sorted([i for i,j in scores.items()])
    n = len(scores)
    print(scores)
    for item in alice:
        while n > index and item >= scores[index]:
            index +=1
        rank_array.append(n+1-index)
    print(rank_array)
    return rank_array




climbingLeaderboard([100,90,90,80,75,60],[50,65,77,90,102])