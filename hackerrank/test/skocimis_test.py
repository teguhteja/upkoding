import upkoding.skocimis as app


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
    my_app(['2 3 5'], [1], app.main)


def test_app2():
    my_app(['3 5 9'], [3], app.main)
