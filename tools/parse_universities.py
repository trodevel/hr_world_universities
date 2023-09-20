import csv
import html

def read_file( filename: str, outp_filename: str, outp_2_filename: str ):

    i = 0

    f = open( outp_filename, "w" )
    f2 = open( outp_2_filename, "w" )

    with open( filename ) as csvfile:
        reader = csv.reader( csvfile, delimiter=',' )
        for row in reader:
            i += 1
            ( country, name_enc, url ) = row[0:3]

            name = html.unescape( name_enc )

            f.write( f"{i};{country};{name};{url}\n" )
            f2.write( f"{i};{name}\n" )

    print( f"INFO: read {i} records from {filename}, wrote result to {outp_filename}" )

read_file( "../externals/world-universities-csv/world-universities.csv", "../resources/universities.csv", "../resources/universities.en.csv" )
