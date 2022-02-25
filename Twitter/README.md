# Twitter

Every folder contains daily files with tweet ids of tweets which contain the word 'ukraine', as retrieved by the search endpoint of the Academic Twitter API.
The date in the filename represents the date of the tweets' creation.

There are two versions:

* those starting with hydrator contain the IDs only, for use with the Tweet hydration tools by DocNow
* those starting with the respective dates contain additional data about our collection, such as the collection date.

Tweets deleted before the collection date will not be in the dataset. This is an important caveat when dealing with this data.
