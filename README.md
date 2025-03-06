# MSA-NPI Locator

A **Metropolitan Statistical Area - NPI Locator** that fetches NPI details using ZIP codes. This project utilizes the **NPI Registry API** to retrieve healthcare provider data efficiently.

---

## Features
- **Batch ZIP Code Processing** for large-scale provider searches.
- **Real-time API Requests** to fetch NPI data.
- **CSV & JSON Export** for structured storage and further analysis.
- **GeoAPI integration** for visualizing provider locations on a map.

---

## 🛠 Tools Used

| Tool          | Description |
|--------------|------------|
| **Python**   | Core programming language for implementation |
| **Pandas**   | Data processing and storage |
| **FastAPI**  | Backend framework for handling API requests |
| **Streamlit** | Frontend for user interface and visualization |
| **GeoAPI**   | Geolocation API for mapping provider addresses |
| **CSV & JSON** | Output formats for easy analysis |

---

## ⚙️ API Setup & Usage

### **API Endpoint:**
The project uses the **NPI Registry API v2.1**:
```plaintext
https://npiregistry.cms.hhs.gov/api/?version=2.1&postal_code=ZIP_CODE
```

---

## 🛠 Setup & Installation

### **Clone the Repository**
```sh
git clone https://github.com/your-username/MSA-NPI-Locator.git
```

### **Install Dependencies**
```sh
pip install requests pandas
```

### **Run the Script**
```sh
python msa_npi_locator.py
```

---

## Backend Setup

### **Prerequisites**
- Python installed
- `pip` installed

### **Steps**
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

### **Steps**
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

---

## Notes
- Ensure that both backend and frontend dependencies are installed before running the respective applications.
- If you face any permission issues on Windows, try running PowerShell as Administrator.
- The backend should be running before starting the frontend to ensure smooth communication between the services.

