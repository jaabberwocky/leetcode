#URL: https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniqueEmails = set()
        for email in emails:
            if email in uniqueEmails:
                continue
            
            splitNameAndDomain = email.split("@")
            localName = splitNameAndDomain[0]
            
            if "." in localName:
                # apply "." rule
                localName = localName.replace(".", "")
            
            if "+" in localName:
                # apply "+" rule
                indexPlus = localName.find("+")
                localName = localName[:indexPlus]
            
            # insert into set
            combined = localName + splitNameAndDomain[1]
            uniqueEmails.add(combined)
        
        return len(uniqueEmails)