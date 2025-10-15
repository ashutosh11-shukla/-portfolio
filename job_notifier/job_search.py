import os
import requests
import simplepush
import json

# --- Configuration ---
SERPAPI_API_KEY = os.environ.get("SERPAPI_API_KEY", "YOUR_SERPAPI_API_KEY")
SIMPLEPUSH_API_KEY = os.environ.get("SIMPLEPUSH_API_KEY", "YOUR_SIMPLEPUSH_API_KEY")
JOB_HISTORY_FILE = "job_history.json"
SEARCH_QUERY = "fresher software tester"
LOCATION = "Austin, Texas, United States"

def search_jobs(query, location):
    """Searches for jobs using the SerpApi."""
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": SERPAPI_API_KEY,
    }
    response = requests.get("https://serpapi.com/search.json", params=params)
    response.raise_for_status()
    return response.json().get("jobs_results", [])

def send_notification(title, body):
    """Sends a notification using Simplepush."""
    simplepush.send(SIMPLEPUSH_API_KEY, title, body)

def load_job_history():
    """Loads the job history from a file."""
    if not os.path.exists(JOB_HISTORY_FILE):
        return []
    with open(JOB_HISTORY_FILE, "r") as f:
        return json.load(f)

def save_job_history(history):
    """Saves the job history to a file."""
    with open(JOB_HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def main():
    """Main function to search for jobs and send notifications."""
    job_history = load_job_history()
    jobs = search_jobs(SEARCH_QUERY, LOCATION)

    new_jobs = 0
    for job in jobs:
        job_id = job.get("job_id")
        if job_id and job_id not in job_history:
            title = job.get("title")
            company = job.get("company_name")
            location = job.get("location")
            description = job.get("description")

            notification_title = f"New Job: {title} at {company}"
            notification_body = f"{location}\n\n{description}"

            send_notification(notification_title, notification_body)
            job_history.append(job_id)
            new_jobs += 1

    if new_jobs > 0:
        save_job_history(job_history)
        print(f"Found and sent {new_jobs} new job notifications.")
    else:
        print("No new jobs found.")

if __name__ == "__main__":
    main()
