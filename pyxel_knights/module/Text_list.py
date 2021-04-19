# -*- coding: utf-8 -*-
#Text_list.py

def text_get():
    txt = {
               "0":["HA","JI","ME","KA","RA"],
               "1":["YA","ME","RU"],
               "2":["SO","NO","KU","NI","DE","HA","TA","I","YO",
                          "U","WO","O","U","NO",],
               "3":["KE","SI","NN","TO","KA","NN","GA","E",","],
               "4":["HI","GA","KA","GE","RU","KO","TO","WO","O",
                          "U","NO","TI","KA","RA","NO"],
               "5":["KA","GE","RI","TO","KA","NN","GA","E","TE",
                          "I","TA"],
               "6":["SE","-","BU","SI","MA","SI","TA"],
               "7":["SE","-","BU","NI","SI","tu","PA","I","SI","MA","SI","TA"],
               "8":["RO","-","DO","SI","MA","SI","TA"],
               "9":["RO","-","DO","NI","SI","tu","PA","I","SI","MA","SI","TA"],
               "10":["TU","DU","KI","KA","RA"],
               "11":["HI","NO","KA","GE","RI","WO","MI","TO","ME","TA"],
               "12":["DA","I","SI","NN","KA","NN","HA","O","U","GO","RO","SI",
                     "NO",],
               "13":["KA","I","SI","WO","SE","NN","GE","NN","SI","TA"],
               "14":["O","U","WO","KO","RO","SI","TA","MO","NO","GA",],
               "15":["TU","GI","NO","O","U","TO","NA","RU",],
               "16":["NA","NO","KA","KA","NN","O","U","GA","I","KI","NO","BI",
                     "TA","RA",","],
               "17":["SO","NO","TI","KA","RA","HA","I","MA","DA","KE","NN",
                     "ZA","I","TO","SI",","],
               "18":["O","U","GO","RO","SI","HA","O","WA","RU",],
               "19":["GI","yo","KU","ZA","WO","NE","RA","U","HI","TO","RI",
                     "TO","SI","TE"],
               "20":["A","NA","TA","MO","KO","U","DO","U","WO","KA","I","SI",
                     "SI","TA",],
               "21":[".",".",".","KO","NO","GE","NN","SI","yo","U","GA",],
               "22":["NI","tu","SI","yo","KU",],
               "23":["TO","SI","TE","YO","NI","SI","RA","RE","RU","NO","HA",],
               "24":["MA","DA","SA","KI","NO","HA","NA","SI","DE",
                     "A","RU",".",".","."],
               "50":["BU","KI","WO","KE","NN","NI","MO","TI","KA","E","TA"],
               "51":["BU","KI","WO","TU","E","NI","MO","TI","KA","E","TA"],
               "52":["BU","KI","WO","O","NO","NI","MO","TI","KA","E","TA"],
               "53":["BU","KI","WO","E","RA","NN","DE","KU","DA","SA","I"],
               "100":["KA","GI","GA","A","I","TA",],
               "101":["KA","GI","GA","KA","KA","tu","TE","I","RU"],
               "102":["SI","KA","KE","GA","SA","DO","U","SI","TA"],
               "103":["DO","KU","RO","WO","HA","KA","I","SI","TA"],
               "104":["KU","DA","KA","RE","TA","DO","KU","RO",],
               "105":["NI","MU","KA","I","MA","SU",".",".","."],
               "105_0":["DO","KO","HE","I","KI","MA","SU","KA","?"],
               "105_1":["HE","NN","KI","yo","U","NO","MU","RA"],
               "105_2":["O","U","RI","TU","MA","DO","U","I","NN"],
               "105_3":["HI","GA","SI","NO","MI","YA","KO",],
               "105_4":["KE","I","SI","yo","U","NO","SA","I","DA","NN"],
               "105_6":["KI","yu","U","SI","GA","I","NO","MI","NA","TO"],
               "105_7":["SU","I","MO","NN","GA","A","I","TE","I","NA","I","!"],
               "106":["MA","MO","NO","NI","TI","yu","U","I"],
               "107":["KO","NO","SA","KI","MI","YA","KO","SE","I","MO","NN",],
               "108":["TA","TI","I","RI","KI","NN","SI",],
               "109":["KI","yu","U","SI","GA","I","TA","TI","I","RI","KI",
                      "NN","SI",],
               "110":["DA","I","NI","TI","KU","HU","NA","TU","KI","BA",],
               "111":["I","BA","RA","GA","MI","TI","WO","HU","SA","I","DE",
                      "I", "RU",],
               "112":["I","BA","RA","WO","YA","KI","HA","RA","tu","TA",],
               "113":["TA","I","MA","TU","WO","TE","NI","I","RE","TA"],
               "113_1":["BA","KU","YA","KU","WO","TE","NI","I","RE","TA"],
               "114":["NA","NI","MO","NA","I",],
               "115":["KA","GI","YO","NN","WO","TE","NI","I","RE","TA"],
               "116":["JI","yo","U","HO","U","SA","NN","WO","TE","NI","I",
                      "RE","TA"],
               "117":["SO","KO","MA","DE","DA",",","TA","BI","BI","TO","YO",],
               "118":["HE","I","KA","HA","SU","DE","NI","TA","BI","DA","TA",
                      "RE","TA"],
               "119":["I","KA","NI","KU","NI","NO","O","KI","TE","TO",
                      "HA","I","E",","],
               "120":["HE","I","KA","HA","KO","RO","SA","SE","NN"],
               "121":[".",".",".",".",".",".",".",".","."],
               "122":["KI","KO","U",",","SI","NN","DE","MO","RA","U",
                      "ZO","!",],
               "123":["KI","SI","DA","NN","TI","yo","U",],
               "124":["KI","TI","yo","U","HI","NN","WO","TE","NI","I","RE",
                      "TA"],
               "125":["O","U","GO","RO","SI","NO","TA","BI","BI","TO","KA"],
               "126":["GI","SI","KI","NI","SA","NN","KA","SI","TA",
                      "I","NA","RA"],
               "127":["O","U","KE","NO","ME","DA","RU","WO","MI","TU","KE",
                      "RU","KO","TO","JI","ya"],
               "128":["SE","I","ZE","I","TA","tu","SI","ya","DE","NA"],
               "129":["KO","NO","SA","KI","SI","NN","SE","I","TI","KU"],
               "130":["KO","NO","SA","KI","MU","RA","I","RI","GU","TI"],
               "131":["KE","I","SI","yo","U","NO","SA","I","DA","NN"],
               "132":["KA","GI","GO","WO","TE","NI","I","RE","TA",],
               "133":["KA","I","ZU","NO","TA","BA","WO","TE","NI","I","RE",
                      "TA"],
               "134":["I","MA","HA","DA","RE","MO","I","NA","I"],
               "135":["TO","BI","RA","WO","HI","RA","I","TA",],
               "136":["HA","KU","GI","NN","NO","KI","SI",],
               "137":["O","MO","tu","TA","YO","RI","SU","BA","YA","I","NA"],
               "138":["I","SO","I","DE","JI","NN","WO","SI","KE","!",],
               "139":["MU","KA","E","U","TU","ZO","!",],
               "140":["GA","NN","BA","NN","DE","HU","SA","GA","RE","TE","I",
                      "RU"],
               "141":["BA","KU","YA","KU","WO","TU","KA","tu","TA",],
               "200":[".",".",".",".",".",".",],
               "201":["KO","NN","NI","TI","HA",],
               "202":["SA","I","KI","NN","MA","MO","NO","GA","O","O",
                      "KU","NA","tu","TA",],
               "203":["O","U","SA","MA","WO","SI","BA","RA","KU","MI",
                      "TE","I","NA","I","NA",],
               "204":["MI","YA","KO","NO","TI","KA","NI","TU","U","RO",
                      "GA","A","RU","RA","SI","I",],
               "205":["KO","NN","NI","TI","HA",],
               "206":["KO","NN","NI","TI","HA",],
               "207":["MI","NA","TO","GA","HU","U","SA","SA","RE","TE",
                      "KO","MA","tu","TE","MA","SU",],
               "208":["KO","NN","NI","TI","HA",],
               "209":["KO","NN","NI","TI","HA",],
               "210":["MI","NA","TO","NO","E","I","HE","I","HA","I",
                      "NE","MU","RI","BA","KA","RI",],
               "211":["KO","NN","NI","TI","HA",],
               "212":["KO","NN","NI","TI","HA",],
               "300":["MI","YA","KO","NO","E","I","HE","I",],
               "301":["MI","YA","KO","NO","JI","yu","U","NI","NN"],
               "302":["RO","U","JI","NN"],
               "999":["KO","KO","MA","DE","SI","KA","DE","KI","TE","MA",
                      "SE","NN"],
               "999_1":["GO","ME","NN","NA","SA","I","!","!",],

    }
    return txt

def text_get_s():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["E","I","HE", "I", "NO", "ME", "MO", "GA"],
               "56":["KI"],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["O","U","KI", "yu", "U", "KA", "RA", "NO"],
               "59":["TE","GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SA","BI","TA", "O", "O", "KI", "NA", "KA"],
               "64":["GI"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],

    }
    return txt

def text_get_s2():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["GU","NN","RE", "I", "JI", "yo", "U"],
               "56":[],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["SO","NN","TI", "yo", "U", "NO", "ME", "MO"],
               "59":["GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["JI","NN","TI", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SI","NN","E", "I", "TA", "I", "NO",],
               "64":["WA", "NN", "SI", "yo" ,"U"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],

    }
    return txt

def text_get_s3():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["E","I","HE", "I", "NO", "ME", "MO", "GA"],
               "56":["KI"],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["O","U","KI", "yu", "U", "KA", "RA", "NO"],
               "59":["TE","GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SA","BI","TA", "O", "O", "KI", "NA", "KA"],
               "64":["GI"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],
    }
    return txt

def text_get_s4():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["E","I","HE", "I", "NO", "ME", "MO", "GA"],
               "56":["KI"],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["O","U","KI", "yu", "U", "KA", "RA", "NO"],
               "59":["TE","GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SA","BI","TA", "O", "O", "KI", "NA", "KA"],
               "64":["GI"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],
    }
    return txt

def text_get_s5():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["E","I","HE", "I", "NO", "ME", "MO", "GA"],
               "56":["KI"],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["O","U","KI", "yu", "U", "KA", "RA", "NO"],
               "59":["TE","GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SA","BI","TA", "O", "O", "KI", "NA", "KA"],
               "64":["GI"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],
    }
    return txt

def text_get_s6():
    txt = {

               "51":["I","RA","tu", "SI", "ya", "I", "MA", "SE"],
               "52":["SI","yo","U", "HI", "NN", "NO", "BA", "NN"],
               "53":["GO","U","WO", "E", "RA", "NN", "DE", "KU"],
               "54":["DA","SA","I"],
               "55":["E","I","HE", "I", "NO", "ME", "MO", "GA"],
               "56":["KI"],
               "57":["KA","I","MA","SU","KA","?"],
               "58":["O","U","KI", "yu", "U", "KA", "RA", "NO"],
               "59":["TE","GA","MI",],
               "60":["KA","I","MA","SU","KA","?"],
               "61":["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
               "62":["KA","I","MA","SU","KA","?"],
               "63":["SA","BI","TA", "O", "O", "KI", "NA", "KA"],
               "64":["GI"],
               "65":["KA","I","MA","SU","KA","?"],
               "66":["U","RI","KI", "RE", "DE", "SU",],
               "67":["O","KA","NE", "GA", "TA", "RI", "MA", "SE"],
               "68":["NN"],
               "69":["MA","I","DO", "A", "RI",],
    }
    return txt               
               
def item_get():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["JI","yo","U","HO","U","I","TI"],
               "2":["JI","yo","U","HO","U","NI"],
               "3":["KA","GI","I","TI"],
               "4":["KA","GI","NI"],
               "5":["TA","I","MA","TU",],
               "6":["KI","TI","yo","U","HI","NN","I","TI",],
               "7":["KA","GI","YO","NN"],
               "8":["JI","yo","U","HO","U","SA","NN",],

    }
    return txt

def item_get2():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["JI","yo","U","HO","U","YO","NN"],
               "2":["JI","yo","U","HO","U","GO",],
               "3":["KA","GI","RO","KU",],
               "4":["WA","NN","SI","yo","U"],
               "5":["BA","KU","YA","KU",],
               "6":["KI","TI","yo","U","HI","NN","NI"],
               "7":["KA","GI","NA","NA",],
               "8":["JI","yo","U","HO","U","RO","KU"],

    }
    return txt

def item_get3():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["SA","KU","SE","I","TI","yu","U"],
               "2":["SA","KU","SE","I","TI","yu","U"],
               "3":["SA","KU","SE","I","TI","yu","U"],
               "4":["SA","KU","SE","I","TI","yu","U"],
               "5":["SA","KU","SE","I","TI","yu","U"],
               "6":["SA","KU","SE","I","TI","yu","U"],
               "7":["SA","KU","SE","I","TI","yu","U"],
               "8":["SA","KU","SE","I","TI","yu","U"],

    }
    return txt

def item_get4():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["SA","KU","SE","I","TI","yu","U"],
               "2":["SA","KU","SE","I","TI","yu","U"],
               "3":["SA","KU","SE","I","TI","yu","U"],
               "4":["SA","KU","SE","I","TI","yu","U"],
               "5":["SA","KU","SE","I","TI","yu","U"],
               "6":["SA","KU","SE","I","TI","yu","U"],
               "7":["SA","KU","SE","I","TI","yu","U"],
               "8":["SA","KU","SE","I","TI","yu","U"],

    }
    return txt

def item_get5():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["KA","GI","GO",],
               "2":["SA","KU","SE","I","TI","yu","U"],
               "3":["SA","KU","SE","I","TI","yu","U"],
               "4":["SA","KU","SE","I","TI","yu","U"],
               "5":["KA","I","ZU","I","TI"],
               "6":["KA","I","ZU","NI",],
               "7":["KA","I","ZU","SA","NN"],
               "8":["KA","I","ZU","YO","NN"],

    }
    return txt

def item_get6():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["KA","GI","GO",],
               "2":["SA","KU","SE","I","TI","yu","U"],
               "3":["SA","KU","SE","I","TI","yu","U"],
               "4":["SA","KU","SE","I","TI","yu","U"],
               "5":["SA","KU","SE","I","TI","yu","U"],
               "6":["SA","KU","SE","I","TI","yu","U"],
               "7":["SA","KU","SE","I","TI","yu","U"],
               "8":["SA","KU","SE","I","TI","yu","U"],

    }
    return txt

def item_get_t():
    txt = {
               "1":[["E","I","HE","I","NO","ME","MO","GA","KI"],
                    ["O","U","KI","yu","U","NO","HI","JI","yo","U","TU"],
                    ["U","RO","NO","TE","NN","KE","NN","GA","A","tu","TA"],
                    ["DA","I","SI","yo","KO","NO","SO","U","TI","HA","SA"],
                    ["I","TE","NN","KE","NN","GA","HI","TU","YO","U"],],
               "2":[["O","U","KI","yu","U","KA","RA","NO","TE","GA","MI"],
                    ["MI","NA","TO","HA","SI","BA","RA","KU","HE","I","SA"],
                    ["SU","RU",],
                    ["KI","NN","KI","yu","U","JI","NI","HA","KI","yu","U"],
                    ["SI","GA","I","NO","DA","I","NI","TI","KU","WO","TU"],
                    ["KA","U","KO","TO",]],
               "3":[["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","HA","ZU","RE","NI","A","RU","DA"],
                    ["I","SI","yo","KO","NO","KA","GI",]],
               "4":[["SA","BI","TA", "O", "O", "KI", "NA", "KA","GI"],
                    ["TO","KU","SI","yu","NA","TU","KU","RI","NO","O","O"],
                    ["KI","NA","KA","GI"]],
               "5":[["TA","I","MA","TU"],
                    ["KU","RA","YA","MI","WO","TE","RA","SI","TA","RI"],
                    ["KU","SA","KI","WO","YA","KI","HA","RA","U","NO","NI"],
                    ["TU","KA","U"],],
               "6":[["HU","RU","BI","TA","ME","DA","RU"],
                    ["SA","BI","DE","YO","GO","RE","TA","ME","DA","RU",],
                    ["O","U","KE","NO","MO","NN","SI","yo","U","GA",],
                    ["HO","RA","RE","TE","I","RU",]],
               "7":[["KA","NN","SI", "yu", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","TI","KA","RO","U","NO","KA","NN"],
                    ["SI","yu","NO","KA","GI",]],
               "8":[["KI","SI","NO", "ME", "MO", "GA","KI"],
                    ["O","U","GO","RO","SI","GA","HA","JI","MA","tu","TA"],
                    ["NO","DE","HE","I","KA","HA","KE","I","SI","yo","U","NO"],
                    ["SA", "I","DA","NN","HE","TO","MU","KA","WA","RE","TA"],
                    ["WA","TA","SI","MO","MI","NO","HU","RI","KA","TA","WO"],
                    ["KA","NN","GA","NE","BA","NA","RA","NA","I",".",".","."]],

    }
    return txt

def item_get_t2():
    txt = {
               "1":[["GU","NN","RE", "I", "JI", "yo", "U"],
                    ["KI","TA","NO","KO","U","DO","U","NO","TI","yo","U","SA"],
                    ["GA","O","WA","RU","MA","DE","MU","RA","HA",],
                    ["KI","SI","DA","NN","NO","SI","KI","KA","TO","SU","RU"],
                    ["SI","JI","NI","SI","TA","GA","U","KO","TO"],],
               "2":[["SO","NN","TI", "yo", "U", "NO", "ME", "MO","GA","KI"],
                    ["MI","YA","KO","KA","RA","SI","SI","ya","GA","KI","TA"],
                    ["MU","RA","NO","HI","MI","TU","WO","MA","MO","RU","KO",],
                    ["NO","YA","KU","ME","KA","RA","MO","YA","tu","TO",],
                    ["KA","I","HO","U","SA","RE","RU",],
                    ["WA","SI","HA","TE","WO","YO","GO","SI","SU","GI","TA"]],
               "3":[["JI","NN","TI", "NO", "KA", "GI"],
                    ["MU","RA","NI","SE","TU","E","I","SA","RE","TA",],
                    ["JI","NN","TI","NO","KA","GI",]],
               "4":[["WA", "NN", "SI", "yo" ,"U"],
                    ["JI","NN","TI","NO","SI","NN","E","I","TA","I","NO"],
                    ["WA", "NN", "SI", "yo" ,"U"]],
               "5":[["BA","KU","YA","KU"],
                    ["GA","NN","BA","NN","WO","HA","KA","I","SU","RU"],
                    ["KO","TO","GA","DE","KI","RU","KI","yo","U","RI","yo"],
                    ["KU","NA","KA","YA","KU"],],
               "6":[["SU","I","SI","yo","U","DA","MA"],
                    ["MU","RA","NO","KI","TA","NO","KO","U","DO","U",],
                    ["DE","MI","TU","KE","TA","SU","I","SI","yo","U",],
                    ["KU","RO","I","HE","BI","NO","YO","U","NA","MO","NO"],
                    ["GA","NA","KA","NI","MI","E","RU",]],
               "7":[["SI","NN","PI", "BU", "NO", "KA", "GI"],
                    ["SI","NN","SE","I","TI","KU","NO","SI","NN","PI","BU"],
                    ["NO","KA","GI",]],
               "8":[["KI","SI","NO", "ME", "MO", "GA","KI"],
                    ["HE","I","KA","NO","NA","SA","RU","KO","TO","NI",],
                    ["ZE","NN","ME","NN","TE","KI","NI","DO","U","I","HA",],
                    ["DE", "KI","NA","I","GA",".",".",".",],
                    ["KO","RE","DE","SU","BE","TE","GA","KA","I","KE","TU"],
                    ["SU","RU","NA","RA","YA","MU","WO","E","MA","I",]],

    }
    return txt

def item_get_t3():
    txt = {
               "1":[["E","I","HE","I","NO","ME","MO","GA","KI"],
                    ["O","U","KI","yu","U","NO","HI","JI","yo","U","TU"],
                    ["U","RO","NO","TE","NN","KE","NN","GA","A","tu","TA"],
                    ["DA","I","SI","yo","KO","NO","SO","U","TI","HA","SA"],
                    ["I","TE","NN","KE","NN","GA","HI","TU","YO","U"],],
               "2":[["O","U","KI","yu","U","KA","RA","NO","TE","GA","MI"],
                    ["MI","NA","TO","HA","SI","BA","RA","KU","HE","I","SA"],
                    ["SU","RU",],
                    ["KI","NN","KI","yu","U","JI","NI","HA","KI","yu","U"],
                    ["SI","GA","I","NO","DA","I","NI","TI","KU","WO","TU"],
                    ["KA","U","KO","TO",]],
               "3":[["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","HA","ZU","RE","NI","A","RU","DA"],
                    ["I","SI","yo","KO","NO","KA","GI",]],
               "4":[["SA","BI","TA", "O", "O", "KI", "NA", "KA","GI"],
                    ["TO","KU","SI","yu","NA","TU","KU","RI","NO","O","O"],
                    ["KI","NA","KA","GI"]],
               "5":[["TA","I","MA","TU"],
                    ["KU","RA","YA","MI","WO","TE","RA","SI","TA","RI"],
                    ["KU","SA","KI","WO","YA","KI","HA","RA","U","NO","NI"],
                    ["TU","KA","U"],],
               "6":[["HU","RU","BI","TA","ME","DA","RU"],
                    ["SA","BI","DE","YO","GO","RE","TA","ME","DA","RU",],
                    ["O","U","KE","NO","MO","NN","SI","yo","U","GA",],
                    ["HO","RA","RE","TE","I","RU",]],
               "7":[["KA","NN","SI", "yu", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","TI","KA","RO","U","NO","KA","NN"],
                    ["SI","yu","NO","KA","GI",]],
               "8":[["KI","SI","NO", "ME", "MO", "GA","KI"],
                    ["O","U","GO","RO","SI","GA","HA","JI","MA","tu","TA"],
                    ["NO","DE","HE","I","KA","HA","KE","I","SI","yo","U","NO"],
                    ["SA", "I","DA","NN","HE","TO","MU","KA","WA","RE","TA"],
                    ["WA","TA","SI","MO","MI","NO","HU","RI","KA","TA","WO"],
                    ["KA","NN","GA","NE","BA","NA","RA","NA","I",".",".","."]],

    }
    return txt

def item_get_t4():
    txt = {
               "1":[["E","I","HE","I","NO","ME","MO","GA","KI"],
                    ["O","U","KI","yu","U","NO","HI","JI","yo","U","TU"],
                    ["U","RO","NO","TE","NN","KE","NN","GA","A","tu","TA"],
                    ["DA","I","SI","yo","KO","NO","SO","U","TI","HA","SA"],
                    ["I","TE","NN","KE","NN","GA","HI","TU","YO","U"],],
               "2":[["O","U","KI","yu","U","KA","RA","NO","TE","GA","MI"],
                    ["MI","NA","TO","HA","SI","BA","RA","KU","HE","I","SA"],
                    ["SU","RU",],
                    ["KI","NN","KI","yu","U","JI","NI","HA","KI","yu","U"],
                    ["SI","GA","I","NO","DA","I","NI","TI","KU","WO","TU"],
                    ["KA","U","KO","TO",]],
               "3":[["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","HA","ZU","RE","NI","A","RU","DA"],
                    ["I","SI","yo","KO","NO","KA","GI",]],
               "4":[["SA","BI","TA", "O", "O", "KI", "NA", "KA","GI"],
                    ["TO","KU","SI","yu","NA","TU","KU","RI","NO","O","O"],
                    ["KI","NA","KA","GI"]],
               "5":[["TA","I","MA","TU"],
                    ["KU","RA","YA","MI","WO","TE","RA","SI","TA","RI"],
                    ["KU","SA","KI","WO","YA","KI","HA","RA","U","NO","NI"],
                    ["TU","KA","U"],],
               "6":[["HU","RU","BI","TA","ME","DA","RU"],
                    ["SA","BI","DE","YO","GO","RE","TA","ME","DA","RU",],
                    ["O","U","KE","NO","MO","NN","SI","yo","U","GA",],
                    ["HO","RA","RE","TE","I","RU",]],
               "7":[["KA","NN","SI", "yu", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","TI","KA","RO","U","NO","KA","NN"],
                    ["SI","yu","NO","KA","GI",]],
               "8":[["KI","SI","NO", "ME", "MO", "GA","KI"],
                    ["O","U","GO","RO","SI","GA","HA","JI","MA","tu","TA"],
                    ["NO","DE","HE","I","KA","HA","KE","I","SI","yo","U","NO"],
                    ["SA", "I","DA","NN","HE","TO","MU","KA","WA","RE","TA"],
                    ["WA","TA","SI","MO","MI","NO","HU","RI","KA","TA","WO"],
                    ["KA","NN","GA","NE","BA","NA","RA","NA","I",".",".","."]],

    }
    return txt

def item_get_t5():
    txt = {
               "1":[["KI","SI","DA","NN","TI","yo","U","NO","KA","GI"],
                    ["KA","RE","GA","KI","SI","DA","NN","TI","yo","U","NI"],
                    ["NI","NN","JI","RA","RE","TA","TO","KI","NI",],
                    ["O","U","KA","RA","SA","ZU","KE","RA","RE","TA",],
                    ["KA","GI",]],
               "2":[["O","U","KI","yu","U","KA","RA","NO","TE","GA","MI"],
                    ["MI","NA","TO","HA","SI","BA","RA","KU","HE","I","SA"],
                    ["SU","RU",],
                    ["KI","NN","KI","yu","U","JI","NI","HA","KI","yu","U"],
                    ["SI","GA","I","NO","DA","I","NI","TI","KU","WO","TU"],
                    ["KA","U","KO","TO",]],
               "3":[["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","HA","ZU","RE","NI","A","RU","DA"],
                    ["I","SI","yo","KO","NO","KA","GI",]],
               "4":[["SA","BI","TA", "O", "O", "KI", "NA", "KA","GI"],
                    ["TO","KU","SI","yu","NA","TU","KU","RI","NO","O","O"],
                    ["KI","NA","KA","GI"]],
               "5":[["HU","RU","BI","TA","KA","I","ZU",],
                    ["HE","NN","KI","yo","U","NO","MU","RA","HE","NO"],
                    ["KO","U","RO","GA","KA","I","TE","A","RU",]],
               "6":[["MA","A","TA","RA","SI","I","KA","I","ZU",],
                    ["O","U","RI","TU","MA","DO","U","I","NN","HE","NO"],
                    ["KO","U","RO","GA","KA","I","TE","A","RU",]],
               "7":[["SU","NA","BO","KO","RI","NO","KA","I","ZU",],
                    ["HI","GA","SI","NO","MI","YA","KO","HE","NO"],
                    ["KO","U","RO","GA","KA","I","TE","A","RU",]],
               "8":[["O","U","KE","NO","KA","I","ZU",],
                    ["KE","I","SI","yo","U","NO","SA","I","DA","NN","HE","NO"],
                    ["KO","U","RO","GA","KA","I","TE","A","RU",]],

    }
    return txt

def item_get_t6():
    txt = {
               "1":[["KI","SI","DA","NN","TI","yo","U","NO","KA","GI"],
                    ["KA","RE","GA","KI","SI","DA","NN","TI","yo","U","NI"],
                    ["NI","NN","JI","RA","RE","TA","TO","KI","NI",],
                    ["O","U","KA","RA","SA","ZU","KE","RA","RE","TA",],
                    ["KA","GI",]],
               "2":[["O","U","KI","yu","U","KA","RA","NO","TE","GA","MI"],
                    ["MI","NA","TO","HA","SI","BA","RA","KU","HE","I","SA"],
                    ["SU","RU",],
                    ["KI","NN","KI","yu","U","JI","NI","HA","KI","yu","U"],
                    ["SI","GA","I","NO","DA","I","NI","TI","KU","WO","TU"],
                    ["KA","U","KO","TO",]],
               "3":[["DA","I","SI", "yo", "KO", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","HA","ZU","RE","NI","A","RU","DA"],
                    ["I","SI","yo","KO","NO","KA","GI",]],
               "4":[["SA","BI","TA", "O", "O", "KI", "NA", "KA","GI"],
                    ["TO","KU","SI","yu","NA","TU","KU","RI","NO","O","O"],
                    ["KI","NA","KA","GI"]],
               "5":[["KA","I","ZU","I","IT"],
                    ["HE","NN","KI","yo","U","NO","MU","RA","HE","NO"],
                    ["KO","U","RO","GA","KA","I","TE","A","RU",]],
               "6":[["HU","RU","BI","TA","ME","DA","RU"],
                    ["SA","BI","DE","YO","GO","RE","TA","ME","DA","RU",],
                    ["O","U","KE","NO","MO","NN","SI","yo","U","GA",],
                    ["HO","RA","RE","TE","I","RU",]],
               "7":[["KA","NN","SI", "yu", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","TI","KA","RO","U","NO","KA","NN"],
                    ["SI","yu","NO","KA","GI",]],
               "8":[["KI","SI","NO", "ME", "MO", "GA","KI"],
                    ["O","U","GO","RO","SI","GA","HA","JI","MA","tu","TA"],
                    ["NO","DE","HE","I","KA","HA","KE","I","SI","yo","U","NO"],
                    ["SA", "I","DA","NN","HE","TO","MU","KA","WA","RE","TA"],
                    ["WA","TA","SI","MO","MI","NO","HU","RI","KA","TA","WO"],
                    ["KA","NN","GA","NE","BA","NA","RA","NA","I",".",".","."]],

    }
    return txt