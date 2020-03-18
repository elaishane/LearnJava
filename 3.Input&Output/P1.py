# Write a Python Program to accept id,name,phone,email.address and pincode from user

s1 = input('Enter id: ')
id = int(s1)
name = input("Enter Name: ")
s2  = input("Enter Phone Number: ")
Phone = int(s2)
address = input("Enter Address: ")
pincode = int(input("Enter Pincode: "))

print("id: ",id)
print("Name: ",name)
print("Phone Number: ",Phone)
print("Address: ",address)
print('Pincode: ',pincode)

print('id: ',id, 'name: ',name, 'phone: ',Phone, 'Address: ',address, 'pincode: ',pincode)

'''
Output:
Enter id: 1
Enter Name: Yash
Enter Phone Number: 8850306639
Enter Address: 25/263,Janaganga,Borivali-West
Enter Pincode: 400091
id:  1
Name:  Yash
Phone Number:  8850306639
Address:  25/263,Janaganga,Borivali-West
Pincode:  400091
id:  1 name:  Yash phone:  8850306639 Address:  25/263,Janaganga,Borivali-West pincode:  400091
'''