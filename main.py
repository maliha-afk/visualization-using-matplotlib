import matplotlib.pyplot as plt
import numpy as np

companysproduct=np.array(["face cream","face wash","hair spray","hair wash","body wash","shaving cream"])
profit=np.array([30,50,10,70,65,90])

plt.plot(companysproduct,profit)
plt.title("company's product & profit")
plt.xlabel("company's product")
plt.ylabel("profit")

plt.show()