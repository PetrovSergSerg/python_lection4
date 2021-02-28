from selenium.webdriver.support.ui import Select
from model.contact import Contact
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint


class ContactHelper:
    def __init__(self, app):
        self.app = app
        self.menu = app.menu

    def create(self, contact: Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        self.fill_contact(contact)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

        self.menu.home()

    def edit_any_contact(self, contact: Contact):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit = edit_list[randint(0, len(edit_list) - 1)]
        edit.click()

        self.fill_contact(contact)

        update = wd.find_element_by_xpath("//input[@type='submit'][@value='Update']")
        update.click()

        self.menu.home()

    def fill_contact(self, contact):
        self.type_in_field("firstname", contact.firstname)
        self.type_in_field("middlename", contact.middlename)
        self.type_in_field("lastname", contact.lastname)
        self.type_in_field("nickname", contact.nickname)

        self.type_in_field("title", contact.title)
        self.type_in_field("company", contact.company)
        self.type_in_field("address", contact.address)

        self.type_in_field("home", contact.phone_home)
        self.type_in_field("mobile", contact.mobile)
        self.type_in_field("work", contact.phone_work)
        self.type_in_field("fax", contact.fax)

        self.type_in_field("email", contact.email_main)
        self.type_in_field("email2", contact.email_secondary)
        self.type_in_field("email3", contact.email_other)
        self.type_in_field("homepage", contact.homepage)

        self.select_in_field("bday", contact.bday)
        self.select_in_field("bmonth", contact.bmonth)
        self.type_in_field("byear", contact.byear)

        self.select_in_field("aday", contact.aday)
        self.select_in_field("amonth", contact.amonth)
        self.type_in_field("ayear", contact.ayear)

        self.type_in_field("address2", contact.address_secondary)
        self.type_in_field("phone2", contact.phone_secondary)
        self.type_in_field("notes", contact.notes)

    def type_in_field(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def select_in_field(self, selector_name, value):
        wd = self.app.wd
        if value is not None:
            selector = Select(wd.find_element_by_name(selector_name))
            selector.select_by_visible_text(value)

    def delete_any_contact_from_itself(self):
        wd = self.app.wd
        self.menu.home()

        edit_list = wd.find_elements_by_xpath("//img[@title='Edit']")
        assert len(edit_list) > 0

        edit = edit_list[randint(0, len(edit_list) - 1)]
        edit.click()

        delete = wd.find_element_by_xpath("//input[@type='submit'][@value='Delete']")
        delete.click()

        self.menu.home()

    def delete_any_contact_form_list(self):
        wd = self.app.wd
        self.menu.home()

        checkbox_list = wd.find_elements_by_name("selected[]")
        assert len(checkbox_list) > 0

        checkbox_last = checkbox_list[len(checkbox_list) - 1]
        checkbox_last.click()

        delete = wd.find_element_by_xpath("//input[@type='button'][@value='Delete']")
        delete.click()

        try:
            WebDriverWait(wd, 1).until(EC.alert_is_present(), 'Не дождались алёрта')
            alert = wd.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert")
        finally:
            self.menu.home()

    def count(self):
        wd = self.app.wd
        self.menu.home()

        return len(wd.find_elements_by_name("selected[]"))