#!/usr/bin/perl

use warnings;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI qw( :standard );

print( header() );
print( start_html( "GPA Calculator" ) );

print( end_html() );