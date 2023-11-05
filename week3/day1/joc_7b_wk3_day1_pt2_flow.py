#JoC 7 Basics Week 3 Day 1 Pt 2
# by Anthony Rodriguez

# 1. h(4)
# 2. h(5)

def f(x): 
	x = x-1
	return g(x)+1

def g(x):
	return x*2

def h(x):
	if x%2 == 1:      # x odd
		return f(x) + x
	else:             # x even
		return f(f(x))

print(h(3)) # 8
print(h(4))
print(h(5))