
algos = [
    {
        "num": 1,
        "shema":
            [
                ['_', '_', 'Y', '_', '_'],
                ['Y', '_', '_', 'Y', '_'],
                ['_', 'Y', 'Y', 'Y', '_'],
                ['Y', '_', '_', 'Y', '_'],
                ['_', '_', 'Y', '_', '_']
            ],
        "mouves": ["F", "R", "U", "R'", "U'", "F'"],
    },

    {
            "num": 2,
            "shema":
                [
                    ['_', '_', '_', 'Y', '_'],
                    ['Y', '_', 'Y', '_', '_'],
                    ['_', 'Y', 'Y', '_', 'Y'],
                    ['Y', '_', '_', '_', '_'],
                    ['_', '_', 'Y', 'Y', '_']
                ],
            "mouves": ["F", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "F'"],
    },


    {
            "num": 3,
            "shema":
                [
                    ['_', 'Y', '_', 'Y', '_'],
                    ['_', '_', 'Y', '_', '_'],
                    ['_', 'Y', 'Y', 'Y', '_'],
                    ['_', '_', 'Y', '_', '_'],
                    ['_', 'Y', '_', 'Y', '_']
                ],
            "mouves": ["y", "R'", "U'", "R", "U'", "R'", "U", "R", "U'", "R'", "U2", "R"],
    },
    {
        "num": 4,
        "shema":
            [
                ['_', '_', 'Y', '_', '_'],
                ['Y', '_', '_', 'Y', '_'],
                ['Y', '_', 'Y', 'Y', '_'],
                ['Y', '_', 'Y', 'Y', '_'],
                ['_', '_', '_', '_', '_']
            ],
        # f (R U R' U') f'
        "mouves": ["f", "R", "U", "R'", "U'", "f'"],
    },
    {
        "num": 5,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # f (R U R' U') (R U R' U') f'
        "mouves": ["f", "R", "U", "R'", "U'", "R", "U", "R'", "U'", "f'"],

    },
    {
        "num": 6,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # f ' (L' U' L U) f
        "mouves": ["f'", "L'", "U'", "L", "U", "f"],
    },
    {
        "num": 7,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', 'Y'],
            ['_', 'Y', 'Y', '_', '_']
            ],
            # F' (L' U' L U) (L' U' L U) F
        "mouves": ["F'", "L'", "U'", "L", "U", "L'", "U'", "L", "U", "F"],
    },

    {
        "num": 8,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['Y', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', '_']],
        # [F (R U R' U') F'] U [F (R U R' U') F' ]
        "mouves": ["F", "R", "U", "R'", "U'", "F", "U", "F", "R", "U", "R'", "U'", "F'"]
    },
    {
        "num": 9,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # [F' (L' U' L U) F] y [F (R U R' U') F'] 
        # y (r U R' U)(R' F R F') R U2 r'
        "mouves": ["F'", "L'", "U'", "L", "U", "F", "y", "F", "R", "U", "R'", "U'", "F'"]        
                    
    },

    {
        "num": 10,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # [f (R U R' U') f'] U [F (R U R' U') F' ]
        "mouves": ["f", "R", "U", "R'", "U'", "f'", "U", "F", "R", "U", "R'", "U'", "F'"]
    },

    {
        "num": 11,
        "shema":
            [['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        # [f (R U R' U') f'] U' [F (R U R' U') F' ]
        "mouves": ["f", "R", "U", "R'", "U'", "f'", "U'", "F", "R", "U", "R'", "U'", "F'"]

    },
    {
        "num": 12,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # [F (R U R' U') F' ] [f (R U R' U') f']
        "mouves": ["F", "R", "U", "R'", "U'", "F'", "f", "R", "U", "R'", "U'", "f'"],

    },
    {
        "num": 13,
        "shema":
            [['_', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_']],
        # R U2' R2' U' R2 U' R2' U2 R
        "mouves": ["R", "U2", "R2", "U'", "R2", "U'", "R2", "U2", "R"]
    },
    {
        "num": 14,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['Y', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', 'Y'],
            ['_', 'Y', 'Y', '_', '_']],
            # (r U r') (R U R' U') (r U' r')
        "mouves": ["r", "U", "r'", "R", "U", "R'", "U'", "r", "U'", "r'"]
    },
    {
        "num": 15,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_']],
        # (l' U' l) (L' U' L U) (l' U l)
        "mouves": ["l'", "U'", "l", "L'", "U'", "L", "U", "l'", "U", "l"],
    },
    {
        "num": 16,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', '_', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', '_', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        # R' [F (R U R' U') F'] U R
        "mouves": ["R'", "F", "R", "U", "R'", "U'", "F'", "U", "R"]
    },
    {
        "num": 17,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', 'Y', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        # (R U R' U') M' (U R U' r')
        "mouves": ["R", "U", "R'", "U'", "M'", "U", "R", "U'", "r'"]
    },
    {
        "num": 18,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        # M U (R U R' U') M2 (U R U' r')
        "mouves": ["M", "U", "R", "U", "R'", "U'", "M2", "U", "R", "U'", "r'"]
    },
    {
        "num": 19,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['Y', '_', '_', '_', 'Y'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', 'Y', '_', 'Y', 'Y'],
            ['_', '_', 'Y', '_', '_']],
        # F (R U R' U') R F' (r U R' U') r'
        "mouves": ["F", "R", "U", "R'", "U'", "R", "F'", "r", "U", "R'", "U'", "r'"]
    },
    {
        "num": 20,
        "shema":
            [['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # (R U R' U') (R' F R F')
        "mouves": ["R", "U", "R'", "U'", "R'", "F", "R", "F'"]
    },
    {
        "num": 21,
        "shema":
        [['_', 'Y', '_', '_', '_'],
        ['_', '_', 'Y', 'Y', '_'],
        ['_', 'Y', 'Y', 'Y', '_'],
        ['_', '_', 'Y', 'Y', '_'],
        ['_', 'Y', '_', '_', '_']],

        # (r U R' U') (r' F R F')
        "mouves": ["r", "U", "R'", "U'", "r'", "F", "R", "F'"],
    },

    {
        "num": 22,
        "shema":
            [['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', '_']],
        # F' (r U R' U') (r' F R )
        "mouves": ["F'", "r", "U", "R'", "U'", "r'", "F", "R"]
    },
    {
        "num": 23,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # R' U' (R' F R F') U R
        "mouves": ["R'", "U'", "R'", "F", "R", "F'", "U", "R"]

    },
    {
        "num": 24,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # R' U' (R' F R F') U R
        "mouves": ["R'", "U'", "R'", "F", "R", "F'", "U", "R"]
    },
    {
        "num": 25,
        "shema":
            [['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        # (R U2 R') (R' F R F') (R U2 R')
        "mouves": ["R", "U2", "R'", "R'", "F", "R", "F'", "R", "U2", "R'"]
    },
    {
        "num": 26,
        "shema":
            [['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # M ?????
        # M U (R U R' U') M' (R' F R F')
        "mouves": ["M", "U", "R", "U", "R'", "U'", "M'", "R'", "F", "R", "F'"]
    },
    {
        "num": 27,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_']],
        # (R' F R' F') R2 U2 y (R' F R F')
        "mouves": ["R'", "F", "R'", "F'", "R2", "U2", "y", "R'", "F", "R", "F'"]

    },

    {
        "num": 28,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', 'Y'],
            ['_', '_', 'Y', '_', '_']],
        # (R U R' U) (R U' R' U') (R' F R F')
        "mouves": ["R", "U", "R'", "U", "R", "U'", "R'", "U'", "R'", "F", "R", "F'"]
    },
    {
        "num": 29,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # (L' U' L U') (L' U L U) (L F' L' F)
        "mouves": ["L'", "U'", "L", "U'", "L'", "U", "L", "U", "L", "F'", "L'", "F"]

    },

    {
        "num": 30,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', '_']],
        # (R U R' U) R d' R U' R' F'
        "mouves": ["R", "U", "R'", "U", "R", "d'", "R", "U'", "R'", "F'"]

    },
    {
        "num": 31,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['Y', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
            # (R U R' U) (R' F R F') U2 (R' F R F')
        "mouves": ["R", "U", "R'", "U", "R'", "F", "R", "F'", "U2", "R'", "F", "R", "F'"]
    },
    {
        "num": 32,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', 'Y'],
            ['_', '_', 'Y', '_', '_']
            ],
        "mouves": ["F", "R", "U", "R'", "U", "F'", "y'", "U2", "R", "F", "R", "F'"],
    },

    {
        "num": 33,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # r' U2 (R U R' U) r
        "mouves": ["r'", "U2", "R", "U", "R'", "U", "r"],

    },
    {
        "num": 34,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_']],
        # (r U R' U) R U2 r'
        "mouves": ["r", "U", "R'", "U", "R", "U2", "r'"]
    },
    {
        "num": 35,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_']],
        # (R U R' U) R U2 R'
        "mouves": ["R", "U", "R'", "U", "R", "U2", "R'"],

    },
    {
        "num": 36,
        "shema":
            [['_', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # R U2 R' U' R U' R'
        "mouves": ["R", "U2", "R'", "U'", "R", "U'", "R'"]

    },
    {
        "num": 37,

        "shema":
            [['_', '_', '_', '_', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', '_', 'Y', '_'],
            ['_', '_', 'Y', '_', '_']],
        #1 [ R' U2 (R U R' U) R] y [F (R U R' U') F']
        #2 (R' F R F') (R' F R F') (R U R' U') (R U R')
        "mouves": ["R'", "U2", "R", "U", "R'", "U", "R", "y", "F", "R", "U", "R'", "U'", "F'"]
    },
    {
            "num": 38,
            "shema":
                [['_', '_', 'Y', '_', '_'],
                 ['_', 'Y', '_', 'Y', '_'],
                 ['Y', '_', 'Y', 'Y', '_'],
                 ['_', '_', 'Y', '_', '_'],
                 ['_', 'Y', '_', 'Y', '_']],
            "mouves": ["R", "U", "R'", "U", "R", "U2", "R'", "F", "R", "U", "R'", "U'", "F'"]
    },
    {
        "num": 39,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', 'Y'],
            ['_', '_', 'Y', '_', '_']],
        # (r U R' U) (R U' R' U) R U2' r'
        "mouves": ["r", "U", "R'", "U", "R", "U'", "R'", "U", "R", "U2", "r'"]

    },
    {
        "num": 40,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['Y', '_', '_', '_', 'Y'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        "mouves": ["l'", "U'", "L", "U'", "L'", "U", "L", "U'", "L'", "U2", "l"]
    },

    {
        "num": 41,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # r U2 R' U' R U' r'
        "mouves": ["r", "U2", "R'", "U'", "R", "U'", "r'"]
    },
    {
        "num": 42,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # F R U' R' U' R U R' F'
        "mouves": ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'"]
    },
    {
            "num": 43,
            "shema":
                [['_', '_', 'Y', 'Y', '_'],
                 ['_', 'Y', '_', '_', '_'],
                 ['_', 'Y', 'Y', '_', 'Y'],
                 ['_', '_', 'Y', '_', 'Y'],
                 ['_', 'Y', '_', '_', '_']],
            "mouves": ["r'", "U'", "R", "U'", "R'", "U2", "r"]
    },
    {
        "num": 44,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', '_']],
        # M' U M U2 M' U M
        "mouves": ["M'", "U", "M", "U2", "M'", "U", "M"]
    },

    {
            "num": 45,
            "shema":
                [
                    ['_', '_', 'Y', '_', '_'],
                    ['Y', '_', '_', '_', 'Y'],
                    ['_', 'Y', 'Y', 'Y', '_'],
                    ['_', 'Y', '_', 'Y', '_'],
                    ['_', '_', 'Y', '_', '_']
                ],
            "mouves": ["R", "U", "R2", "U'", "R'", "F", "R", "U", "R", "U'", "F"]
    },

    {
        "num": 46,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', '_']],

        # F U R U' R2 F' R (U R U' R')
        "mouves": ["F", "U", "R", "U'", "R2", "F'", "R", "U", "R", "U'", "R'"]
    },
    {
        "num": 47,
        "shema":
            [['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', '_', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', '_', '_', '_', 'Y'],
            ['_', 'Y', 'Y', '_', '_']],
        # R' F R U R' F' R y' (R U' R')
        "mouves": ["R'", "F", "R", "U", "R'", "F'", "R", "y'", "R", "U'", "R'"]
    },
    {
        "num": 48,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', 'Y', '_']],
        # R2 [D (R' U2) R] [D' (R' U2) R']
        "mouves": ["R2", "D", "R'", "U2", "R", "D'", "R'", "U2", "R'"]
    },
    {
        "num": 49,
        "shema":
            [['_', '_', '_', '_', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # R' U2 R2 U R' U R U2 x' U' R' U
        "mouves": ["R'", "U2", "R2", "U", "R'", "U", "R", "U2", "x'", "U'", "R'", "U"]
    },
    {
        "num": 50,
        "shema":
        [['_', 'Y', 'Y', '_', '_'],
        ['_', '_', '_', 'Y', '_'],
        ['Y', '_', 'Y', 'Y', '_'],
        ['_', '_', 'Y', 'Y', '_'],
        ['_', 'Y', '_', '_', '_']],
        # R U B' U' R' U R B R' 
        # R d L' d' R' U R B R'
    "mouves": ["R", "U", "B'", "U'", "R'", "U", "R", "B", "R'"]

    },
    {
        "num": 51,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # R' U' F U R U' R' F' R
    },
    {
        "num": 52,
        "shema":
            [['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', 'Y', '_'],
            ['_', 'Y', '_', '_', 'Y'],
            ['_', '_', 'Y', '_', '_']],
        # R B' R' U' R U B U' R' y2 L F' (L' U' L U) F U' L'
        "mouves": ["R", "B'", "R'", "U'", "R", "U", "B", "U'", "R'", "y2", "L", "F'", "L'", "U'", "L", "U", "F", "U'", "L'"],
    },
    {
        "num": 53,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', '_', 'Y'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', 'Y'],
            ['_', 'Y', 'Y', '_', '_']],
        # R' F R2 B' R2' F' R2 B R'
        "mouves": ["R'", "F", "R2", "B'", "R2", "F'", "R2", "B", "R'"]
    },
    {
        "num": 54,
        "shema":
            [['_', 'Y', '_', '_', '_'],
            ['_', '_', 'Y', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],

        # 1 (R U R' U') R U' R' F' U' F (R U R')
        # 2 [F (R U R' U') F'] U2 [(R U R' U') (R' F R F')]
        "mouves": ["R", "U", "R'", "U'", "R", "U'", "R'", "F'", "U'", "F", "R", "U", "R'"]
    },
    {
        "num": 55,
        "shema":
            [['_', '_', 'Y', '_', '_'],
            ['_', 'Y', '_', 'Y', '_'],
            ['Y', '_', 'Y', 'Y', '_'],
            ['Y', '_', 'Y', '_', 'Y'],
            ['_', '_', '_', '_', '_']],
        # (R2 U R' B' R) U' (R2 U R B R')
        "mouves": ["R2", "U", "R'", "B'", "R", "U'", "R2", "U", "R", "B", "R'"]
    },

    {
        "num": 56,
        "shema":
            [['_', '_', '_', 'Y', '_'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', '_']],
        # (R U R' U') R' F R2 U R' U' F'
        "mouves": ["R", "U", "R'", "U'", "R'", "F", "R2", "U", "R'", "U'", "F'"]
    },
    {
        "num": 57,
        "shema":
            [['_', 'Y', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_'],
            ['_', 'Y', 'Y', '_', 'Y'],
            ['Y', '_', 'Y', '_', '_'],
            ['_', '_', '_', 'Y', '_']],
        # R U R' y R' F R U' R' F' R
        "mouves": ["R", "U", "R'", "y", "R'", "F", "R", "U'", "R'", "F'", "R"]
    },
]

# 46