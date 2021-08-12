SELECT FirstName,LastName,City,State
FROM Person AS a
left join
Address AS b
ON a.PersonId=b.PersonId;