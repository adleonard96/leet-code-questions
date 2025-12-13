class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = set([i for i in range(numberOfUsers)])
        offline = []
        all_count = 0
        orders = {"MESSAGE": 1, "ONLINE": 0, "OFFLINE":0}
        events = sorted(events, key=lambda x: (int(x[1]), orders[x[0]]))
        for event in events:
            event_name, time, message = event  
            if event[0] == "OFFLINE":
                if int(message) in online:
                    online.remove(int(message))
                    offline.append([int(time), int(message)])
                else:
                    for account in offline:
                        if account[1] == int(message):
                            offline.remove(account)
                            offline.append([int(time), int(message)])
            elif event[0] == "ONLINE":
                online.add(int(message))
            else:
                if message == "HERE":
                    #pop through offline, add any that need to be online
                    while offline and offline[0][0] + 60 <= int(time):
                        online.add(offline[0][1])
                        offline = offline[1:]
                    #go through online and update vals in the res
                    for user in online:
                        mentions[user] += 1
                elif message == "ALL":
                    all_count += 1
                else:
                    message_split = message.split(" ")
                    for split in message_split:
                        mentions[int(split[2:])] += 1
        
        if all_count > 0:
            for i in range(len(mentions)):
                mentions[i] += all_count
        
        return mentions
    
print(Solution().countMentions(numberOfUsers=3, events=[["MESSAGE","1","ALL"],["OFFLINE","66","1"],["MESSAGE","66","HERE"],["OFFLINE","5","1"]]))