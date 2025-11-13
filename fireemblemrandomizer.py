# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:15:18 2021

@author: Christian
"""

import numpy as np
import random
import scipy.optimize as optimize

class Game:
    def __init__(self, game, **kwargs):
        self.game = game
        self.gba_supp = {"Fire" : [0.5, 0.0, 2.5, 2.5, 2.5, 0.0],
                         "Thunder": [0.0, 0.5, 0.0, 2.5, 2.5, 2.5],
                         "Wind": [0.5, 0.0, 2.5, 0.0, 2.5, 2.5],
                         "Ice": [0.0, 0.5, 2.5, 2.5, 0.0, 2.5],
                         "Dark": [0.0, 0.0, 2.5, 2.5, 2.5, 2.5],
                         "Light": [0.5, 0.5, 2.5, 0.0, 2.5, 0.0],
                         "Anima": [0.5, 0.5, 0.0, 2.5, 0.0, 2.5]}
        if self.game == "Blade of Light" or self.game == 1:
            pass
        if self.game == "Gaiden" or self.game == 2:
            pass
        if self.game == "New Mystery" or self.game == 3:
            pass
        if self.game == "Genealogy" or self.game == 4:
            pass
        if self.game == "Thracia" or self.game == 5:
            self.game = 5
            self.game_name = "fe5"
            self.lords = ["Leif"]
            self.characters = ["Leif", "Finn", "Orsin", "Halvan", 
                               "Eyvel", "Dagdar", "Tanya", "Marty",
                               "Ronan", "Safiya", "Lifis", "Machyua",
                               "Brighton", "Lara", "Fergus", "Karin",
                               "Dalsin", "Asbel", "Nanna", "Hicks",
                               "Shiva", "Carrion", "Selphina", "Kane",
                               "Alba", "Robert", "Alfred", "Olwen",
                               "Mareeta", "Salem", "Pan", "Trude",
                               "Tina", "Glade", "Dean", "Eda",
                               "Homer", "Linoan", "Ralph", "Ilios",
                               "Sleuf", "Misha", "Sara", "Shannam",
                               "Miranda", "Xavier", "Amalda", "Conomor",
                               "Diarmuid", "Saias", "Ced", "Galzus"]
            self.recruitment = ['1', '1', '1', '1',
                                '1', '1', '1', '1',
                                '2', '3', '3', '4',
                                '4', '4', '4', '4',
                                '4', '4x', '5','6',
                                '7', '8', '9', '9',
                                '9', '9', '11x', '11x',
                                '12', '12x', '12x', '12x',
                                '12x', '13', '14', '14',
                                '14', '14x', '15', '16A',
                                '16A', '17A', '17A/16B', '16B',
                                '16B', '18', '19', '19',
                                '21', '23', '23', '24']
            self.num_splits = 2
            # Olwen and Ilios are considered a split in this case.
            self.split_chars = [[["Ilios", "Sleuf", "Misha", "Amalda"],
                                ["Shannam", "Miranda", "Conomor"]],
                                [["Olwen"], ["Ilios"]]]
            self.start_chars = ["Leif", "Finn", "Orsin", "Halvan", "Eyvel",
                                "Dagdar", "Tanya", "Marty"]
            self.supports = {"Leif": {"Characters": ["Finn", "Eyvel",
                                                     "Ronan", "Safiya",
                                                     "Dalsin", "Asbel",
                                                     "Nanna", "Hicks",
                                                     "Carrion", "Selphina",
                                                     "Olwen", "Tina",
                                                     "Linoan", "Miranda",
                                                     "Sara", "Xavier"],
                                      "Bonus": ["10"]*16
                                      },
                             "Finn": {"Characters": ["None"],
                                      "Bonus": ["None"]
                                      },
                             "Orsin": {"Characters": ["Tanya"],
                                       "Bonus": ["10"]
                                      },
                             "Halvan": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Eyvel": {"Characters": ["Orsin", "Halvan",
                                                     "Dagdar", "Mareeta"],
                                       "Bonus": ["10"]*4
                                       },
                             "Dagdar": {"Characters": ["Marty"],
                                        "Bonus": ["None"]
                                        },
                             "Tanya": {"Characters": ["Orsin", "Dagdar"],
                                        "Bonus": ["10"]*2
                                       },
                             "Marty": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Ronan": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Safiya": {"Characters": ["Shiva", "Lifis",
                                                    "Tina"],
                                        "Bonus": ["10"]*3
                                      },
                             "Lifis": {"Characters": ["None"],
                                       "Bonus": ["None"]
                                       },
                             "Machyua": {"Characters": ["Brighton"],
                                        "Bonus": ["10"]
                                         },
                             "Brighton": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                          },
                             "Lara": {"Characters": ["Pan"],
                                        "Bonus": ["10"]
                                      },
                             "Fergus": {"Characters": ["Karin"],
                                        "Bonus": ["10"]
                                        },
                             "Karin": {"Characters": ["Fergus", "Misha"],
                                        "Bonus": ["10"]*2
                                       },
                             "Dalsin": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Asbel": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Nanna": {"Characters": ["Leif", "Finn",
                                                      "Homer", "Diarmuid"],
                                        "Bonus": ["10"]*4
                                       },
                             "Hicks": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Shiva": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Carrion": {"Characters": ["None"],
                                         "Bonus": ["None"]
                                         },
                             "Selphina": {"Characters": ["Carrion", "Glade",
                                                       "Kane", "Alba",
                                                       "Robert"],
                                          "Bonus": ["10"] + ["20"] + ["10"]*3
                                          },
                             "Kane": {"Characters": ["None"],
                                      "Bonus": ["None"]
                                      },
                             "Alba": {"Characters": ["None"],
                                      "Bonus": ["None"]
                                      },
                             "Robert": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Alfred": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                      },
                             "Olwen": {"Characters": ["Alfred"],
                                        "Bonus": ["10"]
                                       },
                             "Mareeta": {"Characters": ["Eyvel", "Galzus"],
                                        "Bonus": ["10"] + ["20"]
                                         },
                             "Salem": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Pan": {"Characters": ["Lara", "Trude",
                                                      "Salem"],
                                        "Bonus": ["10"]*3
                                       },
                             "Trude": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Tina": {"Characters": ["Safiya"],
                                        "Bonus": ["10"]
                                      },
                             "Glade": {"Characters": ["Selphina", "Kane",
                                                        "Alba", "Robert"],
                                        "Bonus": ["10"]*4
                                       },
                             "Dean": {"Characters": ["Eda", "Linoan"],
                                        "Bonus": ["10"]*2
                                      },
                             "Eda": {"Characters": ["Dean"],
                                        "Bonus": ["10"]
                                     },
                             "Homer": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Linoan": {"Characters": ["Dean"],
                                        "Bonus": ["20"]
                                        },
                             "Ralph": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                      },
                             "Ilios": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Sleuf": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Misha": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Sara": {"Characters": ["Salem"],
                                        "Bonus": ["10"]
                                      },
                             "Shannam": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                         },
                             "Miranda": {"Characters": ["Conomor"],
                                        "Bonus": ["20"]
                                         },
                             "Xavier": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Amalda": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                        },
                             "Conomor": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                         },
                             "Diarmuid": {"Characters": ["Nanna"],
                                        "Bonus": ["10"]
                                          },
                             "Saias": {"Characters": ["None"],
                                        "Bonus": ["None"]
                                       },
                             "Ced": {"Characters": ["Asbel", "Machyua",
                                                    "Karin"],
                                        "Bonus": ["10"]*3
                                     },
                             "Galzus": {"Characters": ["Mareeta"],
                                        "Bonus": ["10"]
                                        }
                            }
        if self.game == "Binding Blade" or self.game == 6:
            self.game = 6
            self.game_name = "fe6"
            self.version = kwargs.get("version", "Vanilla")
            self.lords = ["Roy"]
            self.characters = ["Roy", "Marcus", "Alen", "Lance", "Wolt",
                               "Bors", "Elen", "Dieck", "Wade", "Lot",
                               "Shanna", "Chad", "Lugh", "Clarine", "Rutger",
                               "Saul", "Dorothy", "Sue", "Zelot", "Trec",
                               "Noah", "Astolfo", "Lilina", "Gwendolyn",
                               "Barthe", "Ogier", "Fir", "Sin", "Gonzalez",
                               "Geese", "Klein", "Thea", "Larum", "Echidna",
                               "Elffin", "Bartre", "Raigh", "Cath", "Melady",
                               "Perceval", "Cecilia", "Sophia", "Igrene",
                               "Garret", "Fae", "Hugh", "Zeiss", "Douglas",
                               "Niime", "Dayan", "Juno", "Yoder", "Karel"]
            self.num_splits = 2
            self.split_chars = [[["Larum", "Echidna"], ["Elffin", "Bartre"]], [["Juno"], ["Dayan"]]]
            self.start_chars = ["Roy", "Marcus", "Alen", "Lance", "Wolt", "Bors"]
            if self.version == "Ember".lower():
                self.characters += ["Lowen", "Debias", "Galle", "Guinivere"]
            self.supports = {"Roy": {"Characters": ["Marcus", "Alen",
                                                       "Lance", "Wolt",
                                                       "Shanna", "Sue",
                                                       "Lilina", "Larum",
                                                       "Cecilia", "Sophia"],
                                        "Affinity": "Fire"},
                             "Marcus": {"Characters": ["Alen", "Lance",
                                                     "Wolt", "Lilina",
                                                     "Roy"],
                                        "Affinity": "Ice"},
                             "Alen": {"Characters": ["Lance", "Wolt",
                                                     "Wade", "Thea",
                                                     "Roy", "Marcus"],
                                      "Affinity": "Fire"},
                             "Lance": {"Characters": ["Wolt", "Lot",
                                                      "Clarine", "Roy",
                                                      "Marcus", "Alen"],
                                       "Affinity": "Anima"},
                             "Wolt": {"Characters": ["Roy", "Marcus",
                                                     "Alen", "Lance",
                                                     "Sue"],
                                      "Affinity": "Ice"},
                             "Bors": {"Characters": ["Astolfo", "Lilina",
                                                     "Ogier", "Gwendolyn",
                                                     "Barthe"],
                                      "Affinity": "Wind"},
                             "Elen": {"Characters": ["Saul", "Melady",
                                                     "Zeiss", "Lugh",
                                                     "Chad"],
                                      "Affinity": "Wind"},
                             "Dieck": {"Characters": ["Wade", "Lot",
                                                      "Shanna", "Clarine",
                                                      "Rutger", "Klein"],
                                       "Affinity": "Thunder"},
                             "Wade": {"Characters": ["Lot", "Dieck",
                                                     "Shanna", "Echidna",
                                                     "Alen"],
                                      "Affinity": "Fire"},
                             "Lot": {"Characters": ["Wade", "Dieck",
                                                    "Shanna", "Echidna",
                                                    "Lance"],
                                     "Affinity": "Anima"},
                             "Shanna": {"Characters": ["Lot", "Wade",
                                                       "Dieck", "Thea",
                                                       "Juno", "Zelot",
                                                       "Roy"],
                                        "Affinity": "Wind"},
                             "Chad": {"Characters": ["Lugh", "Raigh",
                                                     "Cath", "Hugh",
                                                     "Elen"],
                                      "Affinity": "Thunder"},
                             "Lugh": {"Characters": ["Raigh", "Chad",
                                                     "Hugh", "Elen",
                                                     "Melady"],
                                      "Affinity": "Fire"},
                             "Clarine": {"Characters": ["Rutger", "Dorothy",
                                                        "Klein", "Lance",
                                                        "Dieck"],
                                         "Affinity": "Thunder"},
                             "Rutger": {"Characters": ["Clarine", "Dieck",
                                                       "Fir", "Karel",
                                                       "Dayan"],
                                        "Affinity": "Dark"},
                             "Saul": {"Characters": ["Dorothy", "Yoder",
                                                     "Cecilia", "Igrene",
                                                     "Elen"],
                                      "Affinity": "Ice"},
                             "Dorothy": {"Characters": ["Saul", "Perceval",
                                                        "Clarine", "Sin",
                                                        "Yoder"],
                                         "Affinity": "Fire"},
                             "Sue": {"Characters": ["Sin", "Roy",
                                                    "Dayan", "Fae",
                                                    "Wolt"],
                                     "Affinity": "Wind"},
                             "Zelot": {"Characters": ["Trec", "Noah",
                                                      "Juno", "Thea",
                                                      "Shanna"],
                                       "Affinity": "Dark"},
                             "Trec": {"Characters": ["Noah", "Zelot",
                                                     "Melady", "Gonzalez",
                                                     "Juno"],
                                      "Affinity": "Wind"},
                             "Noah": {"Characters": ["Trec", "Zelot",
                                                     "Juno", "Fir",
                                                     "Karel"],
                                      "Affinity": "Anima"},
                             "Astolfo": {"Characters": ["Lilina", "Bors",
                                                        "Barthe", "Igrene",
                                                        "Gwendolyn"],
                                         "Affinity": "Dark"},
                             "Lilina": {"Characters": ["Barthe", "Gwendolyn",
                                                       "Ogier", "Gonzalez",
                                                       "Cecilia", "Garret",
                                                       "Roy", "Marcus",
                                                       "Bors", "Astolfo"],
                                        "Affinity": "Light"},
                             "Gwendolyn": {"Characters": ["Bors", "Barthe",
                                                          "Astolfo", "Ogier",
                                                          "Lilina"],
                                           "Affinity": "Fire"},
                             "Barthe": {"Characters": ["Gwendolyn", "Bors",
                                                       "Astolfo", "Ogier",
                                                       "Lilina"],
                                        "Affinity": "Ice"},
                             "Ogier": {"Characters": ["Lilina", "Gwendolyn",
                                                      "Barthe", "Bors",
                                                      "Larum"],
                                       "Affinity": "Wind"},
                             "Fir": {"Characters": ["Noah", "Rutger",
                                                    "Bartre", "Sin",
                                                    "Karel"],
                                     "Affinity": "Fire"},
                             "Sin": {"Characters": ["Sue", "Fir",
                                                     "Dorothy", "Zeiss",
                                                     "Dayan"],
                                      "Affinity": "Ice"},
                             "Gonzalez": {"Characters": ["Lilina", "Echidna",
                                                         "Bartre", "Garret",
                                                         "Dayan", "Trec"],
                                          "Affinity": "Thunder"},
                             "Geese": {"Characters": ["Cath", "Echidna",
                                                      "Douglas", "Garret",
                                                      "Larum"],
                                       "Affinity": "Fire"},
                             "Klein": {"Characters": ["Clarine", "Dieck",
                                                      "Thea", "Elffin",
                                                      "Perceval"],
                                       "Affinity": "Ice"},
                             "Thea": {"Characters": ["Klein", "Alen",
                                                     "Shanna", "Juno",
                                                     "Zelot"],
                                      "Affinity": "Ice"},
                             "Larum": {"Characters": ["Geese", "Garret",
                                                      "Roy", "Douglas",
                                                      "Ogier", "Echidna",
                                                      "Perceval"],
                                       "Affinity": "Thunder"},
                             "Echidna": {"Characters": ["Wade", "Lot",
                                                        "Gonzalez", "Geese",
                                                        "Larum"],
                                         "Affinity": "Ice"},
                             "Elffin": {"Characters": ["Perceval", "Fae",
                                                       "Douglas", "Klein",
                                                       "Cecilia"],
                                        "Affinity": "Light"},
                             "Bartre": {"Characters": ["Fir", "Karel",
                                                       "Zeiss", "Cath",
                                                       "Gonzalez"],
                                        "Affinity": "Thunder"},
                             "Raigh": {"Characters": ["Chad", "Hugh",
                                                      "Lugh", "Niime",
                                                      "Sophia"],
                                       "Affinity": "Ice"},
                             "Cath": {"Characters": ["Garret", "Hugh",
                                                     "Chad", "Geese",
                                                     "Bartre"],
                                      "Affinity": "Anima"},
                             "Melady": {"Characters": ["Zeiss", "Yoder",
                                                       "Elen", "Lugh",
                                                       "Trec"],
                                        "Affinity": "Dark"},
                             "Perceval": {"Characters": ["Cecilia", "Douglas",
                                                         "Larum", "Elffin",
                                                         "Dorothy", "Klein"],
                                          "Affinity": "Dark"},
                             "Cecilia": {"Characters": ["Roy", "Perceval",
                                                        "Saul", "Elffin",
                                                        "Douglas", "Lilina"],
                                         "Affinity": "Anima"},
                             "Sophia": {"Characters": ["Igrene", "Fae",
                                                       "Niime", "Roy",
                                                       "Raigh"],
                                        "Affinity": "Dark"},
                             "Igrene": {"Characters": ["Fae", "Sophia",
                                                       "Saul", "Douglas",
                                                       "Astolfo"],
                                        "Affinity": "Ice"},
                             "Garret": {"Characters": ["Gonzalez", "Cath",
                                                       "Geese", "Lilina",
                                                       "Larum"],
                                        "Affinity": "Wind"},
                             "Fae": {"Characters": ["Sophia", "Igrene",
                                                    "Sue", "Niime",
                                                    "Elffin"],
                                     "Affinity": "Light"},
                             "Hugh": {"Characters": ["Niime", "Raigh",
                                                     "Cath", "Chad",
                                                     "Lugh"],
                                      "Affinity": "Wind"},
                             "Zeiss": {"Characters": ["Karel", "Elen",
                                                      "Sin", "Bartre",
                                                      "Melady"],
                                       "Affinity": "Thunder"},
                             "Douglas": {"Characters": ["Elffin", "Geese",
                                                        "Perceval", "Cecilia",
                                                        "Larum", "Igrene"],
                                         "Affinity": "Thunder"},
                             "Niime": {"Characters": ["Fae", "Raigh",
                                                      "Sophia", "Yoder",
                                                      "Hugh"],
                                       "Affinity": "Anima"},
                             "Dayan": {"Characters": ["Yoder", "Rutger",
                                                      "Sue", "Sin",
                                                      "Gonzalez"],
                                       "Affinity": "Anima"},
                             "Juno": {"Characters": ["Shanna", "Thea",
                                                     "Zelot", "Trec",
                                                     "Noah"],
                                      "Affinity": "Light"},
                             "Yoder": {"Characters": ["Saul", "Niime",
                                                      "Dorothy", "Dayan",
                                                      "Melady"],
                                       "Affinity": "Light"},
                             "Karel": {"Characters": ["Bartre", "Fir",
                                                      "Noah", "Rutger",
                                                      "Zeiss"],
                                       "Affinity": "Light"}
                            }
        if self.game == "Fire Emblem" or self.game==7:
            # Need to work on route splits (can only get Wallace OR Geitz, for
            # example).
            # Also need to fix for HHM characters.
            self.game = 7
            self.game_name = "fe7"
            self.mode = kwargs.get("mode", "Eliwood")
            self.lords = ["Lyn", "Eliwood", "Hector"]
            self.characters = ["Lyn", "Sain", "Kent", "Florina", "Wil",
                               "Dorcas", "Serra", "Erk", "Rath", "Matthew",
                               "Nils", "Lucius", "Wallace", "Eliwood", "Marcus",
                               "Lowen", "Rebecca", "Bartre", "Hector", "Oswin",
                               "Guy", "Priscilla", "Raven", "Canas",
                               "Dart", "Fiora", "Legault", "Ninian", "Isadora",
                               "Heath", "Hawkeye", "Geitz", "Pent", "Louise",
                               "Karel", "Harken", "Nino", "Jaffar", "Vaida",
                               "Renault", "Athos"]
            if self.mode == "Hector":
                self.characters = np.append(self.characters, ["Farina", "Karla"])
            if self.mode == "Lyn".lower():
                self.start_chars = ["Lyn"]
            elif self.mode == "Eliwood".lower():
                self.start_chars = ["Eliwood", "Marcus", "Lowen", "Rebecca",
                                    "Bartre", "Dorcas"]
            elif self.mode =="Hector".lower():
                self.start_chars = ["Hector", "Matthew"]
        if self.game == "Sacred Stones" or self.game == 8:
            self.game = 8
            self.game_name = "fe8"
            self.lords = ["Eirika", "Ephraim"]
            self.characters = ["Eirika", "Seth", "Franz", "Gilliam", "Vanessa",
                               "Moulder", "Ross", "Garcia", "Neimi", "Colm",
                               "Artur", "Lute", "Natasha", "Joshua", "Ephraim",
                               "Forde", "Kyle", "Tana", "Amelia", "Innes",
                               "Gerik", "Tethys", "Marisa", "L'Arachel",
                               "Dozla", "Saleh", "Ewan", "Cormag", "Rennac",
                               "Duessel", "Knoll", "Myrrh", "Syrene"]
            self.start_chars = ["Eirika", "Seth"]
            self.supports = {"Eirika": {"Characters": ["Ephraim", "Forde",
                                                       "Innes", "L'Arachel",
                                                       "Saleh", "Seth",
                                                       "Tana"],
                                        "Affinity": "Light"},
                             "Seth": {"Characters": ["Eirika", "Franz",
                                                     "Garcia", "Natasha",
                                                     "Cormag"],
                                        "Affinity": "Anima"},
                             "Franz": {"Characters": ["Seth", "Amelia",
                                                      "Gilliam", "Forde",
                                                      "Natasha"],
                                       "Affinity": "Light"},
                             "Gilliam": {"Characters": ["Franz", "Garcia",
                                                        "Syrene", "Moulder",
                                                        "Neimi"],
                                         "Affinity": "Thunder"},
                             "Vanessa": {"Characters": ["Moulder", "Syrene",
                                                        "Lute", "Forde",
                                                        "Innes"],
                                         "Affinity": "Anima"},
                             "Moulder": {"Characters": ["Vanessa", "Colm",
                                                        "Gilliam", "Syrene"],
                                         "Affinity": "Anima"},
                             "Ross": {"Characters": ["Garcia", "Lute",
                                                     "Amelia", "Ewan",
                                                     "Gerik"],
                                      "Affinity": "Fire"},
                             "Garcia": {"Characters": ["Seth", "Gilliam",
                                                       "Ross", "Dozla",
                                                       "Neimi"],
                                        "Affinity": "Fire"},
                             "Neimi": {"Characters": ["Gilliam", "Garcia",
                                                      "Colm", "Amelia",
                                                      "Artur"],
                                       "Affinity": "Fire"},
                             "Colm": {"Characters": ["Moulder", "Neimi",
                                                     "Marisa", "Rennac",
                                                     "Kyle"],
                                      "Affinity": "Light"},
                             "Artur": {"Characters": ["Neimi", "Lute",
                                                      "Tethys", "Cormag",
                                                      "Joshua"],
                                       "Affinity": "Ice"},
                             "Lute": {"Characters": ["Vanessa", "Ross",
                                                     "Artur", "Knoll",
                                                     "Kyle"],
                                      "Affinity": "Anima"},
                             "Natasha": {"Characters": ["Seth", "Franz",
                                                        "Joshua", "Knoll",
                                                        "Cormag"],
                                         "Affinity": "Ice"},
                             "Joshua": {"Characters": ["Artur", "Natasha",
                                                       "Innes", "L'Arachel",
                                                       "Marisa", "Gerik"],
                                        "Affinity": "Wind"},
                             "Ephraim": {"Characters": ["Eirika", "Kyle", 
                                                        "Forde", "Myrrh",
                                                        "L'Arachel", "Duessel",
                                                        "Tana"],
                                         "Affinity": "Fire"},
                             "Forde": {"Characters": ["Eirika", "Ephraim",
                                                      "Franz", "Vanessa",
                                                      "Kyle"],
                                       "Affinity": "Wind"},
                             "Kyle": {"Characters": ["Ephraim", "Colm",
                                                     "Lute", "Forde",
                                                     "Syrene"],
                                      "Affinity": "Ice"},
                             "Tana": {"Characters": ["Eirika", "Ephraim",
                                                     "Syrene", "Cormag",
                                                     "Innes", "Marisa"],
                                      "Affinity": "Wind"},
                             "Amelia": {"Characters": ["Franz", "Ross",
                                                       "Neimi", "Ewan",
                                                       "Duessel"],
                                        "Affinity": "Thunder"},
                             "Innes": {"Characters": ["Eirika", "Vanessa",
                                                      "Joshua", "Tana",
                                                      "Gerik", "L'Arachel"],
                                       "Affinity": "Ice"},
                             "Gerik": {"Characters": ["Ross", "Joshua",
                                                      "Innes", "Tethys",
                                                      "Marisa", "Saleh"],
                                       "Affinity": "Thunder"},
                             "Tethys": {"Characters": ["Artur", "Gerik",
                                                       "Ewan", "Marisa",
                                                       "Rennac"],
                                        "Affinity": "Fire"},
                             "Marisa": {"Characters": ["Colm", "Joshua",
                                                       "Tana", "Gerik",
                                                       "Tethys"],
                                        "Affinity": "Ice"},
                             "L'Arachel": {"Characters": ["Eirika", "Ephraim",
                                                          "Joshua", "Innes",
                                                          "Dozla", "Rennac"],
                                           "Affinity": "Light"},
                             "Dozla": {"Characters": ["Garcia", "Ewan",
                                                      "L'Arachel", "Myrrh",
                                                      "Rennac"],
                                       "Affinity": "Thunder"},
                             "Saleh": {"Characters": ["Eirika", "Gerik",
                                                      "Myrrh", "Ewan"],
                                       "Affinity": "Wind"},
                             "Ewan": {"Characters": ["Ross", "Tethys",
                                                     "Saleh", "Dozla",
                                                     "Amelia"],
                                      "Affinity": "Light"},
                             "Cormag": {"Characters": ["Seth", "Artur",
                                                       "Natasha", "Tana",
                                                       "Duessel"],
                                        "Affinity": "Fire"},
                             "Rennac": {"Characters": ["Colm", "Dozla",
                                                       "L'Arachel", "Tethys"],
                                        "Affinity": "Dark"},
                             "Duessel": {"Characters": ["Ephraim", "Cormag",
                                                        "Amelia", "Knoll"],
                                         "Affinity": "Anima"},
                             "Knoll": {"Characters": ["Lute", "Duessel",
                                                      "Natasha"],
                                       "Affinity": "Dark"},
                             "Myrrh": {"Characters": ["Ephraim", "Saleh",
                                                      "Dozla"],
                                       "Affinity": "Wind"},
                             "Syrene": {"Characters": ["Gilliam", "Moulder",
                                                       "Vanessa", "Kyle",
                                                       "Tana"],
                                        "Affinity": "Thunder"}
                            }
            self.num_splits = 0.
        if self.game == "Path of Radiance" or self.game == 9:
            self.game = 9
            self.game_name = "path_of_radiance"
            self.lords = ["Ike"]
            self.start_chars = ["Ike"]
            self.num_splits = 2
            self.split_chars = ([["Ena"], ["Nasir"]],
                                [["Tibarn"], ["Naesala"], ["Giffca"]])
            self.characters = ["Ike", "Titania", "Oscar", "Boyd",
                               "Rhys", "Shinon", "Gatrie", "Soren",
                               "Mia", "Ilyana", "Mist", "Rolf",
                               "Marcia", "Lethe", "Mordecai", "Volke",
                               "Kieran", "Brom", "Nephenee", "Zihark",
                               "Sothe", "Jill", "Astrid", "Makalov",
                               "Tormod", "Muarim", "Stefan", "Devdan",
                               "Tanith", "Reyson", "Janaff", "Ulki",
                               "Calill", "Tauroneo", "Haar", "Ranulf",
                               "Bastian", "Lucia", "Geoffrey", "Largo",
                               "Elincia", "Nasir", "Ena", "Tibarn",
                               "Naesala", "Giffca"]
            self.supports = {"Ike": {"Characters": ["Titania", "Oscar",
                                                    "Soren", "Lethe",
                                                    "Reyson", "Ranulf",
                                                    "Elincia"],
                                     "Affinity": "Earth"},
                             "Titania": {"Characters": ["Ike", "Boyd",
                                                     "Rhys", "Mist"],
                                        "Affinity": "Light"},
                             "Oscar": {"Characters": ["Ike", "Kieran",
                                                     "Janaff", "Tanith"],
                                      "Affinity": "Earth"},
                             "Boyd": {"Characters": ["Titania", "Mist",
                                                      "Brom", "Ulki"],
                                       "Affinity": "Fire"},
                             "Rhys": {"Characters": ["Titania", "Mia",
                                                     "Rolf", "Kieran",
                                                     "Ulki"],
                                      "Affinity": "Fire"},
                             "Shinon": {"Characters": ["Gatrie", "Rolf",
                                                     "Janaff"],
                                      "Affinity": "Thunder"},
                             "Gatrie": {"Characters": ["Ilyana", "Astrid",
                                                     "Marcia", "Shinon"],
                                      "Affinity": "Light"},
                             "Soren": {"Characters": ["Ike", "Stefan"],
                                       "Affinity": "Dark"},
                             "Mia": {"Characters": ["Rhys", "Ilyana",
                                                     "Largo"],
                                      "Affinity": "Fire"},
                             "Ilyana": {"Characters": ["Gatrie", "Mia",
                                                    "Mordecai", "Zihark",
                                                    "Lucia"],
                                     "Affinity": "Light"},
                             "Mist": {"Characters": ["Titania", "Boyd",
                                                       "Rolf", "Mordecai",
                                                       "Jill"],
                                        "Affinity": "Water"},
                             "Rolf": {"Characters": ["Rhys", "Shinon",
                                                     "Marcia", "Mist",
                                                     "Tauroneo"],
                                      "Affinity": "Wind"},
                             "Marcia": {"Characters": ["Gatrie", "Rolf",
                                                     "Kieran", "Tanith"],
                                      "Affinity": "Fire"},
                             "Lethe": {"Characters": ["Ike", "Jill",
                                                      "Muarim", "Ranulf"],
                                         "Affinity": "Heaven"},
                             "Mordecai": {"Characters": ["Ilyana", "Mist",
                                                       "Stefan", "Ulki",
                                                       "Ranulf"],
                                        "Affinity": "Water"},
                             "Volke": {"Characters": ["Bastian"],
                                      "Affinity": "Wind"},
                             "Kieran": {"Characters": ["Oscar", "Rhys",
                                                        "Marcia"],
                                         "Affinity": "Wind"},
                             "Brom": {"Characters": ["Boyd", "Nephenee",
                                                    "Zihark"],
                                     "Affinity": "Water"},
                             "Nephenee": {"Characters": ["Brom", "Devdan",
                                                      "Calill"],
                                       "Affinity": "Wind"},
                             "Zihark": {"Characters": ["Ilyana", "Brom",
                                                     "Muarim"],
                                      "Affinity": "Earth"},
                             "Sothe": {"Characters": ["Astrid", "Tormod"],
                                      "Affinity": "Wind"},
                             "Jill": {"Characters": ["Mist", "Lethe",
                                                     "Haar"],
                                         "Affinity": "Thunder"},
                             "Astrid": {"Characters": ["Gatrie", "Sothe",
                                                       "Makalov"],
                                        "Affinity": "Wind"},
                             "Makalov": {"Characters": ["Astrid", "Haar",
                                                          "Bastian"],
                                           "Affinity": "Thunder"},
                             "Tormod": {"Characters": ["Sothe", "Devdan",
                                                       "Reyson", "Calill"],
                                        "Affinity": "Fire"},
                             "Muarim": {"Characters": ["Lethe", "Zihark",
                                                      "Largo"],
                                       "Affinity": "Thunder"},
                             "Stefan": {"Characters": ["Soren", "Mordecai"],
                                     "Affinity": "Heaven"},
                             "Devdan": {"Characters": ["Nephenee", "Tormod",
                                                     "Largo"],
                                      "Affinity": "Fire"},
                             "Tanith": {"Characters": ["Oscar", "Marcia",
                                                         "Reyson"],
                                          "Affinity": "Earth"},
                             "Reyson": {"Characters": ["Ike", "Tormod",
                                                      "Tanith"],
                                       "Affinity": "Fire"},
                             "Janaff": {"Characters": ["Oscar", "Shinon",
                                                      "Lucia"],
                                       "Affinity": "Thunder"},
                             "Ulki": {"Characters": ["Boyd", "Rhys",
                                                     "Mordecai"],
                                      "Affinity": "Water"},
                             "Calill": {"Characters": ["Nephenee", "Tormod",
                                                      "Geoffrey"],
                                       "Affinity": "Dark"},
                             "Tauroneo": {"Characters": ["Rolf", "Largo"],
                                         "Affinity": "Thunder"},
                             "Haar": {"Characters": ["Jill", "Makalov"],
                                        "Affinity": "Wind"},
                             "Ranulf": {"Characters": ["Ike", "Lethe",
                                                       "Mordecai"],
                                        "Affinity": "Wind"},
                             "Bastian": {"Characters": ["Volke", "Makalov",
                                                      "Lucia"],
                                       "Affinity": "Wind"},
                             "Lucia": {"Characters": ["Ilyana", "Janaff",
                                                     "Bastian"],
                                      "Affinity": "Earth"},
                             "Geoffrey": {"Characters": ["Calill", "Elincia"],
                                        "Affinity": "Fire"},
                             "Largo": {"Characters": ["Mia", "Muarim",
                                                         "Devdan", "Tauroneo"],
                                          "Affinity": "Wind"},
                             "Elincia": {"Characters": ["Ike", "Geoffrey"],
                                         "Affinity": "Heaven"},
                             "Nasir": {"Characters": [],
                                        "Affinity": "Light"},
                             "Ena": {"Characters": [],
                                        "Affinity": "Earth"},
                             "Tibarn": {"Characters": [],
                                        "Affinity": "Heaven"},
                             "Naesala": {"Characters": [],
                                     "Affinity": "Dark"},
                             "Giffca": {"Characters": [],
                                      "Affinity": "Dark"}
                            }
        if self.game == "Radiant Dawn" or self.game == 10:
            self.game = 10
            self.game_name = "radiant_dawn"
            tower = kwargs.get("tower", False)
            if tower:
                herons = ["Rafiel", "Reyson", "Leanne"]
                self.lords = ["Micaiah", "Ike", "Sothe", "Sanaki", "Ena", "Kurthnaga"] + [herons[random.randrange(3)]]
                self.num_splits = 1
                self.split_chars = [["Rafiel"], ["Reyson"], ["Leanne"]]
            else:
                self.lords = ["Micaiah", "Ike"]
                self.num_splits = 0
                self.split_chars = []
            self.characters = ["Micaiah", "Edward", "Leonardo", "Nolan",
                               "Laura", "Sothe", "Ilyana", "Aran",
                               "Meg", "Volug", "Zihark", "Tauroneo",
                               "Jill", "Fiona", "Tormod", "Muarim",
                               "Vika", "Nailah", "Rafiel", "Black Knight", "Elincia",
                               "Marcia", "Leanne", "Nealuchi", "Haar",
                               "Nephenee", "Brom", "Heather", "Lucia",
                               "Mordecai", "Lethe", "Geoffrey", "Kieran",
                               "Makalov", "Astrid", "Danved", "Calill",
                               "Ike", "Titania", "Oscar", "Boyd",
                               "Rolf", "Shinon", "Soren", "Mist",
                               "Gatrie", "Rhys", "Mia", "Ranulf", 
                               "Kyza", "Lyre", "Reyson", "Janaff",
                               "Ulki", "Sigrun", "Tanith", "Naesala",
                               "Skrimir", "Sanaki", "Tibarn", "Pelleas", "Stefan",
                               "Oliver", "Bastian", "Volke", "Renning",
                               "Caineghis", "Giffca", "Ena", "Kurthnaga",
                               "Nasir", "Gareth"]
            self.supports = {"Micaiah": {"Affinity": "Dark"},
                             "Edward": {"Affinity": "Light"},
                             "Leonardo": {"Affinity": "Water"},
                             "Nolan": {"Affinity": "Earth"},
                             "Laura": {"Affinity": "Wind"},
                             "Sothe": {"Affinity": "Wind"},
                             "Ilyana": {"Affinity": "Light"},
                             "Aran": {"Affinity": "Thunder"},
                             "Edward": {"Affinity": "Light"}
                             }
                             
            self.num_chapters = 38
            self.num_characters = len(self.characters)
            self.availability = np.zeros((self.num_characters, self.num_chapters))
            clear = kwargs.get("clear", False)
            """
            Indices for Chapters.
            Part 1:
                Prologue : 0
                Chapter 1 : 1
                Chapter 2 : 2
                Chapter 3 : 3
                Chapter 4 : 4
                Chapter 5 : 5
                Chapter 6 : 6
                Chapter 7 : 7
                Chapter 8 : 8
                Chapter 9 : 9
                Final : 10
            Part 2:
                Prologue : 11
                Chapter 1 : 12
                Chapter 2 : 13
                Chapter 3 : 14
                Final : 15
            Part 3:
                Prologue : 16
                Chapter 1 : 17
                Chapter 2 : 18
                Chapter 3 : 19
                Chapter 4 : 20
                Chapter 5 : 21
                Chapter 6 : 22
                Chapter 7 : 23
                Chapter 8 : 24
                Chapter 9 : 25
                Chapter 10 : 26
                Chapter 11 : 27
                Chapter 12 : 28
                Chapter 13 : 29
                Final : 30
            Part 4:
                Prologue : 31
                Chapter 1 : 32
                Chapter 2 : 33
                Chapter 3 : 34
                Chapter 4 : 35
                Chapter 5 : 36
                Final : 37
            """
            # Micaiah
            dawn_avail = list(range(0, 9)) + [10] + [22] + list(range(28, 30)) + list(range(31, 38))
            mic_avail = list(range(0, 11)) + [22] + list(range(28, 30)) + [31] + [34] + [37]
            ily_avail = list(range(3, 9)) + [10] + list(range(18, 22)) + list(range(23, 25)) + list(range(26, 28)) + list(range(30, 38))
            ike_avail = list(range(16, 22)) + list(range(23, 25)) + list(range(26, 28)) + [30] + [32] + [35] + [37]
            self.availability[0, mic_avail] = 1
            # Edward
            self.availability[1, dawn_avail] = 1
            # Leonardo
            self.availability[2, dawn_avail] = 1
            # Nolan
            avail = dawn_avail[:]
            avail.remove(0)
            self.availability[3, avail] = 1
            # Laura
            avail.remove(1)
            self.availability[4, avail] = 1
            # Sothe
            special_avail = mic_avail[:]
            del special_avail[0:2]
            special_avail.remove(9)
            self.availability[5, special_avail] = 1
            # Ilyana
            self.availability[6, ily_avail] = 1
            # Aran
            avail.remove(2)
            self.availability[7, avail] = 1
            # Meg
            avail.remove(3)
            self.availability[8, avail] = 1
            # Volug
            avail.remove(4)
            self.availability[9, avail] = 1
            # Tauroneo
            special_avail = [6] + list(range(28, 30)) + [33] + [36] + [37]
            self.availability[10, special_avail] = 1
            # Jill
            special_avail = list(range(6, 8)) + [10] + list(range(22, 25)) + list(range(26, 38))
            self.availability[11, special_avail] = 1
            # Zihark
            special_avail = special_avail + [8]
            self.availability[12, special_avail] = 1
            # Fiona
            special_avail = [7] + [10] + [22] + [28] + [29] + list(range(31, 38))
            self.availability[13, special_avail] = 1
            # Tormod
            special_avail = list(range(7, 9)) + [10] + [35] + [37]
            self.availability[14, special_avail] = 1
            # Muarim
            self.availability[15, special_avail] = 1
            # Vika
            self.availability[16, special_avail] = 1
            # Nailah
            special_avail = [8] + [10] + [32] + [35] + [37]
            self.availability[17, special_avail] = 1
            # Rafiel
            self.availability[18, special_avail] = 1
            # Black Knight
            special_avail = list(range(9, 11)) + [22]
            self.availability[19, special_avail] = 1
            # Elincia
            special_avail = [11] + [15] + [33] + [36] + [37]
            self.availability[20, special_avail] = 1
            # Marcia
            special_avail = [11] + [14] + [15] + [25] + [27] + list(range(30, 38))
            self.availability[21, special_avail] = 1
            # Nealuchi
            special_avail = [11] + [13] + [15] + list(range(31, 38))
            self.availability[22, special_avail] = 1
            # Leanne
            special_avail = [11] + [13] + [15] + [27] + [31] + [34] + [37]
            self.availability[23, special_avail] = 1
            # Haar
            special_avail = [11] + [15] + list(range(18, 22)) + list(range(23, 25)) + list(range(26, 28)) + list(range(30, 38))
            self.availability[24, special_avail] = 1
            # Brom
            special_avail = [12] + [13] + [15] + list(range(18, 22)) + list(range(23, 25)) + list(range(26, 28)) + list(range(30, 38))
            self.availability[25, special_avail] = 1
            # Nephenee
            self.availability[26, special_avail] = 1
            # Heather
            self.availability[27, special_avail] = 1
            # Lucia
            special_avail = [13] + [33] + [36] + [37]
            self.availability[28, special_avail] = 1
            # Lethe
            special_avail = [13] + [15] + [20] + list(range(23, 25)) + list(range(26, 28)) + list(range(30, 38))
            self.availability[29, special_avail] = 1
            # Mordecai
            self.availability[30, special_avail] = 1
            # Geoffrey
            special_avail = [14] + [15] + [25] + [36] + [37]
            self.availability[31, special_avail] = 1
            # Kieran
            special_avail = special_avail + [27] + list(range(30, 36))
            self.availability[32, special_avail] = 1
            # Astrid
            self.availability[33, special_avail] = 1
            # Makalov
            self.availability[34, special_avail] = 1
            # Danved
            self.availability[35, special_avail] = 1
            # Calill
            special_avail.remove(14)
            self.availability[36, special_avail] = 1
            # Ike
            self.availability[37, ike_avail] = 1
            # Titania
            self.availability[38, ike_avail] = 1
            # Soren
            self.availability[39, ike_avail] = 1
            # Mist
            self.availability[40, ike_avail] = 1
            # Rolf
            avail = ike_avail[:]
            avail = avail + [31] + [33] + [34] + [36]
            self.availability[41, avail] = 1
            # Boyd
            self.availability[42, avail] = 1
            # Oscar
            self.availability[43, avail] = 1
            # Shinon
            self.availability[44, avail] = 1
            # Gatrie
            self.availability[45, avail] = 1
            # Rhys
            self.availability[46, avail] = 1
            # Mia
            self.availability[47, avail] = 1
            # Ranulf
            avail = [20] + [23] + [24] + [26] + [27] + [30] + [33] + [36] + [37]
            self.availability[48, avail] = 1
            # Kyza
            avail = avail + list(range(31, 33)) + list(range(34, 36))
            self.availability[49, avail] = 1
            # Lyre
            self.availability[50, avail] = 1
            # Reyson
            avail = [21] + [23] + [24] + [26] + [30] + [33] + [36] + [37]
            self.availability[51, avail] = 1
            # Janaff
            avail = [23] + [24] + [26] + [27] +  [30] + list(range(31, 38))
            self.availability[52, avail] = 1
            # Ulki
            self.availability[53, avail] = 1
            # Sigrun
            avail = [27] + [30] + [31] + [34] + [37]
            self.availability[54, avail] = 1
            # Tanith
            avail = avail + [32] + [33] + [35] + [36]
            self.availability[55, avail] = 1
            # Skrimir
            avail = [31] + [34] + [37]
            self.availability[56, avail] = 1
            # Sanaki
            self.availability[57, avail] = 1
            # Naesala
            self.availability[58, avail] = 1
            # Tibarn
            avail = [33] + [36] + [37]
            self.availability[59, avail] = 1
            # Pelleas
            if clear:
                self.availability[60, avail] = 1
            else:
                pass
            # Stefan
            avail = [34] + [37]
            self.availability[61, avail] = 1
            # Oliver
            avail.remove(34)
            avail = avail + [35]
            self.availability[62, avail] = 1
            # Bastian
            self.availability[63, 36:] = 1
            # Volke
            self.availability[64, 36:] = 1
            # Caineghis
            self.availability[65, 37] = 1
            # Giffca
            self.availability[66, 37] = 1
            # Kurthnaga
            self.availability[67, 37] = 1
            # Ena
            self.availability[68, 37] = 1
            # Renning
            self.availability[69, 37] = 1
            # Nasir
            self.availability[70, 37] = 1
            # Gareth
            self.availability[71, 37] = 1
            # Lehran
            if clear:
                self.availability[72, 37] = 1
            else:
                pass
        if self.game == "Shadow Dragon" or self.game == 11:
            self.game = 11
            self.game_name = "shadow_dragon"
            self.lords = ["Marth"]
            self.start_chars = ["Marth", "Jagen", "Abel", "Cain",
                                "Gordin", "Draug", "Caeda"]
            self.characters = ["Marth", "Jagen", "Abel", "Cain",
                               "Gordin", "Draug", "Caeda", "Wrys",
                               "Ogma", "Barst", "Bord", "Cord",
                               "Castor", "Darros", "Julian", "Lena",
                               "Navarre", "Merric", "Matthis", "Hardin",
                               "Wolf", "Sedgar", "Roshea", "Vyland",
                               "Wendell", "Rickard", "Bantu", "Caesar",
                               "Radd", "Roger", "Jeorge", "Maria",
                               "Minerva", "Linde", "Jake", "Midia",
                               "Dolph", "Macellan", "Tomas", "Boah",
                               "Beck", "Astram", "Palla", "Catria",
                               "Arran", "Samson", "Xane", "Est",
                               "Tiki", "Lorenz", "Elice", "Gotoh",
                               "Athena", "Horace", "Etzel", "Ymir",
                               "Nagi"]
            self.mode = kwargs.get("mode", "Hard")
            self.normal_characters = self.characters + ["Frey", "Norne"]
            self.num_splits = 2
            self.split_chars = ([["Arran"], ["Samson"]], [["Gotoh", "Tiki"], ["Nagi"]])
        if self.game == "New Mystery" or self.game == 12:
            pass
        if self.game == "Awakening" or self.game == 13:
            self.game = 13
            self.game_name = "awakening"
            self.lords = ["Chrom"]
            self.start_chars = ["Chrom", "Robin (M)", "Robin (F)", "Lissa",
                                "Frederick"]
            self.characters = ["Chrom", "Robin (M)", "Robin (F)", "Lissa",
                               "Frederick", "Sully", "Virion", "Stahl", 
                               "Vaike", "Miriel", "Sumia", "Kellam", "Donnel",
                               "Lon'qu", "Ricken", "Maribelle", "Panne",
                               "Gaius", "Cordelia", "Gregor", "Nowi",
                               "Libra", "Tharja", "Anna", "Olivia",
                               "Cherche", "Henry", "Say'ri", "Tiki",
                               "Basilio", "Flavia", "Gangrel", "Walhart",
                               "Emmeryn", "Yen'fay", "Aversa", "Priam"]
            self.children = ["Lucina", "Owain", "Inigo", "Brady",
                             "Kjelle", "Cynthia", "Severa", "Gerome",
                             "Morgan (M)", "Morgan (F)", "Yarne", "Laurent",
                             "Noire", "Nah"]
            self.supports = {"Chrom": {"Romantic": ["Robin (F)", "Maribelle",
                                                    "Olivia", "Sully",
                                                    "Sumia"],
                                       "Other": ["Robin (M)", "Frederick",
                                                 "Gaius", "Lissa", "Vaike",
                                                 "Lucina", "Brady", "Cynthia",
                                                 "Inigo", "Kjelle", "Morgan"]
                                       },
                             "Robin (M)": {"Romantic": ["Lissa", "Sully",
                                                        "Miriel", "Sumia",
                                                        "Maribelle", "Panne",
                                                        "Cordelia", "Nowi",
                                                        "Tharja", "Anna",
                                                        "Olivia", "Cherche",
                                                        "Say'ri", "Nowi",
                                                        "Flavia", "Lucina",
                                                        "Kjelle", "Cynthia",
                                                        "Severa", "Noire",
                                                        "Nah", "Emmeryn",
                                                        "Aversa"],
                                           "Other": ["Chrom", "Frederick",
                                                     "Virion", "Stahl", "Vaike",
                                                     "Lucina", "Brady", "Cynthia",
                                                     "Inigo", "Kjelle", "Morgan"]
                                       },
                             "Oscar": {"Characters": ["Ike", "Kieran",
                                                     "Janaff", "Tanith"],
                                      "Affinity": "Earth"},
                             "Boyd": {"Characters": ["Titania", "Mist",
                                                      "Brom", "Ulki"],
                                       "Affinity": "Fire"},
                             "Rhys": {"Characters": ["Titania", "Mia",
                                                     "Rolf", "Kieran",
                                                     "Ulki"],
                                      "Affinity": "Fire"},
                             "Shinon": {"Characters": ["Gatrie", "Rolf",
                                                     "Janaff"],
                                      "Affinity": "Thunder"},
                             "Gatrie": {"Characters": ["Ilyana", "Astrid",
                                                     "Marcia", "Shinon"],
                                      "Affinity": "Light"},
                             "Soren": {"Characters": ["Ike", "Stefan"],
                                       "Affinity": "Dark"},
                             "Mia": {"Characters": ["Rhys", "Ilyana",
                                                     "Largo"],
                                      "Affinity": "Fire"},
                             "Ilyana": {"Characters": ["Gatrie", "Mia",
                                                    "Mordecai", "Zihark",
                                                    "Lucia"],
                                     "Affinity": "Light"},
                             "Mist": {"Characters": ["Titania", "Boyd",
                                                       "Rolf", "Mordecai",
                                                       "Jill"],
                                        "Affinity": "Water"},
                             "Rolf": {"Characters": ["Rhys", "Shinon",
                                                     "Marcia", "Mist",
                                                     "Tauroneo"],
                                      "Affinity": "Wind"},
                             "Marcia": {"Characters": ["Gatrie", "Rolf",
                                                     "Kieran", "Tanith"],
                                      "Affinity": "Fire"},
                             "Lethe": {"Characters": ["Ike", "Jill",
                                                      "Muarim", "Ranulf"],
                                         "Affinity": "Heaven"},
                             "Mordecai": {"Characters": ["Ilyana", "Mist",
                                                       "Stefan", "Ulki",
                                                       "Ranulf"],
                                        "Affinity": "Water"},
                             "Volke": {"Characters": ["Bastian"],
                                      "Affinity": "Wind"},
                             "Kieran": {"Characters": ["Oscar", "Rhys",
                                                        "Marcia"],
                                         "Affinity": "Wind"},
                             "Brom": {"Characters": ["Boyd", "Nephenee",
                                                    "Zihark"],
                                     "Affinity": "Water"},
                             "Nephenee": {"Characters": ["Brom", "Devdan",
                                                      "Calill"],
                                       "Affinity": "Wind"},
                             "Zihark": {"Characters": ["Ilyana", "Brom",
                                                     "Muarim"],
                                      "Affinity": "Earth"},
                             "Sothe": {"Characters": ["Astrid", "Tormod"],
                                      "Affinity": "Wind"},
                             "Jill": {"Characters": ["Mist", "Lethe",
                                                     "Haar"],
                                         "Affinity": "Thunder"},
                             "Astrid": {"Characters": ["Gatrie", "Sothe",
                                                       "Makalov"],
                                        "Affinity": "Wind"},
                             "Makalov": {"Characters": ["Astrid", "Haar",
                                                          "Bastian"],
                                           "Affinity": "Thunder"},
                             "Tormod": {"Characters": ["Sothe", "Devdan",
                                                       "Reyson", "Calill"],
                                        "Affinity": "Fire"},
                             "Muarim": {"Characters": ["Lethe", "Zihark",
                                                      "Largo"],
                                       "Affinity": "Thunder"},
                             "Stefan": {"Characters": ["Soren", "Mordecai"],
                                     "Affinity": "Heaven"},
                             "Devdan": {"Characters": ["Nephenee", "Tormod",
                                                     "Largo"],
                                      "Affinity": "Fire"},
                             "Tanith": {"Characters": ["Oscar", "Marcia",
                                                         "Reyson"],
                                          "Affinity": "Earth"},
                             "Reyson": {"Characters": ["Ike", "Tormod",
                                                      "Tanith"],
                                       "Affinity": "Fire"},
                             "Janaff": {"Characters": ["Oscar", "Shinon",
                                                      "Lucia"],
                                       "Affinity": "Thunder"},
                             "Ulki": {"Characters": ["Boyd", "Rhys",
                                                     "Mordecai"],
                                      "Affinity": "Water"},
                             "Calill": {"Characters": ["Nephenee", "Tormod",
                                                      "Geoffrey"],
                                       "Affinity": "Dark"},
                             "Tauroneo": {"Characters": ["Rolf", "Largo"],
                                         "Affinity": "Thunder"},
                             "Haar": {"Characters": ["Jill", "Makalov"],
                                        "Affinity": "Wind"},
                             "Ranulf": {"Characters": ["Ike", "Lethe",
                                                       "Mordecai"],
                                        "Affinity": "Wind"},
                             "Bastian": {"Characters": ["Volke", "Makalov",
                                                      "Lucia"],
                                       "Affinity": "Wind"},
                             "Lucia": {"Characters": ["Ilyana", "Janaff",
                                                     "Bastian"],
                                      "Affinity": "Earth"},
                             "Geoffrey": {"Characters": ["Calill", "Elincia"],
                                        "Affinity": "Fire"},
                             "Largo": {"Characters": ["Mia", "Muarim",
                                                         "Devdan", "Tauroneo"],
                                          "Affinity": "Wind"},
                             "Elincia": {"Characters": ["Ike", "Geoffrey"],
                                         "Affinity": "Heaven"},
                             "Nasir": {"Characters": [],
                                        "Affinity": "Light"},
                             "Ena": {"Characters": [],
                                        "Affinity": "Earth"},
                             "Tibarn": {"Characters": [],
                                        "Affinity": "Heaven"},
                             "Naesala": {"Characters": [],
                                     "Affinity": "Dark"},
                             "Giffca": {"Characters": [],
                                      "Affinity": "Dark"}
                            }
        if self.game == "Fates" or self.game == 14:
            self.characters = ["Corrin (M)", "Corrin (F)", "Azura",
                               "Felicia", "Jakob", "Silas", "Kaze",
                               "Mozu", "Shura"]
            characters_conquest = ["Xander", "Camilla", "Leo", "Elise",
                                   "Laslow", "Peri", "Selena", "Beruka",
                                   "Odin", "Niles", "Effie", "Arthur",
                                   "Nyx", "Charlotte", "Benny", "Keaton",
                                   "Gunter", "Flora", "Izana"]
        if self.game == "Shadows of Valentia" or self.game == 15:
            pass
        if self.game == "Three Houses" or self.game == 16:
            pass
            
            
    def rd_optimize(self, chosen):
        result_mat = np.zeros_like(self.availability)
        result = np.zeros(self.num_chapters)
        for i in range(self.num_chapters):
            result_mat[:, i] = np.multiply(chosen, self.availability[:, i])
        for j in range(self.num_chapters):
            result[j] = np.sum(result_mat[:, j])
        return result
                
        
    def randomize(self, num_chars, **kwargs):
        if self.game == 10:
            all_chapters = kwargs.get("all_chapters", True)
            repeat = True
            if all_chapters:
                while repeat:
                    force_lord = kwargs.get("force_lord", False)
                    if force_lord:
                        lord = kwargs.get("lord", "all")
                    available_chars = self.characters[:]
                    self.chars_run = []
                    if force_lord:
                        if lord == "all":
                            starter_char = self.lords
                            num_start = len(self.lords)
                            for s in starter_char:
                                self.chars_run.append(s)
                                available_chars.remove(s)
                        else:
                            starter_char = lord
                            num_start = len(lord)
                            for s in starter_char:
                                self.chars_run.append(s)
                                available_chars.remove(s)
                    else:
                        if all_chapters:
                            starter_char = self.start_chars[random.randrange(len(self.start_chars))]
                            num_start = 1
                            self.chars_run.append(starter_char)
                            available_chars.remove(starter_char)
                        else:
                            num_start = 0
                    split_chosen = False
                    for i in range(num_chars - num_start):
                        next_char = available_chars[random.randrange(len(available_chars))]
                        self.chars_run.append(next_char)
                        available_chars.remove(next_char)
                        if split_chosen == False:
                            if self.num_splits > 1:
                                if next_char in np.concatenate(sum(self.split_chars, [])):
                                    for i in range(self.num_splits):
                                        split = self.split_chars[i]
                                        for j in range(len(split)):
                                            if next_char not in split[j]:
                                                for k in range(len(split[j])):
                                                    available_chars.remove(split[j][k])
                            else:
                                if next_char in sum(self.split_chars, []):
                                    for i in range(len(self.split_chars)):
                                        split = self.split_chars[i]
                                        if next_char not in split:
                                            for j in range(len(split)):
                                                available_chars.remove(split[j])
                            split_chosen = True
                    chosen = np.zeros(self.num_characters)
                    for i in range(num_chars):
                        idx = self.characters.index(self.chars_run[i])
                        chosen[idx] = 1
                    cons = {'type': 'eq',
                                  'fun' : lambda x: np.sum(x) - num_chars}
                    if 0 not in self.rd_optimize(chosen):
                        repeat = False
                    
        else:
            force_lord = kwargs.get("force_lord", False)
            if force_lord:
                lord = kwargs.get("lord", "all")
            all_chapters = kwargs.get("all_chapters", True)
            available_chars = self.characters[:]
            self.chars_run = []
            if force_lord:
                if lord == "all":
                    starter_char = self.lords
                    num_start = len(self.lords)
                    for s in starter_char:
                        self.chars_run.append(s)
                        available_chars.remove(s)
                else:
                    starter_char = lord
                    num_start = len(lord)
                    for s in starter_char:
                        self.chars_run.append(s)
                        available_chars.remove(s)
            else:
                if all_chapters:
                    starter_char = self.start_chars[random.randrange(len(self.start_chars))]
                    num_start = 1
                    self.chars_run.append(starter_char)
                    available_chars.remove(starter_char)
                else:
                    num_start = 0
            if self.num_splits > 0:
                split_chosen = False
            else:
                split_chosen = True
            for i in range(num_chars - num_start):
                next_char = available_chars[random.randrange(len(available_chars))]
                self.chars_run.append(next_char)
                available_chars.remove(next_char)
                if not split_chosen:
                    if self.num_splits > 1:
                        if next_char in np.concatenate(sum(self.split_chars, [])):
                            for i in range(self.num_splits):
                                split = self.split_chars[i]
                                for j in range(len(split)):
                                    if next_char not in split[j]:
                                        for k in range(len(split[j])):
                                            available_chars.remove(split[j][k])
                            split_chosen = True
                    else:
                        if next_char in sum(self.split_chars, []):
                            for i in range(len(self.split_chars)):
                                split = self.split_chars[i]
                                if next_char not in split:
                                    for j in range(len(split)):
                                        available_chars.remove(split[j])
                            split_chosen -= 1
                            
        self.chars_run_ordered = []
        for i in range(len(self.characters)):
            for j in range(len(self.chars_run)):
                if self.chars_run[j] == self.characters[i]:
                    self.chars_run_ordered.append(self.characters[i])
        print(self.chars_run_ordered)
        
        details = kwargs.get("detailed_report", False)
        if details:
            fn = "./" + self.game_name + "randomizer_report.txt"
            f = open(fn, "w")
            f.write("Fire Emblem " + str(self.game) + " Random Draft\n")
            f.write("-----------------------------------------\n\n")
            for chars in self.chars_run_ordered:
                if self.game > 5:
                    # Add recruitment here
                    if self.game == 10:
                        f.write(chars + ": " + "\n------------------")
                    elif self.game == 11:
                        f.write(chars + ": " + "\n------------------")
                    else:
                        f.write(chars + ": " + self.supports[chars]["Affinity"] + "\n------------------")
                        for j in range(len(self.supports[chars]["Characters"])):
                            if self.supports[chars]["Characters"][j] in self.chars_run_ordered:
                                sup_idx = self.chars_run_ordered.index(self.supports[chars]["Characters"][j])
                                sup_char = self.chars_run_ordered[sup_idx]
                                f.write("\n" + self.supports[chars]["Characters"][j] + " : " + self.supports[sup_char]["Affinity"])
                    f.write("\n\n")
                elif self.game == 5:
                    char_idx = self.characters.index(chars)
                    f.write(chars + ": " + "Recruited in Chapter " + self.recruitment[char_idx] + "\n------------------")
                    for j in range(len(self.supports[chars]["Characters"])):
                        if self.supports[chars]["Characters"][j] in self.chars_run_ordered:
                            sup_idx = self.chars_run_ordered.index(self.supports[chars]["Characters"][j])
                            sup_char = self.chars_run_ordered[sup_idx]
                            f.write("\n" + self.supports[chars]["Characters"][j] + " : " + self.supports[chars]["Bonus"][j])
                    f.write("\n\n")
        
        
fe = Game(8)
fe.randomize(12, all_chapters=True, force_lord=True, detailed_report=True)
        