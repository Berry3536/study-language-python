# import travel_package.thailand
# import travel_package.vietnam
# trip_to = travel_package.thailand.ThailandPackage()
# trip_to.detail()

# trip_to = travel_package.vietnam.VietnamPackage()
# trip_to.detail()

from travel_package import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))