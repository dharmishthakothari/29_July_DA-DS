# checking whether email id are valid or not
lst_email = ['test@gmail.com','test123@gmail.com','asd.com','dddd@gmail.com']
for i in lst_email:
    if i.endswith("gmail.com"):
        print(f" {i} is valid email")