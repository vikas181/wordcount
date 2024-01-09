import Ops

string = 'This is a test string. Count the number of words in it'

#Method 1
#strOpsObj = Ops.StringOps()
#wcount = strOpsObj.wordcount(string)

#Method 2
wcount = Ops.StringOps.wordcount('',string)


print(' Number OF words = ',wcount)
