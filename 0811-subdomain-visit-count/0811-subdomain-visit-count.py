import re
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        name_to_domain = {}
        for word in cpdomains:
            result_arr = re.split(r'[ .]', word)
            count = int(result_arr[0])
            
            for i in range(1, len(result_arr)):
                key = '.'.join(result_arr[i:])
                name_to_domain[key] = count + name_to_domain.get(key, 0)
        
        
        return [f"{count} {domain}" for domain, count in name_to_domain.items()]