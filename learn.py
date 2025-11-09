def test(cmd, *args):
    print(args[0])

test('bla', 'arg1')

txt = 'rm file'.split()
print(txt)

test(txt[0], txt[1])