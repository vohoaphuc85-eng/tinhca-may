# Chép tệp từ một đường dẫn công khai (vd cdn.ai33.pro) lên kho media R2 tinhca-media.
#   python3 tools/chuyen_tep.py "<url> <khóa-R2>" ["<url> <khóa-R2>" ...]
import os, sys, urllib.request, boto3
c = boto3.client('s3', endpoint_url=f"https://{os.environ['R2_ACCOUNT_ID']}.r2.cloudflarestorage.com",
                 aws_access_key_id=os.environ['R2_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['R2_SECRET_ACCESS_KEY'], region_name='auto')
for cap in ' '.join(sys.argv[1:]).split(';'):
    cap = cap.split()
    if len(cap) != 2: continue
    url, key = cap
    assert url.startswith('https://cdn.ai33.pro/'), url
    data = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'tinhca-may'}), timeout=120).read()
    c.put_object(Bucket='tinhca-media', Key=key, Body=data, ContentType='audio/mpeg', CacheControl='public, max-age=86400')
    print('ok', key, len(data))
