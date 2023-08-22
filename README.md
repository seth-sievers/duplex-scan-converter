# duplex-scan-converter
A simple python script that converts a simplex scan from a scanner into a duplex pdf document by reordering the pages

## Purpose
This script was created since some scanners and scanner-printer combo units do not 
have good support for duplex scanning of pages. For example, the duplex scan on the 
Canon G7020 (using the auto document feeder) wants the user to feed a single page, wait for it to scan, and then flip it over and scan the other side. This must be done in order for every page that is to be scanned, defeating
the purpose of the auto document scanner. 

This script fixes this issue. To create a properly ordered pdf from a duplex scan, users follow the below steps.
1. Scan one side of the stack of pages
2. Flip the entire stack over and feed it back through the scanner (do not change the orientation of the pages)
3. Take the improperly ordered .pdf and feed it into the 'create-duplex.py' script

The script will reorder the pages into the proper front back format and create a new .pdf file.
