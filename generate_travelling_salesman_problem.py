import numpy as np
import os


def write_distance_matrix(n, mean, sigma, i):
    distance_matrix = np.zeros((n, n))
    random_distance = []
    num_distance = int(n * (n-1) / 2)
    for _ in range(num_distance):
        distance = 0
        while distance <= 0:
            distance = np.random.normal(mean, sigma)
            # distance = np.random.randint(1,10)

        random_distance.append(distance)
    
    iu = np.triu_indices(n, 1)
    distance_matrix[iu] = random_distance
    distance_matrix += distance_matrix.T

    np.savetxt(
        f"Problems2/{n}/{n}_{mean}_{sigma}_{i}.out",
        distance_matrix,
        delimiter=" ",
        fmt="%1.4f",
        header=str(n),
        comments="",
    )


if __name__ == "__main__":
    n = int(input("Enter the number of locations: "))
    mean = 100
    sigma = 60
    times = 10
    # int(input("Enter the times of generation: "))
    os.makedirs(f"Problems2/{n}")
    for i in range(times):
        write_distance_matrix(n, mean, sigma, i)
