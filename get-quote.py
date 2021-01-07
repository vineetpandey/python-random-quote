import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  # 1 & 4. Added quotes programmatically
  f = open("quotes.txt", "a+")
  f.writelines("Let's try out adding a new line." + str(rnd) + "\n")
  f.close()
  # Read the quotes
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  # 2. Printed random no. of quotes
  # 3. removed that extra line(newline) while printing
  for i in range(0, rnd):
    print(quotes[i].rstrip(), end='')
    
  print()

if __name__== "__main__":
  primary()
