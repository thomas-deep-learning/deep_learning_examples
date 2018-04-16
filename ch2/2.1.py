import numpy as np

"""""""""""""""""""""""""""
scalar

"""""""""""""""""""""""""""
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

# float types
a = np.dtype('half').type(1.0) # float16
b = np.dtype('single').type(2.2) # float32
c = np.dtype('double').type(3.4) # float64
d = np.dtype('float_').type(123.1) # float64 which is python float type
e = np.dtype('longfloat').type(1321.4323) # float128
f = np.dtype('float64').type(1232122.112) # float64
# f = np.dtype('float96').type(1232122.112)
# sometimes it doesn't have the float96 type, I guess be careful with this type
g = np.dtype('float128').type(1238.1232) # float128

print('a', a)
print('type a', type(a))
print('b', b)
print('type b', type(b))
print('c', c)
print('type c', type(c))
print('d', d)
print('type d', type(d))
print('e', e)
print('type e', type(e))
print('f', f)
print('type f', type(f))
print('g', g)
print('type g', type(g))

"""""""""""""""""""""""""""
vector

"""""""""""""""""""""""""""
# using a Python list object to build a numpy array
x = np.array([1, 2, 3, 4])
print('x', x)
print('shape of x', x.shape)
print('type of x', x.dtype)
y = np.array([[1], [2], [3], [4]])
print('y', y)
print('shape of y', y.shape)
print('type of y', y.dtype)
z = np.array([[1,2], [2, 3], [3,4 ], [4, 5]])
print('z', z)
print('shape of z', z.shape)
print('type of z', z.dtype)
print('reshape (4, ) to (4, 1)', x.reshape((4, 1)))
# [[1], [2], [3], [4]]
print('reshape (4, ) to (1, 4)', x.reshape((1, 4)))
# [[1, 2, 3, 4]]

########################################################
# using some other simple ways to build a numpy array  #
#### initializing with np.arange() # array range       #
########################################################
x = np.arange(10) # this actually will generate an array, not a matrix
print('x', x)
print('shape of x', x.shape)
print('type of x', x.dtype)
y = np.zeros((3, 3)) # default type for zeros is float64?
print('y', y)
print('shape of y', y.shape)
print('type of y', y.dtype)
z = np.linspace(1, 60, 1000) # default type for this is float64 as well
print('z', z)
print('shape of z', z.shape)
print('type of z', z.dtype)
å = np.indices((6, 6)) # I don't know how important this is, but definitely a weird one
print('å', å)
print('shape of å', å.shape)
print('type of å', å.dtype)

print('some examples of how to form an array np.arange(400).reshape((20, 20))\n', np.arange(400).reshape((20, 20)))
print('its transpose: ', np.transpose(np.arange(400).reshape((20, 20))))

# last, show broadcasting and prove some theorems they mentioned in the book