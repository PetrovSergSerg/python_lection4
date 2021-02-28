from model.group import Group


def test_edit_any_group(app):
    if app.group.count() == 0:
        group = Group().set_all_parameters_to_random_value()
        app.group.create(group)
    old_groups = app.group.get_group_list()
    group_new_state = Group().set_random_parameters_to_random_value()

    # get id of randomly chosen group
    group_id = app.group.edit_any_group(group_new_state)

    # next(iterator, None) returns first group by condition or None if no group found
    # But we got this group_id, so group exists! And we will not get None
    # so we can get field "name" of Not None Object
    # change "name" of edited group on new_state.value
    next((group for group in old_groups if group.id == group_id), None).name = group_new_state.name

    # get new list
    new_groups = app.group.get_group_list()

    # check len of list was not changed
    assert len(new_groups) == len(old_groups)

    # check equalizing of sorted lists
    assert new_groups.sort() == old_groups.sort()
