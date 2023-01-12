import numpy as np
import matplotlib.pyplot as plt

## root((interval in tuple form), precision =5)
# function to be tested is within class and must be editted in func() and funcPlot()
# interval can any number values but must be in tuple form, contain a root and be an
# interval starting from a point less than the end point. 

class root:

    def __init__(self, interval, precision = 5):
        self.interval = interval
        self.precision = int(precision)

    def __str__(self):
        return f'Your interval is {self.interval}'
    
    def func(self,x):
        funcVal = np.exp(x) - 7*x**3 + x**5 - 20 + x**4
        funcVal = np.exp(x) - np.sin(x)
        #funcVal = np.exp(x) - 2
        #funcVal = np.exp(5-np.cos(x))-x**3
        #funcVal = np.exp(x) - np.sin(x) + 5*np.cos(x) - x**4
        return funcVal

    def intervalChecker(self, newInterval):
        start,end = newInterval
        if not isinstance(newInterval,tuple):
            #raise ValueError('Interval must be of type tuple!')
            return False # print(f'Interval must be of type tuple!')
        elif start >= end:
            # raise ValueError('Interval must complete!')
            return False #print('Interval must complete!')
        elif self.func(start)*self.func(end) > 0 :
            #raise ValueError('Interval must contain root!')
            return False #print('Interval must contain root!')
        else:
            return True
    
    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, newInterval):
        if self.intervalChecker(newInterval) == True:
            self._interval = newInterval
        elif self.intervalChecker(newInterval) == False:
            raise ValueError('Interval must contain a root, be in tuple form, and be complete!')

    def funcPlot(self):
        start,end = self.interval
        x = np.arange(start,end,.01)
        plt.figure()
        plt.plot(x, self.func(x), 'b-')
        plt.grid()
        plt.title('Function')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis()
        plt.show()

    def newtonsMethod(self):
        start, end = self.interval
        x = (start+end)/2
        xList = []
        yList = []
        print(f'x\t\t\t\ty\t\t\t\t%error')
        print(f'***********************************************************************')
        while self.func(x) >= 1/10**self.precision or \
            self.func(x) <= -1/10**self.precision:
            dx = .00001
            dy = self.func(x+dx) - self.func(x)
            m = dy/dx
            oldx = x
            x = x - self.func(x)/m
            error = abs((x-oldx)/x)
            xList.append(round(x,2))
            yList.append(round(self.func(x),2))
            print(f'{x:>10.{self.precision}f}\t{self.func(x):>20.{self.precision}f}\t{error:>30.4%}')

        plt.figure()
        plt.scatter(xList, yList)
        for i in range(len(xList)):
            plt.annotate(i, (xList[i],yList[i]))
        plt.grid()
        plt.title('Points for Newtons Method')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis()
        plt.show()    
        return print(f'Newtons root x value with precision {self.precision}: {x:.{self.precision}f}')

    def bisectionMethod(self):
        x0, x1 = self.interval
        x2 = (x0+x1)/2
        xList = []
        yList = []
        print(f'x\t\t\t\ty\t\t\t\t%error')
        print(f'***********************************************************************')
        while self.func(x2) >= 1/10**self.precision or \
            self.func(x2) <= -1/10**self.precision:
            oldx2 = x2
            x2 = (x0+x1)/2
            error = abs((x2-oldx2)/x2)
            if self.intervalChecker((x0,x2)) == True:
                x1 = x2
            elif self.intervalChecker((x2,x1)) == True:
                x0 = x2
            xList.append(round(x2,2))
            yList.append(round(self.func(x2),2))
            print(f'{x2:>10.{self.precision}f}\t{self.func(x2):>20.{self.precision}f}\t{error:>30.4%}')

        plt.figure()
        plt.scatter(xList, yList)
        for i in range(len(xList)):
            plt.annotate(i, (xList[i],yList[i]))
        plt.grid()
        plt.title('Points for Bisection Method')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis()
        plt.show()
        return print(f'Bisection root x value with precision {self.precision}: {x2:.{self.precision}f}')

    def secantMethod(self):
        x0, x1 = self.interval
        xList = []
        yList = []
        x2 = x1
        print(f'x\t\t\t\ty\t\t\t\t%error')
        print(f'***********************************************************************')
        while self.func(x2) >= 1/10**self.precision or \
            self.func(x2) <= -1/10**self.precision:
            dx = x1-x0
            dy = self.func(x1) - self.func(x0)
            m = dy/dx
            oldx2 = x2
            x2 = x1 - self.func(x1)/m
            error = abs((x2-oldx2)/x2)
            if self.intervalChecker((x0,x2)) == True:
                x1 = x2
            elif self.intervalChecker((x2,x1)) == True:
                x0 = x2
            print(f'{x2:>10.{self.precision}f}\t{self.func(x2):>20.{self.precision}f}\t{error:>30.4%}')
            xList.append(round(x2,2))
            yList.append(round(self.func(x2),2))
        plt.figure()
        plt.scatter(xList, yList)
        for i in range(len(xList)):
            plt.annotate(i, (xList[i],yList[i]))
        plt.grid()
        plt.title('Points for Secants Method')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axis()
        plt.show()
        return print(f'Secant root x value with precision {self.precision}: {x2:.{self.precision}f}')


a = root((-4,2),4)
print(a)
a.funcPlot()
# a.newtonsMethod()
# a.bisectionMethod()
# a.secantMethod()