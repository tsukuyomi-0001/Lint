import lint
"""
app -
    |- file1
    |- model-
            |-model1
            |-model2
            |-model3

"""
app = lint.map('app')
file1 = app.create_obj('avvag/file1')
model1 = app.create_obj('model/model1', 'some data')
model2 = app.create_obj('model/model2', 'some more data')
model3 = app.create_obj('model/model3', 'lots of data')
app.read('model/model3')
app.write('model/model3', 'new data', 'a')
app.read('model/model3')

x = """
x = ['a', 'b', 'c']
for i in x:
    print(x)
"""

nex = app.create_obj('first.py', x)
app.script('first.py')

app.save()