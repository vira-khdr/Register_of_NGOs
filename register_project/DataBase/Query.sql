(Select name_full From ngos Where address_id IN(Select id from addresses where city = 'Kiev' OR 'Lviv')) 
Union 
(Select name_full From insurance_funds Where address_id IN(Select id from addresses where city = 'Kiev' OR 'Lviv')) 
Union 
(Select name_full From party Where address_id IN(Select id from addresses where city = 'Kiev' OR 'Lviv')) 