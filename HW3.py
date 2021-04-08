student1= str(input("1.Öğrenci Adı: "))
midtern1= int(input("Midtern Grade: "))
project1= int(input("Project: "))
final1= int(input("Final: "))
a= ((midtern1)*0.3 + (project1)*0.3 + (final1)*0.4)

student2 =  str(input("2.Öğrenci Adı:"))
midtern2= int(input("Midtern Grade: "))
project2= int(input("Project: "))
final2= int(input("Final: "))
b= ((midtern2)*0.3 + (project2)*0.3 + (final2)*0.4)

student3 =  str(input("3.Öğrenci Adı:"))
midtern3= int(input("Midtern Grade: "))
project3= int(input("Project: "))
final3= int(input("Final: "))
c= ((midtern3)*0.3 + (project3)*0.3 + (final3)*0.4)

student4 =  str(input("4.Öğrenci Adı:"))
midtern4= int(input("Midtern Grade: "))
project4= int(input("Project: "))
final4= int(input("Final: "))
d= ((midtern4)*0.3 + (project4)*0.3 + (final4)*0.4)

student5 =  str(input("5.Öğrenci Adı:"))
midtern5= int(input("Midtern Grade: "))
project5= int(input("Project: "))
final5= int(input("Final: "))
e= ((midtern5)*0.3 + (project5)*0.3 + (final5)*0.4)
dict= {"Student1": [student1, midtern1,project1,final1,a],"Student2": [student2, midtern2,project2,final2,b],
    "Student3": [student3, midtern3,project3,final3,c],"Student4": [student4, midtern4,project4,final4,d],
    "Student5": [student5, midtern5,project5,final5,e] }
print(dict)

list=[dict["Student1"][4],dict["Student2"][4],dict["Student3"][4],dict["Student4"][4],dict["Student5"][4]]

print(list)
list.sort(reverse=True)
print(list)

