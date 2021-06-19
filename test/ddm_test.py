import designer_door_mat as app


def my_app(my_input, my_output, my_test):
    # write your input
    input_values = my_input
    output = []

    def mock_input(s):
        # output.append(s)
        return input_values.pop(0)
    app.input = mock_input
    app.print = lambda s: output.append(s)

    my_test()

    # write your output
    assert output == my_output


def test_app1():
    output = [
        '------------.|.------------\n'
        '---------.|..|..|.---------\n'
        '------.|..|..|..|..|.------\n'
        '---.|..|..|..|..|..|..|.---\n'
        '----------WELCOME----------\n'
        '---.|..|..|..|..|..|..|.---\n'
        '------.|..|..|..|..|.------\n'
        '---------.|..|..|.---------\n'
        '------------.|.------------'
    ]
    my_app(['9 27'], output, app.main)
