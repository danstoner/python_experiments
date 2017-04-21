import easygui

result = easygui.ynbox('Shall I continue?', 'Title', ('Yes', 'No'))

if result:
    easygui.buttonbox('Click on your favorite flavor.', 'Favorite Flavor', ('Chocolate', 'Vanilla', 'Strawberry'))
else:
    raise SystemExit
