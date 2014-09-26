#author guojingyu
#date      Sep 25, 2014
from routes import Mapper

NUMERIC = R"\d+"
#DATE_FORMAT = {"year":R"\d\d\d\d","month":"\d\d","day":"\d\d"}  
DATE_FORMAT = {"year":R"\d{4}","month":"\d{2}","day":"\d{2}"}  

m = Mapper()
m.connect("/boards/games/{year}/list",requirements={"year":NUMERIC})
m.connect("/{year}/{month}/{day}",requirements=DATE_FORMAT)

games_of = "/board/games/2012/list"
category_by_date = "/2014/12/12"
result = m.match(category_by_date)
print result 
result = m.match(games_of)
print result 