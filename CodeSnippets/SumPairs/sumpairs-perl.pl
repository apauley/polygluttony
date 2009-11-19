use strict;
use warnings;
use Data::Dumper;

my @array = (1, 2, 3, 4, 5, 6, 7, 8, 9);
push @array, 0 if scalar @array % 2;
my %hash = @array;
my @sum = map { $hash{$_}+$_ } sort keys %hash;

print Dumper(\@sum);
