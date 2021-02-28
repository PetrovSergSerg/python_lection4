from model.contact import Contact


def test_edit_any_contact_from_list_to_random_parameters(app):
    if app.contact.count() == 0:
        contact = Contact(lastname='first', firstname='contact')
        app.contact.create(contact)
    contact_new_state = Contact().set_random_parameters_to_random_value()
    app.contact.edit_any_contact(contact_new_state)


def test_edit_any_contact_from_list_to_handled_parameters(app):
    if app.contact.count() == 0:
        contact = Contact(lastname='first', firstname='contact')
        app.contact.create(contact)
    contact_new_state = Contact(lastname='lastname', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                                company='lll', address='mmm', phone_home='111', mobile='222', phone_work='333',
                                fax='444', email_main='a@a.ru', email_secondary='b@b.ru', email_other='c@c.ru',
                                homepage='http://', byear='1994', bmonth='April', bday='15', ayear='2003',
                                amonth='September', aday='4', address_secondary='xxx', phone_secondary='777',
                                notes='zzz')
    app.contact.edit_any_contact(contact_new_state)
