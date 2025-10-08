emoji_data ={
    'love':'❤️',
    'angry':'😡',
    'please':'🙏',
    'happy':'😊',
    'confuse':'😕'
}

message=input("Enter your message : ")
seperator_string=" "
updated=[]

for word in message.split():
    clean_msg= word.lower().strip(".,?,!")
    emoji= emoji_data.get(clean_msg)
    if emoji:
        updated_word= f"{word} {emoji}"
        # updated_message+=updated_word
        updated.append(updated_word)
    else:
        # updated_message+=word
        updated.append(word)
    
updated_message= seperator_string.join(updated)
print(updated_message)