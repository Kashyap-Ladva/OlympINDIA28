# run_pipeline.py
import subprocess

notebooks = [
    "notebooks/01_data_loading_and_validation.ipynb",
    "notebooks/02_clean_tokyo_2020_noc.ipynb",
    "notebooks/03_paris_dataset.ipynb",
    "notebooks/04_adding_2020_2024.ipynb",
    "notebooks/World_summer_master.ipynb",
    "notebooks/W1_world_master_from_events.ipynb",
    "notebooks/India_Olympic_Deep_Analysis.ipynb",
    "notebooks/W3_world_weighted_medal_model.ipynb",
    "notebooks/W4_Sports_Intelligence.ipynb",
    "notebooks/W5_global_comparative_intelligence.ipynb",
]

for nb in notebooks:
    print(f"Running: {nb}")
    subprocess.run([
        "jupyter", "nbconvert", "--to", "notebook",
        "--execute", nb, "--inplace"
    ], check=True)
    print(f"✅ Done: {nb}")

print("\n🏁 Full pipeline complete.")