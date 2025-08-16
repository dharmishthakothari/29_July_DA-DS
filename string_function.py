# string function

name="Tops technologies pvt ltd. is technology company"

print(f" {name} lower() {name.lower()}")
print(f" {name} upper() {name.upper()}")
print(f"{name} title() {name.title()}")
print(f"{name} capitlize() {name.capitalize()}")
print(f"{name} replace() {name.replace("tech","123",1)}")
print(f"{name} count() {name.count("t")}")
name1=name.split()
print(name1)
print(f"{name} split() {name.split(".")}")
lst_name=['Dhruvi','Patel','Python student']
name2="*".join(lst_name)
print(name2)
a="  This is new string  "
print(len(a))
print(len(a.strip()))