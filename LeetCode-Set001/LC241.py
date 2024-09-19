class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def operation(x, y, operator):
            if operator == "-":
                return x - y
            elif operator == "+":
                return x + y
            else:
                return x * y

        if expression.isdigit():
            return [int(expression)]

        res = []
        
        for i, char in enumerate(expression):
            if char in "-+*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])

                for n in left:
                    for m in right:
                        res.append(operation(n, m, char))

         

        return res