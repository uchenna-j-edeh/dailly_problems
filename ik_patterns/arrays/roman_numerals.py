"""This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14
    """

# algo. keep going, convert the letter. if you meet letter bigger than current. nega

def convert(letter):
    result = 0
    my_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    previous = "x"
    end = len(letter) - 1
    for i in range(len(letter)):
        if previous == '-':
            result -= letter[end - 1]
        else:
            previous = '+'
            

         