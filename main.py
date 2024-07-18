import sys
import os

# Add current directory to Python path
current_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_path)
print("Current Path:", current_path)
print("Python Path:", sys.path)

# Print directory contents for debugging
print("Directory Contents:", os.listdir(current_path))

app_path = os.path.join(current_path, 'app')
print("App Directory Contents:", os.listdir(app_path))

try:
    from app import create_app
    print("Module 'app' imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing module: {e}")

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
