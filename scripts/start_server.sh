#!/bin/bash
cd "$(dirname "$0")"
echo "シミュレータ起動中... http://localhost:8888/"
python3 -c "
import uvicorn, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath('.')))
from sim_server import app
uvicorn.run(app, host='0.0.0.0', port=8888, log_level='warning', loop='asyncio', http='h11')
"
