#Below is the tesTallySheet.py PYTHON script as mentioned on the Part A question. It also needs to be updated
from tallySheet import TallySheet 
def main(): 
  outcomeTallies = TallySheet() 
  # Test TallySheet() 
  try:
    birds = TallySheet("Birds") 
  except TypeError:
    print("TypeError, the given title is not of string format") 
  # Test getTitle()
  print(birds.getTitle()) 
  # Test setTitle()
  try:
    birds.setTitle("Birds 1/1/19") 
  except ValueError:
    print("ValueError, the given title is not of string format")
  # Test addCategory()
  try: 
    birds.addCategory("sparrow") 
    birds.addCategory("robin", 5) 
  except ValueError:
    print("ValueError, the given amount is less than zero") 
  except TypeError:
    print("TypeError, the given amount is not of integer type") 
  # Test removeCategory() 
  try:
    birds.removeCategory("eagle")
  except KeyError: 
    print("KeyError, the given category does not exist")
  # Test getTally() 
  try: 
    count = birds.getTally("robin")
  except KeyError:
    print("KeyError, the given category does not exist") 
  # Test setTally() 
  try: 
    birds.setTally("robin", 3) 
  except ValueError:
    print("ValueError, The given amount is negative") 
  except KeyError:
    print("KeyError, The given category does not exist")
  # Test increment() 
  try:
    birds.increment("sparrow") 
    birds.increment("robin", 5)
  except ValueError:
    print("ValueError, The given amount is negative")
  except KeyError: 
    print("KeyError, The given category does not exist")
  # Test decrement()
  try:
    birds.decrement("sparrow") 
    birds.decrement("robin", 5) 
  except ValueError: 
    print("ValueError, The given amount is invalid") 
  except KeyError: 
    print("KeyError, The given category does not exist") 
  # Test zeroAll() 
  birds.zeroAll() 
  # Test str()
  print(str(birds))
  # Test itemsSortedByCategory() 
  cats = birds.itemsSortedByCategory() 
  print(cats)
  # Test itemsSortedByCount 
  birds.setTally("sparrow", 3) 
  birds.setTally("robin", 5) 
  cnts = birds.itemsSortedByCount() 
  print(cnts) 
  # YOUR EXISTING TESTING CODE 
  ''' 
  tSheet = TallySheet("Birds on June 1, 2018") 
  print("Title:", tSheet.getTitle()) 
  tSheet.addCategory("robin", 5) 
  tSheet.addCategory("sparrow", 10) 
  tSheet.addCategory("cardinal", 3) 
  tSheet.addCategory("blue jay", 4) 
  print(tSheet)
  print("\nitemsSortedByCount:", tSheet.itemsSortedByCount()) 
  # Test getTally 
  try: 
  print("eagle:",tSheet.getTally("eagle")) 
  except KeyError:
    print("TypeError, the given title is not of string format")
  # Test decrement
  try:
    for count in range(5):
    tSheet.decrement("cardinal")
    print("cardinal decremented to:", tSheet.getTally("cardinal"))
    except ValueError:
    print("ValueError encountered cannot decrement cardinal to negative amount")
    try: 
    tSheet.decrement("eagle") 
    print("eagle decremented to:", tSheet.getTally("eagle")) 
    except KeyError:
    print("KeyError encountered cannot decrement since eagle is not a category") 
    print("Done") 
    '''
main() # start main function running
                               
