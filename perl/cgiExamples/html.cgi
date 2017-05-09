#!/usr/bin/perl
# Printing the square of the numbers 1-10 as an HTML file.

use warnings;
use strict;

print( "Content-type: text/html\n\n" );
print( "<html><head><title>Current date and time</title>" );
print( "</head><body>" );
print( "<h1 align=\"center\">First Ten Square Numbers</h1>" );
print( "<center>\n" );

foreach ( 1 .. 10 ) {
	print( "$_ ^ 2 = ", $_ ** 2, "<br>\n" );
 }
print( "</center>" );
print( "</body></html>" );