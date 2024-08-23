import os
import importlib.util
import pytest


def test_submission_files_exist(developer):
    base_path = f"submissions/developer_{developer}"
    folders = ["tests", "results"]

    for folder in folders:
        assert os.path.exists(
            os.path.join(base_path, folder)
        ), f"{folder.capitalize()} directory does not exist"

        files = os.listdir(os.path.join(base_path, folder))
        assert len(files) > 0, f"No {folder} files found"
