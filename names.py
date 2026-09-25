"""Name generation for characters, superpowers, cities and countries."""

import random
from typing import Literal

# ==========================================
# NATIONS AND PERSON NAME SETS
# Each country has its own independent name set (~20 male, ~20 female, ~50 last).
# ==========================================
NATIONS = [
    'USA', 'UK', 'China', 'Russia', 'India',
    'Germany', 'France', 'Canada', 'Spain', 'Italy',
    'Japan', 'Mexico', 'Brazil', 'Indonesia', 'Argentina',
    'Nigeria', 'Egypt', 'Philippines', 'South Africa', 'Iran',
    'Australia', 'Saudi Arabia', 'Turkey', 'South Korea', 'Poland',
    'Greece', 'Thailand'
]

NAMES_M_EN = ['James','William','Thomas','George','Edward','Henry','Charles','Frederick','Arthur','Albert','Alfred','Harry','Jack','Oliver','Samuel','Benjamin','Joseph','Daniel','Matthew','David']
NAMES_W_EN = ['Elizabeth','Mary','Margaret','Emma','Alice','Sarah','Florence','Rose','Catherine','Emily','Charlotte','Anne','Victoria','Beatrice','Eleanor','Grace','Lily','Clara','Jane','Sophia']
NAMES_L_EN = ['Smith','Jones','Taylor','Brown','Williams','Wilson','Johnson','Davies','Robinson','Wright','Thompson','Evans','Walker','White','Roberts','Green','Hall','Wood','Jackson','Clarke','Harrison','Lewis','Morris','King','Allen','Scott','Young','Gordon','Douglas',"O'Brien","O'Connor",'James','Knight','Ward','Hughes','Morgan','Edwards','Hill','Moore','Clark','Carter','Mitchell','Phillips','Patel','Adams','Campbell','Anderson','Bell','Kelly','Baker','Davis','Bennett','Cook','McCarthy','McDonald','McKenzie']

NAMES_M_RU = ['Alexander','Dmitry','Mikhail','Ivan','Sergei','Andrei','Alexei','Nikolai','Vladimir','Artem','Maxim','Oleg','Yuri','Pavel','Konstantin','Anton','Denis','Igor','Roman','Vasily','Marat','Ruslan']
NAMES_W_RU = ['Anastasia','Maria','Ekaterina','Anna','Olga','Natalia','Svetlana','Irina','Yulia','Daria','Polina','Elena','Tatiana','Marina','Vera','Ludmila','Sofia','Valentina','Galina','Kristina','Kamilla','Renata']
NAMES_L_RU = ['Ivanov','Smirnov','Kuznetsov','Popov','Sokolov','Lebedev','Kozlov','Novikov','Morozov','Petrov','Volkov','Solovyov','Vasilyev','Zaitsev','Pavlov','Stepanov','Orlov','Andreev','Makarov','Nikitin','Zakharov','Fyodorov','Yegorov','Medvedev','Gusev','Vinogradov','Belyaev','Titov','Davydov','Zhukov','Vorobyov','Semyonov','Alekseyev','Fedotov','Dorofeev','Egorov','Isaev','Kirillov','Maksimov','Osipov','Romanov','Sorokin','Tarasov','Ustinov','Fomin','Kharitonov','Chernov','Shcherbakov','Yakovlev','Belov','Abramov','Shevchenko','Tkachenko','Kravchenko','Boyko','Dmitrenko','Magomedov','Ibragimov','Karimov','Abdullaev','Safiullin','Zainullin','Dzagoev','Petrosyan','Mikoyan','Beridze','Dudaev','Yunusov']

NAMES_M_PL = ['Jan','Stanisław','Andrzej','Józef','Tadeusz','Jerzy','Zbigniew','Krzysztof','Henryk','Ryszard','Kazimierz','Marek','Marian','Piotr','Adam','Wiesław','Grzegorz','Paweł','Dariusz','Michał']
NAMES_W_PL = ['Anna','Maria','Katarzyna','Małgorzata','Agnieszka','Barbara','Ewa','Elżbieta','Zofia','Joanna','Teresa','Jadwiga','Danuta','Halina','Irena','Beata','Helena','Bożena','Marta','Aleksandra']
NAMES_L_PL = ['Nowak','Kowalski','Wiśniewski','Wójcik','Kowalczyk','Kamiński','Lewandowski','Zieliński','Szymański','Woźniak','Dąbrowski','Kozłowski','Jankowski','Mazur','Wojciechowski','Kwiatkowski','Krawczyk','Kaczmarek','Piotrowski','Grabowski','Nowakowski','Pawłowski','Michalski','Nowicki','Adamczyk','Dudek','Zając','Więczorek','Jabłoński','Król','Majewski','Olszewski','Jaworski','Malinowski','Pająk','Walczak','Stępień','Górski','Sikora','Ostrowski','Borkowski','Cieślak','Sawicki','Sokołowski','Maciejewski','Szulc','Kucharski','Włodarczyk','Lis','Bąk','Chmielewski']

NAMES_M_EL = ['Alexander','Andreas','Christos','Demetrios','Dimitrios','Elias','Georgios','Ioannis','Konstantinos','Kyriakos','Leonidas','Michail','Nikolaos','Panagiotis','Petros','Spyridon','Stavros','Theodoros','Vasilios','Yiannis']
NAMES_W_EL = ['Alexandra','Anastasia','Angeliki','Athina','Christina','Despina','Eleni','Georgia','Ioanna','Katerina','Konstantina','Maria','Nefeli','Olga','Panagiota','Paraskevi','Sofia','Theodora','Vasiliki','Zoe']
NAMES_L_EL = ['Papadopoulos','Papadakis','Ioannidis','Georgiou','Konstantinidis','Dimitriou','Athanasiou','Vasileiou','Nikolaidis','Pappas','Angelopoulos','Antonopoulos','Apostolou','Argyropoulos','Christodoulopoulos','Dimitropoulos','Economou','Eleftheriou','Floros','Fotopoulos','Galanis','Georgiadis','Giannopoulos','Iordanou','Kaklamanis','Kalogeropoulos','Karagiannis','Katsaros','Kokkinos','Kontos','Kouris','Kyriakou','Lambropoulos','Lazaridis','Leventis','Makris','Maniatis','Mavros','Michalopoulos','Nikolaou','Panagiotopoulos','Pantazis','Papageorgiou','Papakonstantinou','Paraskevopoulos','Pavlidis','Petrakis','Platis','Polyzos','Raptis']

NAMES_M_ZH = ['Hao','Wei','Jun','Bo','Yang','Feng','Yi','Chen','Yu','Lei','Kai','Xin','Qiang','Dong','Bin','Gang','Tao','Peng','Ran','Song']
NAMES_W_ZH = ['Mei','Li','Jing','Xue','Fang','Yu','Ting','Xin','Yan','Ling','Rui','Lan','Yue','Xi','Qi','Jia','Wen','Ying','Hong','Jie']
NAMES_L_ZH = ['Li','Wang','Zhang','Liu','Chen','Yang','Zhao','Huang','Zhou','Wu','Xu','Sun','Hu','Zhu','Gao','Lin','He','Guo','Ma','Luo','Liang','Song','Zheng','Xie','Han','Tang','Feng','Yu','Dong','Xiao','Cheng','Cao','Yuan','Deng','Fu','Shen','Zeng','Peng','Lu','Su','Jiang','Cai','Jia','Ding','Wei','Xue','Ye','Yan','Pan','Du','Dai']

NAMES_M_FR = ['Léo','Gabriel','Raphaël','Louis','Noah','Jules','Adam','Lucas','Hugo','Arthur','Maël','Liam','Paul','Nolan','Nathan','Ethan','Tom','Sacha','Enzo','Théo']
NAMES_W_FR = ['Emma','Jade','Louise','Alice','Ambre','Rose','Chloé','Léa','Mia','Lina','Manon','Inès','Juliette','Camille','Olivia','Zoé','Anna','Mila','Jeanne','Léna']
NAMES_L_FR = ['Martin','Bernard','Dubois','Thomas','Robert','Richard','Petit','Durand','Leroy','Moreau','Simon','Laurent','Lefebvre','Michel','Garcia','David','Bertrand','Roux','Vincent','Fournier','Morel','Girard','André','Lefèvre','Mercier','Dupont','Lambert','Bonnet','François','Martinez','Legrand','Garnier','Faure','Rousseau','Blin','Muller','Henry','Roussel','Giraud','Denis','Masson','Marchand','Mathieu','Clement','Gauthier','Noel','Perrin','Marie','Joly','Gaillard']

NAMES_M_ES = ['Antonio','Manuel','José','Francisco','David','Juan','Javier','Daniel','Carlos','Luis','Miguel','Alejandro','Pablo','Adrián','Sergio','Álvaro','Fernando','Rafael','Marcos','Jorge']
NAMES_W_ES = ['María','Carmen','Ana','Isabel','Laura','Sofía','Lucía','Elena','Paula','Marta','Julia','Patricia','Beatriz','Rosa','Andrea','Teresa','Clara','Alicia','Inés','Victoria']
NAMES_L_ES = ['García','Fernández','González','Rodríguez','López','Martínez','Sánchez','Pérez','Martín','Gómez','Ruiz','Hernández','Jiménez','Díaz','Moreno','Álvarez','Romero','Navarro','Torres','Domínguez','Ramos','Vázquez','Gil','Ramírez','Serrano','Blanco','Molina','Morales','Suárez','Ortega','Delgado','Castro','Ortiz','Rubio','Marín','Núñez','Iglesias','Medina','Garrido','Cortés','Castillo','Calvo','Prieto','Santos','Lozano','Guerrero','Méndez','Cruz','Flores','Herrera']

NAMES_M_PT = ['Miguel','Gabriel','Arthur','Davi','Bernardo','Lucas','Heitor','Pedro','Enzo','Lourenço','Rafael','Felipe','Matheus','Guilherme','Gustavo','Nicolas','Samuel','Caio','Joaquim','Vicente']
NAMES_W_PT = ['Alice','Sofia','Laura','Valentina','Isabella','Manuela','Júlia','Heloísa','Luiza','Maria Eduarda','Beatriz','Maria Clara','Giovanna','Larissa','Mariana','Yasmim','Ana Clara','Isabelly','Rafaela','Esther']
NAMES_L_PT = ['Silva','Santos','Oliveira','Souza','Rodrigues','Ferreira','Alves','Pereira','Lima','Gomes','Costa','Ribeiro','Martins','de Jesus','Carvalho','Araújo','Fernandes','Barbosa','Rocha','Dias','Moreira','Mendes','Nascimento','Amorim','Duarte','Teixeira','Melo','Cortês','Cunha','Cavalcanti','Pires','Franco','Miranda','Domingues','Peixoto','Fonseca','Guimarães','Sampaio','Tavares','Andrade','Vieira','Leal','Aguiar','Brito','Farias','Barros','Bezerra','Campos','Cardoso','Dantas']

NAMES_M_DE = ['Alexander','Andreas','Anton','Benedikt','Christian','Daniel','Elias','Felix','Florian','Jonas','Julian','Leon','Lukas','Manuel','Matthias','Michael','Niklas','Paul','Sebastian','Tobias']
NAMES_W_DE = ['Anna','Claudia','Elena','Emilia','Emma','Franziska','Hannah','Ines','Johanna','Julia','Katharina','Leonie','Lena','Marie','Mia','Nadine','Nina','Paula','Sophie','Viktoria']
NAMES_L_DE = ['Müller','Schmidt','Schneider','Fischer','Weber','Meyer','Wagner','Becker','Schulz','Hoffmann','Schäfer','Koch','Bauer','Richter','Klein','Wolf','Schröder','Neumann','Schwarz','Zimmermann','Braun','Krüger','Hofmann','Hartmann','Lange','Schmitt','Werner','Schmitz','Krause','Meier','Lehmann','Schmid','Schulze','Maier','Köhler','Herrmann','König','Walter','Mayer','Huber','Kaiser','Fuchs','Peters','Lang','Scholz','Möller','Weiß','Jung','Hahn','Vogel']

NAMES_M_IT = ['Alessandro','Andrea','Antonio','Carlo','Davide','Enzo','Francesco','Giorgio','Giovanni','Leonardo','Lorenzo','Luca','Marco','Matteo','Nicola','Paolo','Pietro','Riccardo','Simone','Tommaso']
NAMES_W_IT = ['Alessia','Anna','Beatrice','Camilla','Chiara','Elena','Federica','Francesca','Ginevra','Giulia','Ilaria','Isabella','Laura','Lucia','Marta','Sara','Sofia','Valentina','Veronica','Viola']
NAMES_L_IT = ['Rossi','Russo','Ferrari','Esposito','Bianchi','Romano','Colombo','Ricci','Marino','Greco','Bruno','Gallo','Conti','De Luca','Costa','Giordano','Mancini','Rizzo','Lombardi','Moretti','Di Stefano','De Angelis',"D'Amico",'Leone','Santoro','Vitali','Serra','Marchetti','Barbieri','Galli','De Santis','Caruso','Ferraro','Marini','Pellegrini','Fabbri','Silvestri','Rinaldi','Palumbo','Sanna','Villa','Fontana','Monti','De Rosa','Ferri','Gatti','Parisi','Lombardo','Messina','Amato']

NAMES_M_JA = ['Haruto','Ren','Yuto','Sota','Riku','Kaito','Yuma','Daiki','Shota','Hayato','Takumi','Ryota','Yuki','Haru','Keita','Sho','Kota','Tsubasa','Minato','Jin']
NAMES_W_JA = ['Yui','Aoi','Mio','Rin','Hina','Sakura','Riko','Yuna','Nana','Haruka','Saki','Mei','Ayaka','Noa','Reina','Kana','Misaki','Tomo','Yuri','Ema']
NAMES_L_JA = ['Satō','Suzuki','Takahashi','Tanaka','Watanabe','Itō','Yamamoto','Nakamura','Kobayashi','Katō','Yoshida','Yamada','Sasaki','Yamaguchi','Saitō','Matsumoto','Inoue','Kimura','Hayashi','Shimizu','Yamazaki','Ikeda','Hashimoto','Ishikawa','Yamashita','Ogawa','Ishibashi','Maeda','Fujita','Gotō','Okada','Hasegawa','Murakami','Ono','Takeuchi','Kojima','Endō','Aoki','Fujii','Nishimura','Fukuda','Ōta','Miura','Fujiwara','Okamoto','Matsuda','Nakagawa','Nakano','Morimoto','Arai','Ōno']

NAMES_M_IN = ['Arjun','Rohan','Aryan','Aditya','Vikram','Karthik','Rajesh','Siddharth','Dev','Rishabh','Amar','Nikhil','Suresh','Harish','Vijay','Prem','Deepak','Ganesh','Manoj','Anil']
NAMES_W_IN = ['Priya','Ananya','Divya','Meera','Kavita','Sunita','Neha','Pooja','Shreya','Jyoti','Deepa','Asha','Leela','Madhuri','Sita','Tara','Anjali','Radha','Maya','Nisha']
NAMES_L_IN = ['Patel','Sharma','Singh','Kumar','Reddy','Khan','Desai','Mehta','Rao','Choudhury','Iyer','Chatterjee','Joshi','Malhotra','Agarwal','Gupta','Varma','Nair','Menon','Das','Tiwari','Mishra','Yadav','Jain','Saxena','Bhat','Acharya','Dubey','Thakur','Kapoor','Srinivasan','Pandey','Shah','Trivedi','Oberoi','Biswas','Banerjee','Mukherjee','Sen','Gowda','Shetty','Naidu','Rajput','Dutta','Ranganathan','Pillai','Subramanian','Krishnan','Venkatesh','Raman']

NAMES_M_ID = 'Agus,Ahmad,Akbar,Andi,Arif,Bagus,Bambang,Bayu,Bimo,Budi,Cahya,Dedi,Dimas,Dwi,Eko,Fajar,Fauzi,Fikri,Galih,Guntur,Hendra,Herman,Iman,Irfan,Jaka,Joko,Kamal,Lukman,Mahendra,Muhammad,Nanda,Rahmat,Reza,Rizki,Rohman,Rudi,Sandi,Satria,Slamet,Sukma,Taufik,Tomi,Umar,Wahyu,Wawan,Yanto,Yusuf,Zaki,Zulkifli'.split(',')
NAMES_W_ID = 'Ai,Aida,Aisyah,Amalia,Anisa,Asih,Ayu,Citra,Dewi,Dian,Dinda,Eni,Fitri,Fitria,Gita,Hesti,Indah,Intan,Kartika,Larasati,Lestari,Mira,Nadia,Nenden,Nia,Nur,Nurul,Oyong,Popon,Putri,Ratna,Rina,Risma,Salsabila,Sari,Sekar,Tika,Tuti,Wulan,Yuni,Yunita,Zahrah,Zulfa'.split(',')
# Indonesian names are mostly mononymous: a single "callsign" is normal, but the
# formal name (used on documents, incl. this university roster) often adds a family
# name inherited from the father, plus an honorific such as "Dr." or "H.".
NAMES_L_ID = 'Aditya,Anggara,Anwar,Asmara,Firmansyah,Gunawan,Handoko,Hardiman,Hidayat,Hartono,Hasibuan,Kurniawan,Lubis,Marjono,Maulana,Nugroho,Permana,Pratama,Prasetyo,Prayoga,Ramadhan,Santoso,Saputra,Setiawan,Sihombing,Simanjuntak,Siregar,Soerjanto,Susanto,Wibisono,Wibowo,Widyanto,Wicaksono,Yulianto,Yudhoyono'.split(',')
# Only women get these -i / -y family names, men keep the inherited surname unchanged.
NAMES_L_ID_F = 'Anggraini,Fadhilah,Handayani,Kusuma,Kusumawardani,Lestari,Maharani,Mayangsari,Ningrum,Novitasari,Oktaviani,Permatasari,Rahayu,Rahmawati,Ramadhani,Safitri,Suryani,Wulandari'.split(',')
# Fathers named in "bin" / "binti" patronymics.
NAMES_FATHER_ID = 'Ahmad,Andi,Arif,Bambang,Budi,Eko,Hendra,Iman,Joko,Kamal,Muhammad,Rahmat,Reza,Rizki,Sandi,Sukma,Taufik,Yusuf,Zulkifli'.split(',')
ID_TITLES_M = ['Dr.', 'Drs.', 'Ir.', 'H.']
ID_TITLES_W = ['Dr.', 'Drs.', 'Hj.']

NAMES_M_NG = ['Adebayo','Olumide','Chinedu','Emeka','Ifeanyi','Tunde','Kayode','Segun','Uche','Kelechi','Ibrahim','Sani','Musa','Abdullahi','Bassey','Jide','Kunle','Nnamdi','Femi','Biodun']
NAMES_W_NG = ['Adebimpe','Yetunde','Titilayo','Bukola','Sade','Ngozi','Chioma','Adaeze','Amaka','Ifunanya','Hauwa','Zainab','Aisha','Maryam','Fatima','Oluwaseyi','Temiloluwa','Olamide','Folake','Eno']
NAMES_L_NG = ['Adeboye','Adegoke','Adekunle','Adelaja','Adeniyi','Adeyemi','Adewole','Akinwunmi','Akintola','Balogun','Bamgbose','Fagbemi','Ige','Ogunleye','Ojo','Okeke','Olanrewaju','Olarewaju','Olawale','Olowo','Oluwaseyi','Oni','Oyebode','Oyeniyi','Sowole','Taiwo','Talabi','Achebe','Chukwu','Ekwueme','Ihejirika','Kanu','Mbachu','Mgbechi','Nwabueze','Nwachukwu','Nwadike','Nwagwu','Nwankwo','Nwapa','Nwaubani','Nwosu','Obasanjo','Obi','Okafor','Okonkwo','Okoro','Okoye','Okpara','Okorie','Onyejekwe']

NAMES_M_AR = ['Adam','Omar','Ali','Yusuf','Ahmed','Hassan','Hussein','Mohammed','Khalid','Ibrahim','Mustafa','Tariq','Malik','Zayn','Rayan','Sami','Karim','Faisal','Jamal','Rashid']
NAMES_W_AR = ['Aisha','Fatima','Layla','Zainab','Mariam','Nora','Sara','Leila','Amira','Hana','Yasmin','Salma','Rana','Nadia','Lina','Jamila','Dina','Rania','Farah','Noura']
NAMES_L_AR = ['Abbas','Abdel','Abdullah','Abed','Ahmad','al-Fayed','al-Khatib','al-Saud','Ali','Amin','Asad','Ashraf','Assad','Awad','Aziz','Baig','Bakir','Barakat','Bashir','Behnam','Bekhit','Belal','ben Ali','Bishara','Darwish','Dawoud','Diab','Ebeid','Eissa','Elamin','Elmasry','Fadel','Fahmy','Farag','Farah','Farhat','Farid','Farooq','Fawaz','Fayad','Ganim','Ghanem','Ghannam','Ghazi','Habib','Haddad','Hafez','Hakim','Halabi','Hamad']

NAMES_M_PH = ['Jacob','Nathaniel','Gabriel','Nathan','Ethan','Ezekiel','Angelo','James','Joshua','Kyle','Matthew','Zion','Liam','Jayden','Noah','Christian','Daniel','John Mark','Marvic','Dakila']
NAMES_W_PH = ['Althea','Angel','Samantha','Princess','Nathalie','Sofia','Sophia','Jasmine','Andrea','Angela','Chloe','Zoey','Ayesha','Zia','Athena','Alexa','Janella','Ashley','Luzviminda','Maricar']
NAMES_L_PH = ['Santos','Reyes','Cruz','Bautista','Ocampo','García','Mendoza','Torres','Villanueva','de los Reyes','Abad','Abella','Aguilar','Alba','Alcaraz','Alejandro','Almario','Alvarez','Aquino','Arroyo','Asuncion','Baltazar','Barretto','Bernal','Cabrera','Castro','Chavez','Clemente','Cordero','Corpus','Cortez','Dalisay','Daza','de Guzmán','de León','del Castillo','del Rosario','dela Cruz','dela Peña','dela Torre','Diaz','Dominguez','Encarnacion','Enriquez','Esguerra','Esteban','Evangelista','Fernandez','Fernando','Flores','Francisco','Galang']

NAMES_M_ZA = ['Liam','Ethan','Lethabo','Junior','Lubanzi','Kagiso','David','Jason','Simba','Sipho','Daniel','Michael','Blessing','Gift','Thabo','Thomas','Banele','Neo','Nathan','Joshua']
NAMES_W_ZA = ['Precious','Emma','Zoe','Amahle','Mia','Chloe','Isabella','Kagiso','Olivia','Ava','Leah','Ayanda','Naledi','Thando','Nomvula','Nomsa','Zinhle','Sarah','Lisa','Amy']
NAMES_L_ZA = ['Nkosi','Zulu','Khumalo','Mthembu','Ndlovu','Ngcobo','Mkhize','Zungu','Cele','Majozi','Xulu','Mbatha','Mthethwa','Buthelezi','Dlamini','Gumede','Shabangu','Ntuli','Biyela','Hlongwane','Mhlongo','Zondo','Mbhele','Nxumalo','Zuma','Gwala','Mchunu','Ntanzi','Sithole','Ngubane','Shezi','Khuzwayo','Mnguni','Mdluli','Nkomo','Ngwenya','Nene','Mzobe','Maphumulo','Shandu','Sibiya','Nsele','Mbokazi','Mncwango','Ntshangase','Gcumisa','Dube','Mahlangu','Zikhali','Phakathi','Mvelase']

NAMES_M_FA = ['Amir','Arash','Behzad','Kourosh','Dariush','Ehsan','Farhad','Hamed','Hossein','Kamran','Kian','Mehdi','Navid','Omid','Pedram','Reza','Saeed','Shahin','Sohrab','Yashar']
NAMES_W_FA = ['Aida','Anahita','Arezoo','Bahar','Donya','Elaheh','Fatemeh','Golnaz','Mahsa','Marjan','Maryam','Nazanin','Neda','Parisa','Roya','Sanaz','Shirin','Simin','Yalda','Zara']
NAMES_L_FA = ['Abbaszadeh','Abdi','Ahmadi','Akbari','Alavi','Amini','Ansari','Asadi','Asghari','Azimi','Babaei','Bagheri','Bahrami','Barati','Bakhshi','Dastani','Davari','Ebrahimi','Ehsani','Esfahani','Fahim','Farahani','Farhadi','Fathi','Ghanbari','Ghazali','Gholami','Ghorbani','Habibi','Haghighat','Hajian','Hakimi','Hamidi','Hashemi','Hassani','Hejazi','Hosseini','Imani','Jafari','Jalali','Jamali','Javadi','Karami','Karimi','Kashani','Kazemi','Khadem','Khalili','Kiani']

NAMES_M_TR = ['Kerem','Emre','Arda','Deniz','Efe','Can','Barış','Alp','Kaan','Umut','Ozan','Yiğit','Doruk','Cem','Mert','Batu','Onur','Selim','Volkan','Mete']
NAMES_W_TR = ['Elif','Zeynep','Ayşe','Fatma','Defne','Esra','İrem','Seda','Melis','Aslı','Ceren','Dilara','Gizem','İpek','Leyla','Naz','Özlem','Pınar','Serra','Zehra']
NAMES_L_TR = ['Yılmaz','Kaya','Demir','Şahin','Çelik','Yıldız','Öztürk','Aydın','Özdemir','Arslan','Taş','Kılıç','Aslan','Doğan','Erdoğan','Kurt','Koç','Polat','Avcı','Kaplan','Acar','Aksoy','Aktaş','Ateş','Bakır','Baran','Bulut','Çetin','Çakır','Durmuş','Eren','Genç','Güler','Güneş','Güngör','Işık','Karaca','Karadağ','Karahan','Korkmaz','Özkan','Sarı','Sert','Solak','Şen','Tekin','Tok','Tuna','Tunç','Türk']

NAMES_M_KR = ['Min-jun','Seo-jun','Do-yun','Si-woo','Ha-jun','Ji-ho','Jun-seo','Eun-woo','Yu-jun','Jae-hyun','Jun-ho','Seung-min','Hyun-woo','Ji-hun','Min-jae','Sung-min','Dong-hyun','Woo-jin','Jin-woo','Tae-hyun']
NAMES_W_KR = ['Seo-yeon','Ha-yoon','Ji-woo','Seo-hyun','Ha-eun','Min-jung','Yeon-woo','Ji-yoo','Soo-ah','Ji-an','Chae-won','Eun-ji','Yu-na','Hye-rim','Da-bin','Ji-hye','Na-yoon','Ga-eul','Bom','Sol']
NAMES_L_KR = ['Kim','Lee','Park','Choi','Jung','Kang','Cho','Yoon','Jang','Lim','Shin','Yoo','Han','Oh','Seo','Son','Bang','Baek','Hwang','Song','Hong','Yang','Go','Moon','Nam','Do','Ryu','Cha','Ma','Sohn','Namgoong','Hwangbo','Jegal','Seonu','Sagong','Dokgo','Dongbang','Seomun','Namman','Jangso','An','Byun','Chun','Gwak','Gyeom','Ha','Heo','Hyeon','Jin','Joo','Koo']

NAMES_M_TH = ['Thanawat','Natthawut','Kittipong','Chananan','Piyawat','Worawut','Supachai','Wichai','Atthaphon','Sarawut','Jirawat','Thitipong','Siraphop','Panuwat','Ratchanon','Mongkol','Surachai','Arunroj','Krittin','Somchai']
NAMES_W_TH = ['Waraporn','Thanyarat','Nattaporn','Supaluck','Phatchara','Chompunuch','Jutarat','Siriluck','Rapeepat','Ploypailin','Pimnara','Thanaporn','Kanyanart','Narinya','Wimonrat','Patcharee','Suthida','Saowalak','Kanchana','Malinee']
NAMES_L_TH = ['Sriworakul','Boonmee','Akkharawiboon','Methawikrai','Wattanasiri','Phokinthara','Rungsimanont','Kanyamethi','Siriwat','Phumisawat','Chantraprapa','Thanakul','Phongphiphat','Rattanaipaisan','Wisesuk','Ketkaew','Chotikawirot','Ampaiphisut','Serithada','Inthrasuwan','Kanokwan','Chaimongkol','Suphasawat','Chotikawanich','Rueangrot','Phiphatkul','Srisawat','Woranyu','Nanthawisan','Amornstit','Bunnyong','Piyamaphon','Mettaprateep','Sirinthon','Chaloemchai','Krairerk','Siripong','Thanyawat','Prasompon','Weeratham','Suksathit','Komen','Udomrat','Thewanruedi','Phanthuwet','Wimonmat','Charuwan','Pantharanont','Sakthamrong','Paisansin']

# Country-specific indigenous / regional additions
MEXICAN_M = ['Tenoch','Cuauhtémoc','Itzcóatl','Xicoténcatl']
MEXICAN_W = ['Xochitl','Itzel','Citlali','Tonantzin']
MEXICAN_L = ['Zapata','Villa','Cárdenas','Godínez','Esparza']
ARGENTINE_L = ['Sosa','Lucero','Pereyra','Villagra','Guzmán']
SAUDI_L = ['al-Otaibi','al-Harbi','al-Ghamdi','al-Dossari','al-Qahtani']
# Egyptians do not use the Saudi al- forms, and Egyptian family names are very often
# the father's own given name, so they get their own pool.
EGYPT_L = 'Mubarak,Shaker,Soliman,Naguib,Zaki,Fahmy,Farghaly,Attia,Badawi,Fouad,Gaber,Hegazy,Kassem,Lotfy,Mansour,Rifaa,Saad,Shafik,Sorour,Taha,Wahba,Yassin,Zeid,Elsayed,Elshazly,Elsherbiny,Elhusseiny,Elgendy,Elkholy,Elnaggar,Eltayeb,Emam,Fayad,Hamad,Kamel,Khalil,Magdy,Mahmoud,Masoud,Mounir,Nazir,Noor,Osman,Rifai,Saleh,Samir,Shalaby,Sharkawy,Younes,Tawfik'.split(',')

NATIONS_NAMES = {
    'USA':       (NAMES_M_EN, NAMES_W_EN, NAMES_L_EN),
    'UK':        (NAMES_M_EN[3:] + NAMES_M_EN[:3], NAMES_W_EN[4:] + NAMES_W_EN[:4], NAMES_L_EN[12:] + NAMES_L_EN[:12]),
    'China':     (NAMES_M_ZH, NAMES_W_ZH, NAMES_L_ZH),
    'Russia':    (NAMES_M_RU, NAMES_W_RU, NAMES_L_RU),
    'India':     (NAMES_M_IN, NAMES_W_IN, NAMES_L_IN),
    'Germany':   (NAMES_M_DE, NAMES_W_DE, NAMES_L_DE),
    'France':    (NAMES_M_FR, NAMES_W_FR, NAMES_L_FR),
    'Canada':    (NAMES_M_FR[:10] + NAMES_M_EN[10:],
                  NAMES_W_FR[:10] + NAMES_W_EN[10:],
                  NAMES_L_FR[:25] + NAMES_L_EN[25:]),
    'Spain':     (NAMES_M_ES, NAMES_W_ES, NAMES_L_ES),
    'Italy':     (NAMES_M_IT, NAMES_W_IT, NAMES_L_IT),
    'Japan':     (NAMES_M_JA, NAMES_W_JA, NAMES_L_JA),
    'Mexico':    (NAMES_M_ES[:16] + MEXICAN_M, NAMES_W_ES[:16] + MEXICAN_W, NAMES_L_ES[:45] + MEXICAN_L),
    'Brazil':    (NAMES_M_PT, NAMES_W_PT, NAMES_L_PT),
    'Indonesia': (NAMES_M_ID, NAMES_W_ID, NAMES_L_ID),
    'Argentina': (NAMES_M_ES[2:] + NAMES_M_ES[:2], NAMES_W_ES[3:] + NAMES_W_ES[:3], NAMES_L_ES[:45] + ARGENTINE_L),
    'Nigeria':   (NAMES_M_NG, NAMES_W_NG, NAMES_L_NG),
    'Egypt':     (NAMES_M_AR, NAMES_W_AR, EGYPT_L),
    'Philippines': (NAMES_M_PH, NAMES_W_PH, NAMES_L_PH),
    'South Africa': (NAMES_M_ZA, NAMES_W_ZA, NAMES_L_ZA),
    'Iran':      (NAMES_M_FA, NAMES_W_FA, NAMES_L_FA),
    'Australia': (NAMES_M_EN[6:] + NAMES_M_EN[:6], NAMES_W_EN[7:] + NAMES_W_EN[:7], NAMES_L_EN[20:] + NAMES_L_EN[:20]),
    'Saudi Arabia': (NAMES_M_AR[4:] + NAMES_M_AR[:4], NAMES_W_AR[5:] + NAMES_W_AR[:5], NAMES_L_AR + SAUDI_L),
    'Turkey':    (NAMES_M_TR, NAMES_W_TR, NAMES_L_TR),
    'South Korea': (NAMES_M_KR, NAMES_W_KR, NAMES_L_KR),
    'Poland':    (NAMES_M_PL, NAMES_W_PL, NAMES_L_PL),
    'Greece':    (NAMES_M_EL, NAMES_W_EL, NAMES_L_EL),
    'Thailand':  (NAMES_M_TH, NAMES_W_TH, NAMES_L_TH),
}

def generate_nation(rand: random.Random):
    return rand.choice(NATIONS)

# In these cultures the family name comes first when a name is written out in full.
FAMILY_NAME_FIRST = ('Japan', 'South Korea', 'Thailand')

def generate_real_name(nation: str, gender: Literal['male', 'female'], rand: random.Random):
    names_m, names_w, names_l = NATIONS_NAMES[nation]
    if nation == 'Indonesia':
        pool = names_m if gender == 'male' else names_w
        given = rand.choice(pool)
        extra = rand.random()
        if extra < 0.08:
            # Malay / Minangkabau patronymic: "Sukma bin Rahmat", "Siti binti Agus"
            given += f' {"bin" if gender == "male" else "binti"} {rand.choice(NAMES_FATHER_ID)}'
        elif extra < 0.58:
            given += ' ' + rand.choice(names_l + ([] if gender == 'male' else NAMES_L_ID_F))
        elif extra < 0.78:
            # two given names, the callsign first: "Dewi Ayu", "Agus Iman"
            given += ' ' + rand.choice([n for n in pool if n != given])
        if rand.random() < 0.05:
            given = f'{rand.choice(ID_TITLES_M if gender == "male" else ID_TITLES_W)} {given}'
        return given
    elif nation == 'China':
        l_name = rand.choice(names_l)
        n_givenname = rand.randint(1, 2)
        return l_name + ' ' + ''.join(rand.sample(names_m if gender == 'male' else names_w, k=n_givenname)).capitalize()

    l_name = rand.choice(names_l)
    f_name = rand.choice(names_m if gender == 'male' else names_w)
    if gender == 'female':
        if nation == 'Russia':
            if l_name.endswith('ov') or l_name.endswith('ev') or l_name.endswith('in'):
                l_name += 'a'
            elif l_name.endswith('sky'):
                l_name = l_name.removesuffix('sky') + 'skaya'
        elif nation == 'Poland':
            if l_name.endswith('ki'):
                l_name = l_name.removesuffix('ki') + 'ka'
            elif l_name.endswith('y'):
                l_name = l_name.removesuffix('y') + 'a'
        elif nation == 'Greece':
            if l_name.endswith('os'):
                l_name = l_name.removesuffix('os') + 'ou'
            elif l_name.endswith('is') or l_name.endswith('as'):
                l_name = l_name.removesuffix('s')

    if nation in FAMILY_NAME_FIRST:
        return l_name + ' ' + f_name
    return f_name + ' ' + l_name

# ==========================================
# HERO APPENDICES (titles and adjectives, full forms)
# 'Man','Woman','Boy','Girl','Guy' come after the nickname; the rest come before.
# ==========================================
APPENDICES_M_BEFORE = 'Mister,Doctor,Captain,King,Master,Commander,General,Colonel,Major,Baron,Duke,Count,Lord,Sir,Knight,Agent,Chief,Warden,Super,Incredible,Brave,Bold,Agile,Mighty,Great,Grand,Ultra,Mega,Supreme,Fantastic,Dynamic,Fearless,Noble,Radiant,Invincible,Peerless,Valiant'.split(',')
APPENDICES_W_BEFORE = 'Miss,Madame,Mistress,Doctor,Captain,Queen,Duchess,Countess,Lady,Baroness,Agent,Chief,Super,Incredible,Brave,Bold,Agile,Mighty,Great,Grand,Ultra,Supreme,Fantastic,Dynamic,Fearless,Noble,Radiant,Invincible,Peerless,Valiant'.split(',')
SUFFIX_APPENDICES_M = 'Man,Boy,Guy'.split(',')
SUFFIX_APPENDICES_W = 'Woman,Girl'.split(',')

VILLAIN_APPENDICES_M_BEFORE = 'Mister,Doctor,Professor,Captain,King,Master,Commander,General,Colonel,Baron,Duke,Count,Lord,Sir,Chief,Dark,Ebon,Crimson,Iron,Steel,Dread,Sinister,Grim,Mad,Cruel,Ruthless,Twisted,Malicious,Macabre,Ominous'.split(',')
VILLAIN_APPENDICES_W_BEFORE = 'Miss,Madame,Mistress,Doctor,Professor,Captain,Queen,Duchess,Countess,Lady,Baroness,Chief,Dark,Ebon,Crimson,Iron,Dread,Sinister,Grim,Mad,Cruel,Ruthless,Twisted,Malicious,Macabre,Ominous'.split(',')

def generate_superhero_name(gender: Literal['male', 'female'], power: str, rand: random.Random):
    before = APPENDICES_M_BEFORE if gender == 'male' else APPENDICES_W_BEFORE
    suffix = SUFFIX_APPENDICES_M if gender == 'male' else SUFFIX_APPENDICES_W
    nickname = rand.choice(FACULTY_NICKNAMES[power])
    if rand.random() < 0.3:
        return f'{nickname} {rand.choice(suffix)}'
    return f'{rand.choice(before)} {nickname}'

def generate_supervillain_name(rand: random.Random):
    gender = rand.choice(['male', 'male', 'male', 'female'])
    nickname = rand.choice(NICKNAMES_VILLAIN)
    before = VILLAIN_APPENDICES_M_BEFORE if gender == 'male' else VILLAIN_APPENDICES_W_BEFORE
    suffix = SUFFIX_APPENDICES_M if gender == 'male' else SUFFIX_APPENDICES_W
    if rand.random() < 0.3:
        villain = f'{nickname} {rand.choice(suffix)}'
    else:
        villain = f'{rand.choice(before)} {nickname}'
    machine = rand.choice(MACHINES)
    machine_desc = rand.choice(NICKNAMES_MACHINE)
    return villain, f' and {"his" if gender == "male" else "her"} {machine_desc} {machine}'

# ==========================================
# SUPERPOWER NICKNAMES (~50 each)
# ==========================================
NICKNAMES_STRENGTH = 'Muscle,Powerhouse,Strongman,Brawn,Brute,Titan,Goliath,Colossus,Behemoth,Leviathan,Monolith,Boulder,Crag,Anvil,Forge,Hammer,Maul,Bull,Ox,Mastiff,Bulldog,Greatdane,Gorilla,Silverback,Orangutan,Chimpanzee,Elephant,Mammoth,Mastodon,Rhinoceros,Rhino,Hippo,Bison,Buffalo,Moose,Elk,Wapiti,Stallion,Draft,Bear,Grizzly,Kodiak,Wolverine,Dinosaur,Tyrannosaurus,Triceratops,Stegosaurus,Diplodocus,Argentinosaurus,Titanosaurus'.split(',')
NICKNAMES_SPEED = 'Dash,Rush,Blitz,Haste,Speed,Swift,Quick,Fleet,Speedy,Velocity,Turbo,Nitro,Sprint,Dart,Flash,Zip,Zoom,Bolt,Blink,Charge,Courier,Messenger,Cheetah,Gazelle,Antelope,Springbok,Impala,Jackrabbit,Hare,Pronghorn,Whippet,Greyhound,Saluki,Ostrich,Emu,Swift,Swallow,Peregrine,Marlin,Sailfish,Tuna,Swordfish,Wahoo,Barracuda,Mako,Shortfin,Roadrunner,Dragonfly,Spinetail,Dashhound,Scout'.split(',')
NICKNAMES_FLIGHT = 'Wind,Breeze,Gust,Zephyr,Monsoon,Storm,Tempest,Nimbus,Vortex,Cyclone,Tornado,Fog,Mist,Cloud,Whirlwind,Sky,Soar,Glide,Hover,Drift,Ascend,Wing,Albatross,Eagle,Falcon,Hawk,Osprey,Kestrel,Buzzard,Goshawk,Harrier,Kite,Vulture,Condor,Heron,Crane,Stork,Pelican,Cormorant,Gannet,Frigate,Tern,Swan,Goose,Swallow,Swift,Nightjar,Swiftlet,Seagull,Raven,Magpie'.split(',')
NICKNAMES_FIRE = 'Volcano,Ember,Flame,Blaze,Spark,Cinder,Ash,Soot,Torch,Heat,Magma,Lava,Crater,Plume,Fissure,Eruption,Glow,Char,Pyroclast,Obsidian,Basalt,Kiln,Wildfire,Panther,Lion,Tiger,Jaguar,Leopard,Cheetah,Ocelot,Serval,Lynx,Bobcat,Cougar,Meerkat,Fennec,Caracal,Okapi,Orca,Python,Cobra,Viper,Mamba,Gecko,Iguana,Chameleon,Tortoise,Camel,Wildebeest,Scorpion,Wasp,Firefly,Macaw,Monitor'.split(',')
NICKNAMES_SLASH = 'Warrior,Gladiator,Samurai,Paladin,Chevalier,Musketeer,Swordsman,Blade,Edge,Cleaver,Saber,Katana,Scimitar,Scythe,Reaper,Glaive,Pike,Lance,Spear,Trident,Halberd,Bardiche,Polearm,Rapier,Falchion,Khopesh,Claymore,Broadsword,Longsword,Shotel,Wakizashi,Kris,Flail,Mace,Axe,Tomahawk,Warhammer,Chakram,Shuriken,Kukri,Machete,Bolo,Espada,Cutlass,Sickle,Dagger,Poniard,Stiletto,Champion,Vanguard,Juggernaut,Berserker'.split(',')
NICKNAMES_ELECTRIC = 'Volt,Watt,Ampere,Ohm,Current,Charge,Spark,Flash,Circuit,Wire,Coil,Electron,Proton,Ion,Plasma,Static,Zap,Tesla,Dynamo,Generator,Transformer,Capacitor,Inductor,Grid,Relay,Fuse,Powerline,Eel,Stingray,Ray,Catfish,Platypus,Echidna,Honeybee,Jaguar,Tapir,Toucan,Macaw,Anaconda,Caiman,Capybara,Piranha,Arapaima,Tamarin,Sloth,Anteater,Ocelot,Harpy,Manedwolf,Rhea'.split(',')
NICKNAMES_LASER = 'Retina,Iris,Pupil,Lens,Cornea,Sclera,Optic,Beam,Focus,Glare,Glimmer,Glint,Shine,Sparkle,Gleam,Luster,Prism,Spectrum,Photon,Refraction,Reflection,Coherence,Neon,Fovea,Vigil,Falcon,Hawk,Eagle,Kestrel,Osprey,Goshawk,Peregrine,Owl,Eagleowl,Harrier,Mantis,Kingfisher,Lynx,Bobcat,Caracal,Cat,Tarsier,Chameleon,Dragonfly,Octopus,Squid,Cuttlefish,Marlin,Manta,Blackbird'.split(',')
NICKNAMES_TECH = 'Robot,Automaton,Cyborg,Mech,Servo,Actuator,Sensor,Transistor,Diode,Microchip,Processor,Mainframe,Servosystem,Algorithm,Protocol,Gateway,Router,Inverter,Converter,Transformer,Chopper,Regulator,Stabilizer,Feedback,Blaster,Railgun,Turret,Cannon,Launcher,Gauss,Rocket,Missile,Grenade,Torpedo,Shotgun,Plasma,Quantum,Photon,Neutron,Pulse,Cybertron,Mechatron,Voltar,Sparkwire,Omnibot,Dreadnought,Ironclad,Sentinel,Turbojet,Circuit'.split(',')
NICKNAMES_SOLAR = 'Sun,Sunlight,Sol,Helio,Corona,Solaris,Radiance,Bright,Aurora,Sunburst,Sunbeam,Sunray,Solstice,Equinox,Daybreak,Dawn,Daystar,Heliacal,Sirius,Canopus,Alpha Centauri,Arcturus,Vega,Capella,Rigel,Procyon,Achernar,Betelgeuse,Hadar,Altair,Acrux,Aldebaran,Antares,Spica,Pollux,Fomalhaut,Deneb,Mimosa,Regulus,Adhara,Shaula,Gacrux,Bellatrix,Elnath,Peacock,Polaris,Algol,Castor'.split(',')
NICKNAMES_WEATHER = 'Rain,Storm,Tempest,Nimbus,Cyclone,Tornado,Hurricane,Monsoon,Thunder,Lightning,Thunderbolt,Cloud,Mist,Fog,Drizzle,Downpour,Dew,Frost,Blizzard,Wind,Gale,Gust,Breeze,Drought,Heatwave,Flood,Oak,Birch,Cedar,Pine,Fir,Willow,Maple,Aspen,Elm,Redwood,Sequoia,Spruce,Walnut,Ash,Chestnut,Rowan,Acacia,Eucalyptus,Palm,Olive,Cypress,Yew,Juniper,Banyan,Mangrove,Baobab'.split(',')
NICKNAMES_NATURE = 'Forest,Jungle,Wild,Flora,Fauna,Biome,Ecosystem,Greenwood,Grove,Meander,Glade,Thicket,Canopy,Blossom,Thistle,Fern,Moss,Ivy,Foliage,Verdant,Dodo,Kakapo,Wollemia,Ginkgo,Cycad,Bristlecone,Rose,Tulip,Lily,Peony,Lotus,Vaquita,Amur,Sumatran,Pangolin,Thylacine,Quagga,Moa,Pigeon,Rhinoceros,Gibbon,Bamboo,Orchid,Primrose,Marigold,Sunflower,Wildflower,Greensward,Chaparral,Savanna,Prairie,Tundra,Evergreen'.split(',')
NICKNAMES_SHIELD = 'Shield,Aegis,Barricade,Bulwark,Fortress,Castle,Citadel,Keep,Rampart,Bastion,Redoubt,Palisade,Stockade,Wall,Buckler,Targe,Cuirass,Armor,Breastplate,Plackart,Gambeson,Hauberk,Brigandine,Lorica,Mail,Hoplon,Tower,Bunker,Pillbox,Armadillo,Chelonian,Tortoise,Turtle,Alligator,Ankylosaurus,Glyptodont,Pangolin,Hedgehog,Porcupine,Crocodile,Beetle,Snail,Mollusk,Clam,Oyster,Nautilus,Conch,Walnut,Hazelnut,Chestnut,Acorn,Pecan,Cashew,Almond'.split(',')
NICKNAMES_ELASTIC = 'Elastic,Rubber,Gum,Bungee,Trampoline,Spring,Coil,Zigzag,Contortion,Acrobat,Gymnast,Jester,Tumbler,Pogo,Slinky,Yoyo,Jumping Jack,Stretch,Lithe,Limber,Supple,Sling,Bend,Snap,Twist,Flex,Bounce,Squirrel,Monkey,Gibbon,Treefrog,Gecko,Bushbaby,Galago,Tarsier,Chameleon,Octopus,Snake,Eel,Kangaroo,Wallaby,Springhare,Jerboa,Grasshopper,Flea,Spider,Nimble,Whippet'.split(',')
NICKNAMES_ENERGY = 'Energy,Power,Vigor,Vitality,Kinetic,Thermal,Atomic,Radiance,Luminosity,Geyser,Caloric,Metabolism,Biomass,Stamina,Endurance,Adrenaline,Dopamine,Caffeine,Taurine,Glucose,Mate,Matcha,Yerba,Coffee,Cocoa,Cacao,Tea,Espresso,Latte,Banana,Apple,Date,Blueberry,Goji,Avocado,Pomegranate,Quinoa,Oat,Beetroot,Kale,Spinach,Fig,Grape,Cherry,Mango,Orange,Peach,Plum,Pear,Cardio'.split(',')
NICKNAMES_WATER = 'Rain,River,Ocean,Stream,Lake,Waterfall,Wave,Current,Tide,Fountain,Spring,Mist,Fog,Dew,Droplet,Splash,Drizzle,Flood,Aquifer,Seawater,Puddle,Anemone,Barracuda,Beluga,Coral,Crayfish,Dolphin,Eel,Flounder,Grouper,Guppy,Haddock,Halibut,Hammerhead,Herring,Jellyfish,Koi,Krill,Lobster,Mahi,Manatee,Marlin,Manta,Minnow,Narwhal,Octopus,Oyster,Orca,Otter,Piranha,Porpoise,Ray,Salmon,Sardine,Seahorse,Seal,Seaweed,Shark,Sponge'.split(',')
NICKNAMES_ICE = 'Frost,Glacier,Blizzard,Chill,Rime,Snow,Tundra,Flurry,Drift,Slush,Polar,Gel,Crystal,Freeze,Mantle,Iceberg,Hoarfrost,Winter,Flake,Arctic,Siberian,Glacial,Nival,Walrus,Seal,Harp,Weddell,Crabeater,Ross,Monk,Narwhal,Beluga,Muskox,Caribou,Reindeer,Lemming,Snowshoe,Hare,Ptarmigan,Petrel,Skua,Guillemot,Gull,Tern,Puffin,Penguin,Adelie,Emperor,Chinstrap,Snowyowl,Gyrfalcon'.split(',')
NICKNAMES_ACID = 'Acid,Corrosive,Caustic,Venom,Poison,Toxin,Cyanide,Arsenic,Hemlock,Belladonna,Wolfsbane,Foxglove,Oleander,Nightshade,Monkshood,Aconite,Strychnine,Ricin,Vitriol,Viper,Cobra,Blackmamba,Taipan,Bushmaster,Coral,Rattlesnake,Adder,Krait,Pitohui,Scorpion,Tarantula,Atrax,Funnelweb,Recluse,Black Widow,Cone,Stonefish,Conefish,Jellyfish,Boxjelly,Pufferfish,Blowfish,Fugu,Spider,Frog,Toad,Newt,Stingray,Castorbean,Rosarypea,Milkweed,Digitalis,Salamander'.split(',')
NICKNAMES_MIND = 'Mind,Psyche,Focus,Thought,Cogito,Logos,Nous,Ponder,Contemplation,Reason,Rational,Insight,Wisdom,Sagacity,Introspect,Reflect,Enigma,Puzzle,Riddle,Sphinx,Mystic,Sage,Philosopher,Academic,Scholar,Savant,Genius,Prodigy,Abstract,Paradox,Dilemma,Dolphin,Orca,Elephant,Chimpanzee,Octopus,Crow,Raven,Macaw,Parrot,Cuttlefish,Raccoon,Pig,Shark,Aye-aye,Capuchin,Jay,Magpie,Coyote,Fox'.split(',')
NICKNAMES_GRAVITY = 'Gravity,Friction,Tension,Thrust,Drag,Lift,Torque,Impulse,Momentum,Inertia,Pressure,Stress,Strain,Weight,Force,Accelerator,Decelerator,Jolt,Velocity,Oscillator,Vibration,Wave,Field,Reflect,Scatter,Damping,Resistor,Shear,Compress,Expand,Contract,Traction,Equilibrium,Planet,Star,Galaxy,Comet,Asteroid,Nebula,Orbit,Cosmos,Eclipse,Pulsar,Vacuum,Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune,Ceres,Pluto,Eris,Haumea,Makemake,Gonggong,Ganymede,Titan,Callisto,Io,Moon,Europa,Triton,Titania,Rhea,Oberon,Iapetus'.split(',')
NICKNAMES_TIME = 'Time,Clock,Chronos,Hourglass,Pendulum,Metronome,Moment,Instant,Epoch,Era,Season,Tide,Cycle,Rhythm,Tempo,Pulse,Kairos,Legacy,Dragon,Wyvern,Griffin,Phoenix,Unicorn,Pegasus,Chimera,Manticore,Basilisk,Hydra,Cerberus,Kraken,Minotaur,Centaur,Simurgh,Qilin,Fenghuang,Ifrit,Roc,Garuda,Yeti,Pixiu,Kitsune,Tanuki,Ouroboros,Quetzalcoatl,Winged,Feathered,Serpent,Thunderbird'.split(',')
NICKNAMES_CYBER = 'Cyber,Cipher,Bit,Byte,Kilobyte,Kernel,Syscall,Firewall,Backdoor,Trojan,Virus,Worm,Zombie,Bot,Rootkit,Keylogger,Ransomware,Phish,Spoof,Sniffer,Proxy,Tunnel,Packet,Latency,Hex,Binary,Neural,Net,Bug,Crash,Glitch,Script,Compiler,Debugger,Recursion,Mutex,Cache,Stack,Heap,Bruteforce,Malware,Exploit,Payload,Botnet,Digit,Node,Mesh,Syntax,Hacker,Netrunner,Codepoet'.split(',')
NICKNAMES_SONIC = 'Sonic,Sound,Echo,Resonance,Reverb,Vibration,Frequency,Pitch,Tone,Timbre,Chord,Rhythm,Beat,Tempo,Melody,Harmony,Aria,Chorus,Crescendo,Decibel,Forte,Treble,Bass,Alto,Tenor,Soprano,Baritone,Sonata,Symphony,Serenade,Anthem,Overture,Riff,Cymbal,Gong,Trumpet,Horn,Whistle,Hum,Buzz,Ring,Clang,Chime,Bat,Moth,Owl,Wolf,Fox,Dolphin,Sealion,Elephant,Rat,Whale,Shrew,Tenrec,Aye-aye,Swiftlet,Oilbird,Dormouse'.split(',')

FACULTY_NICKNAMES = {
    'Strength': NICKNAMES_STRENGTH,
    'Speed': NICKNAMES_SPEED,
    'Flight': NICKNAMES_FLIGHT,
    'Fire': NICKNAMES_FIRE,
    'Slash': NICKNAMES_SLASH,
    'Electric': NICKNAMES_ELECTRIC,
    'Laser': NICKNAMES_LASER,
    'Tech': NICKNAMES_TECH,
    'Solar': NICKNAMES_SOLAR,
    'Weather': NICKNAMES_WEATHER,
    'Nature': NICKNAMES_NATURE,
    'Shield': NICKNAMES_SHIELD,
    'Elastic': NICKNAMES_ELASTIC,
    'Energy': NICKNAMES_ENERGY,
    'Water': NICKNAMES_WATER,
    'Ice': NICKNAMES_ICE,
    'Acid': NICKNAMES_ACID,
    'Mind': NICKNAMES_MIND,
    'Gravity': NICKNAMES_GRAVITY,
    'Time': NICKNAMES_TIME,
    'Cyber': NICKNAMES_CYBER,
    'Sonic': NICKNAMES_SONIC,
}

# ==========================================
# VILLAIN & MACHINE NICKNAMES (~100 each)
# ==========================================
NICKNAMES_VILLAIN = 'Arson,Assault,Battery,Blackmail,Burglar,Carnage,Coercion,Conspiracy,Contraband,Corrupt,Embezzler,Extort,Fraud,Forger,Graft,Hijack,Homicide,Harass,Kidnap,Larceny,Mugger,Murder,Perjury,Phisher,Pirate,Poacher,Racketeer,Robber,Sabotage,Smuggler,Thief,Trafficker,Vandal,Violent,Aggressor,Anarchist,Arsonist,Assailant,Accomplice,Alien,Ambusher,Assassin,Abductor,Animosity,Abuser,Attempt,Bankrupt,Break,Confiscator,Convictor,Crime,Cybercrime,Deceptor,Deporter,Destructor,Disorder,Extortionist,Falsifier,Fugitive,Grafter,Hostage,Indict,Intimidator,Invader,Inquest,Kidnapper,Lifter,Looter,Lynch,Manslaughter,Menace,Maniac,Mischief,Motive,Negligence,Offense,Perpetrator,Poisoner,Propaganda,Recidivism,Restitution,Swindle,Thug,Transgressor,Trespasser,Trial,Vagrant,Verdict,Warrant,Witness,Wrongdoer,Tyrant,Doom,Subjugator,Oppressor,Oblivion,Dissent,Rebel,Insurrect,Mutant,Contagion,Contaminator,Famine,Fervor,Extremist,Purge,Brainwasher,Defector,Betrayal,Treason,Traitor,Crackdown'.split(',')
NICKNAMES_MACHINE = 'Saw,Blaster,Ripper,Shredder,Gouger,Scorcher,Frostbite,Splicer,Splitter,Vaporizer,Ionizer,Plasma,Noxious,Venomizer,Toxin,Scythe,Reaper,Slicer,Cutter,Guillotine,Skewer,Stabber,Spike,Harpoon,Trampler,Crusher,Grinder,Chopper,Driller,Borer,Puncher,Hammer,Mallet,Anvil,Mauler,Gnasher,Jawbreaker,Claw,Talons,Vortex,Cyclone,Tempest,Blackout,Shadow,Nullifier,Disruptor,Suppressor,Overload,Backfire,Igniter,Combustor,Flare,Ember,Kindler,Pyro,Furnace,Ragnarok,Obliterator,Annihilator,Terminator,Wrecker,Demolisher,Saboteur,Sunder,Shatter,Fracture,Sever,Cinder,Razor,Whiplash,Hurricane,Glacier,Thunderbolt,Lightning,Voltager,Magnetar,Railgun,Gauss,Ionstorm,Pulse,Shockwave,Thunder,Gravwell,Singularity,Blackhole,Comet,Meteor,Tremor,Earthshaker,Seismic,Crater,Quake,Tidalwave,Floodgate,Whirlwind,Spiral,Rift,Portal,Warp,Cannon,Charger,Emitter,Flayer,Glaive,Injector,Launcher,Necrobolt,Obelisk,Orbiter,Penetrator,Pulverizer,Rivetgun,Rocket,Sabot,Scanner,Stunner,Taloner,Thresher,Tracer,Vanguard,Vector,Warden,Warhead,Wavecaster,Abyssal,Arcblade,Astronail,Atomizer,Bioforge,Blastcoil,Bubblegun,Chaosbolt,Chronolance,Coldsnap,Deathray,Drone,Dynabolt,Electroshock,Entangler,Forcepike,Gravgun,Grievancer,Heatwisp,Holoblade,Ionic,Javelin,Kinetics,Killshot,Kraken,Lockbolt,Magnetizer,Monoblade,Mortarbite,Nullray,Pinpoint,Plagueshard,Quasarblade,Radar,Ricochet,Riftbolt,Scorch,Spear,Spinstorm,Starfire,Stasis,Stormcaster,Talon,Unmaker,Vacuumshot,Voidcaster,Voidblade,Zapper'.split(',')
MACHINES = 'Machine,Robot,Device,Suit,Army,Mobile,Team,Gang,Bot,Ray,Battalion,Engine,Cannon,Fleet,Swarm,Legion,Factory,Protocol,Program,Nexus'.split(',')

# ==========================================
# COURSE NAMES
# The +PWR course name list is different for each superpower.
# Some superpowers have their own names for other courses too.
# ==========================================
COURSE_NAMES = {
    'HP': 'First Aid,Emergency Medicine,Nutrition,Rehabilitation,Physiotherapy,Field Care,Resilience Training,Fortitude Practice'.split(','),
    'MP': 'Aerobics,Meditation,Breath Control,Mana Flow,Focus Drills,Energy Balance,Rhythm Gymnastics,Inner Calm'.split(','),
    'DMG': 'Martial Arts,Boxing,Striking,Combat Drills,Power Training,Close Combat,Iron Fist,Knuckle Work'.split(','),
    'PWR': 'Superpower Control,Power Manifestation,Ability Mastery,Power Flow,Potential Release,Inner Power,Ability Boost,Focus Fire'.split(','),
    'DEF': 'Iron Body,Toughness,Resilience,Fortitude,Grounding,Hardening,Brace Training,Unyielding Stance'.split(','),
    'AGL': 'Parkour,Agility Drills,Balance,Acrobatics,Dodge Training,Reflex Work,Mobility,Footwork'.split(','),
}

POWER_COURSE_NAMES = {
    'Strength': {
        'DMG': 'Weightlifting,Iron Pump,Squat Rack,Powerlifting,Deadlift,Brute Press,Muscle Build,Herculean Lift'.split(','),
        'PWR': 'Raw Power,Overdrive Muscle,Titanic Force,Peak Strength,Muscle Surge,Force Unleashed,Power Press,Primal Might'.split(','),
    },
    'Speed': {
        'AGL': 'Sprint Drills,Dash Practice,Velocity Runs,Quickstep,Blink Drills,Footspeed,Turbo Steps,Lightning Footwork'.split(','),
        'PWR': 'Velocity Surge,Turbo Boost,Quicksilver,Momentum,Acceleration,Hyperdrive,Speed Force,Afterburner'.split(','),
    },
    'Flight': {
        'DEF': 'Aerial Defense,Hover Shielding,Sky Balance,Wind Sailing,Glide Practice,Aerial Stance,Air Cushion,Altitude Control'.split(','),
        'PWR': 'Sky Power,Ascension,Air Superiority,Lift,Thrust,Glide Surge,Wing Power,Aerial Force'.split(','),
    },
    'Fire': {
        'PWR': 'Heat Surge,Inferno,Combustion,Pyro Force,Blaze Up,Overheat,Incinerate,Furnace'.split(','),
    },
    'Slash': {
        'DMG': 'Swordplay,Blade Work,Cleave Training,Edge Practice,Saber Drills,Slasher Course,Cutting Form,Fencing'.split(','),
        'PWR': 'Slash Force,Cleave Power,Edge Force,Fury Cut,Blade Surge,Rend,Sever,Pierce'.split(','),
    },
    'Electric': {
        'PWR': 'Volt Surge,Power Surge,Charge Up,Voltage Spike,Overload,Spark Force,Amperage,Wattage'.split(','),
    },
    'Laser': {
        'PWR': 'Beam Power,Focus,Laser Burn,Optical Overcharge,Intensity,Coherence Boost,Ray Surge,Amplification'.split(','),
    },
    'Tech': {
        'HP': 'Armor Plating,Emergency Repair,Maintenance,Dampening,Reinforcement,Hardening Suite,Servo Care,Cooling Unit'.split(','),
        'MP': 'Buy Ammo,Power Cell,Battery Charge,Capacitor Fill,Fuel Intake,Software Patch,Reload,Overclock'.split(','),
        'PWR': 'Power Core,Overclock,System Surge,Firmware Flash,Cybernetic Boost,CPU Spike,Energy Charge,Logic Boost'.split(','),
    },
    'Solar': {
        'PWR': 'Solar Overcharge,Sunburst,Radiance,Solar Flare,Heliacal Force,Sun Power,Photon Surge,Corona Charge'.split(','),
    },
    'Weather': {
        'PWR': 'Storm Surge,Climatic Force,Weather Whip,Tempest,Front Advance,Pressure Drop,Forecast,Atmospheric Push'.split(','),
    },
    'Nature': {
        'PWR': 'Growth,Bloom,Wild Surge,Photosynthesis,Nourish,Root Force,Flourish,Green Power'.split(','),
    },
    'Shield': {
        'PWR': 'Bulwark,Bastion Force,Barrier,Aegis Power,Shelter,Protection,Fortify,Unyielding Surge'.split(','),
    },
    'Elastic': {
        'PWR': 'Stretch,Bounce,Snapback,Elastic Surge,Spring Force,Flex,Rebound,Bungee Power'.split(','),
    },
    'Energy': {
        'PWR': 'Energy Surge,Vitality,Stamina Boost,Metabolic Fire,Endurance,Kinetic Charge,Essence,Spark of Life'.split(','),
    },
    'Water': {
        'PWR': 'Tidal Force,Current,Flood,Pressure Surge,Crushing Depth,Hydro Force,Cascade,Wave Power'.split(','),
    },
    'Ice': {
        'PWR': 'Frost Surge,Deep Freeze,Cryo,Glacial Force,Chill,Permafrost,Icicle Surge,Cold Snap'.split(','),
    },
    'Acid': {
        'PWR': 'Caustic Surge,Dissolve,Corrosion,Meltdown,Acid Burn,Decompose,Erode,Caustic Force'.split(','),
    },
    'Mind': {
        'PWR': 'Mind Force,Psy Surge,Telepathy,Clarity,Mindwave,Suggestion,Empathy,Thought Surge'.split(','),
    },
    'Gravity': {
        'PWR': 'Gravity Surge,Mass,Pull,Crush,Distortion,Field Force,Attraction,Graviton'.split(','),
    },
    'Time': {
        'PWR': 'Chrono Boost,Temporal Surge,Haste,Rewind,Momentum,Flow,Chronology,Instant'.split(','),
    },
    'Cyber': {
        'PWR': 'Cyber Surge,Data Surge,Mind Hack,Digital Force,Bit Burst,Net Power,Plug,Node'.split(','),
    },
    'Sonic': {
        'PWR': 'Sonic Surge,Sound Wave,Crescendo Boost,Decibel Bomb,Bass Force,Echo Blast,Resonance,Vibra Course'.split(','),
    },
}

# ==========================================
# CITIES
# ==========================================
CITIES = {
    'USA': 'New York,Los Angeles,Chicago,Houston,Phoenix,Philadelphia,San Antonio,San Diego,Dallas,Fort Worth,Jacksonville,Austin,San Jose,Charlotte,Columbus,Indianapolis,San Francisco,Seattle,Denver,Nashville,Oklahoma City,Washington,El Paso,Las Vegas,Boston,Detroit,Louisville,Portland,Memphis,Baltimore,Milwaukee,Albuquerque,Fresno,Tucson,Sacramento,Atlanta,Kansas City,Mesa,Raleigh,Colorado Springs,Miami,Omaha,Virginia Beach,Long Beach,Oakland,Minneapolis'.split(','),
    'UK': 'London,Manchester,Birmingham,Leeds,Glasgow,Liverpool,Portsmouth,Newcastle upon Tyne,Nottingham,Sheffield,Bristol,Belfast,Leicester,Edinburgh,Brighton and Hove,Bournemouth,Cardiff,Middlesbrough,Stoke-on-Trent,Coventry,Sunderland,Birkenhead,Reading,Kingston upon Hull,Preston,Newport,Swansea,Southend-on-Sea,Derby,Plymouth,Luton,Farnborough,Gillingham,Blackpool,Barnsley,Northampton,Norwich,Aberdeen,Swindon,Crawley,Ipswich'.split(','),
    'China': "Shanghai,Beijing,Shenzhen,Guangzhou,Chengdu,Tianjin,Wuhan,Dongguan,Chongqing,Xi'an,Hangzhou,Foshan,Nanjing,Shenyang,Zhengzhou,Qingdao,Suzhou,Jinan,Changsha,Kunming,Harbin,Shijiazhuang,Hefei,Dalian,Xiamen,Nanning,Changchun,Taiyuan,Guiyang,Wuxi,Ürümqi,Zhongshan,Shantou,Ningbo,Fuzhou,Nanchang,Changzhou,Lanzhou,Nantong,Huizhou,Xuzhou,Zibo,Linyi,Wenzhou,Tangshan,Hohhot,Haikou".split(','),
    'Russia': "Moscow,Saint Petersburg,Novosibirsk,Yekaterinburg,Kazan,Nizhny Novgorod,Chelyabinsk,Krasnoyarsk,Samara,Ufa,Rostov-on-Don,Omsk,Krasnodar,Voronezh,Perm,Volgograd,Saratov,Tyumen,Tolyatti,Barnaul,Izhevsk,Makhachkala,Khabarovsk,Ulyanovsk,Irkutsk,Vladivostok,Yaroslavl,Kemerovo,Tomsk,Naberezhnye Chelny,Sevastopol,Stavropol,Orenburg,Novokuznetsk,Ryazan,Balashikha,Penza,Cheboksary,Lipetsk,Kaliningrad,Astrakhan,Tula,Kirov,Sochi,Kursk,Ulan-Ude,Tver".split(','),
    'India': 'Mumbai,Delhi,Bengaluru,Hyderabad,Chennai,Ahmedabad,Kolkata,Surat,Pune,Jaipur,Lucknow,Kanpur,Nagpur,Indore,Thane,Bhopal,Visakhapatnam,Pimpri-Chinchwad,Patna,Vadodara,Ghaziabad,Ludhiana,Agra,Nashik,Faridabad,Meerut,Rajkot,Kalyan-Dombivli,Vasai-Virar,Varanasi,Srinagar,Chhatrapati Sambhajinagar,Dhanbad,Amritsar,Navi Mumbai,Prayagraj,Howrah,Ranchi,Jabalpur,Gwalior,Coimbatore,Vijayawada,Jodhpur'.split(','),
    'Germany': "Berlin,Hamburg,Munich,Cologne,Frankfurt am Main,Stuttgart,Düsseldorf,Leipzig,Dortmund,Essen,Bremen,Dresden,Hanover,Nuremberg,Duisburg,Bochum,Wuppertal,Bielefeld,Bonn,Münster,Mannheim,Karlsruhe,Augsburg,Wiesbaden,Mönchengladbach,Gelsenkirchen,Aachen,Braunschweig,Kiel,Chemnitz,Halle,Magdeburg,Freiburg im Breisgau,Krefeld,Mainz,Lübeck,Erfurt,Oberhausen,Rostock,Kassel,Hagen,Potsdam,Saarbrücken".split(','),
    'France': "Paris,Marseille,Lyon,Toulouse,Nice,Nantes,Montpellier,Strasbourg,Bordeaux,Lille,Rennes,Toulon,Reims,Saint-Étienne,Le Havre,Villeurbanne,Dijon,Angers,Grenoble,Saint-Denis,Nîmes,Aix-en-Provence,Clermont-Ferrand,Le Mans,Brest,Tours,Amiens,Annecy,Limoges,Metz,Perpignan,Boulogne-Billancourt,Besançon,Rouen,Orléans,Montreuil,Caen,Mulhouse,Nancy,Tourcoing,Roubaix".split(','),
    'Canada': "Toronto,Montreal,Calgary,Ottawa,Edmonton,Winnipeg,Mississauga,Vancouver,Brampton,Hamilton,Surrey,Quebec City,Halifax,Laval,London,Markham,Vaughan,Gatineau,Saskatoon,Kitchener,Longueuil,Burnaby,Windsor,Regina,Oakville,Richmond,Richmond Hill,Burlington,Oshawa,Sherbrooke,Greater Sudbury,Abbotsford,Lévis,Coquitlam,Barrie,Saguenay,Kelowna,Guelph,Trois-Rivières,Whitby".split(','),
    'Spain': "Madrid,Barcelona,Valencia,Zaragoza,Seville,Málaga,Murcia,Palma,Las Palmas de Gran Canaria,Alicante,Bilbao,Córdoba,Valladolid,Vigo,L'Hospitalet de Llobregat,Gijón,Vitoria-Gasteiz,A Coruña,Elche,Granada,Terrassa,Badalona,Sabadell,Oviedo,Cartagena,Jerez de la Frontera,Móstoles,Santa Cruz de Tenerife,Pamplona,Almería,Alcalá de Henares,Leganés,Getafe,Fuenlabrada,Donostia".split(','),
    'Italy': 'Rome,Milan,Naples,Turin,Palermo,Genoa,Bologna,Florence,Bari,Catania,Verona,Venice,Messina,Padua,Brescia,Parma,Trieste,Prato,Taranto,Modena,Reggio Emilia,Reggio Calabria,Perugia,Ravenna,Livorno,Rimini,Cagliari,Foggia,Ferrara,Latina,Salerno,Giugliano in Campania,Monza,Bergamo,Sassari,Trento,Pescara,Forlì,Syracuse'.split(','),
    'Japan': 'Tokyo,Yokohama,Osaka,Nagoya,Sapporo,Fukuoka,Kawasaki,Kobe,Kyoto,Saitama,Hiroshima,Sendai,Chiba,Kitakyushu,Setagaya,Sakai,Niigata,Hamamatsu,Nerima,Kumamoto,Sagamihara,Okayama,Ōta,Shizuoka,Edogawa,Adachi,Kagoshima,Funabashi,Hachiōji,Kawaguchi,Himeji,Suginami,Itabashi,Matsuyama,Higashiōsaka,Utsunomiya,Matsudo,Mito'.split(','),
    'Mexico': "Mexico City,Tijuana,Ecatepec,León,Puebla,Ciudad Juárez,Guadalajara,Monterrey,Nezahualcóyotl,Zapopan,Chihuahua,Mérida,Naucalpan,Cancún,Saltillo,Aguascalientes,Hermosillo,Mexicali,San Luis Potosí,Culiacán,Querétaro,Morelia,Chimalhuacán,Reynosa,Torreón,Tlalnepantla".split(','),
    'Brazil': 'São Paulo,Rio de Janeiro,Brasília,Fortaleza,Salvador,Belo Horizonte,Manaus,Curitiba,Recife,Goiânia,Belém,Porto Alegre,Guarulhos,Campinas,São Luís,Maceió,Campo Grande,São Gonçalo,Teresina,João Pessoa,Duque de Caxias,Nova Iguaçu,São Bernardo do Campo,Natal,Santo André,Sorocaba,Uberlândia,Osasco,Ribeirão Preto,São José dos Campos,Cuiabá,Jaboatão dos Guararapes,Joinville,Feira de Santana,Contagem,Aracaju'.split(','),
    'Indonesia': 'Jakarta,Surabaya,Bekasi,Bandung,Medan,Depok,Tangerang,Palembang,Semarang,Makassar,South Tangerang,Batam,Bogor,Bandar Lampung,Pekanbaru,Padang,Samarinda,Malang,Tasikmalaya,Serang,Balikpapan,Banjarmasin,Pontianak,Denpasar,Jambi,Cimahi,Surakarta,Kupang,Manado,Cilegon'.split(','),
    'Argentina': 'Buenos Aires,Córdoba,Rosario,La Plata,Mar del Plata,San Miguel de Tucumán,Salta,Santa Fe de la Vera Cruz,Vicente López Partido,Corrientes,Pilar,Bahía Blanca,Resistencia,Posadas,San Salvador de Jujuy,Santiago del Estero,Paraná,Merlo,Neuquén'.split(','),
    'Nigeria': 'Lagos,Kano,Ibadan,Benin City,Port Harcourt,Aba,Jos,Ilorin,Abuja,Kaduna,Enugu,Zaria,Ogbomosho,Warri,Ikorodu,Maiduguri,Ife,Bauchi,Akure,Abeokuta,Uyo'.split(','),
    'Egypt': 'Cairo,Alexandria,Giza,Luxor,Banha,El Mansura,Al Zaqaziq,Asyut,El Mahalla El Kubra,Suhaj,Tanta,Port Said,Faiyum,Mit Ghamr,Damietta,Beni Suef,Al Ismailiya,Shibin Al-Kom,Damanhur,Suez'.split(','),
    'Philippines': 'Quezon City,Manila,Davao City,Caloocan,Taguig,Zamboanga City,Cebu City,Antipolo,Pasig,Dasmariñas,Cagayan de Oro,Valenzuela,General Santos,Parañaque,San Jose del Monte,Bacoor,Bacolod,Las Piñas,Biñan,Calamba'.split(','),
    'South Africa': 'Johannesburg,Cape Town,Durban,Pretoria,Klipgat,Tembisa,Evaton,Gqeberha,Masetjhaba View,Bloemfontein,Polokwane,Chief Albert Luthuli Park,Edendale,Kanyamazane,Madadeni,Kimberley,Paarl,Vanderbijlpark,Centurion'.split(','),
    'Iran': 'Tehran,Mashhad,Karaj,Isfahan,Ahwaz,Tabriz,Sarvestan,Kharameh,Shiraz,Kavar,Kermanshah,Qom,Urmia,Rasht,Zahedan,Kerman,Hamedan,Yazd,Ardabil'.split(','),
    'Australia': 'Sydney,Melbourne,Brisbane,Perth,Adelaide,Gold Coast,Canberra,Newcastle,Central Coast,Sunshine Coast,Wollongong,Hobart,Geelong,Townsville,Cairns,Darwin,Toowoomba,Ballarat,Bendigo,Maitland'.split(','),
    'Saudi Arabia': 'Riyadh,Jeddah,Dammam,Hofuf,Tabuk,Buraydah,Taif,Khamis Mushait,Jubail,Hail,Khobar,Najran,Abha,Yanbu,Al-Saih,Al-Mubarraz,Sabya,Arar,Unaizah'.split(','),
    'Turkey':    'Istanbul,Ankara,Bursa,İzmir,Konya,Gaziantep,Diyarbakır,Adana,Kayseri,Samsun,Antalya,Mersin,Esenyurt,Çankaya,Keçiören,Osmangazi,Eskişehir,Seyhan,Erzurum'.split(','),
    'South Korea': 'Seoul,Busan,Incheon,Daegu,Gwangju,Daejeon,Suwon,Ulsan,Tongjin,Goyang,Changwon,Hwasu-dong,Sŏngnam,Cheongju,Bucheon,Yanggok,Ch’ŏnan,Ansan,Kimhae'.split(','),
    'Poland':    'Warsaw,Kraków,Gdańsk,Wrocław,Łódź,Poznań,Szczecin,Bydgoszcz,Lublin,Białystok,Katowice,Gdynia,Zielona Góra,Częstochowa,Radom,Toruń,Rzeszów,Sosnowiec,Kielce,Gliwice'.split(','),
    'Greece':    'Athens,Thessaloníki,Piraeus,Týrnavos,Irákleio,Pátra,Peristéri,Lárisa,Acharnés,Kallithéa,Kalamariá,Glyfáda,Níkaia,Vólos,Ílion,Évosmos,Chalándri,Ilioúpoli,Keratsíni'.split(','),
    'Thailand':  'Bangkok,Chiang Mai,Nakhon Ratchasima,Khon Kaen,Hat Yai,Chon Buri,Phatthaya,Si Racha,Phitsanulok,Pak Kret,Mukdahan,Surat Thani,Udon Thani,Nakhon Pathom,Ban Bang Pu Mai,Ban Mangkon'.split(','),
}

OTHER_CITIES = [
    citycountry.split(',') for citycountry in
    'Lisbon,Portugal|Porto,Portugal|Amsterdam,Netherlands|The Hague,Netherlands|Brussels,Belgium|Dublin,Ireland|Luxembourg,Luxembourg|Prague,Czech Republic|Vienna,Austria|Zürich,Switzerland|Budapest,Hungary|Belgrade,Serbia|Bucharest,Romania|Sofia,Bulgaria|Kiev,Ukraine|Minsk,Belarus|Helsinki,Finland|Copenhagen,Denmark|Oslo,Norway|Stockholm,Sweden|Algiers,Algeria|Tripoli,Libya|Casablanca,Morocco|Kinshasa,D.R.Congo|Luanda,Angola|Khartoum,Sudan|Abidjan,Ivory Coast|Nairobi,Kenya|Accra,Ghana|Dar es Salaam,Tanzania|Bamako,Mali|Kampala,Uganda|Addis Ababa,Ethiopia|Dakar,Senegal|Douala,Cameroon|Baghdad,Iraq|Dubai,UAE|Amman,Jordan|Kuwait City,Kuwait|Doha,Qatar|Tashkent,Uzbekistan|Almaty,Kazakhstan|Tbilisi,Georgia|Yerevan,Armenia|Islamabad,Pakistan|Karachi,Pakistan|Dhaka,Bangladesh|Colombo,Sri Lanka|Hanoi,Vietnam|Kuala Lumpur,Malaysia|Pyongyang,North Korea|Phnom Penh,Cambodia|Yangon,Myanmar|Singapore,Singapore|Auckland,New Zealand|Wellington,New Zealand|Honolulu,US|Port Moresby,Papua New Guinea|Bogotá,Colombia|Medellín,Colombia|Lima,Peru|Santiago,Chile|Caracas,Venezuela|La Paz,Bolivia|Santo Domingo,Dominican Republic|Havana,Cuba|San José,Costa Rica|Montevideo,Uruguay|Kingston,Jamaica'.split('|')
]

def generate_country_and_city(rand: random.Random):
    nation = rand.choice(NATIONS + ['Other'])
    if nation == 'Other':
        city, nation = rand.choice(OTHER_CITIES)
    else:
        city = rand.choice(CITIES[nation])
    return nation, city
