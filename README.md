# bq_agent_app

This is a sample application for managing BigQuery operations using an agent.

## Reference

This agent is inspired by the concepts outlined in Google Cloud's documentation on building AI agents. You can find more information [here](https://cloud.google.com/vertex-ai/docs/generative-ai/mlops/build-deploy-agents) (Note: This is a placeholder URL. Please replace with the actual reference if available).

## Setup Steps

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:anirbankonar/bq_agent_app.git
    cd bq_agent_app
    ```

2.  **Set up your Python environment:**
    It is recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    You will need to install the necessary Python packages. Make sure you have a `requirements.txt` file (if not, create one with `google-cloud-bigquery` and `google-api-python-client`).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Google Cloud authentication:**
    Ensure your Google Cloud credentials are set up. This typically involves:
    *   Having a Google Cloud project with BigQuery API enabled.
    *   Authenticating using `gcloud auth application-default login` or by setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to a service account key file.

5.  **Run the agent:**
    Execute the agent script.
    ```bash
    python agent.py
    ```

## Usage

(Further instructions on how to interact with the agent will go here)
