# UCSB-COURSE-VIEWER
This is the unofficial UCSB course catalog mobile app. Please note this is neither endorsed nor approved by the University of California, Santa Barbara. 

##### Current Developments 
* iOS App
* Documentation
* Infrastructure Enhancements 
  * Changing the structure of the data in the NoSQL database
  * Creating a course data update script that will allow for ZERO downtime updates
  * Speeding up course data update script 

#### Documentation - Brief explanation of different files and functions within them. (In depth docs will come later)
## Backend
  * **Main Components**
    * **UCSB GOLD** - UCSB website where students view and sign up for courses. This is where we get the course data from.
    * **UCSB GOLD API/lib** - An api that was made to facilitate the scraping and retrieval of course data from GOLD. 
    * **MongoDB hosted on mLab** - DB that is currently being used to store course data. 
    * **Course Data REST API** - API used by clients to GET course data. In later iterations, it will support POST/PUT operations. 

  * **Files**
    * **/backend/courseApi.py** - Api endpoints that the clients will use.
    * **/backend/courseDB.py** - Helper functions that directly interact with the DB. These include the one's used in both the client rest api and the DB update script.
    * **/bakend/goldDataLayer.py** - DB update script, retrieves latest course data and udpates the DB.
    * **/backend/ucsbGoldApi/goldScraper.py** - UCSB GOLD API, Functions that facilitate web scraping to retrieve GOLD course info.
    * **/backend/ucsbGoldApi/settings.py** - Login details for GOLD as well as translation table for names of quarters & subejects. 
