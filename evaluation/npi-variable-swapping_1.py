##NOT FOUND in Flask, Manim and Tensorflow
##Using sample provided by https://www.programiz.com/python-programming/examples/swap-variables
def swapp_variable()
    # To take inputs from the user
    x = input('Enter value of x: ')
    y = input('Enter value of y: ')

    # create a temporary variable and swap the values
    temp = x
    x = y
    y = temp

    print('The value of x after swapping: {}'.format(x))
    print('The value of y after swapping: {}'.format(y))