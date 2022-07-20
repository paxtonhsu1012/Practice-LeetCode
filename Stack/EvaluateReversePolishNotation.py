### https://leetcode.com/problems/evaluate-reverse-polish-notation/
### Medium

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()

        for t in tokens:
            if t.isdigit():
                q.append(int(t))

            elif t[0] == '-' and t[1:].isdigit():
                q.append(-int(t[1:]))

            else:
                n2 = q.pop()
                n1 = q.pop()

                if t == '+':
                    tmp = n1 + n2
                elif t == '-':
                    tmp = n1 - n2
                elif t == '*':
                    tmp = n1 * n2
                elif t == '/':
                    tmp = int(n1 / n2)
                q.append(tmp)

        return q[0]
