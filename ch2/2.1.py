import numpy as np

# scalar
## example like this...
np.dtype('int32').type(2)

# more examples with all the types of numpy
a = np.dtype('byte').type(1)
b = np.dtype('bool_').type(True)
c = np.dtype('bool8').type(False)
d = np.dtype('short').type(10)
e = np.dtype('intc').type(12)
f = np.dtype('int_').type(22) # python int, in my case is 64-bit
g = np.dtype('longlong').type(123876128736) # longlong is 64-bit, nothing impressive
h = np.dtype('intp').type(4323) # intp is 64-bit in my case because I am running on 64-bit OS

print('a', a)
print('type a', type(a))
print('b', b)
print('type b', type(b))
print('c', c)
print('type c', type(c)) # this prints the same type which is interesting
print('d', d)
print('type d', type(d))
print('e', e)
print('type e', type(e))
print('f', f)
print('type f', type(f))
print('g', g)
print('type g', type(g))
print('h', h)
print('type h', type(h))

# not only int32, but also 8, 16, 32, 64
# likewise, almost every type has an unsigned type as well.
