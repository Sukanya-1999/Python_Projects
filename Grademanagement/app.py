"""
dict

collection-  key+value = pair = data1
add 
update
delete
view 
exit



"""
#create a dict
student = {
    "Paras":100,
    "Shubham":200
}

#accessing a element
print(student['Shubham'])

#update
student["Shubham"] = 300
print(student)

#delete
del student['Paras']
print(student)