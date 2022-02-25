# ukraine_data

![Flag of Ukraine](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/320px-Flag_of_Ukraine.svg.png)

Twitter (and maybe later social media) data around the Ukraine Invasion in February 2022

Citation recommendations can be found on OSF:

<https://doi.org/10.17605/OSF.IO/RTQXN>

## FAQ

### What data is available?

Right now, we provide data on tweets that contain the word 'ukraine' in different languages since February 1st.

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

Because we publish tweet IDs only, we comply with the European GDPR as well as the Twitter TOS.

From an ethical standpoint, we do not share any data the conflict parties would not have collected or be able to collect anyway.

We think, sharing this collection contributes to the cause of open science.

Furthermore, while much of the information contained in the tweets will be disinformation, this dataset at least provides transparancy by enabling researchers and OSINT experts to analyse it independently.
