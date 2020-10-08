#coding:utf-8
'''
Cupy （numpy的GPU版本）
官网：https://cupy.chainer.org
====================================
Instruction：

  numpy转cupy: x = cupy.asarray(x) 
  cupy转numpy: x = cupy.asnumpy(x)

'''

'''
测试cupy和numpy在矩阵运算速度上的差别
'''

from tqdm import tqdm
import time
import numpy as np

a = 10000
b = 10000
epochs = 10

print('矩阵大小: %d*%d' % (a, b))
x = np.random.rand(a, b).astype(np.float32)
y = np.random.rand(b, a).astype(np.float32)
start = time.time()
for i in tqdm(range(epochs // 2), 'CPU矩阵乘法速度'):
    np.dot(x, y)
cpu_time = time.time() - start

try:
    import cupy as cp
    x = cp.asarray(x)
    y = cp.asarray(y)
    start = time.time()
    for i in tqdm(range(epochs), 'GPU矩阵乘法速度'):
        cp.asnumpy(cp.dot(x, y))
    gpu_time = time.time() - start
    print('cpu/gpu=%.2f倍时间' % (epochs / (epochs // 2) * cpu_time / gpu_time))
    x = np.random.rand(1024 * 1024 * 256).astype(np.float32)
    for i in tqdm(range(epochs * 10), '内存->显存', unit='GB'):
        cp.asarray(x)
    x = cp.asarray(x)
    for i in tqdm(range(epochs * 10), '显存->内存', unit='GB'):
        cp.asnumpy(x)
except:
    pass
