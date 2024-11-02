@echo off

set source="C:\FluxUI\temp\backup\"
set destination="C:\FluxUI\temp\"

copy /Y "%source%\input.txt" "%destination%\input.txt"
copy /Y "%source%\output.html" "%destination%\output.html"
copy /Y "%source%\output.txt" "%destination%\output.txt"
copy /Y "%source%\prompt_input.txt" "%destination%\prompt_input.txt"
copy /Y "%source%\response.txt" "%destination%\response.txt"

echo Cache Cleared!
