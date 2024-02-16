"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Xander Konell
Lab Time: 3
"""

def inc_5():
    # Write your code here
    initial_value = int(input())
    final_value = int(input())

    if final_value < initial_value:
        print("Second integer can't be less than the first.")
    else:
        current_value = initial_value
        while current_value <= final_value:
            print(current_value, end=" ")
            current_value += 5
        print()



if __name__ == '__main__':
    inc_5()