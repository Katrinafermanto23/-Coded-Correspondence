alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

translated_message = ""

for character in message:
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]
  else:
    translated_message += character

print(translated_message)

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo y wej oekh cuiiqwu, y qc mhyjydw je udshofj iecujxydwi"

translated_message = ""

for character in message: 
    if character in alphabet: 
        character_value = alphabet.find(character)
        translated_message += alphabet[(character_value + 10)%26]
    else:
        translated_message += character 

print(translated_message)

def caesar_decode(message, offset):
    decoded_message = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            decoded_character = alphabet[(character_value - offset) % 26]
            decoded_message += decoded_character
        else:
            decoded_message += character
    
    return decoded_message

message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
decoded_message = caesar_decode(message_one, 10)
print(decoded_message)


