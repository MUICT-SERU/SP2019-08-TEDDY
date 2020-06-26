import sys
import csv
import os
import glob
import pandas as pd
import numpy as np
from math import pi
from datetime import datetime as dt
from bokeh.io import output_file,show
from bokeh.models import DatetimeTickFormatter,ColumnDataSource
from bokeh.models import HoverTool
import bokeh.plotting as plot
from bokeh.transform import jitter
from bokeh.layouts import column,gridplot

def clean(path,fout):

    mylist=[]
    header = []
    foo=[]
    a=0
    i=0
    files = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))
    with open(fout, "w", newline='') as tt:
        print("Style,IdiomName,FileName,Color,Marker,CommitNO",file=tt)


    for f in files:
        commit = os.path.basename(f).replace(".csv","")
        nani = commit.split("_")

        with open(f, "r") as w:
            data = list(csv.reader(w))
        
        with open(fout, "a", newline='') as ttt:
            for row in data:
                temp = row[0].split('/')
                temp2 = temp[len(temp)-1].split('.py') 
                temp3 = temp2[0].split('-')

                for i in range(1,len(temp3)):
                    foo.append(temp3[i])
                idiomname = "-".join(foo)
                header.append(temp3[0])
                header.append(idiomname)
           
                for i in range(1,len(row)):
                    foo = row[i].split('/')
                    foo2 = foo[len(foo)-1].split(".py")
                    filename = foo2[0]+".py"
                    header.append(filename)
                    i = i+1
                
                    if header[0] == 'npi':
                        final = header[0]+","+header[1]+","+header[i]+",red"
                    else:
                        final = header[0]+","+header[1]+","+header[i]+",green"

                    if header[1] == 'dict-comprehension':
                        final = final+",circle"
                    elif header[1] == 'enumerate':
                        final = final+",triangle"
                    elif header[1] == 'file-reading-statement':
                        final = final+",square"
                    elif header[1] == 'list-comprehension':
                        final = final+",diamond"
                    elif header[1] == 'if-statement':
                        final = final+",hex"
                    elif header[1] == 'string-formatting':
                        final = final+",asterisk"
                    elif header[1] == 'code-formatting':
                        final = final+",CircleCross"
                    elif header[1] == 'set':
                        final = final+",cross"
                    elif header[1] == 'tuple':
                        final = final+",InvertedTriangle"
                    elif header[1] == 'variable-swapping':
                        final = final+",SquareCross"
                
                    final = final+","+nani[1]
                    print(final,file=ttt)

                    a=a+1
                foo = []
                header = []

def separate(fin,foutidiom,foutnonidiom):

    final=""
    
    ## Writing only IP rows into idiomatic.csv
    with open(foutidiom, 'w') as outidiom:
        print("Style,IdiomName,FileName,Color,Marker,CommitNO",file=outidiom)
        with open(fin, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[0] == 'pi':
                        final = row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]
                        print(final,file=outidiom)
    
    ## Writing only NIP rows into nonidiomatic.csv
    with open(foutnonidiom, 'w') as outnonidiom:
        print("Style,IdiomName,FileName,Color,Marker,CommitNO",file=outnonidiom)
        with open(fin, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[0] == 'npi':
                    final = row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]
                    print(final,file=outnonidiom)

def plot_graph(ip_input, nip_input):
    plot.output_file("myplot.html")


    idiomin = pd.read_csv(ip_input)
    nonidiomin = pd.read_csv(nip_input)


    sourceipy = ColumnDataSource(data=dict(
        styleipy = idiomin['Style'].astype('str'),
        inameipy = idiomin['IdiomName'].astype('str'),
        fnameipy =  idiomin['FileName'].astype('str'),
        coloripy = idiomin['Color'].astype('str'),
        markeripy = idiomin['Marker'].astype('str'),
        commitNOipy = idiomin['CommitNO']
    ))
        
    sourcenipy = ColumnDataSource(data=dict(
        stylenipy = nonidiomin['Style'].astype('str'),
        inamenipy = nonidiomin['IdiomName'].astype('str'),
        fnamenipy =  nonidiomin['FileName'].astype('str'),
        colornipy = nonidiomin['Color'].astype('str'),
        markernipy = nonidiomin['Marker'].astype('str'),
        commitNOnipy = nonidiomin['CommitNO']
    ))


    filename = idiomin['FileName'].unique().astype('str')

    p = plot.figure(y_range = filename, plot_width = 1500 ,title="Pythonic and Non-pythonic Code Occurences Over the Whole Commit History",tools=['wheel_zoom','pan','reset'])

    ip_plot = p.scatter(
                x='commitNOipy',
                y=jitter('fnameipy',width=0.1, range=p.y_range),
                marker = 'markeripy',
                size = 10,
                source=sourceipy,
                color='coloripy',
                alpha= 0.2,
                legend_label="Pythonic (P)"
                )
    ip_hover = HoverTool(
        tooltips=[
            ("style","@styleipy"),
            ("file name","@fnameipy"),
            ("commit NO","@commitNOipy"),
            ("idiom type", "@inameipy")
        ],
        renderers=[ip_plot]
    )
    p.add_tools(ip_hover)


    nip_plot = p.scatter(
                    x='commitNOnipy',
                    y=jitter('fnamenipy', width=0.1, range=p.y_range),
                    marker = 'markernipy',
                    size = 10,
                    source=sourcenipy,
                    color='colornipy',
                    alpha=0.2,
                    legend_label="Non-pythonic (NP)"
                    )  
    nip_hover = HoverTool(
        tooltips=[
            ("style","@stylenipy"),
            ("file name","@fnamenipy"),
            ("commit NO","@commitNOnipy"),
            ("idiom type", "@inamenipy")
        ],
        renderers=[nip_plot]
    )
    p.add_tools(nip_hover)
        
    p.yaxis.axis_label = "File name"
    p.xaxis.axis_label = "Commit No"

    p.legend.location = "top_right"
    p.legend.click_policy="hide"
    plot.show(p)

## Main
### argv[1]: location of Siamese's CSVs
### argv[2]: Bokeh's IP+NIP CSV (mixed.csv)
### argv[3]: Bokeh's IP CSV (idiomatic.csv)
### argv[4]: BOkeh's NIP CSV (nonidiomatic.csv)
siamese_input = str(sys.argv[1])
mixed_CSV = str(sys.argv[2])
ip_CSV = str(sys.argv[3])
nip_CSV = str(sys.argv[4])

clean(siamese_input,mixed_CSV)
separate(mixed_CSV,ip_CSV,nip_CSV)
plot_graph(ip_CSV,nip_CSV)

print("Starting visualization using Bokeh ...")
print("=======Configuration=======")
print("Siamese's CSV files location: ", str(sys.argv[1]))
print("Bokeh's mixed CSV: ", str(sys.argv[2]))
print("Bokeh's IP CSV: ", str(sys.argv[3]))
print("Bokeh's NIP CSV: ", str(sys.argv[4]))
print("Your plot is ready. See myplot.html")