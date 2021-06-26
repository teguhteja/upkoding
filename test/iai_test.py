import iterables_and_iterators as app


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


def read_files(file):
    with open(file) as f:
        contents = f.read()
        f.close()
    return contents.split('\n')


def test_app1():
    input = read_files('iai.in')
    my_app(input, ['0.8333'], app.main)


def test_app2():
    input = read_files('iai1.in')
    my_app(input, ['0.722222222222'], app.main)
