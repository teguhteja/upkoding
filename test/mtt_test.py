import merge_the_tools as app


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
    my_app(['AABCAAADA', '3'], ['AB', 'CA', 'AD'], app.main)
