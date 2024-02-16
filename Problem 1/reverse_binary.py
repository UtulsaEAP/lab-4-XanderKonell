"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Xander Konell
Lab Time: 3

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    binary_string = ""
    while user_num > 0:
        binary_string += str(user_num % 2)
        user_num //= 2
    
    print(binary_string)

if __name__ == "__main__":
    reverse_binary()