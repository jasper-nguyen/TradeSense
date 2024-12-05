# TradeSense AI-Enhanced Cryptocurrency Trading

## Project Structure

```
Cmpe195a/
├── backend/            # Backend scripts and data processing
|   ├──Inference/
│   	├── retrieveData.py    # Fetches raw cryptocurrency data from APIs
│   	├── sanitizeData.py    # Cleans and prepares the data for machine learning
│   	├── exampleRequest.py  # Example API request script
│   	├── trainModel.py  # create training model from DF data
│   	├── inference.py  # class for inference algorithm
│   	├── Datasets/
│   		├── decreasedCSV/      # Folder for CSV files with reduced data
│   		├── decreasedDF/       # Folder for DataFrame outputs
│   		├── decreasedForest/   # Folder for trained output of decreased data
│   		├── increasedCSV/      # Folder for CSV files with reduced data
│   		├── increasedDF/       # Folder for DataFrame outputs
│   		├── increasedForest/   # Folder for trained output of increased data
│
├── tradesense-next/              # Frontend for TradeSense
|   ├──frontend/
│       ├── public/            # Public assets (e.g., index.html, favicon)
│       ├── src/app/               # Source files
│           ├── api/           # API calls to communicate with backend
│           ├── components/    # Reusable React components (e.g., Navbar, Footer)
│           ├── pages/         # Pages like Home, Dashboard, Login, along with CSS files
│           ├── assets/        # Images, fonts, and other static files
│       ├── package.json       # Frontend dependencies and scripts
│
├── README.md              # This file
```

## Frontend

The frontend is located in the `frontend/` directory. It is a React application created with a React App and components.

### Available Scripts

In the `frontend/` directory, you can run:

- `npm run dev`: Runs the app in development mode.
- `npm run build`: Builds the app for production.
- `npm run eject`: Ejects the configuration files.

## Backend

The backend consists of Python scripts for data retrieval and sanitization.

- `exampleRequest.py`: Handles example requests.
- `retreiveData.py`: Retrieves cryptocurrency data.
- `sanitizeData.py`: Cleans the CSV files.

## Setup Instructions

### Prerequisites

- Node.js and npm (for the frontend)
- Python 3.x and pip (for the backend)
- Git

### Clone the Repository

#### Setting Up the FrontEnd

	git clone https://github.com/yourusername/Cmpe195a.git

	cd frontend

	npm install

	npm run dev

#### Setting Up the Backend
	
	python -m venv venv

(For Windows):
 
 	venv\Scripts\activate

(For mac/Linux):

 	source venv/bin/activate

 Make sure to have all requirements ready:

	pip install -r requirements.txt

	python retreiveData.py

	python sanitizeData.py

### How to Use the CodeBase

#### Frontend

##### Adding Components or Pages:
- Add new reusable UI components in `src/components`.
- Add new pages in `src/pages/(pageID)` along with the corresponding css files.

##### API Calls:
- Add API interaction logic in `src/api/apiClient.js`.
- Use `apiClient` to interact with backend routes.


#### Backend

##### Data Processing:
- Use `retrieveData.py` to collect data from APIs.
- Use `sanitizeData.py` to preprocess the data.

##### API Endpoints:
- Define your API endpoints (e.g., Flask or FastAPI routes) to connect to the FrontEnd.


### Contributions 

1. Create a new branch

		git branch new-feature-branch

		git checkout new-feature-branch

2. Commit changes

		git commit -m 'Added some feature'

3. Push to the repo

4. Open a pull request to be reviewed for conflicts, merge to the main branch. 
