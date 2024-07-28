import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get('PORT') or 5000

if __name__ == "__main__":
    from app import create_app

    app = create_app()
    app.run(port=PORT, debug=True)
