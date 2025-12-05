"""
Tool to compress repository files to plugin zip.
Use by calling: 'python3 zip_plugin.py'
"""

import argparse
import os
import sys
import zipfile

PLUGIN_NAME = "QGIS_TopoToolbox.zip"
EXCLUDE_DIRS = ['.venv', '__pycache__', '.git', '.vscode', '.idea']
EXCLUDE_FILES = []
PLUGIN_ROOT_FOLDER = 'QGISTopoToolbox'

def should_exclude(path: str, base_dir: str, zip_filename: str) -> bool:
    """Checks if a path should be excluded from the zip.

    Parameters
    ----------
    path : str
        Path to be evaluated.
    base_dir : str
        Path to base directory.
    zip_filename : str
        Name of the zip file being created.

    Returns
    -------
    bool
        True if path should be excluded, else False.
    """
    rel_path = os.path.relpath(path, base_dir)

    if rel_path == zip_filename:
        return True

    for exclude in EXCLUDE_DIRS:
        if exclude in rel_path.split(os.sep):
            return True

    if os.path.basename(path) in EXCLUDE_FILES:
        return True

    return False


def get_user_confirmation(plugin_name: str) -> bool:
    """Get user confirmation to remove existing zip file.

    Parameters
    ----------
    plugin_name : str
        Name of the zip file to be removed.

    Returns
    -------
    bool
        True if user confirms removal, False otherwise.
    """
    while True:
        response = input(
            f"Zip file '{plugin_name}' already exists. Remove it? [y/N]\n"
                        ).strip().lower()
        if response in ['y', 'yes', '']:
            return True
        if response in ['n', 'no']:
            return False
        print("Please enter 'y'/'yes'/enter or 'n'/'no'")


def create_zip(plugin_name: str):
    """Creates a zip file of the plugin repository, excluding specified
    directories and files.

    Parameters
    ----------
    plugin_name : str
        Name of the output zip file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, plugin_name)

    # ask user how to handle existing zip file
    if os.path.exists(output_path):
        if get_user_confirmation(plugin_name):
            try:
                os.remove(output_path)
                print(f"Removed existing zip file: {output_path}")
            except Exception as e:
                print(f"Error removing existing zip file: {e}")
                sys.exit(1)
        else:
            print("Operation cancelled.")
            sys.exit(0)

    # create zip file
    try:
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(script_dir):
                dirs[:] = [d for d in dirs if not should_exclude(
                    os.path.join(root, d), script_dir, plugin_name)]

                for file in files:
                    file_path = os.path.join(root, file)

                    if should_exclude(file_path, script_dir, plugin_name):
                        continue

                    relative_path = os.path.relpath(file_path, script_dir)
                    zipf.write(file_path, os.path.join(PLUGIN_ROOT_FOLDER, relative_path))

        print(f"Plugin compressed as {output_path}")

    except Exception as e:
        print(f"Error creating zip file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zip QGIS TopoToolbox Plugin")
    parser.add_argument('-o', '--output', default=PLUGIN_NAME,
                        help="Output zip filename. Default is QGIS_TopoToolbox.zip")

    args = parser.parse_args()

    create_zip(args.output)
