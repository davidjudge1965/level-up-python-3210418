def is_palindrome(text):
    palindrome = False
    compressedtext = ""
    lctext = str.lower(text)
    #print(f'processing >{text}<')
    for letter in lctext:
      #print(letter)
      if letter in "abcdefghijklmnopqrstuvwxyz":
         #print("yes")
         compressedtext += letter
    #print(compressedtext)
    if compressedtext == compressedtext[::-1]:
       #print(f"{compressedtext} is a palindrome")
       palindrome = True

    return palindrome



# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true