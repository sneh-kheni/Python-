'''monthConversions = {

    "jan" : "january",
    "virat" : "king",
    "dhoni" : "thala",
    "mar" : "march",
    5 : "thursday",
    "jeel is smart" : "jeel is good"

}
print(monthConversions["virat"])
print(monthConversions.get("dhoni"))
print(monthConversions.get("rohit","hitman"))
print(monthConversions["jeel is smart"])'''
arr = ["eat","tea","tan","nat","ate","bat"]
mp = {}
for i in arr:
    sorv = tuple(sorted(i))
    if sorv not in mp:
        mp[sorv]=[]
    mp[sorv].append(i)
mp.values()
print(mp.values())
print(mp)







 