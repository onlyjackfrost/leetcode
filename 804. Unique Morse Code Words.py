class Solution:
    def uniqueMorseRepresentations(self, words):
       
        import string
        Morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        diction = {}
        i = 0
        for cha in string.ascii_lowercase[:26]:
            diction[cha] = Morse[i]
            i += 1
        print(diction)
        
        concatenation = []
        for str in words:
            transform = ""
            for cha in str:
                transform = transform + diction[cha]
            print(transform)
            if transform not in concatenation  :   
                concatenation.append(transform)
        num = len(concatenation)
        return num