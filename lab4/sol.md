# Solutions ot my part

## Exercise 9
1. Determine the k-anonymity level
    * k-anonymity of level two since the quasi identifiers age and race each appera in at least 2 rows of the table. We can see that Afro-American and age 34 appear in 3 places and Hispanic and age 18 again in 3 rows, but Caucasian and age 21 only in 2 rows. Thus the k-anonymity level is 2.
2. L-diversity and possible problems
    * We do not see problem with the data set.One out of the 2 quasi-identifiers is generalized , while age isn't we believe that it will be extremely difficult to extract information about a specific individual. The are millions of Caucasian people agen 21 for example. L-divestiry will not help also, since if we do not generalize in some manner the age, the sensitive column will just be 1 for each group. Since each Afro-American aged 34 has Flu, each Cauccasian aged 21 has Viral, and each hispanic aged 18 has Cancer. Thus there really exists no diversty in the data set. We believe that there is no problem with the current data-set and tht although the age identifier might give slightly more information the anonymity of the people in the data set is preserved.

## Exercise 7
1. For the login to happen the user only needs to enter his password. After that the server will compute the key for that password and send it back. Then our computer can use this key to compute a TGT that will allow us to access the network. Assuming that the KDC server is not down authentication is ensured since we only need to obtain a TGT that will have access to the resources of the server for the lifetime of TGT. (Not sure have to ask somebody about it)
2. Timestamps are used in order to prevent relpay attacks. Since the protocol is stateless this is a good way to ensure that an attacker could not forge a request and allow fro replay attacks.A note however is that it is very hard to syncronize clocks thus there should exists some sort of a clock skew to account for inaccuracies.

## Exercise 5
1. C1,C3 -> Finance
    * C1 -> D1,D2,D3
    * C3 -> D5,D7
2. C2,C4,C6 -> Pharmacy
    * C2 -> D4,D6
    * C4 -> D9
    * C6 -> D10,D11
3. C5 -> Media
    * D8

### How to enforce chinese wall policy for two employess E1 and E2
Some obvious things:
1. C1 and C3 are competitors
2. C2,C4,C6 are competitors
3. C5 has no competitors
We can assume their is no conflict of interest between finance and media or finance and pharmy and etc. Conflicts arise in the fields themself. Lets assume E1 acesses C1 and E2 accesses C3 then the Chinese Wall Policy would say that E1 cannot access files about C3 and that E2 cannot access files for C1 since there is a conflict of interest. Howevery E1 could browse the files of the Pharamcy and Media companies for example. But has locked access to documents D5 and D7. If E1 accesses either of the pharmacy companies he should not be able to access any of the other. Basically if the employees operate within the same field (i.e. same type of company:Finance,Pharmacy or Media) they should not be able to see the documents for the oposing employee since that would break the Chinese Wall Policy. If they operate within different field lets say E1 in media and E2 in finance then since finance and media are not competitors and have no conflict of interest E1 and E2 can browse the documents from the cross domain.


## Exercice 1 from the prf
1. 8 from the book
    * 11100111 -> Makes a collision
    * 10001111 -> Makes a collision
In order to create a collision we just need to xor the divisor in our case 10011 with the original message 10101011 startinmg from any bit after the first one and the resulting modified message will produce the same checksum

2. 9 from the textbook
    * one possible value is 11100111 there might be more
