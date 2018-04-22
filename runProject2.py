import os

threads = [1, 2, 4]

coarseness = ['coarse', 'fine']
dynamics = ['staticRun', 'dynamicRun']

for t in threads:
  for c in coarseness:
    for d in dynamics:
      cmd = "g++ -o project2 project2.cpp -DNUMTHREADS=%d -D%s -D%s -lm -O3 -fopenmp" % (t, c, d)
      os.system(cmd)
      cmd = "./project2"
      os.system(cmd)