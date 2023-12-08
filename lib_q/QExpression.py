class QExpression:

    def test(self, expected_expr: str):
        res = str(self)
        print(res)
        assert res == expected_expr

    def print(self):
        print(self)
