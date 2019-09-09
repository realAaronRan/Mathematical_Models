import numpy as np
import matplotlib.pyplot as plt


def foo(arg1, arg2):
    """

    :param[in] arg1:
    :param arg2:
    :return:
    :example: this is an example of the foo function.
    """
transition_mat = np.array([[1/3, 2/3, 0, 0],
                           [1/2, 0, 1/2, 0],
                           [0, 0, 0, 1],
                           [1/2, 0, 1/4, 1/4]])
start_state = np.array([0.8, 0.2, 0, 0])
eigen_values, eigen_vectors = np.linalg.eig(transition_mat.T)
with open('./eigen_decompose.txt', 'a') as file:
    np.savetxt(file, eigen_values, '%.4f')
    file.write('\n\n')
    np.savetxt(file, eigen_vectors, '%.4f')
# print(np.linalg.matrix_power(transition_mat, 20))
# time_steps = 50
# future_state = np.matmul(start_state, transition_mat)
# states_series = future_state
# for time in range(time_steps):
#     future_state = np.matmul(future_state, transition_mat)
#     # np.vstack([states_series, future_state])
#     states_series = np.vstack([states_series, future_state])
# plt.figure()
#
# plt.subplot(2, 2, 1)
# plt.xlabel('Time Step')
# plt.ylabel('States Probability')
# plt.plot(states_series[:, 0], 'g-')
#
#
# plt.subplot(2, 2, 2)
# plt.xlabel('Time Step')
# plt.ylabel('States Probability')
# plt.plot(states_series[:, 1], 'g-')
#
#
# plt.subplot(2, 2, 3)
# plt.xlabel('Time Step')
# plt.ylabel('States Probability')
# plt.plot(states_series[:, 2], 'g-')
#
#
# plt.subplot(2, 2, 4)
# plt.xlabel('Time Step')
# plt.ylabel('States Probability')
# plt.plot(states_series[:, 3], 'g-')
#
# plt.show()
