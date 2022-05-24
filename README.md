**Contributions welcome! Contact us in the issues or create a PR**

# ukraine_data

![Flag of Ukraine](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/320px-Flag_of_Ukraine.svg.png)

Twitter (and maybe later other social media) data around the Ukraine Invasion in February 2022

Data reaches back until February 1st and will be updated daily.

The updates are automatised and should be available every afternoon for the preceding day. Let us know if there are any problems!

Please cite as:

> Münch, F. V., & Kessling, P. (2022, March 1). ukraine_twitter_data. https://doi.org/10.17605/OSF.IO/RTQXN

Other citation styles can be found on OSF:

<https://doi.org/10.17605/OSF.IO/RTQXN>

## FAQ

### What data is available?

Right now, we provide data on all tweets that contain the hashtag or word 'ukraine' (see query below) in different languages since February 1st [here](Twitter/) according to the Twitter Academic API.

Furthermore, data on English tweets containing the term 'bucha' are now available.

Collections:

| language                               | query                              | data nearly complete from    |
| -------------------------------------- | ---------------------------------- | ---------------------------- |
| English                                |  #ukraine AND lang='en'            | 1. February 2022             |
| German                                 |  ukraine AND lang='de'             | 1. February 2022             |
| Russian                                |  Украина AND lang:ru               | 1. February 2022             |
| Ukrainian                              |  Україна AND lang:uk               | 1. February 2022             |
| English                                |  bucha AND lang='en'               | 1. March 2022                |
| German                                 |  (bucha OR butscha) AND lang='de'  | 1. March 2022                |
| Russian                                |  (Бу́ча OR bucha) AND lang:ru       | 1. March 2022                |
| Ukrainian                              |  (Бу́ча OR bucha) AND lang:uk       | 1. March 2022                |


To comply with Twitter TOS and protect people who have decided to delete their tweets, we share tweet IDs, creation date, and metadata about our collection methods and dates only.

If you are elegible for Academic API access with Twitter and want to add further languages, let us know and we are happy to support you.

### How was this data collected?

With the [focalevents](https://github.com/ryanjgallagher/focalevents) tool by @ryanjgallagher using our Academic Twitter API access.

We query tweets that contain the keywords stated above and filter for languages detected by Twitter.

We started collecting tweets on 24. February, backfilling tweets since 1. February.

You find information on whether an ID was collected via the search ('backfilled') or streamed in the data itself. Backfilled data will not contain tweets that have been deleted before the collection time.

### How is the data structured?

We share the data in language specific folders.

The filenames indicate the date of the tweets.

Furthermore, every file is available in two CSV versions:

* one with the IDs only, for easy hydration with tools mentioned below.
* one with metadata on how the data was collected in every line, for you to filter it to your needs

### How many tweets are in each collection?

This many:

#### (\#)Ukraine

![counts_en_hashtag (1)](https://user-images.githubusercontent.com/8951994/157707823-c072c965-9ee3-4fd0-8304-1e144eebd85b.png)
![counts_de (2)](https://user-images.githubusercontent.com/8951994/157707495-280d8925-94e8-4b64-a33c-c715b76f9dd4.png)
![counts_uk (1)](https://user-images.githubusercontent.com/8951994/157707739-8aa1bb4e-0c53-45bd-973f-ef244fbdad3f.png)
![counts_ru (2)](https://user-images.githubusercontent.com/8951994/157707219-451b90de-cd36-4c6c-9cc7-69b9239be3b7.png)
![counts_all (2)](https://user-images.githubusercontent.com/8951994/157707084-d8766e31-a43d-42a7-bda5-0851e6040a53.png)

#### Bucha/Butscha/Бу́ча

![counts_bucha_en](https://user-images.githubusercontent.com/8951994/163465221-e515eedf-dc6c-456b-835c-8ff1c3bd691c.png)
![counts_bucha_de](https://user-images.githubusercontent.com/8951994/163465234-5a6b25d4-76c5-4a45-aeb2-2209aa0c1c5e.png)
![counts_bucha_uk](https://user-images.githubusercontent.com/8951994/163465249-d6994f5b-a361-4424-8590-9369b4e4e8b1.png)
![counts_bucha_ru](https://user-images.githubusercontent.com/8951994/163465252-207f1d0d-1f9d-4215-910e-9d93c6a06be9.png)

These figures will be updated periodically.

### How can I get the content of the tweets?

Via the Twitter API, e.g. with [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#hydrate) or, if you prefer a graphical user interface, with the [Hydrator](https://github.com/DocNow/hydrator) by @DocNow.

We provide files that do contain the tweet IDs only for this purpose.

If you need any data that is not available this way, we might be able to help you, pending an ethical evaluation of your research goals.

### How do you ensure the quality of the data?

Due to connection and other problems there can and always will be gaps in such a large-scale data collection. We are in the process of meticulously backfilling any gaps that we discover in our data collection.

Here we compare our data with the estimated counts returned by the API (number of collected tweets per hour divided by Twitter API count estimates).

We aim for 95% of the hourly estimated counts by Twitter. As you can see, this is not always possible, most likely due to tweet deletions, account bans, account protections, or wrong estimates by Twitter.

In the English and Bucha datasets our count is for one hour 16-18 times higher than the Twitter estimate we got. We will have a closer look at that asap, but more is usually better than less. Maybe its a glitch caused by daylight saving time (even though we should see that also in other languages) or the 'spikyness' of the event 🤷. Most counts are >= 95%, less than 10 hours have only more than 90% of the estimated count.

#### (\#)Ukraine

![target_counts_ratio_ukraine-en-hashtag](https://user-images.githubusercontent.com/8951994/157718253-e40451d8-bdd3-48e6-bfb6-e46106397275.png)
![target_counts_ratio_ukraine](https://user-images.githubusercontent.com/8951994/157718292-60642ecc-8443-4762-9204-87fceac135d3.png)
![target_counts_ratio_ukraine-uk](https://user-images.githubusercontent.com/8951994/157718338-99d88bd2-7bc3-4c3f-ad9d-9e0cf5545a36.png)
![target_counts_ratio_ukraine-ru](https://user-images.githubusercontent.com/8951994/157718371-ce2748b3-3406-4381-bf9c-da1b9ad115b6.png)

#### Bucha/Butscha/Бу́ча

![target_counts_ratio_bucha-en](https://user-images.githubusercontent.com/8951994/163465293-fd457b95-d64b-4664-bfb5-a1549fb1987b.png)
![target_counts_ratio_bucha-de](https://user-images.githubusercontent.com/8951994/163465305-b6759f0e-2e7d-4190-a00d-05c3795b3f18.png)
![target_counts_ratio_bucha-uk](https://user-images.githubusercontent.com/8951994/163465321-79757285-2065-476c-8d39-be2834e9aced.png)
![target_counts_ratio_bucha-ru](https://user-images.githubusercontent.com/8951994/163465334-04f5ff6d-bdc5-4e32-9cab-8b2b07ba6a9d.png)


### Is this ethical/allowed?

Because we publish tweet IDs only, we comply with the Twitter TOS.

Given the public interest in this data and that this data will be indispensable for presenting research findings on events in contemporary history we also comply with the GDPR, especially its German implentation, the DSGVO ([Art 6 (1) f) GDPR in connection with Art 85 GDPR, § 27 BDSG](https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act)).

From an ethical standpoint, we do not share any data the conflict parties would not have collected or be able to collect anyway.

As we share only Tweet IDs, accounts can [protect themselves](https://twitter.com/TwitterSafety/status/1496698664747687942?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1496698664747687942%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.tagesschau.de%2Fausland%2Famerika%2Fsocial-media-sicherheit-ukraine-101.html) at any time.

We think, sharing this collection contributes to the cause of open science.

Furthermore, while much of the information contained in the tweets will be dis- and misinformation, this dataset at least provides transparency by enabling researchers and OSINT experts to analyse it independently, which is in the public interest of democratic states.

However, we still ask you to assess your respective use of this data with your ethical review board, and/or with our ethical and legal guidance questionaire [SOCRATES](<https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act>)

### I don't want all of the data

You can use Git's sparse checkout feature: https://dev.to/kiwicopple/quick-tip-clone-a-single-folder-from-github-44h6

If you're just interested in single days, the easiest way is to just download single files manually in the Github interface or automated with their URL via curl/wget.

## Limitations

This data is mainly limited by the fidelity of the Twitter API and data degradation over time:

* Tweet IDs of Tweets that have been deleted, suspended, hidden or protected before the collection time will not be in the dataset
* Tweets that have been deleted or otherwise depublished after collection time will not be returned during hydration
* The collection depends on Twitter's language detection, which is known to be far from perfect, but good enough for large scale assessments:
  * Tweets that have not been detected as being in one of the collected languages will not be in the collection.
  * Also, there will be mislabeled tweets (e.g. Dutch as German, or maybe even Ukrainian as Russian) in the collection.
  * Tweets that do not contain any text (e.g. links or pictures only) might be missing in the collection.

Furthermore, while we backfilled any gaps occuring in the data so far, there might be gaps in the future due to systems failures or errors in our code or used software. We plan to publish the count estimates by Twitter alongside the data automatically in the near future so that researchers can double check themselves. In the meantime, researchers with access to the Twitter Academic API have access to the count endpoints themselves and are able to compare the counts. Please let us know in the Issues if you see any major deviations.

We do not guarantee any ongoing collection, mainly because Twitter limits the amount of Tweets we can collect per month. So please do not plan with anything beyond what's here already, e.g. for project planning or grant proposals and such. (Or approach us and we will help you to apply for Academic access to the Twitter API yourself and set up your own collection.)
