# -*- coding: utf-8 -*-
# Author : Shubham Aggarwal
# Handle : shuboy2014
# Modified Date : 06-11-2016
from bs4 import BeautifulSoup


# paste complete div element having class infinite-list at line number 10
html = '''
<span title="P135, P136, P137, P138, P139, P140, P141, P142, P143, P144, +91&nbsp;73552&nbsp;04797, +91&nbsp;75088&nbsp;22552, +91&nbsp;76984&nbsp;68406, +91&nbsp;77383&nbsp;17152, +91&nbsp;77588&nbsp;48138, +91&nbsp;77789&nbsp;16712, +91&nbsp;78307&nbsp;13505, +91&nbsp;78439&nbsp;19619, +91&nbsp;78804&nbsp;49468, +91&nbsp;79841&nbsp;13924, +91&nbsp;81080&nbsp;63002, +91&nbsp;81092&nbsp;44485, +91&nbsp;82373&nbsp;33366, +91&nbsp;82669&nbsp;88184, +91&nbsp;83086&nbsp;12812, +91&nbsp;83181&nbsp;80474, +91&nbsp;83687&nbsp;63233, +91&nbsp;84462&nbsp;78974, +91&nbsp;85120&nbsp;97771, +91&nbsp;86375&nbsp;97508, +91&nbsp;86848&nbsp;58048, +91&nbsp;86928&nbsp;50849, +91&nbsp;87359&nbsp;77356, +91&nbsp;87507&nbsp;71670, +91&nbsp;88665&nbsp;16716, +91&nbsp;89593&nbsp;06068, +91&nbsp;89892&nbsp;17784, +91&nbsp;90047&nbsp;12680, +91&nbsp;90133&nbsp;66622, +91&nbsp;90285&nbsp;46757, +91&nbsp;90294&nbsp;38229, +91&nbsp;90352&nbsp;38731, +91&nbsp;91302&nbsp;49264, +91&nbsp;91588&nbsp;33575, +91&nbsp;92157&nbsp;55700, +91&nbsp;92559&nbsp;58640, +91&nbsp;93122&nbsp;12855, +91&nbsp;93500&nbsp;95757, +91&nbsp;94228&nbsp;06084, +91&nbsp;94466&nbsp;30689, +91&nbsp;94625&nbsp;51487, +91&nbsp;95385&nbsp;10284, +91&nbsp;95586&nbsp;98011, +91&nbsp;95598&nbsp;48484, +91&nbsp;95604&nbsp;81788, +91&nbsp;96205&nbsp;60409, +91&nbsp;96334&nbsp;84851, +91&nbsp;96508&nbsp;01823, +91&nbsp;96543&nbsp;44674, +91&nbsp;96600&nbsp;89992, +91&nbsp;96637&nbsp;66958, +91&nbsp;96767&nbsp;66143, +91&nbsp;97130&nbsp;16366, +91&nbsp;97377&nbsp;92747, +91&nbsp;97528&nbsp;36398, +91&nbsp;97563&nbsp;31515, +91&nbsp;97600&nbsp;77899, +91&nbsp;97683&nbsp;10775, +91&nbsp;97827&nbsp;16988, +91&nbsp;98066&nbsp;69565, +91&nbsp;98107&nbsp;26496, +91&nbsp;98114&nbsp;40787, +91&nbsp;98181&nbsp;47755, +91&nbsp;98265&nbsp;38067, +91&nbsp;98338&nbsp;84271, +91&nbsp;98403&nbsp;26547, +91&nbsp;98500&nbsp;95131, +91&nbsp;98791&nbsp;09298, +91&nbsp;98845&nbsp;08818, +91&nbsp;99011&nbsp;16401, +91&nbsp;99101&nbsp;15656, +91&nbsp;99288&nbsp;50458, +91&nbsp;99310&nbsp;22246, +91&nbsp;99403&nbsp;71764, +91&nbsp;99493&nbsp;47810, +91&nbsp;99535&nbsp;73910, +91&nbsp;99585&nbsp;63424, +91&nbsp;99786&nbsp;11237, +91&nbsp;99787&nbsp;65414, +91&nbsp;99915&nbsp;29000, +91&nbsp;99971&nbsp;11354, +91&nbsp;99992&nbsp;09908, +92&nbsp;300&nbsp;0236069, +92&nbsp;308&nbsp;6944069, +92&nbsp;333&nbsp;6987097, +92&nbsp;336&nbsp;3891351, +971&nbsp;55&nbsp;876&nbsp;0041, +974&nbsp;6612&nbsp;9773, You" class="O90ur">P135, P136, P137, P138, P139, P140, P141, P142, P143, P144, +91&nbsp;73552&nbsp;04797, +91&nbsp;75088&nbsp;22552, +91&nbsp;76984&nbsp;68406, +91&nbsp;77383&nbsp;17152, +91&nbsp;77588&nbsp;48138, +91&nbsp;77789&nbsp;16712, +91&nbsp;78307&nbsp;13505, +91&nbsp;78439&nbsp;19619, +91&nbsp;78804&nbsp;49468, +91&nbsp;79841&nbsp;13924, +91&nbsp;81080&nbsp;63002, +91&nbsp;81092&nbsp;44485, +91&nbsp;82373&nbsp;33366, +91&nbsp;82669&nbsp;88184, +91&nbsp;83086&nbsp;12812, +91&nbsp;83181&nbsp;80474, +91&nbsp;83687&nbsp;63233, +91&nbsp;84462&nbsp;78974, +91&nbsp;85120&nbsp;97771, +91&nbsp;86375&nbsp;97508, +91&nbsp;86848&nbsp;58048, +91&nbsp;86928&nbsp;50849, +91&nbsp;87359&nbsp;77356, +91&nbsp;87507&nbsp;71670, +91&nbsp;88665&nbsp;16716, +91&nbsp;89593&nbsp;06068, +91&nbsp;89892&nbsp;17784, +91&nbsp;90047&nbsp;12680, +91&nbsp;90133&nbsp;66622, +91&nbsp;90285&nbsp;46757, +91&nbsp;90294&nbsp;38229, +91&nbsp;90352&nbsp;38731, +91&nbsp;91302&nbsp;49264, +91&nbsp;91588&nbsp;33575, +91&nbsp;92157&nbsp;55700, +91&nbsp;92559&nbsp;58640, +91&nbsp;93122&nbsp;12855, +91&nbsp;93500&nbsp;95757, +91&nbsp;94228&nbsp;06084, +91&nbsp;94466&nbsp;30689, +91&nbsp;94625&nbsp;51487, +91&nbsp;95385&nbsp;10284, +91&nbsp;95586&nbsp;98011, +91&nbsp;95598&nbsp;48484, +91&nbsp;95604&nbsp;81788, +91&nbsp;96205&nbsp;60409, +91&nbsp;96334&nbsp;84851, +91&nbsp;96508&nbsp;01823, +91&nbsp;96543&nbsp;44674, +91&nbsp;96600&nbsp;89992, +91&nbsp;96637&nbsp;66958, +91&nbsp;96767&nbsp;66143, +91&nbsp;97130&nbsp;16366, +91&nbsp;97377&nbsp;92747, +91&nbsp;97528&nbsp;36398, +91&nbsp;97563&nbsp;31515, +91&nbsp;97600&nbsp;77899, +91&nbsp;97683&nbsp;10775, +91&nbsp;97827&nbsp;16988, +91&nbsp;98066&nbsp;69565, +91&nbsp;98107&nbsp;26496, +91&nbsp;98114&nbsp;40787, +91&nbsp;98181&nbsp;47755, +91&nbsp;98265&nbsp;38067, +91&nbsp;98338&nbsp;84271, +91&nbsp;98403&nbsp;26547, +91&nbsp;98500&nbsp;95131, +91&nbsp;98791&nbsp;09298, +91&nbsp;98845&nbsp;08818, +91&nbsp;99011&nbsp;16401, +91&nbsp;99101&nbsp;15656, +91&nbsp;99288&nbsp;50458, +91&nbsp;99310&nbsp;22246, +91&nbsp;99403&nbsp;71764, +91&nbsp;99493&nbsp;47810, +91&nbsp;99535&nbsp;73910, +91&nbsp;99585&nbsp;63424, +91&nbsp;99786&nbsp;11237, +91&nbsp;99787&nbsp;65414, +91&nbsp;99915&nbsp;29000, +91&nbsp;99971&nbsp;11354, +91&nbsp;99992&nbsp;09908, +92&nbsp;300&nbsp;0236069, +92&nbsp;308&nbsp;6944069, +92&nbsp;333&nbsp;6987097, +92&nbsp;336&nbsp;3891351, +971&nbsp;55&nbsp;876&nbsp;0041, +974&nbsp;6612&nbsp;9773, You</span>
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
    soup = BeautifulSoup(html, "lxml")

    # for loop goes through every span in html content
    for i in soup.find_all('span'):
        # if we found span element with class attribute "emojitext ellipsify" and its title attribute on None
        if i.get('class') == ['emojitext', 'ellipsify'] and i.get("title") is not None:
            print concatenate(i.get_text())
            number_of_contact += 1

    print "The Total Number of Contacts are %s" % (number_of_contact,)


if __name__ == "__main__":
    main()
