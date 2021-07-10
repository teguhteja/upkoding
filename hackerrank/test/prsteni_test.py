from upkoding import prsteni as app


def test_app():
    # write your input
    input_values = ['3', '8 4 2']
    output = []

    def mock_input(s):
        # output.append(s)
        return input_values.pop(0)
    app.input = mock_input
    app.print = lambda s: output.append(s)

    app.prsteni()

    # write your output
    assert output == [
        # '3',
        # '8 4 2',
        '2/1',
        '4/1',
    ]
