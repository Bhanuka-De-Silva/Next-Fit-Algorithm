def next_fit_allocation_with_input():
    # Get the number of memory blocks and their sizes
    num_blocks = int(input("Enter the number of memory blocks: "))
    blocks = []
    for i in range(num_blocks):
        size = int(input(f"Enter the size of block {i + 1}: "))
        blocks.append(size)

    # Get the number of processes and their memory requirements
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        size = int(input(f"Enter the memory required for process {i + 1}: "))
        processes.append(size)

    # Initialize variables
    last_allocated = 0  # to Keep track of the last block index used for allocation.
    allocation = [-1] * num_processes  # To store block allocation for each process. -1 means not allocated yet

    # Perform Next Fit Allocation
    for i, process in enumerate(processes):
        allocated = False  # A flag to track whether the process has been allocated
        start_position = last_allocated  # Stores the current position of last_allocated to detect when the algorithm wraps around.

        while True:
            if blocks[last_allocated] >= process:  # Checks if the current block is large enough to accommodate the process(s).
                allocation[i] = last_allocated  # Updates allocation[i] with the index of the allocated block.
                blocks[last_allocated] -= process  # Reduces the size of the allocated block
                allocated = True  # Sets allocated to True and exits the loop using break.
                break

            last_allocated = (last_allocated + 1) % num_blocks  # If the current block cannot accommodate the process, moves to the next block

            if last_allocated == start_position:  # If the search returns to the start_position (full cycle is completed), the loop exits,
                break

        if not allocated:
            allocation[i] = -1  # Process could not be allocated

    # Display the results
    print("\nAllocation Results:")
    for i, process in enumerate(processes):
        if allocation[i] != -1:  # if the process allocated, displays the block number
            print(f"Process {i + 1} of size {process} allocated to block {allocation[i] + 1}.")
        else:  # otherwise displays cannot allocated
            print(f"Process {i + 1} of size {process} could not be allocated.")



# Run the program
next_fit_allocation_with_input()