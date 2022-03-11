**Contributions welcome! Contact us in the issues or create a PR**

**Please report issues with the data if you find any**

# ukraine_data

![Flag of Ukraine](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/320px-Flag_of_Ukraine.svg.png)

Twitter (and maybe later other social media) data around the Ukraine Invasion in February 2022

Data reaches back until February 1st and will be updated daily.

Please cite as:

> Münch, F. V., & Kessling, P. (2022, February 25). ukraine_data. https://doi.org/10.17605/OSF.IO/RTQXN

Other citation styles can be found on OSF:

<https://doi.org/10.17605/OSF.IO/RTQXN>

## FAQ

### What data is available?

Right now, we provide data on tweets that contain the hashtag or word 'ukraine' (see query below) in different languages since February 1st [here](Twitter/).

Collections:

| language                               | query                   | data nearly complete from    |
| -------------------------------------- | ----------------------- | ---------------------------- |
| german                                 | ukraine AND lang='de'   | 1. February 2022             |
| english (not yet complete)             | #ukraine AND lang='en'  | 1. February 2022             |
| russian                                | Украина AND lang:ru     | 1. February 2022             |
| ukrainian                              |  Україна AND lang:uk    | 1. February 2022             |


To comply with Twitter TOS and protect people who have decided to delete their tweets, we share tweet IDs, creation date, and metadata about our collection methods and dates only.

If you are elegible for Academic API access with Twitter and want to add further languages, let us know and we are happy to support you.

### How was this data collected?

With the [focalevents](https://github.com/ryanjgallagher/focalevents) tool by @ryanjgallagher using our Academic Twitter API access.

We query tweets that contain the keywords stated above and filter for languages detected by Twitter.

We started collecting tweets on 24. February, backfilling tweets since 1. February.

You find information on whether an ID was collected via the search ('backfilled') or streamed in the data itself. Backfilled data will not contain tweets that have been deleted before the collection time.

### How is the data structured?

We share the data in language specific folders.

The filenames indicate the date of the tweets, one file per day.

Furthermore, every file is available in two CSV versions:

* one with the IDs only, for easy hydration with tools mentioned below.
* one with metadata on how the data was collected in every line, for you to filter it to your needs

### How many tweets are in each collection?

This many:

![counts_en_hashtag (1)](https://user-images.githubusercontent.com/8951994/157707823-c072c965-9ee3-4fd0-8304-1e144eebd85b.png)
![counts_de (2)](https://user-images.githubusercontent.com/8951994/157707495-280d8925-94e8-4b64-a33c-c715b76f9dd4.png)
![counts_uk (1)](https://user-images.githubusercontent.com/8951994/157707739-8aa1bb4e-0c53-45bd-973f-ef244fbdad3f.png)
![counts_ru (2)](https://user-images.githubusercontent.com/8951994/157707219-451b90de-cd36-4c6c-9cc7-69b9239be3b7.png)
![counts_all (2)](https://user-images.githubusercontent.com/8951994/157707084-d8766e31-a43d-42a7-bda5-0851e6040a53.png)

We will provide more figures with daily counts as soon as we do not notice any gaps anymore that would affect them.

### How can I get the content of the tweets?

Via the Twitter API, e.g. with [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#hydrate) or, if you prefer a graphical user interface, with the [Hydrator](https://github.com/DocNow/hydrator) by @DocNow.

We provide files that do contain the tweet IDs only for this purpose.

If you need any data that is not available this way, we might be able to help you, pending an ethical evaluation of your research goals.

### How do you ensure the quality of the data?

Due to connection and other problems there can and always will be gaps in such a large-scale data collection. We are in the process of meticulously backfilling any gaps that we discover in our data collection.

Here we compare our data with the estimated counts returned by the API (number of collected tweets per hour divided by Twitter API count estimates):

![target_counts_ratio_ukraine-en-hashtag](https://user-images.githubusercontent.com/8951994/157718253-e40451d8-bdd3-48e6-bfb6-e46106397275.png)
![target_counts_ratio_ukraine](https://user-images.githubusercontent.com/8951994/157718292-60642ecc-8443-4762-9204-87fceac135d3.png)
![target_counts_ratio_ukraine-uk](https://user-images.githubusercontent.com/8951994/157718338-99d88bd2-7bc3-4c3f-ad9d-9e0cf5545a36.png)
![target_counts_ratio_ukraine-ru](https://user-images.githubusercontent.com/8951994/157718371-ce2748b3-3406-4381-bf9c-da1b9ad115b6.png)


We aim for 95% of the hourly estimated counts by Twitter. As you can see, this is not always possible, most likely due to tweet deletions, account bans, account protections, or wrong estimates by Twitter.

### Is this ethical/allowed?

Because we publish tweet IDs only, we comply with the Twitter TOS.

Given the public interest in this data and that this data will be indispensable for presenting research findings on events in contemporary history we also comply with the GDPR, especially its German implentation, the DSGVO ([Art 6 (1) f) GDPR in connection with Art 85 GDPR, § 27 BDSG](https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act)).

From an ethical standpoint, we do not share any data the conflict parties would not have collected or be able to collect anyway.

As we share only Tweet IDs, accounts can [protect themselves](https://twitter.com/TwitterSafety/status/1496698664747687942?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1496698664747687942%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.tagesschau.de%2Fausland%2Famerika%2Fsocial-media-sicherheit-ukraine-101.html) at any time.

We think, sharing this collection contributes to the cause of open science.

Furthermore, while much of the information contained in the tweets will be dis- and misinformation, this dataset at least provides transparency by enabling researchers and OSINT experts to analyse it independently, which is in the public interest of democratic states.

However, we still ask you to assess your respective use of this data with your ethical review board, and/or with our ethical and legal guidance questionaire [SOCRATES](<https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act>)
