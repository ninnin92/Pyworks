set PYTHONPATH=%cd%
echo Run %date% %time% > output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt

echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt
python backup_for_Log.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt
python backup_for_Anlyz.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt
echo End %date% %time% >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_backup.txt