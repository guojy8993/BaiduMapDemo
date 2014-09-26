#author guojingyu
#date      Sep 26, 2014
from routes import Mapper

m = Mapper()
REQUEST_CONDITION = {"method":["GET","HEAD"]}

## Match only if the HTTP method is "GET" or "HEAD".
m.connect("/user/list",controller="user",action="list",conditions=REQUEST_CONDITION)

# A sub-domain should be present.
m.connect("/",controller="user",action="home",conditions=dict(sub_domain=True))

#Sub-domain should be either "fred" or "george".
m.connect("/",controller="user",action="home",conditions=dict(sub_domain=["fred","george"]))

# Put the referrer into the resulting match dictionary.
# This function always returns true, so it never prevents the match
# from succeeding.
def referals(environ,result):
    result["referer"] = environ.get("HTTP_REFERER")
    return True

m.connect("/{param1}/{param2}/{sid}",conditions=dict(function=referals))
print m.match("/")
