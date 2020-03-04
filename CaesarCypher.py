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
  if char.isalpha() == True:
    temp = ord(char)
    temp += key
  
    cypher += chr(temp)
    
  else: 
    cypher += char

#print('temp: ', temp)
print("cypher: ",cypher)