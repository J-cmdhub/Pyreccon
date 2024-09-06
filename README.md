## Setting up the Project

### Step 1: Create a `.env` file
You need to create a `.env` file to store API keys and other sensitive information.

1. Copy the `.env.example` file and rename it to `.env`:

    ```bash
    cp .env.example .env
    ```

2. Open the `.env` file and replace the placeholder values with your actual API keys and configuration options:

    ```plaintext
    WHOIS_API_KEY=your-actual-whois-api-key
    IPINFO_API_KEY=your-actual-ipinfo-api-key
    NMAP_OPTION=your-nmap-option
    ```

### Step 2: Install dependencies and run the project
After setting up the `.env` file, you can install the required dependencies and run the project.
