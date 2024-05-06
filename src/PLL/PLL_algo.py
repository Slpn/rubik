algos = [
    {
        "num": 0,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 0)],  # well placed
                [(1, 2), (1, 2)],  # well placed
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        #
        "mouves": []
    },
    {
        "num": 1,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (1, 2)],
                [(1, 0), (0, 1)],
                [(1, 2), (1, 0)],
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        # R U' R U R U R U' R' U' R2
        "mouves": ["R", "U'", "R", "U", "R", "U", "R", "U'", "R'", "U'", "R2"]

        # exemple mix: "U' B' L' F2 R U2 U2 B2 F L2 U2 L F' R2 "
    },
    {
        "num": 2,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (1, 0)],
                [(1, 0), (1, 2)],
                [(2, 1), (2, 1)],  # well placed
                [(1, 2), (0, 1)],
            ],
        },
        # R2 U R U R' U' R' U' R' U R'
        "mouves": ["R2", "U", "R", "U", "R'", "U'", "R'", "U'", "R'", "U", "R'"]
    },
    {
        "num": 3,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (2, 1)],
                [(1, 0), (1, 2)],
                [(2, 1), (0, 1)],
                [(1, 2), (1, 0)],
            ],
        },
        # M2 U M2 U2 M2 U M2
        "mouves": ["M2", "U", "M2", "U2", "M2", "U", "M2"]
    },
    {
        "num": 4,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (1, 2)],
                [(1, 0), (2, 1)],
                [(2, 1), (1, 0)],
                [(1, 2), (0, 1)],
            ],
        },
        # U R' U' R U' R U R U' R' U R U R2 U' R' U
        "mouves": ["U", "R'", "U'", "R", "U'", "R", "U", "R", "U'", "R'", "U", "R", "U", "R2", "U'", "R'", "U"]

        # exemple mix: "U' B' L' F2 R  U2 B2 R U2 U2 F L2 U2 L F' R2  B' L' F2 R  U2 B2"
    },
    {
        "num": 5,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 2)],
                [(2, 2), (0, 2)],
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 0)],  # well placed
                [(1, 2), (1, 2)],  # well placed
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        # x R' U R' D2 R U' R' D2 R2
        "mouves": ["x", "R'", "U", "R'", "D2", "R", "U'", "R'", "D2", "R2"]
    },
    {
        "num": 6,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 2)],
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (0, 0)],
                [(0, 2), (2, 2)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 0)],  # well placed
                [(1, 2), (1, 2)],  # well placed
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        # x' R U' R D2 R' U R D2 R2
        "mouves": ["x'", "R", "U'", "R", "D2", "R'", "U", "R", "D2", "R2"]

        # exemple mix:"U' B' L' F2 R  U2 B2 R U2 U2 F L2 U2 L F' R2 "
    },
    {
        "num": 7,
        "shema":
        {
            "coins": [
                [(0, 0), (2, 0)],
                [(2, 0), (0, 0)],
                [(2, 2), (0, 2)],
                [(0, 2), (2, 2)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 0)],  # well placed
                [(1, 2), (1, 2)],  # well placed
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        # x' (R U' R' D) (R U R' D') (R U R' D) (R U' R' D') x
        "mouves": ["x'", "R", "U'", "R'", "D", "R", "U", "R'", "D'", "R", "U", "R'", "D", "R", "U'", "R'", "D'", "x"]
    },
    {
        "num": 8,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (0, 2)],
                [(0, 2), (2, 2)],
            ],
            "edges": [
                [(0, 1), (1, 2)],
                [(1, 0), (1, 0)],  # well placed
                [(1, 2), (0, 1)],
                [(2, 1), (2, 1)],  # well placed
            ],
        },
        # R U R' F' R U R' U' R' F R2 U' R' U'
        "mouves": ["R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'"]
    },
    {
        "num": 9,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 2)],
                [(2, 2), (2, 0)],
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (2, 1)],
                [(2, 1), (1, 0)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # R' U L' U2 R U' R' U2 R L U'
        "mouves": ["R'", "U", "L'", "U2", "R", "U'", "R'", "U2", "R", "L", "U'"]
    },
    {
        "num": 10,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 2)],
                [(2, 2), (2, 0)],
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (1, 2)],
                [(1, 0), (1, 0)],  # well placed
                [(2, 1), (2, 1)],  # well placed
                [(1, 2), (0, 1)],
            ],
        },
        # R' U2 R U2 R' F R U R' U' R' F' R2 U'
        "mouves": ["R'", "U2", "R", "U2", "R'", "F", "R", "U", "R'", "U'", "R'", "F'", "R2", "U'"]
    },
    {
        "num": 11,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (0, 2)],
                [(0, 2), (2, 2)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (2, 1)],
                [(2, 1), (1, 0)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # y' L U2 L' U2 L F' L' U' L U L F L2' U
        "mouves": ["y'", "L", "U2", "L'", "U2", "L", "F'", "L'", "U'", "L", "U", "L", "F", "L2", "U"]
    },
    {
        "num": 12,
        "shema":
        {
            "coins": [
                [(0, 0), (2, 0)],
                [(2, 0), (2, 2)],
                [(2, 2), (0, 0)],
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(0, 1), (2, 1)],
                [(1, 0), (0, 1)],
                [(2, 1), (1, 0)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # R U R' y' R2 u' R U' R' U R' u R2
        "mouves": ["R", "U", "R'", "y'", "R2", "u'", "R", "U'", "R'", "U", "R'", "u", "R2"]
    },
    {
        "num": 13,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 2)],
                [(2, 0), (0, 0)],
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (1, 0)],
                [(1, 0), (2, 1)],
                [(2, 1), (0, 1)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # R' U' R y R2 u R' U R U' R u'R2
        "mouves": ["R'", "U'", "R", "y", "R2", "u", "R'", "U", "R", "U'", "R", "u'", "R2"]
    },
    {
        "num": 14,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 2)],
                [(2, 0), (0, 0)],
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (1, 0)],
                [(1, 0), (1, 2)],
                [(2, 1), (2, 1)],  # well placed
                [(1, 2), (0, 1)],
            ],
        },
        # R2 u' R U' R U R' u R2 y R U' R'
        "mouves": ["R2", "u'", "R", "U'", "R", "U", "R'", "u", "R2", "y", "R", "U'", "R'"]
    },
    {
        "num": 15,
        "shema":
        {

            "coins": [
                [(0, 0), (2, 0)],
                [(2, 0), (2, 2)],
                [(2, 2), (0, 0)],
                [(0, 2), (0, 2)],  # well placed
            ],
            "edges": [
                [(1, 0), (1, 2)],
                [(2, 1), (1, 0)],
                [(1, 2), (2, 1)],
                [(0, 1), (0, 1)],  # well placed
            ],
        },
        # R2 u R' U R' U' R u' R2 y' R' U R
        "mouves": ["R2", "u", "R'", "U", "R'", "U'", "R", "u'", "R2", "y'", "R'", "U", "R"]

        # exemple mix:  "U' B' L' F2 R U2 L F' R2 L' F2 R U2 L F' R2  B L' U2 B2 F L2 U2 L F' R2 "
    },
    {
        "num": 16,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (0, 2)],
                [(0, 2), (2, 2)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 2)],
                [(2, 1), (2, 1)],  # well placed
                [(1, 2), (1, 0)],
            ],
        },
        # R U R' U' R' F R2 U' R' U' R U R' F'
        "mouves": ["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'"]

        # exemple mix: "U' B' L'  R  U2 R U2 U2 F"
    },
    {
        "num": 17,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (0, 2)],
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (2, 1)],
                [(2, 1), (1, 0)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # F R U' R' U' R U R' F' R U R' U' R' F R F'
        "mouves": ["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'"]
    },
    {
        "num": 18,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (0, 2)],
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 0)],  # well placed
                [(2, 1), (1, 2)],
                [(1, 2), (2, 1)],
            ],
        },
        # R' U R' d' R' F' R2 U' R' U R' F  R F
        "mouves": ["R'", "U", "R'", "d'", "R'", "F'", "R2", "U'", "R'", "U", "R'", "F", "R", "F"]
    },
    {
        "num": 19,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 2)],
                [(2, 0), (2, 0)],  # well placed
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (0, 0)],
            ],
            "edges": [
                [(0, 1), (0, 1)],  # well placed
                [(1, 0), (1, 2)],
                [(2, 1), (2, 1)],  # well placed
                [(1, 2), (1, 0)],
            ],
        },
        # R' U2 R' d' R' F' R2 U' R' U R' F R U' F
        "mouves": ["R'", "U2", "R'", "d'", "R'", "F'", "R2", "U'", "R'", "U", "R'", "F", "R", "U'", "F"]

        # exemple mix: "U' B' L'  R  U2 R U2 U2 F"
    },
    {
        "num": 20,
        "shema":
        {
            "coins": [
                [(0, 0), (2, 2)],
                [(2, 2), (0, 0)],
                [(0, 2), (0, 2)],  # well placed
                [(2, 0), (2, 0)],  # well placed
            ],
            "edges": [
                [(0, 1), (2, 1)],
                [(1, 0), (1, 0)],  # well placed
                [(2, 1), (0, 1)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # R' U L' U2 R U' L R' U L' U2 R U' L U'
        "mouves": ["R'", "U", "L'", "U2", "R", "U'",  "L", "R'",  "U", "L'", "U2", "R", "U'", "L", "U'"]

        # exemple mix: "U' B' L' F2 R U2 L F' R2 B L' U2 B2 F L2 U2 L F' R2 "
    },
    {
        "num": 21,
        "shema":
        {
            "coins": [
                [(0, 0), (0, 0)],  # well placed
                [(2, 0), (0, 2)],
                [(2, 2), (2, 2)],  # well placed
                [(0, 2), (2, 0)],
            ],
            "edges": [
                [(0, 1), (2, 1)],
                [(1, 0), (1, 0)],  # well placed
                [(2, 1), (0, 1)],
                [(1, 2), (1, 2)],  # well placed
            ],
        },
        # L U' R U2 L' U R' L U' R U2 L' U R' U
        "mouves": ["L", "U'", "R", "U2", "L'", "U", "R'", "L", "U'", "R", "U2", "L'", "U", "R'", "U"]
    },

]
