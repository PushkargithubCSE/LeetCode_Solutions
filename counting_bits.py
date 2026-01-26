class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = list((range(n+1)))
        bin_arr = []

        for i in arr:
            binary = bin(i)
            bin_arr.append(binary.count('1'))
        
        return bin_arr   

        
