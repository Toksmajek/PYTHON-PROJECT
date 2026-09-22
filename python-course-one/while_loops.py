# Python course: while loops
# Last lesson: a loop repeats while its condition is True.
# If the condition never becomes False, the loop keeps running.

is_programmer = False

while not is_programmer:
    print("Learn programming")
    answer = input("Have you become a programmer? (yes/no): ")
    is_programmer = answer.strip().lower() == "yes"

print("Keep practising your Python skills!")

# Try it: enter "no" to repeat, then "yes" to finish.
# Write your own practice code below:


