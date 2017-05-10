#!/usr/bin/perl
# Ex 15.7: Ex15_07.pl
# Creating and managing a MySQL database.

use warnings;
use strict;
use DBI;
use DBD::mysql;

my $dbh = DBI->connect( "DBI:mysql:CollegeDB", "root", "", 
                        { RaiseError => 1 } );

my $string = "CREATE TABLE Students ( 
                FirstName   VARCHAR( 30 ),
                LastName    VARCHAR( 30 ),
                Major       VARCHAR( 30 ),
                Credits     INT,
                GPA         FLOAT( 3, 2 ),
                DOB         VARCHAR( 10 ) )";

$dbh->do( $string );

$dbh->do( "INSERT INTO Students ( 
              FirstName, LastName, Major, Credits, 
              GPA, DOB )
           VALUES ( 'John', 'Doe', 'Biology', 
                    132, 2.80, '10-11-1981' )" ); 

$dbh->do( "INSERT INTO Students ( 
              FirstName, LastName, Major, Credits, 
              GPA, DOB )
           VALUES ( 'Jane', 'Doe', 'Biology', 
                    132, 2.80, '10-11-1981' )" ); 

$dbh->do( "INSERT INTO Students ( 
              FirstName, LastName, Major, Credits, 
              GPA, DOB )
           VALUES ( 'Paul', 'Deitel', 'Computer Science', 
                    142, 3.78, '12-25-1980' )" );

$dbh->do( "INSERT INTO Students ( 
              FirstName, LastName, Major, Credits, 
              GPA, DOB )
           VALUES ( 'Tem', 'Nieto', 'Mathematics', 
                    142, 3.87, '2-29-1980' )" ); 

$dbh->do( "INSERT INTO Students ( 
              FirstName, LastName, Major, Credits, 
              GPA, DOB )
           VALUES ( 'Cheryl', 'Constein', 'E-business', 
              
     152, 4.00, '7-9-1979' )" );  

my $choice = "";

my $form = <<FORM;
Enter 'q' to quit.
Enter 'gpa' to sort by gpa.
Enter 'graduate' to graduate students.
Enter 'major' to see the students with
   a certain major.
Enter '?' to repeat these directions.

FORM

print( $form );

while ( $choice ne 'q' ) {
   print( "Please enter choice: " );
   chomp( $choice = <STDIN> );

   if ( $choice eq 'gpa' ) {
      sortbygpa();
   }
   elsif( $choice eq 'graduate' ) {
      deletebygrad();
      printTable();
   }
   elsif( $choice eq 'major' ) {
      print( "Please enter major: " );
      chomp( my $major = <STDIN> );
   
      sortbymajor( $major );
   }
   elsif( $choice eq '?' ) {
      print( "\n" );
      print( $form );
   }
}

sub sortbygpa
{
   print( "\n*************************\n" );
   my $sth1 = $dbh->prepare( q{
      select * FROM Students  
      ORDER BY GPA DESC }) or 
      die( "Cannot prepare statement: $DBI::errstr" );

   my $rc1 = $sth1->execute() or
      die( "Cannot execute statement: $DBI::errstr" );	
      
   while ( my @array = $sth1->fetchrow_array() ) {
      print( "@array\n" );
   } 
 
   $sth1->finish();
   print( "*************************\n\n" );
}

sub deletebygrad
{
   my $sth2 = $dbh->prepare( q{
      delete FROM Students
      WHERE Credits > 150 }) or 
      die( "Cannot prepare statement: $DBI::errstr" ); 

   my $rc2 = $sth2->execute() or
      die( "Cannot execute statement: $DBI::errstr" );	
   
   if( $rc2 ) {
      print( "Records successfully deleted\n" );	
   }
   $sth2->finish();
}

sub sortbymajor
{
   print( "\n*************************\n" );
   my $major = shift();
   my $querystring =
      "select * FROM Students WHERE Major='$major'";
   
   my $sth3 = $dbh->prepare( $querystring ) or 
      die( "Cannot prepare statement: $DBI::errstr" ); 

   my $rc3 = $sth3->execute() or
      die( "Cannot execute statement: $DBI::errstr" );

   while ( my @array = $sth3->fetchrow_array() ) {
      print( "@array\n" );
   } 

   $sth3->finish();		
   print( "*************************\n\n" );
}

sub printTable
{
   print( "\n*************************\n" );
   my $sth = $dbh->prepare( q{
      select * from Students } ) or
      die( "Cannot prepare statement: $DBI::errstr" );
   my $rc = $sth->execute() or
      die( "Cannot execute statement: $DBI::errstr" );
   while ( my @array = $sth->fetchrow_array() ) {
      print( "@array\n" );
   }

   $sth->finish();
   print( "*************************\n\n" );

}

###########################################################################
#  (C) Copyright 2001 by Deitel & Associates, Inc. and Prentice Hall.     #
#  All Rights Reserved.                                                   #
#                                                                         #
#  DISCLAIMER: The authors and publisher of this book have used their     #
#  best efforts in preparing the book. These efforts include the          #
#  development, research, and testing of the theories and programs        #
#  to determine their effectiveness. The authors and publisher make       #
#  no warranty of any kind, expressed or implied, with regard to these    #
#  programs or to the documentation contained in these books. The authors #
#  and publisher shall not be liable in any event for incidental or       #
#  consequential damages in connection with, or arising out of, the       #
#  furnishing, performance, or use of these programs.                     #
###########################################################################