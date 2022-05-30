![image](https://user-images.githubusercontent.com/55177259/170966771-bd04d472-4330-462d-843a-e139dae53241.png)


# Pharmaceutical Sales prediction across multiple stores
## Overview of Business need

 <p>We will explore the behaviour of customers in the various stores. Our goal is to check how some measures such as promos and opening of new stores affect purchasing       behavior.</p>
<h2> Features</h2>
<li>Id - an Id that represents a (Store, Date) duple within the test set</li>
<li>Store - a unique Id for each store
<li>Sales - the turnover for any given day (this is what you are predicting)
<li>Customers - the number of customers on a given day
<li>Open - an indicator for whether the store was open: 0 = closed, 1 = open
<li>StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
<li>SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
<li>StoreType - differentiates between 4 different store models: a, b, c, d
<li>Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
<li>CompetitionDistance - distance in meters to the nearest competitor store
<li>CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
<li>Promo - indicates whether a store is running a promo on that day
<li>Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
<li>Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
<li>PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store
