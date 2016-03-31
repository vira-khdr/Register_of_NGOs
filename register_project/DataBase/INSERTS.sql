insert into addresses(region, area, city, address, post_index) values ('Kyivska', 'Kyiv', 'Kyiv', 'vyl. Dilova, 3', '03056');
insert into addresses(region, area, city, address, post_index) values ('Chernigivska', 'Chernigiv', 'Chernigiv', 'pr. Myru, 175', '07083');
insert into addresses(region, area, city, address, post_index) values ('Kharkivska', 'Kharkiv', 'Kharkiv', 'vyl. Heroiv Pratsi, 13', '01083');
insert into addresses(region, area, city, address, post_index) values ('Zakarpatska', 'Volovetsky', 'Volovets', 'vyl. Karpatska, 3', '04081');
insert into addresses(region, area, city, address, post_index) values ('Kyivska', 'Bila Tserkva', 'Bila Tserkva', 'vyl. Ivana Mazepy, 54', '03044');
insert into addresses(region, area, city, address, post_index) values ('Kyivska', 'Kyiv', 'Boyarka', 'vyl. Shevchenka, 124', '03469');
insert into addresses(region, area, city, address, post_index) values ('Lvivska', 'Lviv', 'Lviv', 'vyl. Lublinska, 4', '09067');
insert into addresses(region, area, city, address, post_index) values ('Ternopilska', 'Ternopil', 'Ternopil', 'vyl. Vesela, 37', '07043');
insert into addresses(region, area, city, address, post_index) values ('Ternopilska', 'Ternopil', 'Ternopil', 'pr. Zluky, 4a', '07056');
insert into addresses(region, area, city, address, post_index) values ('Lvivska', 'Vynnyky', 'Vynnyky', 'vyl. Ivana Franka, 22', '09264');


insert into documents(doc_name, doc_number, doc_date, doc_issued_by) values('Passport', 34567534, '1990-12-13', 'GUDMS Ulraine');
insert into documents(doc_name, doc_number, doc_date, doc_issued_by) values('Passport', 39154287, '1985-04-03', 'GUDMS Ulraine');
insert into documents(doc_name, doc_number, doc_date, doc_issued_by) values('Passport', 15724628, '1997-02-02', 'GUDMS Ulraine');
insert into documents(doc_name, doc_number, doc_date, doc_issued_by) values('Passport', 13462579, '1971-06-23', 'GUDMS Ulraine');
insert into documents(doc_name, doc_number, doc_date, doc_issued_by) values('Passport', 51359762, '1980-10-31', 'GUDMS Ulraine');


insert into certificates(cert_num, cert_date) values(4789125496, '2015-09-12');
insert into certificates(cert_num, cert_date) values(9654785213, '2014-04-16');
insert into certificates(cert_num, cert_date) values(3154892182, '2011-07-18');
insert into certificates(cert_num, cert_date) values(9786518582, '2013-02-13');
insert into certificates(cert_num, cert_date) values(1346843582, '2013-07-19');
insert into certificates(cert_num, cert_date) values(1566723546, '2012-08-22');
insert into certificates(cert_num, cert_date) values(9745684135, '2011-01-25');
insert into certificates(cert_num, cert_date) values(3215464813, '2015-03-02');
insert into certificates(cert_num, cert_date) values(3189458625, '2006-10-08');
insert into certificates(cert_num, cert_date) values(3164978564, '2009-12-13');

insert into arbitrages(id, oper_type, register_number, name_full, address_id, cert_id, doc_id, founder_id, registrator_name, date_start) 
	values(1, 'registration', 4785123631641254, 'Syd Kyiv', 1, 1, 5, '...', '...', '2008-09-15');
insert into arbitrages(id, oper_type, register_number, name_full, address_id, cert_id, doc_id, founder_id, registrator_name, date_start) 
	values(2, 'registration', 1452697584631597, 'Syd Kharkiv', 3, 2, 4, '...', '...', '2013-09-30');
insert into arbitrages(id, oper_type, register_number, name_full, address_id, cert_id, doc_id, founder_id, registrator_name, date_start) 
	values(3, 'registration', 3154264895482854, 'Syd Ternopil', 9, 3, 4, '...', '...', '2014-04-01');