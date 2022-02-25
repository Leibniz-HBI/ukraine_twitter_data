**Disclaimer: This is work in progress! Please validate and verify data via spot checks and make sure its plausible before relying on it.**

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

Right now, we provide data on tweets that contain the word 'ukraine' in different languages since February 1st [here](Twitter/).

Collection complete from 1st to 24th February in the following languages so far:

* German (done)
* ~~English~~ (collection ongoing)
* ~~Russian~~ (not yet started)
* ~~Ukrainian~~ (not yet started)

After the backfill is completed, we plan to collect data every day.

To comply with Twitter TOS and protect people who have decided to delete their tweets, we share tweet IDs, creation date, and metadata about our collection methods and dates only.

### How was this data collected?

With the [focalevents](https://github.com/ryanjgallagher/focalevents) tool by @ryanjgallagher using our Academic Twitter API access.

We query tweets that contain the keyword 'ukraine' and filter for languages detected by Twitter.

We started collecting tweets on 24. February, backfilling tweets since 1. February.

You find information on whether an ID was collected via the search ('backfilled') or streamed in the data itself. Backfilled data will not contain tweets that have been deleted before the collection time.

We will add languages over time. So far we have planned English, German, Russian and Ukrainian.

### How is the data structured?

We share the data in language specific folders.

The filenames indicate the date of the tweets, one file per day.

Furthermore, every file is available in two CSV versions:

* one with the IDs only, for easy hydration with tools mentioned below.
* one with metadata on how the data was collected in every line, for you to filter it to your needs

### How can I get the content of the tweets?

Via the Twitter API, e.g. with [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#hydrate) or, if you prefer a graphical user interface, with the [Hydrator](https://github.com/DocNow/hydrator) by @DocNow.

We provide files that do contain the tweet IDs only for this purpose.

If you need any data that is not available this way, we might be able to help you, pending an ethical evaluation of your research goals.

### Is this ethical/allowed?

Because we publish tweet IDs only, we comply with the Twitter TOS.

Given the public interest in this data and that this data will be indispensable for presenting research findings on events in contemporary history we also comply with the GDPR, especially its German implentation, the DSGVO ([Art 6 (1) f) GDPR in connection with Art 85 GDPR, § 27 BDSG](https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act)).

From an ethical standpoint, we do not share any data the conflict parties would not have collected or be able to collect anyway.

As we share only Tweet IDs, accounts can [protect themselves](https://twitter.com/TwitterSafety/status/1496698664747687942?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1496698664747687942%7Ctwgr%5E%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.tagesschau.de%2Fausland%2Famerika%2Fsocial-media-sicherheit-ukraine-101.html) at any time.

We think, sharing this collection contributes to the cause of open science.

Furthermore, while much of the information contained in the tweets will be dis- and misinformation, this dataset at least provides transparency by enabling researchers and OSINT experts to analyse it independently, which is in the public interest of democratic states.

However, we still ask you to assess your respective use of this data with your ethical review board, and/or with our ethical and legal guidance questionaire [SOCRATES](<https://leibniz-hbi.github.io/socrates/#41-legal-gdpr-and-the-german-federal-data-protection-act>)
