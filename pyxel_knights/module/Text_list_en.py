# -*- coding: utf-8 -*-
#Text_list_en.py

def text_get():
    txt = {
               "0":"New Game",
               "1":"Quit",
               "2":"Sun is the image of the king.",
               "3":"The shade of the sun was ",
               "4":"thought to be the weakening ",
               "5":"of the king's power.",
               "6":"Save completed",
               "7":"Save failed",
               "8":"Load completed",
               "9":"Load failed",
               "10":"Load game",
               "11":"The sun went down.",
               "12":"The Great Priest declared",
               "13":"the start of the \"Regicide\".",
               "14":"The one who killed the king",
               "15":"becomes the next king.",
               "16":"The regiside ends when the king",
               "17":"survives for seven days.",
               "18":"",
               "19":"You also started to act as ",
               "20":"one aiming for the throne.",
               "21":"This phenomenon is",
               "22":"a solar eclipse,",
               "23":"but it is not known",
               "24":"at this time....",
               "50":"You changed weapon to a sword.",
               "51":"You changed weapon to a cane.",
               "52":"You changed weapon to an ax.",
               "53":"Please choose a weapon.",
               "100":"Unlocked.",
               "101":"Locked.",
               "102":"The gimmick was activated.",
               "103":"Destroyed the skull.",
               "104":"Crushed skull",
               "105":"is the destination.",
               "105_0":"Where are you going?",
               "105_1":"Frontier village",
               "105_2":"Royal Magic Institute",
               "105_3":"East capital",
               "105_4":"Inheritance altar",
               "105_6":"Old town harbor",
               "105_7":"The water gate is closed!",
               "106":"Beware of monsters.",
               "107":"The main gate is ahead.",
               "108":"Dead end",
               "109":"Old town, off-limits.",
               "110":"Port of the second district.",
               "111":"Thorns are covering the road.",
               "112":"Burned the thorns.",
               "113":"Got a torch.",
               "113_1":"Got a explosive.",
               "114":"There is nothing.",
               "115":"Got a Key-4.",
               "116":"Got a Information-3.",
               "117":"That's it!",
               "118":"My lord departed.",
               "119":"No matter how national law,",
               "120":"I won't let you kill him.",
               "121":"..........",
               "122":"You should die, kingslayer!!",
               "123":"Knight Captain",
               "124":"Got valuables.",
               "125":"You're kingslayer....",
               "126":"If you want to enter the ritual",
               "127":"You have to find Royal medal.",
               "128":"Take care....ho ho ho",
               "129":"Sacred district ahead.",
               "130":"The entrance to the village",
               "131":"Inheritance altar",
               "134":"There is no one now.",
               "135":"Opened the door.",
               "136":"Silver Knight",
               "137":"You're faster than I expected.",
               "138":"Soldiers! Hurry up!",
               "139":"Take on an enemy!",
               "140":"Blocked by bedrock.",
               "141":"You used explosives.",
               "142":"Stay away from the village.",
               "143":"There is a knight order.",
               "144":"All the villagers evacuated.",
               "145":"Only the village mayor is there.",
               "146":"What are yo doing, strenger?.",
               "147":"\"Curiosity killed the cat\".",
               "148":"I won't say bad things,",
               "149":"so go home early....",
               "150":"Everyone, attack!",
               "151":"Wear an armband",
               "151_1":"when entering beyond this.",
               "152":"Explosives available, danger.",
               "153":"Those who know the secrets,",
               "154":"must die.",
               "155":"Village mayor",
               "156":"Institute of Time",
               "200":"..........",
               "201":"Hello!",
               "202":"There're many monsters recently.",
               "203":"I haven't seen king for a while.",
               "204":"I know an underground passage.",
               "205":"Hello!",
               "206":"Hello!",
               "207":"The port is closed....Ugh....",
               "208":"Hello!",
               "209":"Hello!",
               "210":"Guard sleeping in the harbor.",
               "211":"Hello!",
               "212":"Hello!",
               "213":"This is a sacred district.",
               "214":"Did you need something?",
               "215":"Hello.",
               "216":"To meet the Great Priest,",
               "217":"head to the temple.",
               "218":"At the end of this road is ",
               "219":"the house of the Great Priest.",
               "220":"Welcome, traveler of regiside.",
               "221":"The king is a great man,",
               "222":"but I have to obey ",
               "223":"the commandments of the country.",
               "224":"The king gone to the altar.",
               "225":"The key is held by the aides.",
               "226":"Royal Magic Institute",
               "227":"Door control room",
               "228":"Laboratory entrance",
               "229":"Emergency contact.",
               "230":"This is a shift officer.",
               "231":"Detected an intruder.",
               "232":"Strengthen your vigilance.",
               "233":"That's all.",
               "234":"First basement floor",
               "235":"First adjustment room",
               "236":"Second adjustment room",
               "237":"Third adjustment room",
               "238":"Unlocked",
               "239":"The password is incorrect",
               "240":"Please enter the password",
               "241":"Library",
               "242":"Second basement floor",
               "243":"Third basement floor",
               "244":"Fourth adjustment room",
               "245":"Sixth adjustment room",
               "300":"City guard",
               "301":"Residents of the city",
               "302":"Old man",
               "303":"Old woman",
               "304":"Villager",
               "305":"Resident",
               "306":"Great Priest",
               "307":"Magic Institute officer",
               "308":"Magic institute director",
               "309":"I admire your courage.",
               "310":"I will destroy you ",
               "311":"with my own hands.",
               "999":"I've only made it so far....",
               "999_1":"I'm so sorry!!",
               "1000":"About the old town",
               "1001":"The old town was closed due to",
               "1002":"an accident at ",
               "1003":"the Institute of Time.",
               "1004":"When the rescue team arrived",
               "1005":"at the site, the inhabitants ",
               "1006":"were aging rapidly,",
               "1007":"and some died of senility.",
               "1008":"",
               "1009":"About frontier village",
               "1010":"It is the birthplace of",
               "1011":"the current king and is a ",
               "1012":"peaceful place surrounded ",
               "1013":"by greenery.",
               "1014":"On the north side of ",
               "1015":"the village is an ancient ruin, ",
               "1016":"which is being investigated by ",
               "1017":"Cultural Properties Department.",
               "1018":"About the Royal Magic Institute",
               "1019":"There has been established ",
               "1020":"for the purpose of taking over ",
               "1021":"the Institute of time.",
               "1022":"There's an army-like discipline ",
               "1023":"with the director of ",
               "1024":"the magic institute at the top, ",
               "1025":"and it has military power ",
               "1026":"independent of the Knights.",
               "1027":"About the east capital",
               "1028":"The east capital has been ",
               "1029":"interacting with the kingdom ",
               "1030":"since ancient times.",
               "1031":"Of particular note is the study",
               "1032":"of immortality.   Therefore, ",
               "1033":"their lifespan is long.",
               "1034":"The characteristic mask is ",
               "1035":"a special product.",
               "1036":"About the sacred district",
               "1037":"The sacred district manages",
               "1038":"ritual with the great priest",
               "1039":"The deep part of the temple",
               "1040":"is tightly closed",
               "1041":"and no outsiders are allowed",
               "1042":"to enter.",
               "1043":"",
               "1044":"",
               "1045":"About Ouroboros",
               "1046":"",
               "1047":"",
               "1048":"",
               "1049":"The page is torn....",
               "1050":"",
               "1051":"",
               "1052":"",
               "1053":"",

    }
    return txt

def text_get_s():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s2():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Military warrant",
               "56":"",
               "57":"Do you want to buy?",
               "58":"Village mayor's ",
               "59":"note writing",
               "60":"Do you want to buy?",
               "61":"Base key",
               "62":"Do you want to buy?",
               "63":"Armband of ",
               "64":"the Guard",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s3():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s4():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s5():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def text_get_s6():
    txt = {

               "51":"Welcome.",
               "52":"Please select ",
               "53":"the item number.",
               "54":"",
               "55":"Note writing ",
               "56":"of guards",
               "57":"Do you want to buy?",
               "58":"Letter from ",
               "59":"the palace",
               "60":"Do you want to buy?",
               "61":"Large library key",
               "62":"Do you want to buy?",
               "63":"Big rusty key",
               "64":"",
               "65":"Do you want to buy?",
               "66":"Sold out",
               "67":"Not enough money.",
               "68":"",
               "69":"Thank you!",
    }
    return txt

def item_get():
    txt = {

               "0":"Sold out",
               "1":"Information-1",
               "2":"Information-2",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-3",
               "8":"Information-3",
    }
    return txt

def item_get2():
    txt = {

               "0":"Sold out",
               "1":"Information-4",
               "2":"Information-5",
               "3":"Key-5",
               "4":"Armband",
               "5":"Explosive",
               "6":"Valuables-2",
               "7":"Key-6",
               "8":"Information-6",
    }
    return txt

def item_get3():
    txt = {

               "0":"Sold out",
               "1":"Information-7",
               "2":"Information-8",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-4",
               "8":"Information-9",
    }
    return txt

def item_get4():
    txt = {

               "0":"Sold out",
               "1":"Information-10",
               "2":"Information-11",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-4",
               "8":"Information-12",
    }
    return txt

def item_get5():
    txt = {

               "0":"Sold out",
               "1":"Key-4",
               "2":"Key-7",
               "3":"Key-7",
               "4":"Key-8",
               "5":"Nautical chart-1",
               "6":"Nautical chart-2",
               "7":"Nautical chart-3",
               "8":"Nautical chart-4",
    }
    return txt

def item_get6():
    txt = {

               "0":"Sold out",
               "1":"Information-1",
               "2":"Information-2",
               "3":"Key-1",
               "4":"Key-2",
               "5":"Torch",
               "6":"Valuables-1",
               "7":"Key-4",
               "8":"Information-3",
    }
    return txt

def item_get_t():
    txt = {
               "1":["Note writing of guards",
                    "There was an inspection of",
                    "the emergency passage in ",
                    "the royal palace.",
                    "The equipment",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Torch",
                    "Used to illuminate",
                    "the darkness",
                    "and burn vegetation.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt

def item_get_t2():
    txt = {
               "1":["Military warrant",
                    "The village will be ",
                    "under the command",
                    "of the Knights",
                    "until the investigation",
                    "of the northern mine ",
                    "is completed.",
                    "Follow the instructions.",],
               "2":["Village mayor's memo",
                    "A messenger came from ",
                    "the city.",
                    "It is finally released ",
                    "from the role",
                    "of keeping the secret ",
                    "of the village.",
                    "I got my hands too dirty.",],
               "3":["Base key",
                    "The key to the base",
                    "set up in the village.",],
               "4":["Armband",
                    "Armband of the ",
                    "Guard of the base."],
               "5":["Explosive",
                    "A powerful explosive ",
                    "that can destroy rock.",],
               "6":["Crystal ball",
                    "A crystal ball found in the ",
                    "mine north of the village.",
                    "Something like",
                    "a black snake",
                    "can be seen inside.",],
               "7":["Mysterious area key",
                    "Key to the mysterious area ",
                    "of the sacred district."],
               "8":["Knight's note writing",
                    "I can't agree with everything ",
                    "the king does, ",
                    " but I can't help it.",],

    }
    return txt

def item_get_t3():
    txt = {
               "1":["Note writing of guards",
                    "There was an inspection of",
                    "the emergency passage in ",
                    "the royal palace.",
                    "The equipment",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Torch",
                    "Used to illuminate",
                    "the darkness",
                    "and burn vegetation.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt

def item_get_t4():
    txt = {
               "1":["Note writing of guards",
                    "There was an inspection of",
                    "the emergency passage in ",
                    "the royal palace.",
                    "The equipment",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Torch",
                    "Used to illuminate",
                    "the darkness",
                    "and burn vegetation.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt

def item_get_t5():
    txt = {
               "1":["Knight captain's key",
                    "The key given by the king  ",
                    "when he was appointed ",
                    "as knight captain.",],
               "2":["Silver Knight's key",
                    "The silver knight",
                    "who servedthe king",
                    "was originallya guard ",
                    "of the Great Priest.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Old nautical chart",
                    "A route to  ",
                    "frontier village",
                    "is drawn.",],
               "6":["Brand new nautical chart",
                    "A route to  ",
                    "Royal Magic Institute ",
                    "is drawn.",],
               "7":["Nautical chart of sand",
                    "A route to  ",
                    "east capital",
                    "is drawn.",],
               "8":["Nautical chart of king",
                    "A route to ",
                    "inheritance altar ",
                    "is drawn.",],

    }
    return txt

def item_get_t6():
    txt = {
               "1":["Note writing of guards",
                    "There was an inspection of",
                    "the emergency passage in ",
                    "the royal palace.",
                    "The equipment",
                    "in the large library",
                    "needs to be re-inspected.",],
               "2":["Letter from the palace",
                    "The port will be closed ",
                    "for a while.",
                    "In an emergency, ",
                    "use the second district",
                    "of the old town.",],
               "3":["Large library key",
                    "The key to the ",
                    "large library",
                    "on the outskirts ",
                    "of the city.",],
               "4":["Big rusty key",
                    "A big key with ",
                    "a special structure."],
               "5":["Old nautical chart",
                    "A route to a frontier village ",
                    "is drawn.",],
               "6":["Old medal",
                    "Rust-stained medal.",
                    "The crest of the ",
                    "royal family is carved."],
               "7":["Jailer's key",
                    "The key to the dungeon ",
                    "of the city."],
               "8":["Knight's note writing",
                    "As the \"Regicide\" began, ",
                    "the king headed",
                    "for the inheritance ",
                    "altar.",
                    "I also have to think ",
                    "about what I should do."],

    }
    return txt