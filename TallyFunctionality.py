help = "Welcome to tallybot here is a list of my commands :) \n \
$create name [starting tally] \n \
$remove name \n \
$tally name [increment_amount] \n \
$show tally \n \
$list \n \
"
class tally:
  
  def __init__(self):
    self.tallyMap = {}

  def createTally(self,message):
    temp = message.split(" ")
    if (len(temp) < 2): return "I need a name for the Tally!"
    name = temp[1]
    start = 0
    if(len(temp) > 2):
      try:
        start = int(temp[2])
      except: return temp
    
    if name in self.tallyMap: return "Tally " + name + " already exists"
    self.tallyMap[name] = start
    return "Tally " + name + " created with count " + str(start)

  def removeTally(self,message):
    temp = message.split(" ")
    if (len(temp) < 2): return "I need a name for the Tally!"
    name = temp[1]
    if name not in self.tallyMap: return "Tally " + name + " doesn't exist"
    del self.tallyMap[name]
    return "Tally " + name + " removed"
    
  def printHelp():
    return help

  def showTally(self,message):
    temp = message.split(" ")
    if (len(temp) < 2): return "I need a name for the Tally!"
    name = temp[1]
    if name not in self.tallyMap: return "Tally " + name + " doesn't exists"
    return name + ": " + str(self.tallyMap[name])
  
  def addTally(self, message):
    temp = message.split(" ")
    if (len(temp) < 2): return "I need a name for the Tally!"
    name = temp[1]
    val = 1
    if(len(temp) > 2):
      try:
        val = int(temp[2])
      except: val = 1
    if name not in self.tallyMap:
      self.createTally(message)
    self.tallyMap[name] += val
    return "Tally " + name + " now has value " + str(self.tallyMap[name])

  def listTally(self):
    toRet = "A list of all my tallies: \n"
    for x in self.tallyMap:
      toRet += x + "\n"
    return toRet

