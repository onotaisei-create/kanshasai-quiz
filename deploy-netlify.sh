#!/bin/bash
# Netlify本番デプロイ。トークンは保存しないので実行時に渡す：
#   NETLIFY_AUTH_TOKEN=nfp_xxx ./deploy-netlify.sh
set -e
python3 build.py
mkdir -p dist && cp index.html dist/index.html
npx --yes netlify-cli@latest deploy --prod --dir=dist --site=edd204d5-6735-4935-a761-9e7c8f6161cf
