# Example python script that reads protobuf messages of serialized R objects.
# To (re)produce these messages yourself, see /inst/messages/build.R script 
# in the RProtoBufUtils package. Before running this script, download and 
# compile the .proto files into Python modules (see compile_python.sh).

#import the compiled proto definition, see compile_python.sh
import stocks_pb2;

#reading straight from http url
import urllib2
msg = stocks_pb2.data();
response = urllib2.urlopen('https://raw.github.com/jeroenooms/RProtoBufUtils/master/inst/messages/msg_stocks.bin')
msg.ParseFromString(response.read());
print(msg)
del msg

#reading from a file:
import os;
os.system('wget https://raw.github.com/jeroenooms/RProtoBufUtils/master/inst/messages/msg_stocks.bin');
msg = stocks_pb2.data();
f = open('msg_stocks.bin', 'rb')
msg.ParseFromString(f.read())
f.close();
print(msg)
del msg


