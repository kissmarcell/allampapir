# Hungarian State Bonds Archiver

## Description
This is a simple Python application that regularly downloads the latest rates of state bonds from the Government Debt Management Agency of Hungary and then commits it inside this same repository, via GitHub Actions.

## Schedule
The application is scheduled to run at a given time, specified in the GitHub Action .yml file. [According to GitHub](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule), it may not run at the exact time specified during high loads. The exact moment of the execution is stored in the filename in UNIX timestamp format.

## Disclaimer
This application is not affiliated with the Hungarian Government Debt Management Agency (ÁKK) or the Hungarian State Treasury (MÁK) in any way. The author is not responsible for any damage caused by the use of this application.
