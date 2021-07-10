import upkoding.modular as app


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
    my_app(['1000 3', '1 / 999', '1 / 998', '578 * 178', '13 4', '7 / 9',
            '9 * 3', '0 - 9', '10 + 10', '0 0'], [999, -1, 884, 8, 1, 4, 7], app.main)
