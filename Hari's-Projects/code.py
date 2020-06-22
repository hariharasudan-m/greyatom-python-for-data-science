# --------------
#Registery of Students
class_1=['Geoffrey', 'Hinton', 'Andrew Ng', 'Sebastian Raschika', 'Yoshua Bengio']
class_2=['Hilary', 'Mason', 'Carla Gentry', 'Corinna Cortes']
new_class=class_1+class_2
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print('Registery of Students')
print(new_class)
print('_'*100)
#Dictionary for Geoffrey Hinton's marks to generate his report.
courses={'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
marks=courses.values()
total=sum(marks)
print("Geoffrey Hinton's marks")
print('Total Marks:',total,'out of 500')
percentage=(total/500)*100
print('Percentage:',percentage)
#Finding Maths Topper of the School
mathematics={'Geoffrey Hnton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshuna  Benijio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75}
max_marks_scored=max(mathematics,key=mathematics.get)
topper=max_marks_scored
print('_'*100)
print('Topper of Mathematics:',topper)
print('_'*100)
#Print the Topper name in the certificate by last name first and first name second
first_name=topper.split()[0]
last_name=topper.split()[1]
full_name=last_name+" "+first_name
Full_Name=full_name.upper()
certificate_name=Full_Name
print('#'*100)
print('Cerificate of Merit')
print('  ')
print('Topper of the Mathematics:',certificate_name)


