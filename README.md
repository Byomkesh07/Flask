# Flask

Creating and using a virtual environment in VSCode for a Python project is a good practice to manage dependencies. Here are the steps to create and activate a virtual environment in the VSCode terminal:

Step 1: Open VSCode and Your Project
Open VSCode.
Open your project folder.
Step 2: Open the Terminal in VSCode
Step 3: Create a Virtual Environment
In the terminal, navigate to your project directory if you aren't already there.

Run the following command to create a virtual environment:

python -m venv myenv

This will create a virtual environment named venv in your project directory.

Step 4: Activate the Virtual Environment
On Windows:

.\myenv\Scripts\activate

Step 5: Install Dependencies
With the virtual environment activated, install your project dependencies:

pip install -r requirements.txt
