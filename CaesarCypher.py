"""
The program accepts a key(int) n and converts(Shifts) any given text by n amount. 
"""

# Step 01: Get the key
key = int(input("Please enter the key: "))

# Step 02: Encypher the text

# Get the text to Cypher 
text = input("Enter Text? ")

# Define a cypher text variable
cypher = " "

# Convert the text into ASCII and enter them into a temp valriable 

for char in text: 
  # Chek if the character is a letter
  if char.isalpha() == True:
    # First convert the lower case letters
    if char.islower() == True:
      temp = ord(char) - 97
      temp += key
      # Add the % operator to make sure that the character stays wihin bounds. 
      temp = temp % 26 
      # Add character to cypher text string 
      cypher += chr(temp + 97)
  
    else:
      # now check for uppercase letters
      temp = ord(char) - 65
      temp += key
      # Add the % operator to make sure that the character stays wihin bounds. 
      temp = temp % 26
      # Add the character to Cypher text string 
      cypher += chr(temp + 65) 
  else: 
    cypher += char

print("cypher: ",cypher)