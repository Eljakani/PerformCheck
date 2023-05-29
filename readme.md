# PerfomCheck

## Description
PerfomCheck is a Python script that allows you to measure the performance of a web server by sending multiple HTTP requests in parallel and logging the response times. It supports multi-threading, random generation of usernames and passwords, and provides statistics on successful and error requests.

## Dependencies
PerfomCheck requires the following dependencies:
- Python 3.x
- requests
- matplotlib
- termcolor
- tqdm
You can install the required dependencies using the following command:
```pip install requests matplotlib termcolor tqdm```

## How to Use
1. Clone or download the PerfomCheck repository.
2. Install the required dependencies using the above command.
3. Open a terminal or command prompt and navigate to the PerfomCheck directory.
4. Run the script using the following command:
`python3 script.py`
5. Follow the on-screen prompts to enter the URL, number of threads, number of requests, and export file path.
6. The script will start sending HTTP requests and display a progress bar.
7. Once all requests are sent, statistics and a bar chart of response times will be displayed.
8. The results will be exported to the specified JSON file.

Note: Make sure to adjust the script parameters and customize as per your requirements.
