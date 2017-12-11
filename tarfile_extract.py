'''
Created on 2017年11月27日

@author: Francis
'''
import os
import glob
import tarfile
from multiprocessing import Pool
import time

def unzip_file(file):
    #这里输入解压的目的路径
    target_path = r'D:\公司\项目管理\2017年\02 终端质量报告\XDR\数据解析\unzip_file'
    try:
        tar = tarfile.open(file)
        tar.extractall(target_path)
        tar.close()
    except Exception as e:
        print('Exception:',e)
    
if __name__ == "__main__":
    print ("开始解压")
    #这里输入解压的源路径
    source_path = r'D:\公司\项目管理\2017年\02 终端质量报告\XDR\数据解析\zip_file'
    zip_files_tar=glob.glob(source_path+'\*'+'.tar.gz')
    start_time = time.clock()
    pool = Pool()
    pool.map(unzip_file,zip_files_tar)
    pool.close()
    pool.join()
    end_time = time.clock()
    print ("解压结束，共运行",end_time-start_time,"s")