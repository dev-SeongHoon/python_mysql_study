from restore_backup.backup_restore import BackupRestore

if __name__ == "__main__":
    backup_restore = BackupRestore()
    #backup_restore.data_backup('product')
    #backup_restore.data_backup('sale')
    backup_restore.data_restore('product')
    backup_restore.data_restore('sale')


"""
SHOW variables like "secure_file_priv";


/*
확인후 추가
[mysqld]
secure_file_priv=""
*/
Ubuntu Linux 

SELECT * FROM product
INTO OUTFILE '//product.txt'
CHARACTER SET 'UTF8'
FILES TERMINATED by ','
LINES TERMINATED by '\r\n';

delete form product;
select * from product;

LOAD DATA LOCAL INFILE '//product.txt'
INTO TABLE product 
character set 'UTF8'
fields TERMINATED by ','
LINES TERMINATED by '\r\n';
"""