# class Employee:
#     def __init__(self):
#         self.eid=input('enter the employee id:')
#         self.ename=input('enter the employee name:')
#         self.employee=float(input('enter the employee salary:'))
#     def employeedetails(self):
#         print(self.__dict__)
#         ans=input('do u want to incress the salary of the person type(yes/no):')
#         if ans.lower()=='y':
#             hike=eval(input('how much do u want to incress the salary:'))
#             self.employee=hike+self.employee
#             print(hike,'this amount of salary was hike and total',self.employee)
#         ans=input('do u want to add DA,TA,HRS to this person type(yes/no):')
#         if ans.lower()=='y':
#             ta=eval(input('enter the ta :'))
#             da=eval(input('enter the da :'))
#             hra=eval(input('enter the hra:'))
#             self.employeehike=self.employee+ta+da+hra
#             print("employee basice slary",self.employeehike)
#         ans=input('this person have any leaves (yes/no):')
#         if ans.lower()=='y':
#             leaves=int(input('enter the employee leaves: '))
#             print(self.employeehike)
#             self.employeehike=self.employeehike-(self.employeehike*(0.18))
#             print('after GST',self.employeehike)
#             v1=self.employeehike/(30)
#             print('employee per day salary',v1)
#             v2=v1*leaves
#             print('empoyee leaves amount:',v2)
#             v3=self.employeehike-(v2)
#             print('employee salary with leaves:',v3)
#
# e=Employee()
# e.employeedetails()
#
pin=1111
for x in range(1,4):
    pin=int(input('enter the pin number:'))
    if pin==1111:
        print('welcome user')
        break
    else:
        print('plz enter correct pin number')
else:
    print('your ATM was blocked for 24hrs')
print('thank you')