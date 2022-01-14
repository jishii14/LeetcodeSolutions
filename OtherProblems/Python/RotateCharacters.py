def rotationalCipher(input, rotation_factor):
  # Write your code here
  lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  lcfactor = rotation_factor % len(lowercase)
  ucfactor = rotation_factor % len(uppercase)
  numfactor = rotation_factor % len(numbers)
  
  solution = ""
  for cur in input:
    if cur in lowercase:
      lcindex = (lowercase.index(cur) + lcfactor) if (len(lowercase) > lowercase.index(cur) + lcfactor) else ((lowercase.index(cur) + lcfactor) - len(lowercase))
      solution += lowercase[lcindex]
    elif cur in uppercase:
      ucindex = (uppercase.index(cur) + ucfactor) if (len(uppercase) > uppercase.index(cur) + ucfactor) else ((uppercase.index(cur) + ucfactor) - len(uppercase))
      solution += uppercase[ucindex]
    elif cur in numbers:
      numindex = (numbers.index(cur) + numfactor) if (len(numbers) > numbers.index(cur) + numfactor) else ((numbers.index(cur) + numfactor) - len(numbers))
      solution += numbers[numindex]
    else:
      solution += cur
    
  return solution
