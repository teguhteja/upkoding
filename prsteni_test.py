import math as m
# def prsteni():
n = int(input())
r = list(map(int, input().split(' ')))
for i in range(1,n):    
    g = m.gcd(r[0],r[i])
    print(f'{r[0]//g}/{r[i]//g}')
    


# from unittest import mock, TestCase
# import unittest

# class MyTest(TestCase):
#     @mock.patch('builtins.input', create=True)
#     def test(self, mocked_input, mock_print):
#         mocked_input.side_effect = ['3', '8 4 2']
#         mock_print.assert_called_with(3)

# # Showing what is in mock
#     import sys
#     sys.stdout.write(str( mock_print.call_args ) + '\n')
#     sys.stdout.write(str( mock_print.call_args_list ) + '\n')

# if __name__ == '__main__':
#     unittest.main()