
# time flies like an arrow
# fruit flies like a banana

import arrow

d = arrow.utcnow()
print("base", d)
home = d.to('US/Eastern')
print("home", home)

earlier = home.shift(hours=-3)
print("earlier", earlier)
print("earlier human", earlier.humanize())
