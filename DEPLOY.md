# How to Deploy to the Cloud (Free)

To run this app off your laptop (on a server), follow these steps to use **Render** (a free cloud host).

## Prerequisites (I have done these for you)
1.  **Code Prepared**: I created `requirements.txt` and `Procfile`.
2.  **Git Initialized**: I initialized the git repository and committed your code.

## Step 1: Push to GitHub
1.  Log in to [GitHub.com](https://github.com).
2.  Click **+** (top right) -> **New repository**.
3.  Name it `idea-simulator` and click **Create repository**.
4.  Copy the commands under "…or push an existing repository from the command line".
5.  Paste them in your **Terminal** locally. They will look like this:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/idea-simulator.git
    git branch -M main
    git push -u origin main
    ```
    > **⚠️ IMPACT:** If it says "Password authentication is not supported", you **CANNOT** use your password. You must use a **Token**.
    > 1. Go to [GitHub Tokens](https://github.com/settings/tokens/new) (Settings -> Developer Settings -> Personal access tokens -> Tokens (classic)).
    > 2. Generate new token (classic).
    > 3. Give it a name, select **No Expiration**, and check the **repo** box.
    > 4. Click **Generate token**.
    > 5. **COPY** that long code starting with `ghp_`.
    > 6. Run the push command again.
    > 7. Username: `Atomz117`
    > 8. Password: **Paste the Token** (it won't show on screen).

## Step 2: Deploy on Render
1.  Go to [Render.com](https://render.com) and sign up (you can use your GitHub account).
2.  Click **New +** -> **Web Service**.
3.  Select **Build and deploy from a Git repository**.
4.  Connect your `idea-simulator` repo.
5.  In the settings:
    - **Name**: `idea-simulator`
    - **Region**: Any
    - **Branch**: `main`
    - **Runtime**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app` (Render might auto-detect this from the Procfile I made).
6.  Click **Create Web Service**.

## Step 3: Get Your Link
- Render will deploy the app (takes ~2 minutes).
- Once done, it will give you a link like `https://idea-simulator-xyz.onrender.com`.
- **Share this link!** It works 24/7 without your laptop.
