def max(values):

  _max = values[0]

  for val in values:
      if val > _max:
          _max = val

  print (_max)
  return _max


def min(values):

  _min = values[0]

  for val in values:
      if val < _min:
          _min = val

  return _min

if __name__ == "__main__":
  print(max([9,7,2,4]))
  print(min([9,7,2,4]))
