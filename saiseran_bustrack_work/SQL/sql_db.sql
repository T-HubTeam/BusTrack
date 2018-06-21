/* Database structure and relations */
--  a. MySQL database
 	A structured database is required for driver and bus data maintainance and to form relation with among them.
-- b. MongoDB
 	A noSQL database is required for writing the data received by the device listener.


creating foriegn key relationship
/* CREATE TABLE accounts(
    account_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT( 4 ) NOT NULL ,
    account_type ENUM( 'savings', 'credit' ) NOT NULL,
    balance FLOAT( 9 ) NOT NULL,
    PRIMARY KEY ( account_id ),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
) ENGINE=INNODB;
*/
========================================================================================================
DATABASE NAME "bus_track"
========================================================================================================
1. table_1                          [Driver_details]
    a. col_1 [id]					[int]
    b. col_2 [name]					[varchar]
    c. col_3 [mobile No.]		   	[bigint]
    d. col_4 [emp_id]				[varchar]
	e. col_5 [area/destination]		[varchar]
	f. col_6 [address]		   		[varchar]

	create table table_new(emp_id varchar( 8 ) not null primary key , name varchar( 40 ) not null unique key, p_num bigint( 11 ) not null unique key,l_num varchar(15) not null unique key, area varchar( 30 ) not null unique key, address varchar(200) not null)ENGINE = INNODB;

	insert into table_new(emp_id,name,p_num,l_num,area,address,) values("emp521","Raj Kiran",9933251485,"AP0420184518659","Samalkota","Samalkota");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp522","Surya Rao",9949586214,"AP0420074752168","Peddapuram","Peddapuram");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp523","Lakshmi Narayana",9100548623,"AP0220145236487","Kakinada","Kakinada");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp524","Appa Rao",8324568974,"AP0120154723658","Sitanagaram","Sitanagaram");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp525","Nagababu",7613481664,"AP0120134582892","Ravulapalem","Ravulapalem");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp526","Raju",9933278485,"AP0420184514559","Samalkota","Samalkota");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp527","Surya Krishna",9949586354,"AP0420074751268","Peddapuram","Peddapuram");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp528","Narayana",9100548486,"AP0220145215487","Kakinada","Kakinada");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp529","Appala Swami",8324458264,"AP0120154774858","Goppallai","Goppallai");
	insert into table_new(emp_id,name,p_num,l_num,area,address) values("emp530","Samram Nagaraju",7613412457,"AP0120134748596","Ravulapalem","Ravulapalem");


2. table_2 								[Bus Data]
	a. id [id]						[int]
	b. bus_num [Bus No.]					[varchar]
	c. bus_reg [Bus Registration No.]		[varchar]
	d. area [Driver_details(name)]		[varchar]
	#e. bus_5 [destination/area]			[varchar]

	create table table_2(id int(3) not null auto_increment primary key, bus_num varchar(4) not null unique, bus_reg varchar(10) not null, area varchar(30) not null)ENGINE=INNODB;

	insert into table_2(bus_num,bus_reg,area) values("431","AP05CC1547","Samalkota");
	insert into table_2(bus_num,bus_reg,area) values("471","AP05CC1647","Goppallai");
	insert into table_2(bus_num,bus_reg,area) values("411","AP05CC1247","Samalkota");
	insert into table_2(bus_num,bus_reg,area) values("481","AP05CC1747","Ravulapalem");
;


3. Table_3 [Relation between Driver_details and Bus Data]
