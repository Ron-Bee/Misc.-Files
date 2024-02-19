import os 
dest_dir = os.path.join(os.getcwd(), "dest")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
    
source_file = os.path.join(os.getcwd(), "source")
destination_file = os.path.join(os.getcwd(), "dest", "source")

os.rename(source_file, destination_file)

close(destination_file)
close(source_file)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import csv
hosts = [["workstation.local", "237.84.2.178"], ["webserver.local", "244.178.44.111"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    