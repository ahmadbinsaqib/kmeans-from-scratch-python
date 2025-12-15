def receive_pairs_of_data_points():

    # List to store all input data points (each as [x, y] strings)
    data_points = []

    # List to store the initial cluster centres
    cluster_entries = []

    # Allow up to 100 data points to be entered
    for i in range(100):

        # Read a data point or the word 'quit'
        data = input(
            "Enter x, y (min 10, max 100 pairs). Enter 'quit' after 10+ pairs have been entered: "
        )

        # If at least 10 points have been entered and user types 'quit', stop input
        if i >= 10 and data == "quit":
            break

        # If fewer than 10 points have been entered and user types 'quit', reject it
        elif i < 10 and data == "quit":
            print("Not enough data points to quit. Please enter 10+ pairs of data points.")

        # Otherwise, split the input string and store it as a data point
        else:
            data_points.append(data.split(" "))

    # Ask the user how many clusters should be searched for
    clusters = int(input("How many clusters should be searched for? "))

    # Ensure the number of clusters is between 1 and 5 inclusive
    while not (1 <= clusters <= 5):
        clusters = int(input("Invalid. Enter a value for k where 1 ≤ k ≤ 5: "))

    # Select the first k data points as the initial cluster centres
    for i in range(clusters):
        cluster_entries.append(data_points[i])

    # Return the full list of data points and the initial cluster centres
    return data_points, cluster_entries


def compute_entries(data_points, cluster_entries):

    # List to store which cluster each data point belongs to
    # assignments[j] = cluster index assigned to data point j
    assignments = [0] * len(data_points)

    # Convert initial cluster centres from strings to floats
    for i in range(len(cluster_entries)):
        cluster_entries[i] = [float(cluster_entries[i][0]), float(cluster_entries[i][1])]

    # Repeat the clustering process up to 30 times
    for iteration in range(30):

        # Store previous cluster assignments to check for convergence
        old_assignments = assignments.copy()

        # Assign each data point to the closest cluster centre
        for j in range(len(data_points)):

            # Extract the x and y values of the current data point
            px = float(data_points[j][0])
            py = float(data_points[j][1])

            # Initialise the smallest distance variable
            smallest_distance = 0
            closest_cluster = 0

            # Compute squared distance to a cluster centre
            smallest_distance = (cluster_entries[0][0] - px)**2 + (cluster_entries[0][1] - py)**2

            # Compare this point to all cluster centres
            for i in range(1, len(cluster_entries)):
                distances = (cluster_entries[i][0] - px)**2 + (cluster_entries[i][1] - py)**2

                # Update smallest distance if a closer cluster is found
                if distances < smallest_distance:
                    smallest_distance = distances
                    closest_cluster = i # Index of the closest cluster

            # Store the result of the assignment for this data point
            assignments[j] = closest_cluster

        # Prepare lists to accumulate sums of x, y and counts for each cluster
        sum_x = [0.0] * len(cluster_entries)
        sum_y = [0.0] * len(cluster_entries)
        count = [0] * len(cluster_entries)

        # Accumulate x and y values for points in each cluster
        for j in range(len(data_points)):
            c = assignments[j]  # cluster assigned to data point j
            sum_x[c] += float(data_points[j][0])
            sum_y[c] += float(data_points[j][1])
            count[c] += 1

        # Compute the new mean (centre) for each cluster
        for i in range(len(cluster_entries)):
            if count[i] != 0:
                cluster_entries[i] = [sum_x[i] / count[i], sum_y[i] / count[i]]
            # If no points are assigned, the cluster centre remains unchanged

        # If no assignments changed in this iteration, stop early
        if assignments == old_assignments:
            break

    # Print the final cluster centres
    for i in range(len(cluster_entries)):
        print(f"Cluster {i} : {cluster_entries[i]}")


if __name__ == "__main__":
    # Read input data and initial cluster centres
    data_points, cluster_entries = receive_pairs_of_data_points()

    # Perform k-means clustering
    compute_entries(data_points, cluster_entries)
