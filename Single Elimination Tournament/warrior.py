class Warrior:
  def __init__(self, name, strength):
    self.name = name
    self.strength = strength
    self.wins = 0

  def __str__(self):
    return f"Warrior {self.name} boasts {self.strength} strength"

# Getter strength
  @property
  def strength(self):
    return self._strength

# Getter name
  @property
  def name(self):
    return self._name

# Getter wins
  @property
  def wins(self):
    return self._wins

# Setter for name
  @name.setter
  def name(self, name):
    self._name = name

# Setter for strength
  @strength.setter
  def strength(self, strength):
    self._strength = strength

# Setter for wins
  @wins.setter
  def wins(self, n):
    self._wins = n
