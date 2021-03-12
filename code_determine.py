import re

class Solution():
    def __init__(self, password: str):
        self.password = password
        
        self.lens = len(password)
        
        self.password_list_entry = [i for i in password]
        
        self.low = 0
        
        self.upp = 0
        self.cha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.cha =  [i for i in self.cha]
        self.cha = "{3}|".join(self.cha)
        self.pattern = self.cha
        
        
    def strongPasswordChecker(self):
        self.cha_group = re.findall(self.pattern, self.password, flags=0)
        
        if self.lens >= 6 and self.lens<19 and len(self.cha_group)>0:
            return len(self.cha_group)
        
        
            
        
        if self.lens >= 6 and self.lens <= 19 :
            for i in self.password_list_entry:
                if i.islower(): 
                    self.low = self.low +1

                elif i.isupper(): 
                    self.upp = self.upp +1

                else:
                    continue
            if self.low >0 and self.upp>0:
                return 0

            elif self.low==0:
                return "at least need one lowercase "

            elif self.upp==0:
                return "at least need one uppercase "
            
        elif self.lens < 6 :
            return 6-self.lens
        elif self.lens > 19 :
            return self.lens-19

sol = Solution(password='baaa122234')
print(sol.strongPasswordChecker())