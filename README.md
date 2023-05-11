# DataFarm

## Timeline
1. Board is loaded with neccesary components
    - LoRa WAN Module Loaded
    - DHT11 Sensor Loaded
2. Board is loaded with the correct MI (Manufactoring Information)
    - Correct Node_id
    - Correct SW_ver
    - Correct HW_ver
    ```
    scripts/sw_load/env_load.sh
    ```

    The following bash script loads env variables

3. Board is loaded with the correct SW
    - Dependencies have been installed
    - Program has been loaded into cpu
    ```
    src/emb/get_rasp_temp.py
    ```

    The following file sends the captured data to a MySQL database. The captured data includes environment variables such as temperature, humidity, PH_LEVEL, air quality and other variables.

    The captured data also includes system data such as the NODEID, SW_VER,HW_VER and IPV4.



    ## Timeline of the Data Science Process

    1. Data is retrieved from a MySQL database table known as "dirty_data" and is converted as a pandas Data Frame.
    2. Data is then cleaned
        - This includes the following:
            - Removing NULL values
            - Removing Duplicates 
            - Removing invalid columns
    3. The data frame is saved into a another MySQL table named "clean_data".
    ## Timeline of the User Interface
    1. Once the data has been retrieved and cleaned. It is shown to the user through a web page. While displaying a series of graphs to explore the data. 
    2. The display of data is also dependent on who is logged in. 

    For example:
        
        If the user "johnsmith1001" loggs into the website, then only records with "johnsmith1001" as its user_id will display.


    Note: if any ENV variables are empty then the software will not run. And if it some how does run. The JUHI data server will remove any rows with a NULL value. See later.


## How does the Database work??

The database is currently split into three tables. 

1. clean_data:
    - Contains all data that has been cleaned, it is ready for the user to see.
2. dirty_data:
    - Contains all data that has not been cleaned, it has come from the units of hardware
3. users:
    - Contains all data regarding accounts that have been generated using the web page.

