import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import sys

# from logger import logger

# Path to the folder containing the Python scripts
scripts_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "dragon_data_scripts")


def get_python_scripts(folder):
    """Return a list of all .py files in the given folder."""
    return [file for file in os.listdir(folder) if file.endswith(".py")]

def run_python_script(script):
    """ run a single python script """
    script_path = os.path.join(scripts_folder, script)

    try:
        # subprocess.run(["python", script_path], check=True)
        python_executable = sys.executable
        subprocess.run([python_executable, script_path], check=True, capture_output=True, text=True)
        print(f"Completed: {script_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_path}: {e}")
        print(f"Error output: {e.stderr}")
    except FileNotFoundError:
        print(f"Script not found: {script_path}")


def run_scripts_in_folder(folder):
    """Run all data creation Python scripts in the specified folder."""
    # logger.info('Creating data...')
    scripts = get_python_scripts(folder)
    max_workers = 4

    if not scripts:
        print(f"No Python scripts found in {folder}")
        return

    try:# Execute the script and wait for it to complete
        with ThreadPoolExecutor(max_workers=max_workers) as executor:  # runs scripts in parallel
            executor.map(run_python_script, scripts)
    except Exception as e:
        print(e)

    # logger.info('Data creation complete.')


def run_python_script_in_one_process(folder):
    # logger.info('Creating data...')
    scripts = get_python_scripts(folder)

    for script in scripts:
        script_path = os.path.join(scripts_folder, script)

        try:
            # Import the script as a module
            spec = importlib.util.spec_from_file_location("module.name", script_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules["module.name"] = module
            spec.loader.exec_module(module)
            print(f"Completed: {script_path}")
        except Exception as e:
            print(f"Error while running {script_path}: {e}")


# Run the utility
run_scripts_in_folder(scripts_folder)
# run_python_script_in_one_process(scripts_folder)

