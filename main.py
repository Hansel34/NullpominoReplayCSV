import os
from collections import defaultdict

class replayData():
   def __init__(self):
      self.time = None
      self.finished = None
      self.name = None
      self.timeStamp = None
      

replays = []
replayCount = 0
for filename in os.listdir(os.getcwd()):
   if filename.endswith(".rep"):
      x = replayData()
      with open(filename) as f:
         lines = f.readlines()
         x.name = lines[1]
         for line in lines:
            if line.startswith("0.statistics.time"):
               x.time = int(line[18:-1])/60
            if(line.startswith("0.statistics.lines")):
               x.finished = int(line[19:-1])
            if(line.startswith("timestamp.gmt")):
               x.timeStamp = line[14:-1]

      replays.append(x)
perMonth = defaultdict(list)
perMonthGamesPlayed = defaultdict(int)
for i in replays:
   if(i.finished >= 40 and i.time<85):
      perMonth[i.timeStamp[:7]].append(i.time)
   perMonthGamesPlayed[i.timeStamp[:7]]+=1

perMonthTime = {}
for key in perMonth:
   perMonthTime[key]= sum(perMonth[key])/len(perMonth[key])

print("Time Stamp , Time Taken, Games Played")
for key in perMonthTime:
   print("%s, %s , %f" % (key,perMonthTime[key],perMonthGamesPlayed[key]))
