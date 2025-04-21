# Initialize empty queues
premium_queue = []
standard_queue = []
economy_queue = []

# Read from a file called 'packet_input.txt'
with open("packet_input.txt", "r") as file:
    for line in file:
        # Strip newline/extra whitespace and split the line into priority + name
        parts = line.strip().split()
        if len(parts) >= 2:
            priority = parts[0].upper()
            name = " ".join(parts[1:])

            # Append to appropriate queue
            if priority == 'P':
                premium_queue.append(name)
            elif priority == 'S':
                standard_queue.append(name)
            elif priority == 'E':
                economy_queue.append(name)

# Print the initial queues (for debugging)
print("Premium Queue:", premium_queue)
print("Standard Queue:", standard_queue)
print("Economy Queue:", economy_queue)

print("\nDequeued Packets in WFQ Order:\n")

# Apply Weighted Fair Queuing: 3P : 2S : 1E
while premium_queue or standard_queue or economy_queue:
    # 3 Premium
    for _ in range(3):
        if premium_queue:
            print("P", premium_queue.pop(0))

    # 2 Standard
    for _ in range(2):
        if standard_queue:
            print("S", standard_queue.pop(0))

    # 1 Economy
    if economy_queue:
        print("E", economy_queue.pop(0))
