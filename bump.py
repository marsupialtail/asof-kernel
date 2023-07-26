from ctypes import * 
import pyarrow as pa
import pandas as pd
import time
import numpy as np
trades = pd.DataFrame({"a":list(np.sort(np.random.randint(0,high=1000000, size=(1000000))))})
trades = pa.Table.from_pandas(trades).to_batches()[0]
quotes = pd.DataFrame({"a":list(np.sort(np.random.randint(0,high=1000000, size=(1000000))))})
quotes = pa.Table.from_pandas(quotes).to_batches()[0]
lib = PyDLL('example.cpython-37m-x86_64-linux-gnu.so')
lib._Z10MyFunctionP7_objectS0_i.argtypes = [py_object, py_object, c_int]
lib._Z10MyFunctionP7_objectS0_i.restype = py_object

#print(lib._Z10MyFunctionP7_object(1))
start = time.time()
z = lib._Z10MyFunctionP7_objectS0_i(trades,quotes, 20)
print(z)
print(time.time() - start)
