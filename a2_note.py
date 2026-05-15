Amount = int(input("Enter your Amount: "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("Number of 100 rupees notes: ", note_1)
print("Number of 50 rupees notes: ", note_2)
print("Number of 10 rupees notes: ", note_3)