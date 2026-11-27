#!/usr/bin/env python3
"""Replace every local media reference with an actual public HTTPS URL."""
import argparse,json,re,html
from pathlib import Path
from urllib.parse import urlparse
p=argparse.ArgumentParser();p.add_argument('--base-url',help='Public HTTPS directory containing the uploaded assets');p.add_argument('--map',type=Path,help='JSON mapping assets/filename to a public HTTPS URL');a=p.parse_args()
root=Path(__file__).resolve().parent;s=(root/'newsletter.html').read_text();refs=set(re.findall(r'assets/[\w.-]+',s));mapping=json.loads(a.map.read_text()) if a.map else {}
if not a.base_url and not a.map:p.error('Provide --base-url or --map after uploading the assets.')
for ref in sorted(refs):
 u=mapping.get(ref) or ((a.base_url.rstrip('/')+'/'+ref.split('/')[-1]) if a.base_url else '')
 if urlparse(u).scheme!='https' or not urlparse(u).netloc:p.error('Missing public HTTPS URL for '+ref)
 s=s.replace(ref,html.escape(u,quote=True))
(root/'newsletter-clevertap.html').write_text(s);print('Created newsletter-clevertap.html. Send a test email before launching.')
