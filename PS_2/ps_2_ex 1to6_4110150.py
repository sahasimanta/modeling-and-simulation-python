#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem Sheet 2: Modeling and Simulation by Simanta Saha (4110150)


# In[2]:


## Exercise 1


# In[3]:


import numpy as np

A0 = np.diag([2, 2, 2, 2], k=0)
A1 = np.diag([-3, -3, -3], k=1)
A2 = np.diag([-1, -1], k=2)
A3 = np.diag([-5], k=3)
A4 = np.diag([3, 3, 3], k=-1)
A5 = np.diag([1, 1], k=-2)
A6 = np.diag([5], k=-3)
A = A0 + A1 + A2 + A3 + A4 + A5 + A6
print("Matrix A:")
print(A)


# In[4]:


## Exercise 2


# In[5]:


a = np.array([[5, 0,-2, 1, 8]])
b = np.array([[3, 4, 0, 1, 0]])

print(a)
print(b)
print(a.shape)
print(b.shape)


# In[6]:


c0=a<b
print("Less than:",c0)
c1=a>b
print("Grater than:",c1)
c2=a==b
print("Equals:>",c2)


# In[7]:


## Exercise 3


# In[8]:


### a


# In[9]:


d=np.array([[0,1,5,0]])
print(d)


# In[10]:


### b


# In[11]:


minimum=d[0,0]

for number in d[0]:
    if number<minimum:
        minimum=number
print("Minimum:",minimum)


# In[12]:


###c


# In[13]:


maximum=d[0,0]
i=0
while i<4:
    if d[0,i]>maximum:
        maximum=d[0,i]
    i=i+1
print("Maximum:",maximum)


# In[14]:


###d


# In[15]:


step = np.pi / 20

x_values = []
y_values = []

for i in range(21):
    x = i * step
    y = np.sin(x)
    x_values.append(x)
    y_values.append(y)

print(x_values)
print(y_values)


# In[16]:


import matplotlib.pyplot as plt
plt.plot(x_values, y_values)
plt.show()


# In[17]:


## Exercise 4
    # a


# In[18]:


x=4
y=1
z=1
f= lambda x,y,z:2*x**2 - y**4 + 3*z**3
result = f(x,y,z)
print(result)


# In[19]:


#b


# In[20]:


import runpy
n = 9
A = np.ones((n, n)) + 2 * np.eye(n)
b = np.zeros(n)
for i in range(n):
    for j in range(n):
        b[i] = b[i] + (j + 1) * A[i, j]


gaussian_elimination = runpy.run_path(
    "ps_2_ex 4b_4110150.py"
)["gaussian_elimination"]


x = gaussian_elimination(A, b)

print("Matrix A:")
print(A)

print("Vector b:")
print(b)

print("Solution vector x:")
print(x)

print("Verification:", np.allclose(A @ x, b))


# In[21]:


## Exercise 5


# In[22]:


t = np.linspace(0, 2*np.pi, 100)

x = np.cos(t)
y = np.sin(t)
z = np.sin(t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.grid(True)
plt.show()


# In[23]:


## Exercise 6


# In[24]:


print("1. Physical: A small model of a wind turbine in a laboratory.")

print("2. Abstract: A Python simulation of an RC circuit.")

print("3. Static: A DC voltage divider with constant input voltage.")

print("4. Dynamic: An RC circuit where capacitor voltage changes with time.")

print("5. Real-time: A car driving simulator running in real time.")

print("6. Interactive: A flight simulator controlled by the user.")

print("7. Continuous: A pendulum model showing continuous motion with time.")

print("8. Discrete: A traffic light model changing states at fixed intervals.")

print("9. Realistic: A car braking model considering friction and air resistance.")

print("10. Simplistic: A falling ball model without air resistance.")

print("11. Natural: A model of water flowing in a river.")

print("12. Artificial: A conveyor belt system in a factory.")

print("13. Imagined: A model of a fictional spacecraft propulsion system.")

print("14. Simple: An ideal RC circuit with one resistor and one capacitor.")

print("15. Complex: An electrical power grid with generators, transformers and loads.")

print("16. Deterministic: A projectile motion model with fixed initial conditions.")

print("17. Stochastic: A wireless communication model with random noise.")

print("18. Known input: An RC circuit with a known 5 V input.")

print("19. Statistical input known: A receiver model with Gaussian noise of known mean and variance.")

print("20. Unknown input: A building vibration model affected by an unknown earthquake.")

