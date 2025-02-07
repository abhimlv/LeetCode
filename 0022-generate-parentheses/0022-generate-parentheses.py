class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recursive(s, op_cnt, cl_cnt):
            if len(s) == 2*n:
                result.append(s)
                return
            
            if op_cnt < n:
                recursive(s+ "(", op_cnt +1, cl_cnt)
            
            if cl_cnt < op_cnt:
                recursive(s+ ")", op_cnt , cl_cnt+1)

        result = []
        recursive("", 0,0)
        return result
