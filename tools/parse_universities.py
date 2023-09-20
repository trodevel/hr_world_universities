import csv

def read_file( filename: str ):

    num_lines = 0

    with open( filename ) as csvfile:
        reader = csv.reader( csvfile, delimiter=',' )
        for row in reader:
            ( country, name, url ) = row[0:3]
            #print( "DEBUG: {}, {}, {}".format( username, timestamp, follow_status ) )

    print( f"INFO: read {num_lines} records from {filename}" )



