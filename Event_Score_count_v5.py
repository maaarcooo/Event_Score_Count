import time
# Database
# Use a list to manage scores for scalability
event_list = ["100m", "Long Jump", "Discus", "800m", "High Jump"]
people_list = ["Fraser", "Theo", "Harry", "Marco", "Elvis"]
scores = [0, 0, 0, 0, 0]

print("\nEvent score count program") # \n Skip to new line

continue_running = True  # Control variable for the main loop

while continue_running: # Main loop
    print("\nWhich event?") # \n: Skip to new line
    print("Event list: ")
    for i, event in enumerate(event_list): # for: Executes a block of code for each item in the sequence.
        print(f"{i + 1}. {event}") # f: Printing output with variable values
        # time.sleep(0.1)

    event_input = int(input("Type event number: "))

    if 1 <= event_input <= 5:
        event_scores = [0] * len(people_list)  # Temporary storage for scores from this event
        print(f"\n{event_list[event_input - 1]}: ")
        for i, person in enumerate(people_list):
            while True:  # Loop to ensure valid input (Input of integer)
                try:
                    rank = int(input(f"Where did {person} finish? "))
                    if 1 <= rank <= 5:
                        points_added = 10 - 2 * (rank - 1)
                        scores[i] += points_added
                        event_scores[i] = points_added
                        break
                    else:
                        print("Invalid input. Please enter a rank between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
        
        # Display results for this event with a very fast pace
        print(f"\nResults for {event_list[event_input - 1]}:")
        for person, added_score in zip(people_list, event_scores):
            print(f"{person}: Rank added {added_score} points")
            time.sleep(0.1) #Output streaming visual effect

        # Display and sort current total scores before asking to continue
        sorted_current_scores = sorted(zip(people_list, scores), key=lambda x: x[1], reverse=True)
        print("\nCurrent Total Scores (Sorted by Ranking):")
        for person, score in sorted_current_scores:
            print(f"{person}: {score} points")
            time.sleep(0.1)
    else:
        print("\nInvalid event number.")

    # Ask if user wants to continue or stop
    while True:
        continue_response = input("\nDo you want to continue to another event? (y/n): ").lower()
        if continue_response in ['y', 'yes']:
            break
        elif continue_response in ['n', 'no']:
            continue_running = False # Terminate the main loop
            break
        else:
            print("Invalid input. Please type 'y' for yes or 'n' for no.")

# Sort the final scores in descending order
sorted_final_results = sorted(zip(people_list, scores), key=lambda x: x[1], reverse=True)

print("\nFinal Scores (Sorted by Ranking):")
for person, score in sorted_final_results:
    print(f"{person}: {score} points")
    time.sleep(0.1)

print("\n[Event score count program terminated]")
# print("\nThank you for using the event score count program.")

## Expainations
# \n:
    # Skip to new line
# for:
    # Iterates over an iterable for example list or string and executes a block of code for each item in the sequence.
# emumerate():
    # Loop over an iterable (such as a list, tuple, or string) and have an automatic counter/index along with it.
# i:
    # A varable value for emumerate in this case.
# f:
    # F-Strings provide a concise way to format strings with variables, use for printing output with variable values in this case.
# len:
    # Get the size or length of a sequence-like object.
# try: used to wrap a block of code that might potentially raise an exception (an error). When an exception occurs within the `try` block, the code inside the `except` block will be executed instead.
    # 1. The code in the `try` block is executed.
    # 2. If an exception occurs (e.g., a divide-by-zero error, a missing file, etc.), Python will jump out of the `try` block and execute the `except` block instead.
    # code that might raise an exception# except [exception_type]:
    # code to handle the exception
    # code that might raise an exception# except [exception_type]:
    # code to handle the exception
# break: 
    # Stop executing the rest of the loop's body and proceed with the code following the loop.
# ValueError:
    # A built-in exception type that is raised when a function or method receives an argument that has the right type but is not appropriate for the function's purpose.
# sorted:
    # Returns a new sorted list from the elements of any sequence (such as a list or tuple)
    # my_list = [4, 2, 9, 6, 23, 12, 34, 0]
    # print(sorted(my_list))  # prints: [0, 2, 4, 6, 9, 12, 23, 34]
# zip:
    #
# lambda
    #
# reverse
    #

## Roadmap
# Add more flexibility
# Add DQ function -> No point
