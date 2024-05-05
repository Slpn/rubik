algos = [
    {
        "num": 1,
        "shema":
        {
            "coins": [],
            "edges": [
                [(0, 1), (1, 2)],
                [(1, 0), (0, 1)],
                [(1, 2), (1, 0)]
            ],
        },
        # R U' R U R U R U' R' U' R2
        "mouves": ["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R2"]

        # exemple mix: "U' B' L' F2 R U2 U2 B2 F L2 U2 L F' R2 "
    },
    {
        "num": 20,
        "shema":
        {
            "coins": [
                [(0, 0), (2, 2)],
                [(2, 2), (0, 0)]
            ],
            "edges": [
                [(2, 1), (0, 1)],
                [(0, 1), (2, 1)]
            ],
        },
        # R' U L' U2 R U' L R' U L' U2 R U' L U'
        "mouves": ["R'", "U", "L'", "U2", "R", "U'",  "L", "R'",  "U", "L'", "U2", "R", "U'", "L", "U'"]

        # exemple mix: "U' B' L' F2 R U2 L F' R2 B L' U2 B2 F L2 U2 L F' R2 "
    },
    {
        "num": 15,
        "shema":
        {
            "coins": [
                [(0, 0), (2, 0)],
                [(2, 0), (2, 2)],
                [(2, 2), (0, 0)],
            ],
            "edges": [
                [(1, 0), (1, 2)],
                [(2, 1), (1, 0)],
                [(1, 2), (2, 1)],
            ],
        },
        # R2 u R' U R' U' R u' R2 y' R' U R
        "mouves": ["R2", "u", "R'", "U", "R'", "U'", "R", "u'", "R2", "y'", "R'", "U", "R"]

        # exemple mix:  "U' B' L' F2 R U2 L F' R2 L' F2 R U2 L F' R2  B L' U2 B2 F L2 U2 L F' R2 "
    }
]
