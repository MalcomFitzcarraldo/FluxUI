echo off

if exist "C:\FluxUI\temp\done.txt" (
  del "C:\FluxUI\temp\done.txt"
  echo done.txt deleted successfully.
) else (
  echo done.txt not found.
) 