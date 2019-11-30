#! /usr/bin/perl

use strict;
use warnings;
use Try::Tiny;
use Config::JSON;


if(@ARGV = 0){
   die "ERROR - No configuration file";
}

my $configFile = $ARGV[0];

print $configFile;