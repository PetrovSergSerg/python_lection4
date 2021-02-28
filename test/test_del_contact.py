from model.contact import Contact


def test_delete_any_contact_from_list(app):
    if app.contact.count() == 0:
        contact = Contact(lastname='first', firstname='contact')
        app.contact.create(contact)
    app.contact.delete_any_contact_form_list()


def test_delete_any_contact_from_itself(app):
    if app.contact.count() == 0:
        contact = Contact(lastname='first', firstname='contact')
        app.contact.create(contact)
    app.contact.delete_any_contact_from_itself()





