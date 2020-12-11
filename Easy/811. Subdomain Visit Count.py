class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d, answer = {}, []

        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            currDomain = ""
            for i in range(len(domain) - 1, -1, -1):
                letter = domain[i]
                if i == 0:
                    currDomain = letter + currDomain
                    d[currDomain] = d.get(currDomain, 0) + count
                elif letter == ".":
                    d[currDomain] = d.get(currDomain, 0) + count
                currDomain = letter + currDomain

        for i, val in d.iteritems():
            answer.append(str(val) + " " + i)

        return answer






