from model.contact import Contact


def test_delete_any_contact_from_list(app):
    if app.contact.count() == 0:
        contact = Contact().set_all_parameters_to_random_value()
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_any_contact_form_list()

    # old list is longer, because we deleted 1 element
    assert app.contact.count() == len(old_contacts) - 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_contacts = app.contact.get_contact_list()

    # we removed random element, so knowledge the id of deleted group is the additional complexity
    # so it will be enough to make sure that all elements of NEW list are in OLD list
    assert all(elem in old_contacts for elem in new_contacts)


def test_delete_any_contact_from_itself(app):
    if app.contact.count() == 0:
        contact = Contact().set_all_parameters_to_random_value()
        app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_any_contact_from_itself()

    # old list is longer, because we deleted 1 element
    assert app.contact.count() == len(old_contacts) - 1

    # if new list length is correct, then we can compare lists.
    # so we can get new list
    new_contacts = app.contact.get_contact_list()

    # we removed random element, so knowledge the id of deleted group is the additional complexity
    # so it will be enough to make sure that all elements of NEW list are in OLD list
    assert all(elem in old_contacts for elem in new_contacts)





