Summary:
On September 11th, 2018 starting from 2:39 AM, the establishment's website was down for twenty three minutes. Approximately 91% of the users experienced a 500 internal server error has been identified - a mispelled filename in a configuration file.

Timeline:
2:39AM: DevOps team notifed of reports in high spikes of 500 errors
2:42AM: Check the config files for Apache2 and Nginx
2:46AM: Config files updated to lend more sensitivity towards error
2:50AM: Caught the filename error
2:45AM: Wrote a puppet script and executed onto server
2:59AM: Restored server back to 100%

Root Cause:
We first checked the error logs for potential explaination of the internal server errors. When we found it blank, we configured the error logs to increase verbosity. Using 'strace' command, we subsequently determined that a wordpress filetype has been misspelled. We promptly corrected the error, but not before creating a script that would help automate the task.

Rooms for Future Improvement:
- Test files in development before pushing to production
