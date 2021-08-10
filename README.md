# **US Bikeshare Data Analysis**

### Description:
A bicycle-sharing system (bikeshare system) scheme, is a shared transport service in which bicycles are made available for shared use to individuals on a short term basis for a price or free. Many bikeshare systems allow people to borrow a bike from one station and return it at another station belonging to the same system. Most large-scale urban bike sharing programs have numerous bike check-out stations, and operate much like public transit systems, catering to tourists and visitors as well as local residents. Their central concept is to provide free or affordable access to bicycles for short-distance trips in an urban area as an alternative to private vehicles.

![Bikeshare's Station Image](https://static01.nyt.com/images/2014/03/26/nyregion/26CITIBIKEweb2/26CITIBIKEweb2-articleLarge.jpg?quality=75&auto=webp&disable=upscale)

In this project, analysis has been performed on bikeshare data of three cities chicago, new york city, and washington in Python. Python program has been written which computes descriptive statistics that answers some interesting questions like what time of the day when most bikes are rented out? Which station is the most common from where customers/users rents out bikes etc. The output of the code is interactive i.e user will be asked to enter the city for which they would like to see statistics as well as they'll have the option to filter the data based on months and day of week. Lastly user will be asked if they would like to see raw data for the choosen city.

### Questions answered:
* Popular times of travel:
  * most common month
  * most common day of week
  * most common hour of day
* Popular stations and trip:
  * most common start station
  * most common end station
  * most common trip from start to end (i.e., most frequent combination of start station and end station)
* Trip duration:
  * total travel time
  * average travel time
* User info:
  * counts of each user type
  * counts of each gender (only available for NYC and Chicago)
  * earliest, most recent, most common year of birth (only available for NYC and Chicago)

### The datasets:

 Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core **six (6)** columns:
 * Start Time (e.g., 2017-01-01 00:07:57)
 * End Time (e.g., 2017-01-01 00:20:53)
 * Trip Duration (in seconds - e.g., 776)
 * Start Station (e.g., Broadway & Barry Ave)
 * End Station (e.g., Sedgwick St & North Ave)
 * User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

### Files used:
* bikeshare.py
* [Datasets](https://drive.google.com/file/d/1km4EggJaSvHos_7KKFuHoJxbh-StyM4G/view)

### Softwares needed:
* Python (3.8.8)
* Pandas (1.2.4)
* Text Editor (example: Atom or VS Code)
* Terminal
