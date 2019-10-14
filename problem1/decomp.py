class DecomposedUrl:
    # instance attributes of a decomposed URL
    def __init__(self, protocol, domain, path):
        self.protocol = protocol
        self.domain = domain
        self.path = path

# Function Purpose: input url and split it by it's parts (protocol, domain, and path)
# Function Inputs: 
#                 url: String
def decomposeURL(url):
    decompObj = DecomposedUrl("","","")
    if ':' in url:
        # there is a protocol in the url
        splitUrl = url.split(":",1)
        decompObj.protocol = splitUrl[0]

    if '//' in url:
        # there is a domain in the url
        splitProtocolAndDomain = url.split("//")
        if "/" in splitProtocolAndDomain[1]:
            # there is a path after the domain
            splitDomainAndPath = splitProtocolAndDomain[1].split("/")
            decompObj.domain = splitDomainAndPath[0]
            decompObj.path = splitDomainAndPath[1]
        else:
            # there is no path after the domain
            decompObj.domain = splitProtocolAndDomain[1]
    
    elif '/' in url:
        # there is no protocol or domain in url, just the path
        splitSlashAndPath = url.split("/")
        decompObj.path = splitSlashAndPath[1]

    # return instance attributes in string form
    return "{}, {}, {}".format(decompObj.protocol, decompObj.domain, decompObj.path)