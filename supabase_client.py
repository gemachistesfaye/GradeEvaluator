import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from a .env file if present (useful for local development)
load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY') or os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError('Supabase credentials missing: set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_KEY) in the environment')

# Initialise a single Supabase client instance for the whole application
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
