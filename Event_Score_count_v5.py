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
