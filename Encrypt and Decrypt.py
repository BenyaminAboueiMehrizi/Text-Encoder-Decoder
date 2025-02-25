while True:
   print("Choice Your Option\n\t1-Encrypt\n\t2-Decrypt\n\t3-Exit")
   choice = input("enter = ")
   if choice == "1":
      text_1 = input("Write your text: ")
      encrypted_text = ""
      for c in text_1:
         x = ord(c) * 4 + 6
         encrypted_text += chr(x)
      print("encrypted_text", encrypted_text)
   elif choice == "2":
      if choice == "2":
         encrypted_text = input("Write your text: ")
         text_1 = ""
         for c in encrypted_text:
            x = (ord(c) - 6) // 4
            text_1 += chr(x)
         print("decrypted text: ", text_1)
   elif choice == "3":
      print("See You Later!")
      break
   else:
      print("Wrong! Enter the Write number!")
