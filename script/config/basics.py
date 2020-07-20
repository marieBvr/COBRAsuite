# -*- coding: utf-8 -*-

import os
import socket
from configobj import ConfigObj
from path import config_dir
from prettytable import PrettyTable


def get_hostname():
    """
    Get host name
    :return: host name in lower case
    """
    return socket.gethostname().lower()


def load_config(filepath=None):
    """
    Load config object from a file
    :param filepath: path of config file
    :return: a config object
    """
    if not filepath:
        filename = '%s.ini' % get_hostname()
        filepath = os.path.join(config_dir, filename)
        if not os.path.exists(filepath):
            filepath = os.path.join(config_dir, 'default.ini')
    return ConfigObj(filepath)


def cursor_to_table(c):
    all_results=list(c)
    available_first_level_keys=[]
    for r in all_results:
        for k in r.keys():
            if k not in available_first_level_keys:
                available_first_level_keys.append(k)
    tt=PrettyTable(available_first_level_keys)
    for r in all_results:
        tt.add_row([r.get(k,"NA") for k in available_first_level_keys])
    print(tt)


def parse_tsv_table(src_file,column_keys,n_rows_to_skip,id_col=None):
    rows_to_data=[]
    with open(src_file, 'rb') as f:
        csvreader = reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        cpt=0
        try:
            #logger.info("number of rows:%s",len(list(csvreader)))
            for row in csvreader:
                cpt+=1
                values=[]
                #logger.info("rows:%s and len %d",row,len(row))
                values.append(cpt);
                for col in range(len(row)):
                    #logger.info("rows:%s ",row[col])
                    values.append(row[col])   
                if len(column_keys)!=len(values):
                    logger.info("columns keys length:%d",len(column_keys))
                    logger.info("value length :%d",len(values))
                    logger.critical("Mismatching number of columns and number of keys at location\n%s/nrow:%s"%(src_file,csvreader.line_num))
                    this_dict=dict(zip(column_keys,values))
                    if 'Start' in this_dict:
                        if this_dict['Start']!='':
                            if isinstance(this_dict['Start'],basestring):
                                this_dict['Start']=int(this_dict['Start'])
                    if 'End' in this_dict:
                        if this_dict['End']!='':
                            if isinstance(this_dict['End'],basestring):
                                this_dict['End']=int(this_dict['End'])
                                this_dict['Start']=int(this_dict['Start'])
                    if 'logFC' in this_dict:
                        if this_dict['logFC']!='':
                            if isinstance(this_dict['logFC'],basestring):
                                this_dict['logFC']=float(this_dict['logFC'])
                if id_col: #enforce id col type
                    if isinstance(this_dict[id_col],Number):
                        this_dict[id_col]=str(int(this_dict[id_col]))
                rows_to_data.append(this_dict)      
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (src_file, csvreader.line_num, e))
    logger.info("Successfully parsed %d rows of %d values",len(rows_to_data),len(column_keys))
    return rows_to_data 


def parse_excel_table(src_file,column_keys,n_rows_to_skip,sheet_index,id_col=None):

    wb = open_workbook(src_file)
    current_sheet=wb.sheets()[sheet_index]
    current_sheet.name
    rows_to_data=[]
    logger.info("currentsheet nrows:%d",(current_sheet.nrows))
    for row in range(n_rows_to_skip,current_sheet.nrows):
        values=[row]
        #logger.info("lenght:%d",(len(values)))
        for col in range(current_sheet.ncols):
            values.append(current_sheet.cell(row,col).value)
        if len(column_keys)!=len(values):
            logger.critical("Mismatching number of columns and number of keys at location\n%s/sheet:%d/nrow:%d"%(src_file,sheet_index,row))
        this_dict=dict(zip(column_keys,values))
        if id_col: #enforce id col type 
            if isinstance(this_dict[id_col],Number):
                this_dict[id_col]=str(int(this_dict[id_col]))
        rows_to_data.append(this_dict)
    logger.info("Successfully parsed %d rows of %d values",len(rows_to_data),len(column_keys)-1)
    return rows_to_data

