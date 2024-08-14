def solve():
  print("****************************************")

  statement = input("Enter a statement: ").lower().split()

  print(statement)
  
  ErrorTerms = ['or', 'and', 'not', '"or"', '"not"', '"and"']
  
  And = []
  Or = []
  Not = []
  NoChoice = []
  Choices = []
  Final = None
  
  for index, word in enumerate(statement):
    if word == "and":
      if statement[index - 1] in ErrorTerms or statement[index + 1] in ErrorTerms:
        print("Error happened")
        return 0
      if statement[index - 2] == "not" and statement[index + 1] not in Not or statement[index - 1] not in Not:
        if statement[index + 1] not in Not:
          Not.append(statement[index + 1])
        elif statement[index - 1] not in Not:
          Not.append(statement[index - 1])
      if statement[index - 2] == "or" and statement[index + 1] not in Or or statement[index - 1] not in Or:
        if statement[index + 1] not in Or:
          Or.append(statement[index + 1])
        elif statement[index - 1] not in Or:
          Or.append(statement[index - 1])
      else:
        And.append(statement[index + 1])
        And.append(statement[index - 1])
    elif word == "or":
      if statement[index - 1] in ErrorTerms or statement[index + 1] in ErrorTerms:
        print("Error happened")
        return 0
      elif statement[index - 2] == "and":
        if statement[index - 1] in Not:
          And.append(statement[index + 1])
        elif statement[index + 1] in Not:
          And.append(statement[index - 1])
      elif statement[index - 2] == "not":
        if statement[index - 1] in And:
          Not.append(statement[index + 1])
        elif statement[index + 1] in And:
          Not.append(statement[index - 1])
      else:
        Or.append(statement[index - 1])
        Or.append(statement[index + 1])
    elif word == "not":
      if statement[index - 1] in ErrorTerms or statement[index + 1] in ErrorTerms:
        print("Error happened")
        return 0
      Not.append(statement[index + 1])
  
  for index, _and in enumerate(And):
    if _and not in Choices:
      Choices.append(_and)
  
  for index, _or in enumerate(Or):
    if len(And) == 0:
      Choices.append(_or)
      Final = _or
    if _or in And:
      if _or in Choices:
        Final = _or
      else:
        Choices.append(_or)
        Final = _or
    else:
      if _or not in Choices:
        Choices.append(_or)
      
  for index, _not in enumerate(Not):
    if _not in Choices:
      Choices.remove(_not)
    if _not not in NoChoice:
      NoChoice.append(_not)

  for choice in Choices:
    if choice not in Not:
      Final = choice
      break
  
  print(" .ANDS. ")
  for _and in And:
    print(_and)
  
  print(" .ORS. ")
  for _or in Or:
    print(_or)
  
  print(" .NOTS. ")
  for _not in Not:
    print(_not)
    
  print(" .CHOICES. ")
  for choice in Choices:
    print(choice)
    
  if Final is None:
    print("Final: Not Found")
  else:
    print("FINAL: ", Final)
    print("!!!!!!SUCCESS!!!!!!")

  with open("information.txt", "a") as file:
    file.write(f"Final: {Final}\n")
    file.close()

  main()

def check_reverse():
  print("****************************************")
  word = input("Enter a word: ").lower()
  reversedWord = word[::-1]
  
  if word == reversedWord:
    print("Same word in reverse")
  else:
    print("Not the same word in reverse")

  main()

def check_finals():
  print("****************************************")
  index = 1
  with open("information.txt", "r") as file:
    for line in file:
      print(index, line, sep=". ")
      index = index + 1
    file.close()
  index = 1

  main()

def main():
  print("****************************************")
  choice = input("Choose an AI option (S, CF, CR): ")
  if choice.lower() == "s":
    solve()
  elif choice.lower() == "cr":
    check_reverse()
  elif choice.lower() == "cf":
    check_finals()
  else:
    print("Invalid input.")
    main()

main()
