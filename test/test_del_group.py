from model.group import Group


def test_delete_any_group(app):
    if app.group.count() == 0:
        group = Group().set_all_parameters_to_random_value()
        app.group.create(group)
    old_groups = app.group.get_group_list()
    app.group.delete_any_group()
    new_groups = app.group.get_group_list()
    # old list is longer, because we deleted 1 element
    assert len(new_groups) == len(old_groups) - 1

    # we removed random element, so knowledge the id of deleted group is the additional complexity
    # so it will be enough to make sure that all elements of NEW list are in OLD list
    assert all(elem in old_groups for elem in new_groups)
