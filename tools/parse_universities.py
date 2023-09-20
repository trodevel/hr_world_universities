import csv
import html

def read_file( filename: str, outp_filename: str, outp_2_filename: str ):

    i = 0

    f = csv.writer( open( outp_filename, "w" ), delimiter=';', lineterminator='\n' )
    f2 = csv.writer( open( outp_2_filename, "w" ), delimiter=';', lineterminator='\n' )

    with open( filename ) as csvfile:
        reader = csv.reader( csvfile, delimiter=',' )
        for row in reader:
            i += 1
            ( country, name_enc, url ) = row[0:3]

            name = html.unescape( name_enc )

            f.writerow( ( i, country, name, url ) )
            f2.writerow( ( i, name ) )

    print( f"INFO: read {i} records from {filename}, wrote result to {outp_filename}" )

read_file( "../externals/world-universities-csv/world-universities.csv", "../resources/universities.csv", "../resources/universities.en.csv" )
