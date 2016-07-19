<<<<<<< HEAD
=======
# Thanks for @j2kun's contribution
>>>>>>> origin/master
import numpy
from numpy import array, transpose, dot
from numpy.linalg import inv

<<<<<<< HEAD
# 线性回归统计运算
avg = lambda L: 1.0 * sum(L)/len(L)

=======
avg = lambda L: 1.0 * sum(L)/len(L)

# bestLinearEstimator: [(float, float)] -> (float, float), (float -> float)
>>>>>>> origin/master
# single variable input single variable output linear regression
def bestLinearEstimator(points):
   xAvg, yAvg = map(avg, zip(*points))

   aNum = 0
   aDenom = 0
   for (x,y) in points:
      aNum += (y - yAvg) * x
      aDenom += (x - xAvg) * x

   a = float(aNum) / aDenom
   b = yAvg - a * xAvg
   return (a, b), lambda x: a*x + b

<<<<<<< HEAD
def bestLinearEstimatorMV(points):
   # input points are n+1 tuples of n inputs and 1 output
   X = array([[1] + list(p[:-1]) for p in points]) 
=======

# bestLinearEstimatorMV: [[float]] -> [float], ([float] -> float)
# multivariable input single variable output linear regression
def bestLinearEstimatorMV(points):
   # input points are n+1 tuples of n inputs and 1 output
   X = array([[1] + list(p[:-1]) for p in points]) # add bias as x_0
>>>>>>> origin/master
   y = array([p[-1] for p in points])

   Xt = transpose(X)
   theInverse = inv(dot(Xt, X))
   w = dot(dot(theInverse, Xt), y)
   return w, lambda x: dot(w, x)


<<<<<<< HEAD
# 程序入口
if __name__ == "__main__":

   import random  # 加入随机数生成模块
=======
if __name__ == "__main__":
   import random
>>>>>>> origin/master

   a = 0.5
   b = 7.0
   noise = lambda: random.random() * 0.4 - 0.2
   points = [(x, a*x + b + noise()) for x in [random.random() * 10 for _ in range(100)]]
   print(bestLinearEstimator(points)[0])


   print(bestLinearEstimatorMV(points)[0])

   trueW = array([-3,1,2,3,4,5])
   bias, linearTerms = trueW[0], trueW[1:]
   points = [tuple(v) + (dot(linearTerms, v) + bias + noise(),) for v in [numpy.random.random(5) for _ in range(100)]]

<<<<<<< HEAD
   print(bestLinearEstimatorMV(points)[0])
=======
   print(bestLinearEstimatorMV(points)[0])
>>>>>>> origin/master
