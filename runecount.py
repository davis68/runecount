import glob
source_files = glob.glob( '/home/davis68/code/urbit/**/*.hoon',recursive=True )
print( source_files )

with open( 'runes.txt','r' ) as rune_file:
    rune_list = rune_file.read().split('\n')
del rune_list[ rune_list.index( '' ) ]

runes = { rune:0 for rune in rune_list }
for source_file in source_files:
    with open( source_file,'r' ) as src:
        src_data = src.read()
        for rune in runes:
            runes[ rune ] += src_data.count( rune )

import matplotlib.pyplot as plt
fig = plt.figure()

from collections import OrderedDict
runes_ = OrderedDict( sorted( runes.items(),key=lambda x:x[1],reverse=True ) )

ax1 = fig.add_subplot( 211 )
ax1.bar( range( len( runes_ ) ),list( runes_.values()),align='center' )
ax1.set_xticks( range( len( runes_ ) ) )
ax1.set_xticklabels( list( runes_.keys() ) )
plt.xticks( rotation=90 )
ax1.set_title( 'Frequency of Hoon Runes in the Urbit Codebase' )
#ax1.set_xlabel( 'Runes' )
ax1.set_ylabel( 'Count' )

from numpy import log10,linspace,array,exp
from scipy import polyfit
x = list( range( len( runes_ ) ) )
logy = log10( [ runes_[ key ] for key in runes_.keys() ] )
out = polyfit( x,logy,1 )
out2 = polyfit( x[:-9],logy[:-9],1 )

ax3 = fig.add_subplot( 212 )
ax3.bar( range( len( runes_ ) ),list( runes_.values()),align='center',log=True )
x = array( x )
ax3.plot( x,10**(out[0]*x+out[1] ),color='orange' )
ax3.plot( x,10**(out2[0]*x+out2[1] ),color='red' )
ax3.set_xticks( range( len( runes_ ) ) )
ax3.set_xticklabels( list( runes_.keys() ) )
plt.xticks( rotation=90 )
#ax3.set_title( 'Frequency of Hoon Runes in the Urbit Codebase' )
ax3.set_xlabel( 'Runes' )
ax3.set_ylabel( 'Count (Log Scale)' )

plt.show()

