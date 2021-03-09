'''3、编写一个计算器，使用pytest，完成计算器的测试用例；使用数据驱动完成测试用例的自动生成；在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【结束计算】'''

class Calculator:

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b