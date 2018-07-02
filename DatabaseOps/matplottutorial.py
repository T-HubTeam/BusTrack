import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [5,6,4,3,5,7,7]


# plt.figure()
# ax = plt.subplot(121)

# plt.subplot(1,2,1)
# plt.scatter(x,y)

# plt.subplot(1,2,2)
# plt.plot(x,y)	


# ax.annotate('example', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )




# plt.show() 


fig = plt.figure()
ax = fig.add_subplot(111)

t = [1,2,3,4,5,6]
s = [3,4,5,6,7,8]
line, = ax.plot(t, s, lw=2)

ax.annotate('annotateexample', xy=(4,6), xytext=(5,6),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

# sax.set_ylim(-2,2)
plt.show()