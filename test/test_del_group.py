from model.group import Group


def test_delete_any_group(app):
    if app.group.count() == 0:
        group = Group().set_all_parameters_to_random_value()
        app.group.create(group)
    app.group.delete_any_group()
