# Job Notifier

This workflow automatically searches for fresher software testing jobs and sends notifications for new listings.

## Setup

1.  **API Keys**: You need to get API keys from [SerpApi](https://serpapi.com/) and [Simplepush](https://simplepush.io/).

2.  **Environment Variables**: Set the following environment variables with your API keys:
    ```bash
    export SERPAPI_API_KEY="YOUR_SERPAPI_API_KEY"
    export SIMPLEPUSH_API_KEY="YOUR_SIMPLEPUSH_API_KEY"
    ```
    You can add these lines to your `.bashrc` or `.zshrc` file to make them permanent.

## Manual Execution

To run the job search manually, execute the `run.sh` script:

```bash
./job_notifier/run.sh
```

## Scheduling with Cron

To run the job search automatically at regular intervals, you can use a cron job.

1.  Open your crontab for editing:
    ```bash
    crontab -e
    ```

2.  Add a new line to run the script at your desired interval. For example, to run the script every hour, add the following line:
    ```cron
    0 * * * * /full/path/to/your/repo/job_notifier/run.sh
    ```
    Make sure to replace `/full/path/to/your/repo/` with the absolute path to the repository on your system.
