import time

def typing_speed_test():
    # Sample text for the user to type
    test_text = "The quick brown fox jumps over the lazy dog."

    print("Typing Speed Test")
    print("Type the following sentence as fast and accurately as you can:")
    print("\n" + test_text + "\n")

    # Wait for user to be ready
    input("Press Enter when you're ready to start...")

    # Record the start time
    start_time = time.time()

    # Get user input
    typed_text = input("\nStart typing here:\n")

    # Record the end time
    end_time = time.time()

    # Calculate time taken in seconds
    time_taken = end_time - start_time

    # Calculate words per minute (WPM)
    word_count = len(typed_text.split())
    wpm = (word_count / time_taken) * 60

    # Calculate accuracy
    correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(test_text) and c == test_text[i])
    accuracy = (correct_chars / len(test_text)) * 100

    # Display results
    print("\nResults:")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing speed test
typing_speed_test()
