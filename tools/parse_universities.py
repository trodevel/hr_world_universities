import csv

def read_file( filename: str, outp_filename: str ):

    i = 0

    f = open( outp_filename, "w" )


    with open( filename ) as csvfile:
        reader = csv.reader( csvfile, delimiter=',' )
        i += 1
        for row in reader:
            ( country, name, url ) = row[0:3]
            f.write( f"{i};{country};{name};{url}\n" )

    print( f"INFO: read {i} records from {filename}, wrote result to {outp_filename}" )

read_file( "../externals/world-universities-csv/world-universities.csv", "../resources/universities.csv" )
