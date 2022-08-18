from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
]
dl = [('Read', 1), ('Martin', 7), ('Luther', 7), ('King', 7), ('Jrs', 3), ('I', 15), ('Have', 3), ('a', 43),
      ('Dream', 1), ('speech', 4), ('in', 23), ('its', 4), ('entirety', 1), ('Updated', 1), ('January', 1), ('14', 1),
      ('2022153', 1), ('PM', 1), ('ET', 1), ('Heard', 1), ('on', 17), ('Talk', 2), ('of', 105), ('the', 116),
      ('Nation', 2), ('17Minute', 1), ('Listen', 1), ('Download', 1), ('Transcript', 1), ('Civil', 2), ('rights', 6),
      ('leader', 1), ('Jr', 4), ('addresses', 1), ('crowd', 1), ('at', 8), ('Lincoln', 4), ('Memorial', 4),
      ('Washington', 8), ('DC', 1), ('where', 4), ('he', 2), ('gave', 1), ('his', 6), ('"I', 2), ('Dream"', 2),
      ('Aug', 4), ('28', 4), ('1963', 6), ('as', 20), ('part', 1), ('March', 5), ('AFP', 1), ('via', 3), ('Getty', 4),
      ('Images', 4), ('Monday', 1), ('marks', 1), ('birthday', 1), ('Below', 1), ('is', 24), ('transcript', 1),
      ('celebrated', 1), ('delivered', 1), ('steps', 1), ('NPRs', 1), ('aired', 1), ('2010', 1), ('', 3), ('listen', 1),
      ('to', 61), ('that', 25), ('broadcast', 1), ('audio', 1), ('link', 1), ('above', 1), ('and', 43), ('other', 1),
      ('civil', 2), ('leaders', 1), ('gather', 1), ('before', 1), ('rally', 1), ('National', 1), ('Archives', 1),
      ('Hulton', 2), ('Archive', 2), ('Rev', 1), ('Five', 1), ('score', 1), ('years', 5), ('ago', 1), ('great', 5),
      ('American', 4), ('whose', 1), ('symbolic', 1), ('shadow', 1), ('we', 18), ('stand', 3), ('today', 8),
      ('signed', 1), ('Emancipation', 1), ('Proclamation', 1), ('This', 7), ('momentous', 1), ('decree', 1),
      ('came', 2), ('beacon', 1), ('light', 1), ('hope', 4), ('millions', 1), ('Negro', 13), ('slaves', 2), ('who', 4),
      ('had', 1), ('been', 2), ('seared', 1), ('flames', 1), ('withering', 1), ('injustice', 3), ('It', 4),
      ('joyous', 1), ('daybreak', 1), ('end', 2), ('long', 6), ('night', 1), ('their', 8), ('captivity', 1), ('But', 4),
      ('100', 1), ('later', 4), ('still', 4), ('not', 13), ('free', 3), ('One', 3), ('hundred', 3), ('life', 2),
      ('sadly', 1), ('crippled', 1), ('by', 8), ('manacles', 1), ('segregation', 2), ('chains', 1),
      ('discrimination', 1), ('lives', 1), ('lonely', 1), ('island', 1), ('poverty', 1), ('midst', 1), ('vast', 1),
      ('ocean', 1), ('material', 1), ('prosperity', 1), ('languished', 1), ('corners', 1), ('society', 1), ('finds', 1),
      ('himself', 1), ('exile', 1), ('own', 1), ('land', 3), ('And', 9), ('so', 3), ('weve', 3), ('come', 10),
      ('here', 3), ('dramatize', 1), ('shameful', 1), ('condition', 1), ('In', 2), ('sense', 1), ('our', 16),
      ('nations', 1), ('capital', 1), ('cash', 2), ('check', 5), ('The', 8), ('Power', 2), ('Of', 2), ('Anger', 2),
      ('CODE', 2), ('SWITCH', 2), ('When', 1), ('architects', 1), ('republic', 1), ('wrote', 1), ('magnificent', 1),
      ('words', 3), ('Constitution', 1), ('Declaration', 1), ('Independence', 1), ('they', 3), ('were', 1),
      ('signing', 1), ('promissory', 2), ('note', 3), ('which', 5), ('every', 10), ('was', 2), ('fall', 1), ('heir', 1),
      ('promise', 1), ('all', 7), ('men', 6), ('yes', 1), ('Black', 4), ('well', 1), ('white', 6), ('would', 2),
      ('be', 32), ('guaranteed', 1), ('unalienable', 1), ('liberty', 2), ('pursuit', 1), ('happiness', 1),
      ('obvious', 1), ('America', 5), ('has', 5), ('defaulted', 1), ('this', 11), ('insofar', 1), ('her', 1),
      ('citizens', 1), ('color', 2), ('are', 8), ('concerned', 1), ('Instead', 1), ('honoring', 1), ('sacred', 1),
      ('obligation', 1), ('given', 1), ('people', 3), ('bad', 1), ('back', 9), ('marked', 1), ('insufficient', 2),
      ('funds', 2), ('refuse', 2), ('believe', 2), ('bank', 1), ('justice', 8), ('bankrupt', 1), ('We', 12),
      ('there', 3), ('vaults', 1), ('opportunity', 1), ('nation', 9), ('will', 25), ('give', 1), ('us', 4), ('upon', 1),
      ('demand', 1), ('riches', 1), ('freedom', 20), ('security', 1), ('have', 17), ('also', 1), ('hallowed', 1),
      ('spot', 1), ('remind', 1), ('fierce', 1), ('urgency', 2), ('now', 2), ('time', 5), ('engage', 1), ('luxury', 1),
      ('cooling', 1), ('off', 2), ('or', 1), ('take', 1), ('tranquilizing', 1), ('drug', 1), ('gradualism', 1),
      ('protesters', 1), ('march', 2), ('from', 18), ('Monument', 1), ('for', 10), ('Kurt', 1), ('Severin', 1),
      ('Three', 1), ('Lions', 1), ('Now', 4), ('make', 3), ('real', 1), ('promises', 1), ('democracy', 1), ('rise', 3),
      ('dark', 1), ('desolate', 1), ('valley', 3), ('sunlit', 1), ('path', 1), ('racial', 2), ('lift', 1), ('quick', 1),
      ('sands', 1), ('solid', 1), ('rock', 1), ('brotherhood', 3), ('reality', 1), ('Gods', 3), ('children', 5),
      ('fatal', 1), ('overlook', 1), ('moment', 1), ('sweltering', 3), ('summer', 1), ('Negros', 2), ('legitimate', 1),
      ('discontent', 1), ('pass', 1), ('until', 4), ('an', 3), ('invigorating', 1), ('autumn', 1), ('equality', 1),
      ('but', 2), ('beginning', 1), ('Those', 1), ('needed', 1), ('blow', 1), ('steam', 1), ('content', 2), ('rude', 1),
      ('awakening', 1), ('if', 2), ('returns', 1), ('business', 1), ('usual', 1), ('There', 2), ('neither', 1),
      ('rest', 1), ('nor', 1), ('tranquility', 1), ('granted', 1), ('citizenship', 1), ('whirlwinds', 1), ('revolt', 1),
      ('continue', 1), ('shake', 1), ('foundations', 1), ('bright', 1), ('day', 11), ('emerges', 1), ('something', 1),
      ('must', 8), ('say', 2), ('my', 4), ('warm', 1), ('threshold', 1), ('leads', 1), ('into', 4), ('palace', 1),
      ('process', 1), ('gaining', 1), ('rightful', 1), ('place', 1), ('guilty', 1), ('wrongful', 1), ('deeds', 1),
      ('Let', 8), ('seek', 1), ('satisfy', 1), ('thirst', 1), ('drinking', 1), ('cup', 1), ('bitterness', 1),
      ('hatred', 1), ('Bayard', 2), ('Rustin', 2), ('Man', 2), ('Behind', 2), ('(2021)', 2), ('THROUGHLINE', 1),
      ('forever', 1), ('conduct', 1), ('struggle', 2), ('high', 1), ('plane', 1), ('dignity', 2), ('discipline', 1),
      ('allow', 2), ('creative', 2), ('protest', 1), ('degenerate', 1), ('physical', 2), ('violence', 1), ('Again', 1),
      ('again', 1), ('majestic', 1), ('heights', 1), ('meeting', 1), ('force', 2), ('with', 12), ('soul', 1),
      ('marvelous', 1), ('new', 2), ('militancy', 1), ('engulfed', 1), ('community', 1), ('lead', 1), ('distrust', 1),
      ('many', 1), ('brothers', 2), ('evidenced', 1), ('presence', 1), ('realize', 2), ('destiny', 2), ('tied', 1),
      ('up', 4), ('inextricably', 1), ('bound', 1), ('cannot', 6), ('walk', 2), ('alone', 1), ('pledge', 1),
      ('shall', 5), ('always', 1), ('ahead', 1), ('turn', 1), ('those', 1), ('asking', 1), ('devotees', 1), ('when', 6),
      ('you', 6), ('satisfied', 8), ('can', 4), ('never', 3), ('victim', 1), ('unspeakable', 1), ('horrors', 1),
      ('police', 2), ('brutality', 2), ('bodies', 1), ('heavy', 1), ('fatigue', 1), ('travel', 1), ('gain', 1),
      ('lodging', 1), ('motels', 1), ('highways', 1), ('hotels', 1), ('cities', 2), ('basic', 1), ('mobility', 1),
      ('smaller', 1), ('ghetto', 1), ('larger', 1), ('one', 9), ('stripped', 1), ('selfhood', 1), ('robbed', 1),
      ('signs', 1), ('stating', 1), ('whites', 1), ('only', 2), ('Mississippi', 4), ('vote', 2), ('New', 3),
      ('York', 2), ('believes', 1), ('nothing', 1), ('No', 1), ('rolls', 1), ('down', 4), ('like', 2), ('waters', 1),
      ('righteousness', 1), ('mighty', 2), ('stream', 1), ('How', 4), ('Voting', 2), ('Rights', 2), ('Act', 2),
      ('Came', 2), ('To', 2), ('Be', 2), ('Its', 2), ('Changed', 2), ('POLITICS', 1), ('unmindful', 1), ('some', 1),
      ('out', 3), ('trials', 1), ('tribulations', 1), ('Some', 2), ('fresh', 1), ('narrow', 1), ('jail', 2),
      ('cells', 1), ('areas', 1), ('your', 1), ('quest', 1), ('left', 1), ('battered', 1), ('storms', 1),
      ('persecution', 1), ('staggered', 1), ('winds', 1), ('You', 1), ('veterans', 1), ('suffering', 2),
      ('Continue', 1), ('work', 2), ('faith', 5), ('unearned', 1), ('redemptive', 1), ('Go', 1), ('go', 7),
      ('Alabama', 3), ('South', 2), ('Carolina', 1), ('Georgia', 3), ('Louisiana', 1), ('slums', 1), ('ghettos', 1),
      ('Northern', 1), ('knowing', 2), ('somehow', 1), ('situation', 1), ('changed', 1), ('wallow', 1), ('despair', 2),
      ('friends', 1), ('So', 1), ('even', 2), ('though', 1), ('face', 1), ('difficulties', 1), ('tomorrow', 1),
      ('dream', 11), ('deeply', 1), ('rooted', 1), ('live', 2), ('true', 2), ('meaning', 2), ('creed', 1), ('hold', 1),
      ('these', 1), ('truths', 1), ('selfevident', 1), ('created', 1), ('equal', 1), ('People', 1), ('clap', 1),
      ('sing', 4), ('along', 1), ('song', 1), ('between', 1), ('speeches', 1), ('Jobs', 1), ('Freedom', 1),
      ('Express', 1), ('Newspapers', 1), ('red', 1), ('hills', 1), ('sons', 2), ('former', 2), ('slave', 1),
      ('owners', 1), ('able', 8), ('sit', 1), ('together', 7), ('table', 1), ('state', 3), ('heat', 2),
      ('oppression', 1), ('transformed', 1), ('oasis', 1), ('four', 1), ('little', 3), ('judged', 1), ('skin', 1),
      ('character', 1), ('vicious', 1), ('racists', 1), ('governor', 1), ('having', 1), ('lips', 1), ('dripping', 1),
      ('interposition', 1), ('nullification', 1), ('right', 1), ('boys', 2), ('girls', 2), ('join', 2), ('hands', 2),
      ('sisters', 1), ('exalted', 1), ('hill', 2), ('mountain', 2), ('made', 3), ('low', 1), ('rough', 1),
      ('places', 2), ('plain', 1), ('crooked', 1), ('straight', 1), ('glory', 1), ('Lord', 1), ('revealed', 1),
      ('flesh', 1), ('see', 1), ('it', 2), ('Nikole', 1), ('HannahJones', 1), ('power', 1), ('collective', 1),
      ('memory', 1), ('With', 3), ('hew', 1), ('stone', 1), ('transform', 1), ('jangling', 1), ('discords', 1),
      ('beautiful', 1), ('symphony', 1), ('pray', 1), ('My', 1), ('country', 1), ('tis', 1), ('thee', 2), ('sweet', 1),
      ('Land', 1), ('fathers', 1), ('died', 1), ('pilgrims', 1), ('pride', 1), ('mountainside', 2), ('let', 5),
      ('ring', 12), ('become', 1), ('prodigious', 1), ('hilltops', 1), ('Hampshire', 1), ('mountains', 1),
      ('heightening', 1), ('Alleghenies', 1), ('Pennsylvania', 1), ('snowcapped', 1), ('Rockies', 1), ('Colorado', 1),
      ('curvaceous', 1), ('slopes', 1), ('California', 1), ('Stone', 1), ('Mountain', 2), ('Lookout', 1),
      ('Tennessee', 1), ('molehill', 1), ('From', 1), ('happens', 1), ('village', 1), ('hamlet', 1), ('city', 1),
      ('speed', 1), ('Jews', 1), ('Gentiles', 1), ('Protestants', 1), ('Catholics', 1), ('old', 1), ('spiritual', 1),
      ('Free', 2), ('last', 3), ('Thank', 1), ('God', 1), ('almighty', 1)]

# c = (
#     WordCloud()
#     .add("", dl, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
#     .set_global_opts(title_opts=opts.TitleOpts(title="demo"))
#     .render("demo.html")
# )


def aiycwordcloud(words=words, filename="wordcloud_diamond.html", title="WordCloud-shape-diamond"):
    c = (
        WordCloud()
        .add("", words, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title=title))
        .render(filename)
    )
# wordcloud(words, filename="demo10.html")
import os
# os.startfile("wordcloud_diamond.html")
# print()
#
# import webbrowser
# webbrowser.open("wordcloud_diamond.html")
