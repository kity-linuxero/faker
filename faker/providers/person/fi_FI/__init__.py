# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider
from collections import OrderedDict


class Provider(PersonProvider):

    formats_female = (
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
    )

    formats_male = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
    )

    formats = formats_female + formats_male

    prefixes = (
        'Herra', 'hra', 'Rouva', 'rva', 'Tohtori', 'tri', 'prof.', 'arkkit.'
    )

    suffixes = ('DI', 'PhD', 'MSc', 'BSc')

    # List of most popular given names in Finland: https://www.avoindata.fi/data/en/dataset/none/resource/d35f8973-53da-4b66-8a49-bc2fee1a2996
    first_names_female = OrderedDict((
        ('Aada', 0.001877),
        ('Aila', 0.002778),
        ('Aili', 0.001542),
        ('Aino', 0.00803),
        ('Airi', 0.001591),
        ('Aleksandra', 0.002884),
        ('Alexandra', 0.002718),
        ('Alina', 0.002114),
        ('Alisa', 0.001607),
        ('Amanda', 0.004584),
        ('Anita', 0.005061),
        ('Anja', 0.005627),
        ('Anna', 0.010413),
        ('Anna-Liisa', 0.00232),
        ('Anne', 0.007823),
        ('Anneli', 0.0277),
        ('Anni', 0.004397),
        ('Anniina', 0.003366),
        ('Annika', 0.005193),
        ('Annikki', 0.013414),
        ('Annukka', 0.001424),
        ('Anu', 0.003005),
        ('Arja', 0.004539),
        ('Aulikki', 0.002522),
        ('Aune', 0.00208),
        ('Aurora', 0.003709),
        ('Birgitta', 0.003324),
        ('Carita', 0.001574),
        ('Christina', 0.001534),
        ('Eeva', 0.006403),
        ('Eija', 0.00491),
        ('Eila', 0.005377),
        ('Eliisa', 0.00163),
        ('Elina', 0.014353),
        ('Elisa', 0.00424),
        ('Elisabet', 0.005925),
        ('Elisabeth', 0.004305),
        ('Ella', 0.002958),
        ('Ellen', 0.002243),
        ('Elli', 0.002258),
        ('Elsa', 0.002284),
        ('Emilia', 0.014649),
        ('Emma', 0.003571),
        ('Emmi', 0.002183),
        ('Erika', 0.002084),
        ('Essi', 0.001576),
        ('Esteri', 0.001672),
        ('Eveliina', 0.005899),
        ('Hanna', 0.005409),
        ('Hannele', 0.0193),
        ('Heidi', 0.005315),
        ('Helena', 0.028118),
        ('Heli', 0.003711),
        ('Helinä', 0.002151),
        ('Hellevi', 0.002416),
        ('Helmi', 0.003888),
        ('Helvi', 0.001462),
        ('Henna', 0.002525),
        ('Hilkka', 0.003745),
        ('Hillevi', 0.001577),
        ('Ida', 0.003067),
        ('Iida', 0.003699),
        ('Iiris', 0.001461),
        ('Ilona', 0.004816),
        ('Inkeri', 0.009444),
        ('Irene', 0.005164),
        ('Irja', 0.002691),
        ('Irma', 0.002772),
        ('Irmeli', 0.006537),
        ('Jaana', 0.005125),
        ('Jasmin', 0.001789),
        ('Jenna', 0.002567),
        ('Jenni', 0.004011),
        ('Johanna', 0.025061),
        ('Jonna', 0.002053),
        ('Josefiina', 0.001757),
        ('Julia', 0.004716),
        ('Juulia', 0.001411),
        ('Kaarina', 0.022441),
        ('Kaija', 0.003216),
        ('Kaisa', 0.004424),
        ('Karoliina', 0.006727),
        ('Katariina', 0.010602),
        ('Kati', 0.002463),
        ('Katja', 0.00381),
        ('Katri', 0.00337),
        ('Katriina', 0.004651),
        ('Kerttu', 0.002839),
        ('Kirsi', 0.004856),
        ('Kirsti', 0.003699),
        ('Krista', 0.001465),
        ('Kristiina', 0.016656),
        ('Kristina', 0.002653),
        ('Kyllikki', 0.008537),
        ('Laura', 0.005985),
        ('Lea', 0.002827),
        ('Leena', 0.011052),
        ('Leila', 0.00267),
        ('Liisa', 0.015791),
        ('Lilja', 0.001584),
        ('Linda', 0.001706),
        ('Linnea', 0.004089),
        ('Lotta', 0.002416),
        ('Maaria', 0.00335),
        ('Maarit', 0.012853),
        ('Maija', 0.00721),
        ('Maire', 0.001814),
        ('Margareta', 0.002525),
        ('Margit', 0.002057),
        ('Mari', 0.005431),
        ('Maria', 0.044412),
        ('Marianne', 0.00481),
        ('Marika', 0.005912),
        ('Marita', 0.005339),
        ('Maritta', 0.002299),
        ('Marja', 0.010093),
        ('Marja-Leena', 0.002611),
        ('Marja-Liisa', 0.002389),
        ('Marjaana', 0.004377),
        ('Marjatta', 0.020442),
        ('Marjo', 0.002613),
        ('Marjukka', 0.001486),
        ('Marjut', 0.003021),
        ('Marketta', 0.004413),
        ('Martta', 0.001663),
        ('Matilda', 0.004284),
        ('Merja', 0.004704),
        ('Mervi', 0.002193),
        ('Mia', 0.001736),
        ('Miia', 0.002146),
        ('Milla', 0.002204),
        ('Minna', 0.006615),
        ('Mira', 0.001706),
        ('Mirja', 0.003558),
        ('Mirjam', 0.002435),
        ('Mirjami', 0.003726),
        ('Nea', 0.001605),
        ('Niina', 0.002776),
        ('Nina', 0.003539),
        ('Noora', 0.002609),
        ('Olivia', 0.00384),
        ('Oona', 0.001707),
        ('Orvokki', 0.007473),
        ('Outi', 0.002278),
        ('Päivi', 0.007556),
        ('Päivikki', 0.002189),
        ('Paula', 0.004438),
        ('Pauliina', 0.006648),
        ('Petra', 0.001455),
        ('Pia', 0.002752),
        ('Piia', 0.00155),
        ('Pirjo', 0.006778),
        ('Pirkko', 0.005904),
        ('Raija', 0.005237),
        ('Raili', 0.003592),
        ('Riikka', 0.00301),
        ('Riitta', 0.008817),
        ('Ritva', 0.007408),
        ('Roosa', 0.001641),
        ('Saara', 0.002931),
        ('Sanna', 0.005027),
        ('Sanni', 0.001827),
        ('Sara', 0.003165),
        ('Sari', 0.00656),
        ('Satu', 0.005599),
        ('Seija', 0.005422),
        ('Siiri', 0.002066),
        ('Sini', 0.002038),
        ('Sinikka', 0.010005),
        ('Sirkka', 0.004487),
        ('Sirpa', 0.005252),
        ('Sisko', 0.005153),
        ('Sofia', 0.012669),
        ('Sonja', 0.001978),
        ('Susanna', 0.012647),
        ('Suvi', 0.003093),
        ('Taina', 0.002224),
        ('Tanja', 0.002577),
        ('Tarja', 0.005886),
        ('Taru', 0.001492),
        ('Teija', 0.001634),
        ('Tellervo', 0.007298),
        ('Terhi', 0.001779),
        ('Terttu', 0.004408),
        ('Tiia', 0.002003),
        ('Tiina', 0.006154),
        ('Tuija', 0.002932),
        ('Tuula', 0.007947),
        ('Tuuli', 0.001425),
        ('Tuulia', 0.004341),
        ('Tuulikki', 0.013373),
        ('Ulla', 0.004552),
        ('Veera', 0.002453),
        ('Venla', 0.001985),
        ('Viivi', 0.001505),
        ('Vilhelmiina', 0.002004),
        ('Vilma', 0.001724),
        ('Virpi', 0.00213),
        ('Vuokko', 0.001466)
    ))
    first_names_male = OrderedDict((
        ('Aapo', 0.001263),
        ('Aarne', 0.001939),
        ('Aaro', 0.001601),
        ('Aaron', 0.001246),
        ('Aatos', 0.001552),
        ('Ahti', 0.001192),
        ('Aimo', 0.001399),
        ('Aki', 0.001881),
        ('Akseli', 0.002333),
        ('Aleksanteri', 0.002618),
        ('Aleksi', 0.008346),
        ('Alexander', 0.002728),
        ('Allan', 0.00227),
        ('Anders', 0.001411),
        ('Anssi', 0.001464),
        ('Antero', 0.029891),
        ('Anton', 0.002652),
        ('Antti', 0.011971),
        ('Ari', 0.006403),
        ('Armas', 0.003609),
        ('Arto', 0.004059),
        ('Arttu', 0.00228),
        ('Artturi', 0.001853),
        ('Arvo', 0.001578),
        ('Asko', 0.001363),
        ('Atte', 0.001392),
        ('Aukusti', 0.002011),
        ('Aulis', 0.002725),
        ('Benjamin', 0.002089),
        ('Christian', 0.002142),
        ('Daniel', 0.002919),
        ('Edvard', 0.001248),
        ('Eelis', 0.001359),
        ('Eemeli', 0.004734),
        ('Eemil', 0.002606),
        ('Eerik', 0.001629),
        ('Eero', 0.005572),
        ('Eetu', 0.003098),
        ('Einari', 0.002263),
        ('Eino', 0.004304),
        ('Elias', 0.005129),
        ('Elmeri', 0.001817),
        ('Emil', 0.003422),
        ('Ensio', 0.006508),
        ('Erik', 0.005296),
        ('Erkki', 0.007568),
        ('Esa', 0.0043),
        ('Esko', 0.004194),
        ('Hannu', 0.007429),
        ('Harri', 0.004739),
        ('Heikki', 0.011301),
        ('Henri', 0.003282),
        ('Henrik', 0.007534),
        ('Henrikki', 0.001325),
        ('Henry', 0.001412),
        ('Hermanni', 0.00167),
        ('Iisakki', 0.001193),
        ('Ilari', 0.002866),
        ('Ilkka', 0.003098),
        ('Ilmari', 0.015056),
        ('Ismo', 0.00148),
        ('Jaakko', 0.008225),
        ('Jalmari', 0.002645),
        ('Jan', 0.002011),
        ('Jani', 0.005117),
        ('Janne', 0.006361),
        ('Jari', 0.008664),
        ('Jarkko', 0.002672),
        ('Jarmo', 0.004396),
        ('Jarno', 0.001681),
        ('Jere', 0.002255),
        ('Jesse', 0.002586),
        ('Joel', 0.002105),
        ('Johan', 0.003528),
        ('Johannes', 0.028915),
        ('Joni', 0.003244),
        ('Joona', 0.002503),
        ('Joonas', 0.003828),
        ('Joonatan', 0.001565),
        ('Jorma', 0.005147),
        ('Jouko', 0.003962),
        ('Jouni', 0.004093),
        ('Juha', 0.011567),
        ('Juhana', 0.001862),
        ('Juhani', 0.061356),
        ('Juho', 0.005642),
        ('Jukka', 0.008652),
        ('Julius', 0.00209),
        ('Jussi', 0.004772),
        ('Juuso', 0.002224),
        ('Jyrki', 0.002127),
        ('Kaarlo', 0.002073),
        ('Kai', 0.001942),
        ('Kalervo', 0.008502),
        ('Kalevi', 0.021057),
        ('Kalle', 0.003829),
        ('Kari', 0.009761),
        ('Karl', 0.001779),
        ('Kasper', 0.001177),
        ('Kauko', 0.002169),
        ('Keijo', 0.002259),
        ('Kim', 0.001172),
        ('Kimmo', 0.003441),
        ('Kristian', 0.011096),
        ('Kullervo', 0.002234),
        ('Kustaa', 0.001144),
        ('Lasse', 0.002197),
        ('Lassi', 0.001214),
        ('Lauri', 0.00755),
        ('Leevi', 0.002015),
        ('Leo', 0.003319),
        ('Markku', 0.00843),
        ('Marko', 0.006297),
        ('Markus', 0.009181),
        ('Martti', 0.005521),
        ('Matias', 0.013377),
        ('Matti', 0.01756),
        ('Mauno', 0.001189),
        ('Mauri', 0.002098),
        ('Miika', 0.001845),
        ('Mika', 0.007765),
        ('Mikael', 0.021621),
        ('Mikko', 0.009719),
        ('Miro', 0.001274),
        ('Niilo', 0.002094),
        ('Niklas', 0.002024),
        ('Niko', 0.003908),
        ('Oiva', 0.001202),
        ('Olavi', 0.030903),
        ('Oliver', 0.003026),
        ('Olli', 0.003921),
        ('Onni', 0.004513),
        ('Oskar', 0.001185),
        ('Oskari', 0.007745),
        ('Osmo', 0.001531),
        ('Ossi', 0.001591),
        ('Otto', 0.002902),
        ('Paavo', 0.00381),
        ('Pasi', 0.004109),
        ('Patrik', 0.001474),
        ('Pauli', 0.003105),
        ('Pekka', 0.017016),
        ('Pentti', 0.006344),
        ('Pertti', 0.004406),
        ('Peter', 0.001704),
        ('Petri', 0.00786),
        ('Petteri', 0.015518),
        ('Raimo', 0.004575),
        ('Rainer', 0.001478),
        ('Rasmus', 0.001715),
        ('Rauno', 0.001688),
        ('Reijo', 0.003919),
        ('Reino', 0.002166),
        ('Riku', 0.001803),
        ('Risto', 0.004678),
        ('Robert', 0.001478),
        ('Roope', 0.001412),
        ('Sakari', 0.013891),
        ('Sami', 0.00587),
        ('Samu', 0.001237),
        ('Samuel', 0.00403),
        ('Samuli', 0.004994),
        ('Santeri', 0.00346),
        ('Sebastian', 0.002863),
        ('Seppo', 0.007305),
        ('Simo', 0.002313),
        ('Taisto', 0.001514),
        ('Taneli', 0.00129),
        ('Tapani', 0.02906),
        ('Tapio', 0.024776),
        ('Tauno', 0.001795),
        ('Teemu', 0.004605),
        ('Tero', 0.003188),
        ('Teuvo', 0.001714),
        ('Timo', 0.010557),
        ('Toivo', 0.003649),
        ('Tomi', 0.00341),
        ('Tommi', 0.003191),
        ('Toni', 0.003723),
        ('Topias', 0.001645),
        ('Tuomas', 0.005948),
        ('Tuomo', 0.002739),
        ('Tuukka', 0.001175),
        ('Uolevi', 0.002879),
        ('Väinö', 0.003176),
        ('Valdemar', 0.00152),
        ('Valtteri', 0.006312),
        ('Veeti', 0.001673),
        ('Veijo', 0.001517),
        ('Veikko', 0.007525),
        ('Veli', 0.004415),
        ('Verneri', 0.001164),
        ('Vesa', 0.003926),
        ('Vilhelm', 0.001591),
        ('Vilho', 0.002303),
        ('Viljami', 0.003563),
        ('Viljo', 0.00154),
        ('Ville', 0.007025),
        ('Yrjö', 0.001912)
    ))

    first_names = first_names_male.copy()
    first_names.update(first_names_female)

    # List of most popular last names in Finland: https://www.avoindata.fi/data/en/dataset/none/resource/d25831d1-82a9-476f-8f7c-374c348efc14
    last_names = OrderedDict((
        ('Aalto', 0.004189),
        ('Aaltonen', 0.004828),
        ('Aho', 0.003566),
        ('Ahokas', 0.001182),
        ('Ahola', 0.003697),
        ('Ahonen', 0.005301),
        ('Airaksinen', 0.001075),
        ('Alanen', 0.001124),
        ('Alanko', 0.001131),
        ('Alatalo', 0.001424),
        ('Andersson', 0.002447),
        ('Antikainen', 0.001061),
        ('Anttila', 0.004683),
        ('Anttonen', 0.00121),
        ('Aro', 0.00105),
        ('Asikainen', 0.002),
        ('Autio', 0.002187),
        ('Auvinen', 0.001732),
        ('Backman', 0.001331),
        ('Berg', 0.001362),
        ('Blomqvist', 0.001545),
        ('Eklund', 0.001737),
        ('Elo', 0.00113),
        ('Eloranta', 0.00109),
        ('Eriksson', 0.002454),
        ('Erkkilä', 0.001406),
        ('Eronen', 0.001765),
        ('Eskelinen', 0.002041),
        ('Eskola', 0.001747),
        ('Forsman', 0.001077),
        ('Grönroos', 0.001054),
        ('Gustafsson', 0.001571),
        ('Haapala', 0.001736),
        ('Haapanen', 0.00132),
        ('Haapaniemi', 0.001056),
        ('Haataja', 0.001222),
        ('Haavisto', 0.001782),
        ('Hakala', 0.004682),
        ('Hakkarainen', 0.00272),
        ('Häkkinen', 0.002513),
        ('Halme', 0.001566),
        ('Halonen', 0.003495),
        ('Hämäläinen', 0.009001),
        ('Hänninen', 0.003986),
        ('Hannula', 0.001522),
        ('Harju', 0.003153),
        ('Härkönen', 0.002434),
        ('Hartikainen', 0.002868),
        ('Hautala', 0.001909),
        ('Hautamäki', 0.00165),
        ('Haverinen', 0.001289),
        ('Heikkilä', 0.006931),
        ('Heikkinen', 0.008519),
        ('Heino', 0.00296),
        ('Heinonen', 0.007026),
        ('Heiskanen', 0.003335),
        ('Helenius', 0.001874),
        ('Helin', 0.001682),
        ('Helminen', 0.001458),
        ('Henriksson', 0.001408),
        ('Hietala', 0.002444),
        ('Hietanen', 0.00184),
        ('Hiltunen', 0.004889),
        ('Hirvonen', 0.004428),
        ('Hokkanen', 0.002165),
        ('Holappa', 0.00105),
        ('Holm', 0.001459),
        ('Holmberg', 0.001217),
        ('Holmström', 0.001188),
        ('Holopainen', 0.002501),
        ('Honkanen', 0.00323),
        ('Huhtala', 0.002066),
        ('Huotari', 0.001845),
        ('Huovinen', 0.001733),
        ('Huttunen', 0.003632),
        ('Huuskonen', 0.001163),
        ('Hytönen', 0.001515),
        ('Hyttinen', 0.001835),
        ('Hyvärinen', 0.002703),
        ('Hyvönen', 0.002406),
        ('Ihalainen', 0.001044),
        ('Ikonen', 0.00358),
        ('Immonen', 0.003231),
        ('Jaakkola', 0.002386),
        ('Jääskeläinen', 0.002913),
        ('Jaatinen', 0.001308),
        ('Jalonen', 0.001474),
        ('Jansson', 0.00146),
        ('Jäntti', 0.00125),
        ('Järvelä', 0.001204),
        ('Järvenpää', 0.001797),
        ('Järvi', 0.001061),
        ('Järvinen', 0.007928),
        ('Jauhiainen', 0.001305),
        ('Johansson', 0.003434),
        ('Jokela', 0.002356),
        ('Jokinen', 0.005951),
        ('Juntunen', 0.002955),
        ('Jussila', 0.002127),
        ('Juvonen', 0.001677),
        ('Kähkönen', 0.00158),
        ('Kaikkonen', 0.001253),
        ('Kainulainen', 0.001727),
        ('Kallio', 0.004876),
        ('Kämäräinen', 0.001118),
        ('Kanerva', 0.001436),
        ('Kangas', 0.002883),
        ('Kankaanpää', 0.001337),
        ('Kantola', 0.001513),
        ('Karhu', 0.00234),
        ('Karhunen', 0.001157),
        ('Kari', 0.001082),
        ('Karjalainen', 0.006036),
        ('Kärki', 0.001268),
        ('Kärkkäinen', 0.003561),
        ('Karlsson', 0.002809),
        ('Karppinen', 0.003072),
        ('Karttunen', 0.001799),
        ('Karvinen', 0.001394),
        ('Karvonen', 0.002385),
        ('Kauppila', 0.00126),
        ('Kauppinen', 0.003787),
        ('Keinänen', 0.001261),
        ('Kemppainen', 0.003777),
        ('Keränen', 0.002874),
        ('Keskinen', 0.001651),
        ('Keskitalo', 0.00109),
        ('Ketola', 0.001792),
        ('Kettunen', 0.003871),
        ('Kilpeläinen', 0.001374),
        ('Kinnunen', 0.006796),
        ('Kiuru', 0.001089),
        ('Kivelä', 0.002164),
        ('Kivimäki', 0.001619),
        ('Kivinen', 0.0013),
        ('Kiviniemi', 0.001402),
        ('Kivistö', 0.001447),
        ('Koistinen', 0.001988),
        ('Koivisto', 0.004667),
        ('Koivula', 0.002017),
        ('Koivunen', 0.001881),
        ('Kokko', 0.002672),
        ('Kokkonen', 0.003128),
        ('Kolehmainen', 0.002155),
        ('Komulainen', 0.001657),
        ('Konttinen', 0.001132),
        ('Koponen', 0.003424),
        ('Korhonen', 0.011042),
        ('Korpela', 0.002431),
        ('Korpi', 0.001281),
        ('Kortelainen', 0.001539),
        ('Koskela', 0.003733),
        ('Koski', 0.003231),
        ('Koskinen', 0.008414),
        ('Kosonen', 0.00231),
        ('Kovanen', 0.001198),
        ('Kuisma', 0.001348),
        ('Kujala', 0.002234),
        ('Kukkonen', 0.002415),
        ('Kulmala', 0.001901),
        ('Kumpulainen', 0.001781),
        ('Kuosmanen', 0.001577),
        ('Kurki', 0.001386),
        ('Kuronen', 0.001149),
        ('Kuusela', 0.001972),
        ('Kuusisto', 0.002479),
        ('Kyllönen', 0.001904),
        ('Laakkonen', 0.00201),
        ('Laakso', 0.00436),
        ('Laaksonen', 0.004505),
        ('Lähteenmäki', 0.001609),
        ('Lahti', 0.00373),
        ('Lahtinen', 0.005427),
        ('Laiho', 0.001374),
        ('Laine', 0.008802),
        ('Laitinen', 0.006223),
        ('Lammi', 0.00109),
        ('Lampinen', 0.002147),
        ('Lankinen', 0.001053),
        ('Lappalainen', 0.003902),
        ('Lassila', 0.001343),
        ('Latvala', 0.001139),
        ('Laukkanen', 0.002981),
        ('Laurila', 0.00268),
        ('Lehikoinen', 0.001339),
        ('Lehtimäki', 0.001726),
        ('Lehtinen', 0.007344),
        ('Lehto', 0.004389),
        ('Lehtola', 0.001536),
        ('Lehtonen', 0.00786),
        ('Leino', 0.002813),
        ('Leinonen', 0.004891),
        ('Lepistö', 0.001981),
        ('Leppänen', 0.005224),
        ('Leskinen', 0.002572),
        ('Liimatainen', 0.001943),
        ('Lilja', 0.00115),
        ('Lindberg', 0.001978),
        ('Lindfors', 0.001504),
        ('Lindgren', 0.00175),
        ('Lindholm', 0.003367),
        ('Lindqvist', 0.002171),
        ('Lindroos', 0.002225),
        ('Lindström', 0.002755),
        ('Linna', 0.001114),
        ('Lipponen', 0.00129),
        ('Liukkonen', 0.001696),
        ('Luoma', 0.00193),
        ('Luukkonen', 0.001845),
        ('Määttä', 0.003095),
        ('Mäenpää', 0.00279),
        ('Mäkelä', 0.009299),
        ('Mäki', 0.003044),
        ('Mäkinen', 0.009918),
        ('Makkonen', 0.002549),
        ('Malinen', 0.002249),
        ('Manninen', 0.004752),
        ('Männistö', 0.001155),
        ('Mäntylä', 0.001364),
        ('Markkanen', 0.001624),
        ('Martikainen', 0.002756),
        ('Marttila', 0.001834),
        ('Marttinen', 0.001083),
        ('Matikainen', 0.00149),
        ('Matilainen', 0.001526),
        ('Mattila', 0.005845),
        ('Mattsson', 0.001349),
        ('Meriläinen', 0.001503),
        ('Miettinen', 0.004877),
        ('Mikkola', 0.003284),
        ('Mikkonen', 0.00345),
        ('Moilanen', 0.004065),
        ('Moisio', 0.001273),
        ('Mononen', 0.001237),
        ('Muhonen', 0.001141),
        ('Mustonen', 0.004238),
        ('Myllymäki', 0.001733),
        ('Nevala', 0.001071),
        ('Nevalainen', 0.002639),
        ('Niemelä', 0.004065),
        ('Niemi', 0.006993),
        ('Nieminen', 0.009851),
        ('Niiranen', 0.001315),
        ('Nikula', 0.001193),
        ('Niskanen', 0.003346),
        ('Nissinen', 0.002092),
        ('Nousiainen', 0.002075),
        ('Nurmi', 0.004112),
        ('Nurminen', 0.003196),
        ('Nuutinen', 0.001781),
        ('Nyberg', 0.001381),
        ('Nykänen', 0.002561),
        ('Nylund', 0.001545),
        ('Nyman', 0.003435),
        ('Oikarinen', 0.00114),
        ('Oinonen', 0.001349),
        ('Ojala', 0.005237),
        ('Ojanen', 0.001396),
        ('Oksanen', 0.003372),
        ('Ollikainen', 0.001631),
        ('Ollila', 0.001614),
        ('Pääkkönen', 0.001404),
        ('Paananen', 0.002837),
        ('Paavilainen', 0.001028),
        ('Paavola', 0.001687),
        ('Pajunen', 0.001396),
        ('Pakarinen', 0.001818),
        ('Palomäki', 0.001161),
        ('Parkkinen', 0.001273),
        ('Partanen', 0.003879),
        ('Parviainen', 0.002908),
        ('Pasanen', 0.002364),
        ('Pehkonen', 0.001178),
        ('Pekkala', 0.001172),
        ('Pekkarinen', 0.0011),
        ('Pelkonen', 0.001933),
        ('Peltola', 0.003401),
        ('Peltonen', 0.004111),
        ('Peltoniemi', 0.001325),
        ('Pennanen', 0.001857),
        ('Penttilä', 0.001723),
        ('Penttinen', 0.001875),
        ('Perälä', 0.001592),
        ('Pesonen', 0.003534),
        ('Pietilä', 0.001874),
        ('Piirainen', 0.001336),
        ('Pirinen', 0.001318),
        ('Pitkänen', 0.004831),
        ('Pohjola', 0.001266),
        ('Pöllänen', 0.001097),
        ('Puhakka', 0.001413),
        ('Pulkkinen', 0.003995),
        ('Puranen', 0.001053),
        ('Puustinen', 0.001385),
        ('Raatikainen', 0.001244),
        ('Räisänen', 0.002146),
        ('Rajala', 0.002963),
        ('Ranta', 0.002422),
        ('Rantala', 0.004243),
        ('Rantanen', 0.006076),
        ('Räsänen', 0.004444),
        ('Räty', 0.001319),
        ('Rauhala', 0.001391),
        ('Rautiainen', 0.00292),
        ('Rautio', 0.002231),
        ('Reinikainen', 0.001112),
        ('Repo', 0.001805),
        ('Riihimäki', 0.001097),
        ('Riikonen', 0.001838),
        ('Rinne', 0.002123),
        ('Rintala', 0.001596),
        ('Rissanen', 0.003116),
        ('Ronkainen', 0.001757),
        ('Rönkkö', 0.001111),
        ('Rossi', 0.001203),
        ('Ruotsalainen', 0.002752),
        ('Ruuskanen', 0.001251),
        ('Rytkönen', 0.00144),
        ('Ryynänen', 0.00112),
        ('Saarela', 0.002292),
        ('Saari', 0.003871),
        ('Saarinen', 0.007247),
        ('Saastamoinen', 0.001741),
        ('Sainio', 0.001224),
        ('Sallinen', 0.001148),
        ('Salmela', 0.002572),
        ('Salmi', 0.003705),
        ('Salminen', 0.007146),
        ('Salo', 0.006336),
        ('Salomaa', 0.001099),
        ('Salonen', 0.006757),
        ('Savolainen', 0.005448),
        ('Seppä', 0.001142),
        ('Seppälä', 0.004007),
        ('Seppänen', 0.003731),
        ('Sihvonen', 0.001053),
        ('Sillanpää', 0.002264),
        ('Silvennoinen', 0.001614),
        ('Simola', 0.001116),
        ('Simonen', 0.001049),
        ('Sipilä', 0.001582),
        ('Sirén', 0.001129),
        ('Sirviö', 0.001089),
        ('Sjöblom', 0.001119),
        ('Soini', 0.001102),
        ('Soininen', 0.001422),
        ('Suhonen', 0.001834),
        ('Suomalainen', 0.001609),
        ('Suominen', 0.003582),
        ('Sutinen', 0.001056),
        ('Syrjälä', 0.001196),
        ('Tähtinen', 0.001028),
        ('Taipale', 0.001378),
        ('Takala', 0.001797),
        ('Tamminen', 0.002461),
        ('Tanskanen', 0.001536),
        ('Tarvainen', 0.001396),
        ('Taskinen', 0.001633),
        ('Tervo', 0.001419),
        ('Tiainen', 0.00234),
        ('Tiihonen', 0.001149),
        ('Tikka', 0.001325),
        ('Tikkanen', 0.00266),
        ('Timonen', 0.002211),
        ('Tirkkonen', 0.001193),
        ('Toivanen', 0.002668),
        ('Toivonen', 0.004311),
        ('Tolonen', 0.002122),
        ('Tolvanen', 0.001917),
        ('Tuomi', 0.001608),
        ('Tuominen', 0.006098),
        ('Tuovinen', 0.001894),
        ('Turpeinen', 0.001528),
        ('Turunen', 0.006523),
        ('Uotila', 0.001053),
        ('Uusitalo', 0.002687),
        ('Väänänen', 0.002319),
        ('Vainio', 0.003358),
        ('Väisänen', 0.004904),
        ('Välimäki', 0.001587),
        ('Valkama', 0.001139),
        ('Valkonen', 0.001248),
        ('Valtonen', 0.002171),
        ('Varis', 0.001436),
        ('Vartiainen', 0.002039),
        ('Väyrynen', 0.001426),
        ('Venäläinen', 0.001262),
        ('Vesterinen', 0.001259),
        ('Viitala', 0.001642),
        ('Viitanen', 0.002647),
        ('Viljanen', 0.001859),
        ('Virta', 0.002228),
        ('Virtanen', 0.01083),
        ('Voutilainen', 0.001853),
        ('Vuorela', 0.001156),
        ('Vuori', 0.001701),
        ('Vuorinen', 0.003188),
        ('Ylinen', 0.00105),
        ('Ylitalo', 0.001438),
        ('Ylönen', 0.00125)
    ))
