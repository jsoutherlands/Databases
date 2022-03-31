# Bases-de-Datos
Oracle Covid Database and Twitter SQL PHP were two assignments for the 2021-1 Databases course of Computer Science Engineering Career at Universidad Técnica Federico Santa María, Chile.

## Oracle Covid Database

A global pandemic has been declared, known as Covid-21. This pandemic affects to the whole world population, but mostly to Chile's population.

Given two .csv files: confirmed cases by city and confirmed cases by region, a Database is built with the following characteristics:

- Created on Oracle SQL.
- A menu needs to be created by using Python 3, and the commands are:
	- Create city.
	- Create region.
	- See total cases of a certain city.
	- See total cases of a certain region.
	- See total cases of all cities.
	- See total cases of all regions.
	- Add new cases to a city by adding n cases to existing confirmed cases.
	- Delete new cases to a city by substracting n cases to existing confirmed cases.
	- Combine cities.
	- Combine regions.
	- Top 5 cities with more cases percentage according to its population.
	- Top 5 regions with more cases percentage according to its population.

Due to the existing crisis on this Country, if a region has more than 15% of its population with confirmed cases, a notification will be shown and the region will be deleted of the country.

## Twitter SQL PHP

USMwer is a new social network, where users ("usmers") can write messages ("usmitos") with a maximum length of 279 characters. The usmers can follow each other, "reusmear", like and reply usmitos.

The "close friends" characteristic allows to usmers that follow each other to see private usmitos. Also, the lists feature allows usmers to create a personalized feed, watching only the accounts they want.

A usmer can deactivate or delete his account. If an account is deactivated, the usmer dissapears of USMwer with his lists and usmitos, but all this is not deleted from the Database, because the usmer can come back anytime, reactivate his account and using it normally with all previous characteristics.

Note: this implementation has only the possibility to: publicate usmitos, reusmear, like, create and delete accounts, see a profile and have information about the usmer. Reply function, close friends, lists and deactivation have not been implemented but could be in the future.

***

© José P. Southerland Silva - 2021