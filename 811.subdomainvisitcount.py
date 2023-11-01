from dataclasses import dataclass


@dataclass()
class DomainPair:
    count: int
    domain: str

class Domain:
    def __init__(self, val=DomainPair(0, "ULTIMATE")):
        self.val = val
        self.children = []
    
    def get_child_with_name(self, name):
        for child in self.children:
            if child.val.domain == name:
                return child
        return None


def subdomainVisits(cpdomains: list[str]) -> list[str]:
    domains = Domain()
    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)
        curr_domain = domains
        for subdom in reversed(domain.split('.')):
            subdom_obj = curr_domain.get_child_with_name(subdom)
            if not subdom_obj:
                subdom_obj = Domain(DomainPair(0, subdom))
                curr_domain.children.append(subdom_obj)
            curr_domain = subdom_obj
        curr_domain.val.count += count

    def add_up(dom):
        for child in dom.children:
            dom.val.count += add_up(child)
        return dom.val.count
    
    add_up(domains)

    results = []
    def build_results(dom, domain_so_far):
        if dom.val.domain != "ULTIMATE":
            domain_so_far.append(dom.val.domain)
            results.append(f"{dom.val.count} {'.'.join(reversed(domain_so_far))}")
        for child in dom.children:
            build_results(child, list(domain_so_far))
    build_results(domains, [])

    return results

    

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))