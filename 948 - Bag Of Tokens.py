class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        score=0
        maxscore=0
        while(i<=j):
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1
                i+=1
            else:
                if score>=1:
                    score-=1
                    power+=tokens[j]
                    j-=1
                else:
                    break
            maxscore=max(score,maxscore)
        return maxscore

        
