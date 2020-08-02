def tj():

 # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[10])

if __name__== "__main__":
  tj()
