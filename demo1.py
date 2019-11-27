# # # ans='y'
# # # # value=1
# # # while ans==ans:
# # #     a=int(input('enter the number:'))
# # #     # for x in range(1,a+1):
# # #     #     value=x*value
# # #     print('the given number',a,'thats the factorial value is:',a**a)
# # #     print("do you want to check the another number type(y/n):")
# # # ans='y'
# # # if ans=='y':
# # #     num=int(input('enter the number:'))
# # #     print('power=',num**num)
# # # print('do you wnt see another numbertype(y/n):',ans)
# # ans='y'
# # value=1
# # while ans.lower()=='y':
# #     a=int(input('enter the number:'))
# #     for x in range(1,a+1):
# #         value=x*value
# #     print('given factorial is',a,'the value is',value)
# #     ans = input("Do you want to see another number yes/no : ")
# # num=eval(input('enter the number:'))
# # val = 0
# # for x in range(1,num+1):
# #     val = val+x
# # Function for nth fibonacci number - Space Optimisataion
# # Taking 1st two fibonacci numbers as 0 and 1
# # Function for nth fibonacci number - Dynamic Programing
# # Taking 1st two fibonacci nubers as 0 and 1
# n=int(input('enter the number:'))
# def get(n):
#     if n<0:
#         print("incorrect input")
#     elif n==0:
#         return 0
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return get(n-1)+get(n-2)
# print(get(n))
#
# x=[1,2,3,2,3,4,5,4,6,7,8,7,9,1,11,1,5,13,167,12,134,34,55,66,76,5,43,43,65]
# x.sort()
# print(x)
# print('***********')
# x.sort(reverse=True)
# print(x)
# d1={'x':100,
#     'y':200,
#     'z':300
#     }
# print(d1)
# for x in d1.keys():
#     print(x)
# for x in d1.values():
#     print(x)
# print('************')
#
# d1={'x':100,
#     'y':200,
#     'z':300
#     }
# keys=[]
# values=[]
# item=d1.items()
# for x in item:
#     keys.append(x[0]),
#     values.append(x[1])
# print(keys)
# print(values)
# pin=1111
# for x in range(1,4):
#     pin=int(input("enter your pin number:"))
#     if pin==1111:
#         print('welcome user')
#     else:
#         print('plz enter correct pin number')
#
# else:
#     print('your account was blocker in 24hrs')
# print("***************************")
# pin=1111
# y=1
# while y<4:
#     pin=int(input("enter your pin number:"))
#     if pin==1111:
#         print('welcome user')
#     else:
#         print('plz enter correct pin number')
#     y=y+1
# else:
#     print('your account was blocker in 24hrs')

# letter='hai i am venky from sathya tech python teached by CCreddy'
# for x in letter:
#     if x=='a':
#         print('pass statument is executed.........')
#         pass
#     else:
#         print(x)
# ans='y'
# while ans=='y':
#     a=int(input('ENTER THE NUMBER:'))
#     if a<=0 or a>=101:
#         print('plz enter the number above 0 and below 101 ')
#         continue
#     else:
#         for x in range(1,11):
#             print(x,'*',a,'=',a*x)
#     ans=input('do you see another number type(Y/N):')
ans='y'
while ans.lower()=='y':
    a=int(input('enter the account number:'))
    if a in range(112233,334456) :
        print('welcome user')
        ans=input('do you want to see another account(Y/N): ')
    else:
        print('plz enter correct account number')
        continue
print('thank you')

# a=int(input('plz enter the number:'))
# x=1
# while x<=10:
#     print(a,"*",x,"=",a*x)
#     x=x+1
