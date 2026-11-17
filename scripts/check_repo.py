#!/usr/bin/env python3
"""Public package check; not a complete secret scanner or a live infrastructure test."""
from pathlib import Path
from urllib.parse import unquote
import hashlib, json, re, struct, sys
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and '__pycache__' not in p.parts]
forbidden_ext = {'.docx','.zip','.tar','.tgz','.vmdk','.qcow2','.vdi','.vhd','.vhdx','.ova','.ovf','.iso','.log','.pcap','.pcapng','.pem','.key','.p12','.pfx'}
forbidden_names = {'client.keys','local.yml','wazuh-passwords.txt','archives.json','alerts.json','.env','.DS_Store','ossec.conf','__MACOSX'}
patterns = {
 'home directory': r'/(?:Users|home)/[A-Za-z0-9._-]+/',
 'MAC address': r'(?i)(?<![a-f0-9])(?:[a-f0-9]{2}:){5}[a-f0-9]{2}(?![a-f0-9])',
 'MAC-derived interface': r'\benx[a-fA-F0-9]{12}\b',
 'GitHub token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b',
 'AWS access key': r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
 'private key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
 'live hook identifier': r'/api/v1/hooks/(?!REPLACE_WITH_PRIVATE_ID|<|\[|\{|HOOK_ID\b)[A-Za-z0-9_-]{12,}',
 'JWT-like token': r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b',
 'credential assignment': r'''(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token|secret)\s*[:=]\s*["']?(?!REPLACE|YOUR_|PRIVATE|EXAMPLE|PLACEHOLDER)[A-Za-z0-9+/=_-]{16,}''',
 'email address': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
}
text_ext = {'.md','.txt','.xml','.json','.svg','.ps1','.sh','.example','.yml','.yaml','.py'}
for p in files:
 rel=p.relative_to(ROOT).as_posix()
 if p.suffix.lower() in forbidden_ext or p.name in forbidden_names or (p.name.startswith('.env.') and p.name != '.env.example'):
  errors.append(f'{rel}: forbidden file type/name')
 if p.suffix.lower() in text_ext or p.name=='.gitignore':
  s=p.read_text()
  # Pattern definitions themselves are code, not source credentials.
  if rel!='scripts/check_repo.py':
   for label, pattern in patterns.items():
    for m in re.finditer(pattern,s): errors.append(f'{rel}:{s[:m.start()].count(chr(10))+1}: possible {label} (value withheld)')
   for m in re.finditer(r'(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])',s):
    ip=m.group()
    if ip not in {'127.0.0.1','0.0.0.0'} and all(int(n)<=255 for n in ip.split('.')):
     errors.append(f'{rel}:{s[:m.start()].count(chr(10))+1}: concrete IPv4 address (value withheld)')
 if p.suffix=='.md':
  s=re.sub(r'```[^\n]*\n.*?```','',p.read_text(),flags=re.S)
  for target in re.findall(r'!?\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)',s):
   if target.startswith(('https:','http:','mailto:','#')): continue
   link=unquote(target.split('#')[0].strip('<>'))
   if not link: continue
   dest=(p.parent/link).resolve()
   if not dest.is_relative_to(ROOT) or not dest.exists(): errors.append(f'{rel}: broken/outside relative link: {link}')
 if p.suffix=='.json':
  try: json.loads(p.read_text())
  except ValueError as exc: errors.append(f'{rel}: invalid JSON: {exc}')
 if p.suffix in {'.xml','.svg'}:
  try: ET.parse(p)
  except ET.ParseError as exc: errors.append(f'{rel}: invalid XML: {exc}')
manifest=json.loads((ROOT/'docs/reviewed-images.json').read_text())
reviewed={e['path']:e['sha256'] for e in manifest['images']}
for p in files:
 if p.suffix.lower() not in {'.png','.jpg','.jpeg','.webp','.gif'}: continue
 rel=p.relative_to(ROOT).as_posix()
 if hashlib.sha256(p.read_bytes()).hexdigest()!=reviewed.get(rel): errors.append(f'{rel}: image unreviewed or changed')
 if p.suffix.lower()=='.png':
  data=p.read_bytes(); offset=8
  while offset+12<=len(data):
   length=struct.unpack('>I',data[offset:offset+4])[0]; kind=data[offset+4:offset+8]
   if kind in {b'tEXt',b'zTXt',b'iTXt',b'eXIf'}: errors.append(f'{rel}: embedded image metadata requires review/removal')
   offset+=12+length
for rel in reviewed:
 if not (ROOT/rel).is_file(): errors.append(f'{rel}: reviewed image missing')
ids={}
for p in ROOT.glob('labs/**/*.xml'):
 for rule in ET.parse(p).getroot().iter('rule'):
  rid=rule.attrib.get('id')
  if rid in ids: errors.append(f'duplicate custom rule ID {rid}')
  ids[rid]=str(p.relative_to(ROOT))
if errors:
 print('CHECK FAILED\n'+'\n'.join(errors));sys.exit(1)
print(f'PASS: {len(files)} files; local links and XML/JSON valid; {len(reviewed)} reviewed images unchanged; {len(ids)} unique custom rules; no configured sensitive-text patterns found.')
print('Scope: local package only. Manual privacy review and existing Git-history checks remain necessary.')
