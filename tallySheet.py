class TallySheet(object):
  """ Implements a tally sheet to track a set of category - count pairs. """ 
  def __init__(self, title = "Tally Sheet"): 
    """ Constructs an empty tally sheet with no categories. An optional 
    string title can be provided for the tally sheet (default title 
     is "Tally Sheet"). 
     Precondition: the optional title must be a string. """ 
    if not isinstance(title, str): 
       raise TypeError("The tally sheet title must be a string.") 
       self._title = title 
       self._categories = {} # Holds category : count pairs for tally sheet
  def getTitle(self): 
     """ Returns the title of the tally sheet.""" 
     return self._title 
  def setTitle(self, newTitle): 
    """ Updates the tally sheet title to newTitle. 
    Precondition: the new title must be a string.""" 
    if not isinstance(newTitle, str): 
      raise TypeError("The tally sheet title must be a string.") 
      self.title = newTitle 
  def addCategory(self, category, amount=0): 
    """ Adds a new category to the tally sheet and sets its count to 0
    or the optional initial value. If the category already exists, 
    we'll assume they really wanted to increase its count by 
    the optional value.
    Precondition: the optional initial value must be a non-negative
    integer. 
    """
    # I decided to accept any type of category, but convert it to a string so all the 
    # category values are strings.
    category = str(category)
    if not isinstance(amount, int):
      raise TypeError("A category must have an integer count.") 
    if amount < 0: 
      raise ValueError("A category's initial amount cannot be negative.")
    if category in self._categories.keys():
      self._categories[category] += amount
    else: 
      self._categories[category] = amount 
    def removeCategory(self, category): 
      """ Removes category from the tally sheet.
      Precondition: none (if category is not in the tally sheet its already
      gone)
      """
      category = str(category)
      if category in self._categories.keys():
        del self._categories[category]
      else:
        raise KeyError("The category '", category, "' doesn't exist. Can't remove them")
    def getTally(self, category):
      """ Returns the count for the specied category.
      Precondition: the category is in the tally sheet. 
      """ 
      category = str(category)
      if category in self._categories.keys():
        return self._categories[category]
      else:
        raise KeyError("Cannot get count of category '"+category+"'. It's not found.") 
    def setTally(self, category, amount):
      """ Sets the count of a category to a specied amount. (If category
      is not in the tally sheet, then add it with specied amount)
      Precondition: the specied amount is a non-negative integer.
      """
      category = str(category)
      if amount < 0:
        raise ValueError("The new amount cannot be negative.")
      if category in self._categories.keys(): 
        self._categories[category] = amount
      else:
        raise KeyError("Cannot set amount to category '"+category+"'. Key not found.")
    def increment(self, category, amount = 1):
      """ Adds one to the count of the specied category or adds more
      than one by an optional amount.
      Precondition: the category already exists, and the optional 
      amount must be a non-negative integer. 
      """ 
      category = str(category)
      if amount < 0: 
        raise ValueError("The new amount cannot be negative.") 
      if category in self._categories.keys(): 
        self._categories[category] += amount
      else: 
        raise KeyError("Cannot increment category '"+category+"'. Key not found.")
    def decrement(self, category, amount = 1):
      """ Subtracts one to the count of the specied category or
      subtracts more than one by an optional amount.
      Precondition: the category already exists, and the optional 
      amount must be a non-negative integer. 
      """ 
      category = str(category) 
      if amount < 0: 
        raise ValueError("The new amount cannot be negative.")
      if category in self._categories.keys():
        if amount > self._categories[category]:
          raise ValueError("decrement by "+str(amount)+" would cause negative tally.")
        else: 
          self._categories[category] -= amount
      else: 
          raise KeyError("Cannot decrement '"+category+"'. Key not found.") 
    def zeroAll(self): 
       """ Set the counts of all categories to 0. """
       for key in self._categories.keys():
         self.setTally(key, 0) 
    def __str__(self): 
       """ Returns the string representation of the tally sheet's content
       in a tabular format including the title and two columns for 
       each category and count. 
       """
       resultStr = self._title.center(60) + "\n\n"
       for category in sorted(self._categories.keys()): 
         count = self._categories[category] 
         resultStr += "%-30s %d\n" % (category, count) 
    return resultStr
    def itemsSortedByCategory(self):
        """ Returns the contents of the tally sheet as a list of tuples
        (category, count) sorted by category."""
        resultStr = ""
        for category in sorted(self._categories.keys()):
          count = self._categories[category] 
          resultStr += "%-30s %d\n" % (category, count) 
          return resultStr 
    def itemsSortedByCount(self): 
        """ Returns the contents of the tally sheet as a list of tuples
         (category, count) sorted by count.""" 
        resultStr = ""
        for category, count in sorted(self._categories.items(), key=lambda item: item[1]):
           resultStr += "%-30s %d\n" % (category, count) 
        return resultStr                              
