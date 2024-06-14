# starting point
# learning rate alpha
# number of iterations

x = 10
learning_rate = 0.1
num_iterations = 100

# loop for gradient descent
for i in range(num_iterations):
    gradient = 2*x
    x = x - learning_rate * gradient
    print(f"Iteration {i+1}, x = {x}, f(x) = {x**2}")
print(f"minimum value of x : {x}")