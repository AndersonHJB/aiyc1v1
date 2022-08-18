# d = {'Read': 1, 'Martin': 7, 'Luther': 7, 'King': 7, 'Jrs': 3, 'I': 15, 'Have': 3, 'a': 43, 'Dream': 1}
# no_have_words = [
#     "no", "am", "Martin",
#     "Luther", "jrs"
# ]
# for nh in no_have_words:
#     if nh in d:
#         del d[nh]
#     else:
#         pass
# print(d)
# import subprocess
#
# # in case chrome browser
# subprocess.run(["Chrome", "wordcloud_diamond.html"])
# import webbrowser
# import os
#
# r = os.getcwd() + "/wordcloud_diamond.html"  # /Users/huangjiabao/GitHub/python-library/aiycsnlp/tests
# # print('file:///' + r)
# webbrowser.open('file:///' + r)
# # print(r)
# import urllib.request
# passer = "abcdef"
# passwd_attempt = input("Type in the password please: ")
#
# if passwd_attempt == passer:
#     page = urllib.request.urlopen('wordcloud_diamond.html')
#     text = page.read().decode("utf8")
#     print(text)
# else:
#     print("Wrong password. Please try again.")
