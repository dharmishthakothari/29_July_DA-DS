class ClinicAppointment:
	def bookApprointment(self,dict1):
		self.dr_dict=dict1
		name=input("Enter patient Name")
		age = int(input("Enter Age"))
		mobile_num = int(input("Enter Mobile number "))
		print(list(dict1.keys()))
		pre_doc = input("Please enter prefer doctor ")
		print(list(dict1[pre_doc]))
		time_slot=input("Please enter available slots ")
		print(f"{name} - {age} - {mobile_num} - {pre_doc} - {time_slot} ")
		self.checkAvaibility(pre_doc,time_slot)
		print(self.dr_dict)
		
    # def cancle(self):
	# 	pass
	# def viewApp(self):
	# 	pass
	def checkAvaibility(self,pref_doc,time_slot):
		no_of_slots= self.dr_dict[pref_doc][time_slot]
		print(f"{no_of_slots} ")
		if no_of_slots<3:
			self.dr_dict[pref_doc][time_slot]=no_of_slots+1
			return self.dr_dict
		else:
		 	return "Slots are already Book Please selct other slots"
		
        

dict1 = {'Mr. Patel' :{'10 am':0,'11 am':0,'2 pm':0} ,
	'Mr. Shah' : 	{'11 am':0,'12 am':0,'2 pm':0},
	'Mr. modi' : {'10 am':0 ,'11 am':0}
	}
obj=ClinicAppointment()

while True:
	print("1. Book Approintment " )
	print("2 Exit")
	ch=int(input("Enter your choice"))
	match ch:
		case 1:  obj.bookApprointment(dict1)
		case 2:break