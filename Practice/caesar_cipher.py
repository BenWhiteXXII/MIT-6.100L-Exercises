# Define the alphabet as a list of lowercase letters
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create an empty string to hold the encrypted message
encryptedMsg=""

# Prompt the user for a message to encrypt
unencryptedMsg = input("Please input the unencrypted message: ")

# Convert the message to lowercase to ensure it matches the alphabet array
lowercase_unencryptedMsg = unencryptedMsg.lower()

# Prompt the user for the shift value
shift = int(input("Please input the shift number: "))

# Loop through each letter in the unencrypted message
for letter in lowercase_unencryptedMsg:
    if letter == " ":
        encryptedMsg = encryptedMsg + " "
        continue
    else:
        # Set position to the first letter of the alphabet
        pos = 0
        # Loop through the alphabet to find the position of the letter
        for i in alphabet:
            # If the current letter matches the alphabet calculate its new posistion by adding the shift value
            if letter == i:
                shiftPos = pos + shift
                # If the new position goes beyond the end of the alphabet, wrap around
                if shiftPos > 25:
                    shiftPos -= 26
                # Append the shifted letter to the encrypted message
                encryptedMsg = encryptedMsg + alphabet[shiftPos]
            else:
                pos += 1  # Increment the position for the next letter

# Print the final encrypted message
print("Your encrypted message: ", encryptedMsg)
