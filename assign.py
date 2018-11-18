# Counts Number of tweets for each player
def tweetCount(name, res):
    if name in res.keys():
        res.update({name: int(res[name])+1})
    else:
        res.update({name: 1})

if __name__ == '__main__':
    cases = int(input())
    res = {}
    output = {}
    # Fetching Player Name and tweet ID
    for item in range(cases):
        numOfTweets = int(input())
        for c in range(numOfTweets):
            name, tweet_id = input().split()
            tweetCount(name, res)
    # Filtering players which have same tweet count
    for key1 in res:
        for key2 in res:
            if key1 == key2:
                continue
            elif res[key1] == res[key2]:
                output.update({key1: res[key1]})
    # Printing Data according to players name's alphabetical order
    # Data is arranged in a group of players having similiar number of tweets
    if bool(output):
        values = list(sorted(output.values()))
        removeDuplicate = []
        for i in values:
            if i not in removeDuplicate:
                removeDuplicate.append(i)
        for item in removeDuplicate:
            new = {}
            for k, v in output.items():
                if item == v:
                    new.update({k: v})
            for item in sorted(new.items()):
                print('{} {}'.format(item[0], item[1]))
    # Fetching player's name for maximum number of tweets
    a = max(res.keys(), key=lambda x: res[x])
    # Printing Data if that doesn't exist already
    if a not in output:
        print('{} {}'.format(a, res[a]))
