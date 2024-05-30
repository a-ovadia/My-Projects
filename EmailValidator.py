
valid_email_list = ["@gmail.com", "@outlook.com", "@hotmail.com", "@msn.com",
                    "@yahoo.com", "@icloud.com", "@me.com", "@protonmail.com",
                    "@zoho.com", "@aol.com", "@aovadia.com", "@example.com"]

def is_email_valid(email):
    em = email.lower()
    for domain in valid_email_list:
        if domain in em: return True
    return False