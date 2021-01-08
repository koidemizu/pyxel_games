# -*- coding: utf-8 -*-

def text_get():
    txt = {
               "0":["HA","JI","ME","RU"],
               "1":["YA","ME","RU"],
               "2":["A","NA","TA","HA","O","U","KO","KU","NO",
                          "KA","KI","yu","U","KI","SI"],
               "3":["MI","YA","KO","NO","HA","ZU","RE","NI",
                          "SU","NN","DE","I","MA","SU"],
               "4":["KO","NO","SE","KA","I","WO","KI","MA","MA",
                          "NI"],
               "5":["BO","U","KE","NN","SI","TE","MI","MA","SI",
                          "yo","U"],
               "100":["KA","GI","GA","A","I","TA",],
               "101":["KA","GI","GA","KA","KA","tu","TE","I","RU"],
               "102":["SI","KA","KE","GA","SA","DO","U","SI","TA"],
               "103":["DO","KU","RO","WO","HA","KA","I","SI","TA"],
               "104":["KU","DA","KA","RE","TA","DO","KU","RO",],
               "105":["E","NN","DE","i","NN","GU",],
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
               "114":["NA","NI","MO","NA","I",],
               "115":["KA","GI","YO","NN","WO","TE","NI","I","RE","TA"],
               "116":["JU","yo","U","HO","U","SA","NN","WO","TE","NI","I",
                      "RE","TA"],
               "200":["MI","YA","KO","NO","E","I","HE","I","DA"],
               "201":["MI","YA","KO","NO","JI","yu","U","NI","NN","DA"],

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

def item_get():
    txt = {

               "0":["U","RI","KI","RE"],
               "1":["JI","yo","U","HO","U","I","TI"],
               "2":["JI","yo","U","HO","U","NI"],
               "3":["KA","GI","I","TI"],
               "4":["KA","GI","NI"],
               "5":["TA","I","MA","TU",],
               "6":["KA","GI","SA","NN",],
               "7":["KA","GI","YO","NN"],
               "8":["JI","yo","U","HO","U","SA","NN",],

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
               "6":[["HU","RU","BI","TA","KA","GI"],
                    ["SA","BI","DE","YO","GO","RE","TA","TI","I","SA","NA"],
                    ["KA","GI",]],
               "7":[["KA","NN","SI", "yu", "NO", "KA", "GI"],
                    ["MI","YA","KO","NO","TI","KA","RO","U","NO","KA","NN"],
                    ["SI","yu","NO","KA","GI",]],
               "8":[["KA","NN","SI", "yu", "NO", "ME", "MO", "GA","KI"],
                    ["TA","I","MA","TU"],
                    ["SA","NN",],
                    ["I", "TI",]],

    }
    return txt

