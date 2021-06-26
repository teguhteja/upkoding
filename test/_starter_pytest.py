# 1. change the name files
import _starter as app


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
    # 2 edit input and output files. set output in string
    # 3 change name files input and output. rec using abbrevation
    input_file = read_files('i/starter.in')
    output_file = read_files('o/starter.ou')
    my_app(input_file, output_file, app.main)
