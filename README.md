# NPI-MSA-locator

# Project Setup

## Backend Setup

### Prerequisites
- Python installed
- `pip` installed

### Steps
1. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```
2. **Activate the virtual environment:**
   - **Windows:**
     ```sh
     Set-ExecutionPolicy Unrestricted -Scope Process  # (Optional)
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source venv/bin/activate
     ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the backend server:**
   ```sh
   uvicorn main:app --reload
   ```

---

## Frontend Setup

### Steps
1. **Navigate to the frontend directory:**
   ```sh
   cd fe
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the frontend application:**
   ```sh
   streamlit run fe.py
   ```

## Notes
- Ensure that both backend and frontend dependencies are installed before running the respective applications.
- If you face any permission issues on Windows, try running PowerShell as Administrator.
- The backend should be running before starting the frontend to ensure smooth communication between the services.

