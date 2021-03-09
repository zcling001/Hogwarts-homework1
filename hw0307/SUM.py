'''1）使用for循环实现1~100的之和；'''
# result = 0
# for i in range(101):
#     # print("i=",i)
#     result=result+i
# print("rsult",result)

'''2）然后在该循环中增加分支结构实现1~100的偶数和；'''
# result = 0
# for i in range(101):
#     if i%2==0:
#         print("i=", i)
#         result=result+i
# print("rsult",result)

''' 3）直接使用for循环，实现1~100的偶数和'''
result = 0
for i in range(2,101,2):#range(开始数字，结束数字，步长)
    print("i=", i)
    result=result+i
print("rsult",result)