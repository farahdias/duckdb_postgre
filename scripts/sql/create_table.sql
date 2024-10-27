CREATE TABLE country (
  	Country_Code  INT PRIMARY KEY
	,Country VARCHAR
);


CREATE TABLE restaurants (
	Restaurant_ID	BIGINT PRIMARY KEY
	,Restaurant_Name	VARCHAR
	,Country_Code	BIGINT
	,City	VARCHAR
	,Address	VARCHAR
	,Locality	VARCHAR
	,Locality_Verbose	VARCHAR
	,Longitude	FLOAT
	,Latitude	FLOAT
	,Cuisines	VARCHAR
	,Average_Cost_for_two	BIGINT
	,Currency	VARCHAR
	,Has_Table_booking	BOOLEAN
	,Has_Online_delivery	BOOLEAN
	,Is_delivering_now	BOOLEAN
	,Switch_to_order_menu	BOOLEAN
	,Price_range	BIGINT
	,Aggregate_rating	FLOAT
	,Rating_color	VARCHAR
	,Rating_text	VARCHAR
	,Votes	BIGINT
	,FOREIGN KEY (Country_Code) REFERENCES country(Country_Code)
);

CREATE TABLE resturants_details (
	has_online_delivery	BIGINT
	,photos_url	VARCHAR
	,url	VARCHAR
	,price_range	BIGINT
	,apikey	UUID
	,rating_text	VARCHAR
	,rating_color	VARCHAR
	,votes	JSON
	,aggregate_rating	JSON
	,res_id	BIGINT
	,name	VARCHAR
	,has_table_booking	BIGINT
	,is_delivering_now	BIGINT
	,deeplink	VARCHAR
	,menu_url	VARCHAR
	,average_cost_for_two	BIGINT
	,switch_to_order_menu	BIGINT
	,cuisines	VARCHAR
	,latitude	VARCHAR
	,address	VARCHAR
	,city	VARCHAR
	,country_id	BIGINT
	,locality_verbose	VARCHAR
	,city_id	BIGINT
	,zipcode	VARCHAR
	,longitude	VARCHAR
	,locality	VARCHAR
	,featured_image	VARCHAR
	,currency	VARCHAR
	,id	VARCHAR
	,thumb	VARCHAR
	,events_url	VARCHAR
	,book_url	VARCHAR
	,order_deeplink	VARCHAR
	,order_url	VARCHAR
	,FOREIGN KEY (res_id) REFERENCES restaurants(Restaurant_ID)

);
