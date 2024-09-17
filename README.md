1. **Configure environment variables**:  
   Copy the `.env.sample` file and create a new `.env` file. Update it with your own values.

2. **Create a virtual environment**:  
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:  
   - On Windows:
     ```bashw
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize vectorstore (first-time setup)**:  
   If you're running the project for the first time, initialize the vectorstore:
   ```bash
   python initvs.py
   ```

6. **Run the backend**:  
   ```bash
   uvicorn main:app --reload
   ```