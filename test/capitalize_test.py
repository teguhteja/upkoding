import capitalize as app


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


def output_files(file):
    with open(file) as f:
        contents = f.read()
        f.close()
    return contents


def test_app1():
    # output = output_files('rangoli.txt')
    # output = output.split('\n')
    my_app(['chris alan'], ['Chris Alan'], app.main)


def test_app2():
    # output = output_files('rangoli.txt')
    # output = output.split('\n')
    my_app(['hello   world  lol'], ['Hello   World  Lol'], app.main)