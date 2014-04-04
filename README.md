yelp-data-formatter
===================

* clone repository
* make a virtualenv out of the directory (virtualenv yelp-data-formatter)
* install dependences (pip install https://pypi.python.org/packages/source/S/SexMachine/SexMachine-0.1.1.tar.gz)

File I/O happens in the same directory

Line 59 defines how much output fact data to create.  5 iterations is approx 1 million records, so if you need 100 million change the range to 500.

1 million records winds up taking up a little less than a gig, so figure that 100 million will take about 95-100 gigs of space uncompressed


