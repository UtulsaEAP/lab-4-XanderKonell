"""
Complete the following python code to reverse the string entered by the user.

Name: Xander Konell
Lab Time: 3
"""

def reverse_string():
    # YOUR CODE HERE
    while True:
        user_input = input()
        if user_input.lower() in ['done', 'd']:
            break
        else:
            print(user_input[::-1])

if __name__ == "__main__":
    reverse_string()