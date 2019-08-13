import random
def primary():
#  print ("Keep it logically awesome.")

  f = open("quotes.txt","a+")

  for i in range(2):
    f.write("Appended line %d\r\n" % (i+1))


  #quotes = f.readlines()
  f.close()

  #last = len(quotes) - 1
  #rnd = random.randint(0, last)

  #print (quotes[rnd],end = '')
  #print (quotes[last])

if __name__== "__main__":
  primary()
