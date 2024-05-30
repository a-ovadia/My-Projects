import PhoneNumberValidator as p_validator
import EmailValidator as e_validator
contacts = {}


def add_contacts(name, p_number=None, email=None):
    for entry in name:
        if p_validator.validate_p_number(p_number) and e_validator.is_email_valid(email):
            contacts[name.title()] = [p_validator.convert_string_p_name(p_number), email.lower()]
        else: print("Error! Ypu entered an invalid Phone number or Email Address. Please correct the errors and try again")


def search_contacts(s_name):
    search_results = []
    for name in contacts.keys():
        if s_name.title() in name:
            search_results.append((name, contacts[name]))
    if len(search_results) < 1: print("No contacts come up for: {}".format(s_name))
    return search_results


def isExactMatch(name):
    return name.title() in contacts


def update_contact(name, new_p_number=False, new_email=False):
     # Phone validation
    if not p_validator.validate_p_number(new_p_number): return "You have entered an invalid phone number"
    # Format Phone number properly
    new_p_number = p_validator.convert_string_p_name(new_p_number)
    if new_email:
        if not e_validator.is_email_valid(new_email): return  "You have entered an invalid email address. Please try updating the contact with a valid email address"


    if isExactMatch(name):
        name = name.title()
        if new_p_number and new_email:
            contacts[name] = [new_p_number, new_email]
        elif new_p_number:
            contacts[name] = [p_validator.convert_string_p_name(new_p_number), contacts[name][1]]
        else:
            contacts[name] = [contacts[name][0], new_email]
    else:
        print("You did not add a valid contact. Please check your spelling and try again")


def delete_contact(name):
    if isExactMatch(name):
        contacts.pop(name.title())
    else:
        print("Error: You tried to delete a contact that does not exist.")


# Add Contacts (Positive and Negative Tests)
add_contacts("Alice Johnson", "555-123-4567", "alice@example.com")
add_contacts("Bob Smith", "212-555-1212", "bob@example.com")
add_contacts("John Doe-Hyphen", "5551234567", "johndoe@example.com")
add_contacts("123 Test Name", "555-555-5555", "123test@example.com")
add_contacts("Name With Unicode", "555-555-5555", "unicode@example.com")

# Add Contacts (Negative Tests - Invalid Input)
# add_contacts("Alice Johnson", "555-123-456", "alice@example.com")  # Invalid phone
# add_contacts("Invalid Email", "555-123-4567", "invalidemail")      # Invalid email

# Search Contacts
search_results = search_contacts("ali")
print(search_results)
search_results = search_contacts("smi")
print(search_results)
search_results = search_contacts("nonexistent")
print(search_results)

# Update Contact (Positive and Negative Tests)
update_contact("Bob Smith", "5551231234")  # Update phone only
update_contact("Bob Smith", new_email="newemailforbob@example.com")  # Update email only
update_contact("Nonexistent Name", "555-1212-1212", "nonexistent@email.com")  # Update non-existent contact
update_contact("Alice Johnson", "invalidphone", "newalice@example.com") # Invalid phone

# Delete Contact
#delete_contact("Alice Johnson")

# Final Contacts
print(contacts)