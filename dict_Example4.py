student_data = {
123 : ['Utsav','C G Road',120],
345 : ['Dixita','Parimal',190],
456:['Dhruvi','S G Highway',230]
}
for i,j in student_data.items():
    print(i)
    for k in j:
        print(k,end="\t")
    print()