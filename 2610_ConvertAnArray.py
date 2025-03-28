class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        
        Array2D = []
        #el numero mas repetido
        numRep = max(set(nums), key=nums.count)
        #las veces que se repitio#
        nReps = nums.count(numRep) 
        
        #Crear n listas a partir del numero mas repetido
        for i in range(0,nReps):
            Array2D.append([])        

        for n in nums:
            i = 0
            while i < nReps:
                if n in Array2D[i]:
                    i+=1
                else:
                    Array2D[i].append(n)
                    i = nReps

        return Array2D
        


