from model.group import Group


def test_add_empty_group(app):
    group = Group().set_empty_parameters()
    app.group.create(group)


def test_add_handled_group(app):
    group = Group(name='any group', header='any header', footer='any footer')
    app.group.create(group)


def test_add_random_group(app):
    group = Group().set_all_parameters_to_random_value()
    app.group.create(group)
