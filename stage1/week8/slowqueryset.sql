-- 開啟慢查詢
show variables like '%slow_query_log%';
set global slow_query_log='ON';

/* 
設定慢查詢時間, 預設為10秒
執行時間超過設定時間的sql將記錄到慢查詢日誌
重新登入，設定生效
*/
show variables like '%long_query_time%';
set global long_query_time=1;

-- 查詢慢查詢日誌檔案存放位置
show variables like '%slow_query_log_file%';
/*
set global slow_query_log_file = '/usr/local/mysql/data/laptopc-slow.log';
*/

