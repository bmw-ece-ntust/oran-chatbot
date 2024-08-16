from vectorstore.vectorstore_updater_no_streamlit import create_vectorstore, update_vectorstore
from bot_config.utils import get_config
import os
cfg_name = "multimodal_oran"
config = get_config(os.path.join("bot_config", cfg_name+".config"))
print("opening files...\n")
BASE_DIR = os.path.abspath("vectorstore")
CORE_DIR = os.path.join(BASE_DIR, config["core_docs_directory_name"])
if not os.path.exists(CORE_DIR):
    os.mkdir(CORE_DIR)
    
DOCS_DIR = CORE_DIR

print("Updating Vector DB!\n")
update_vectorstore(DOCS_DIR, config["name"])