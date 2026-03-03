"""
Given a secret message string, and an integer representing the number of letters 
that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.
"""
def decode(message, shift):
    """
    Decodes a secret message that was encoded using a Caesar cipher shift.
    
    Args:
        message (str): The encoded message to be decoded
        shift (int): The number used to shift the original message.
    
    Returns:
        str:
    """
    decoded = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                decoded_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decoded_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decoded += decoded_char
        else:
            decoded += char
    return decoded

#Test Stage
print(decode("Xlmw mw e wigvix qiwweki.", 4))
