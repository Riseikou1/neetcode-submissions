class UnionFind :
    def __init__(self, n) :
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x) :
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) : 
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y : return False

        if self.rank[root_x] > self.rank[root_y] :
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        else :
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailsToAcc = {}

        for idx, emails in enumerate(accounts) :
            for email in emails[1:] :
                if email in emailsToAcc :
                    uf.union(idx, emailsToAcc[email])
                else :
                    emailsToAcc[email] = idx

        res = []
        idxToEmails = defaultdict(list)
        for email, idx in emailsToAcc.items() :
            parent = uf.find(idx)
            idxToEmails[parent].append(email)

        for idx, emails in idxToEmails.items() :
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res

        