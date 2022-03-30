class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        newPeople = sorted(people, key=lambda x: (-x[0], x[1]))
        for i in range(len(newPeople)):
            h, k = newPeople[i]
            if k != i:
                newPeople.pop(i)
                newPeople.insert(k, [h, k])
                
        return newPeople
        
        