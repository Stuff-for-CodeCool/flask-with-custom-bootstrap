# Flask with custom Bootstrap

This base project creates a simple Flask site, with a custom build of Bootstrap for the layout.

Requires Python and NPM to be installed.

Also contains required files for Heroku deployment. Make sure to comment line 31 in `app/database.py` and uncomment line 32 in same file.

## Setting up

1. Clone this repo
2. Create a virtual environment and activate it:
    ```bash
    python -m virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements
    ```
3. Install node dependencies:
    ```bash
    npm install
    ```
4. Set up any needed SCSS variables in `scss/_variables.scss`
5. Uncomment any needed Bootstrap components in `scss/_bootstrap.scss`
6. Extend any need Bootstrap classes in `scss/style.scss`
7. Build the CSS:
    ```bash
    npm run build
    ```
8. Rename `.env.template` to `.env` and fill in the required values
9.  Run everything:
    ```bash
    npm run start
    ```