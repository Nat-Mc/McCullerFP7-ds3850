def main():
    print("Let's fill in a funny script!")
    
    adjective = input("Please enter an adjective: ")
    large_objects_plural = input("Please enter a plural noun (large objects): ")
    body_part = input("Please enter a body part: ")
    restaurant = input("Please enter a restaurant name: ")
    first_food = input("Please enter a food item (first food): ")
    second_food = input("Please enter a food item (second food): ")
    large_object_singular = input("Please enter a singular noun (large object): ")
    
    script = (f"I’ve had a very {adjective} day. "
              f"This morning, I dropped a box of {large_objects_plural} on my {body_part}. "
              f"Then, at lunch, I went to {restaurant} for their delicious {first_food}, "
              f"But the waiter brought me {second_food}, which I was not hungry for. "
              f"Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof.")
    
    print("\nHere's your filled-in script:")
    print(script)

if __name__ == "__main__":
    main()
