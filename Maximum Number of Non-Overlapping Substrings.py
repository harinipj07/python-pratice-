class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def revg(g):
            revg = [set() for _ in range(26)]
            for i in range(len(g)):
                for j in g[i]:
                    revg[j].add(i)
            return revg
        #store min and max pos     
        loc = {}
        #sstore all chars in the string
        chrs = set()
        for i in range(len(s)):
            if not (s[i] in loc):
                loc[s[i]] = [i,i]
            else:
                loc[s[i]][1] = i
            chrs.add(s[i])
            
        
        #construct the graph 
        g = [set() for _ in range(26)]
        for i in range(26):
            for j in range(26):
                a = chr(i+ord("a"))
                b = chr(j+ord("a"))
                if a in chrs and b in chrs and a != b:
                    st = loc[a][0]
                    e = loc[a][1]
                    while st <= e:
                        if s[st] == b or s[e] == b:
                            g[i].add(j)
                            break
                        st += 1
                        e -= 1
        ans = []
        seen = set()
        #topo sort for kosaraju
        def f(node):
            seen.add(node)
            for i in range(26):
                if i in g[node] and not (i in seen):
                    f(i)
            ans.append(node)
        #rev topo sort for kosaraju
        def f2(node,batch,g):
            if batches[node] < 0:
                batches[node] = batch
                for i in range(26):
                    c = chr(i+ord("a"))
                    n = chr(node+ord("a"))
                    if c in chrs and i in g[node]:
                        f2(i,batch,g)
            else:
                if batches[node] != batch:
                    degree[batches[node]] += 1
        #getting the topo sort
        for i in range(26):
            c = chr(i+ord("a"))
            if c in chrs and not (i in seen):
                f(i)
        batch = 0
        degree = [0 for _ in range(26)]
        batches = [-1 for _ in range(26)]
        #getting the rev graph for kosaraju
        rev = revg(g)
        while ans:
            curr = ans.pop()
            if batches[curr] < 0:
                f2(curr,batch,rev)
                batch += 1  
        ans = []
        #going for only scc's with outdegree 0
        for i in range(batch-1,-1,-1):
            if degree[i] == 0:
                mini = float("inf")
                maxe = -1
                for j in range(26):
                    c = chr(j+ord("a"))
                    if batches[j] == i:   
                        mini = min(loc[c][0],mini)
                        maxe = max(loc[c][1] ,maxe)
                ans.append(s[mini:maxe+1])
        return ans
        
