# -*- coding: utf-8 -*-
# Author : Shubham Aggarwal
# Handle : shuboy2014
# Modified Date : 06-11-2016
from bs4 import BeautifulSoup


# paste complete div element having class infinite-list at line number 10
html = '''
https://github.com/shuboy2014/Whatsapp-Group-Phone-Number-Extractor/blob/master/Whatsapp-group-phone-number-extractor-3.py

'''


# which concatenate phone number string
#  [ +91 99956 96485 ] to [ +919995696845 ]
def concatenate(contact):
    contact = contact.split()
    return u"".join(contact)


def main():
    # Number of Contact in your group
    number_of_contact = 0

    # BeautifulSoup object html content as argument
    soup = BeautifulSoup(html, "html.parser")

    # for loop goes through every span in html content
    for i in soup.find_all('span'):
        # if we found span element with class attribute "emojitext ellipsify" and its title attribute on None
        if i.get('class') == ['emojitext', 'ellipsify'] and i.get("title") is not None:
            print (concatenate(i.get_text()))
            number_of_contact += 1

    print ("The Total Number of Contacts are {}".format(number_of_contact))


if __name__ == "__main__":
	main()
