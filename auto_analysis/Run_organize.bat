set PYTHONPATH=%cd%
echo Run %date% %time% > output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt

echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
python copy_from_site_to_files.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt 2>&1


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
python organize_for_summary.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt 2>&1


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
python organize_for_time-series.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt 2>&1


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
python organize_for_A-time-series.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt 2>&1


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
python ready_for_R.py >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt 2>&1


echo; >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
echo End %date% %time% >> output/%date:~-10,4%%date:~-5,2%%date:~-2,2%_organize.txt
