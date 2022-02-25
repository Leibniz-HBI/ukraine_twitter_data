![Flag of Ukraine](https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Flag_of_Ukraine.svg/320px-Flag_of_Ukraine.svg.png)

# ukraine_data

Twitter (and maybe later social media) data around the Ukraine Invasion in February 2022

## FAQ

### What data is available?

To comply with Twitter TOS and protect people who have decided to delete their tweets, we share tweet IDs only.

### How is the data structured?

### How can I get the content of the tweets?

Via the Twitter API, e.g. with [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2_en_us/#hydrate) or, if you prefer a graphical user interface, with the [Hydrator](https://github.com/DocNow/hydrator) by @DocNow.

If you need any data that is not available this way, we might be able to help you, pending an ethical evaluation of your research goals.

### How was this data collected?

With the [focalevents](https://github.com/ryanjgallagher/focalevents) tool by @ryanjgallagher using our Academic Twitter API access.

We query tweets that contain the keyword 'ukraine' and filter for languages detected by Twitter,

### Is this ethical/allowed?

Because we publish tweet IDs only, we comply with the European GDPR as well as the Twitter TOS.

From an ethical standpoint, we do not share any data the conflict parties would not have collected or be able to collect anyway.

We think, sharing this collection contributes to the cause of open science.

Furthermore, while much of the information contained in the tweets will be disinformation, this dataset at least provides transparancy by enabling researchers and OSINT experts to analyse it independently.
