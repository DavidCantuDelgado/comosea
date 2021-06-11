# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    ["-4"],
    ["87"],
    ["45"]
]

# List of lists, where each inner list has all the output/prints that end in the terminal
output_values = [
    ["Dame un número: "] + [v for v in range(-4, 101)],
    ["Dame un número: "] + [v for v in range(87, 101)],
    ["Dame un número: "] + [v for v in range(45, 101)],
]

# List of hints for each test, in case of an error
error_messages = ["", "", ""]