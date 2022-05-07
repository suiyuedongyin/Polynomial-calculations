"""
多项式代数表达式形如：f(x)=a0+a1*x+a2*x^2+a3*x^3+....+an*x^n
1. 设计一个多项式类Polynomial (10分)
2. 采用修饰器函数计算多项式的值 (10分)
3. 重载格式化输出函数, 可以显示多项式的代数表达式 (10分)
4. 重载加法运算符“+”, 可以实现两多项式的加法运算 (10分)
5. 重载减法运算符“-”, 可以实现两多项式的减法运算 (10分)
6. 编写一个测试主程序:
   给定多项式列表f1, 输出其代数表达式 (10分)
   给定多项式列表f2, 输出其代数表达式 (10分)
   测试加法运算f3=f1+f2, 输出其代数表达式 (10分)
   测试减法运算f4=f1-f2, 输出代数表达式 (10分)
   给定x的值, 计算f1、f2、f3、f4的值 (10分)

测试用例1:
    f1(x) = 1+2x+x^2
    f2(x) = 1+2x
    x = 1.0
测试用例2:
    f1(x) = 1-3x+5x^2-7x^3
    f2(x) = 1-2x+4x^2
    x = 2.0
"""
class Polynomial:
    def __init__(self,f):
        self.f=f
        self.cishu=len(f)
        self.biaodashi2=[]
        for i in range(len(f)):
            if i==0 :
                if f[i]==0:
                    biaodashi1='0'
                else :
                    biaodashi1='%d'%f[0]
            elif i==1:
                if f[1]==1:
                    biaodashi1='x'
                elif f[1]==0:
                    biaodashi1='0'
                else:
                    biaodashi1='%dx'%f[1]    
            else:
                if f[i]==1:
                    biaodashi1='x^%d'%i
                elif f[i]==0:
                    biaodashi1='0'
                else:
                    biaodashi1='%dx^%d'%(f[i],i)
            self.biaodashi2.append(biaodashi1)
        self.biaodashi3='+'.join(self.biaodashi2)
        self.biaodashi='f(x)='+self.biaodashi3
    def __add__(self,other):
        f=[]
        if self.cishu>other.cishu:
            for i in range(other.cishu):
                a=self.f[i]+other.f[i]
                f.append(a)
            for i in range(other.cishu,self.cishu):
                a=self.f[i]
                f.append(a)
        else :
            for i in range(self.cishu):
                a=other.f[i]+self.f[i]
                f.append(a)
            for i in range(self.cishu,other.cishu):
                a=other.f[i]
                f.append(a)
        return Polynomial(f)
    def __sub__(self,other):
        f=[]
        if self.cishu>other.cishu:
            for i in range(other.cishu):
                a=self.f[i]-other.f[i]
                f.append(a)
            for i in range(other.cishu,self.cishu):
                a=self.f[i]
                f.append(a)
        else :
            for i in range(self.cishu):
                a=self.f[i]-other.f[i]
                f.append(a)
            for i in range(self.cishu,other.cishu):
                a=-1*other.f[i]
                f.append(a)
        return Polynomial(f)
    def intro(self):
        print(self.biaodashi)
    def calculation(self,x):
        result=0
        for i in self.f:
            if i==0:
                result1=0
            else:
                result1=i*x^self.f.index(i)    
        result+=result1
        print(result)
        #未调试完全
f1=[1,2,1]
polynomial1=Polynomial(f1)
polynomial1.intro()
polynomial1.calculation(1)

f2=[1,2]
polynomial2=Polynomial(f2)
polynomial2.intro()
polynomial2.calculation(1)

polynomial3=polynomial1+polynomial2
polynomial3.intro()
polynomial3.calculation(1)

polynomial4=polynomial1-polynomial2
polynomial4.intro()
polynomial4.calculation(1)

f11=[1,-3,5,-7]
f22=[1,-2,4]

polynomial11=Polynomial(f1)
polynomial11.intro()
polynomial11.calculation(1)

f2=[1,2]
polynomial22=Polynomial(f2)
polynomial22.intro()
polynomial22.calculation(1)

polynomial33=polynomial1+polynomial2
polynomial33.intro()
polynomial33.calculation(1)

polynomial44=polynomial1-polynomial2
polynomial44.intro()
polynomial44.calculation(1)