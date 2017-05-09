#!/usr/bin/perl
# Printing the square of the numbers 1–10 in table format.

use warnings;
use strict;
use CGI qw( :standard );

print( header() );
print( start_html() );
print( h1( "First Ten Square Numbers" ) );
print( '<table width="80%" border="3">' );
print( Tr( th( "Number" ), th( "Number Squared" ) ) );
print( Tr( td( $_ ), td( $_ ** 2 ) ) ) foreach ( 1 .. 10 );
print( "</table>" );
print( end_html() );