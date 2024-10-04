class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
      
        skill.sort()

        res = 0
        
        left, right = 0, len(skill)-1
        p = skill[left] + skill[right]
        
        while left < right:
            if skill[left] + skill[right] != p:
                return -1
            res += skill[left] * skill[right]
            left += 1
            right -= 1

        return res