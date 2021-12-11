
import os,requests,time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_tracker.settings')

import django
django.setup()
from core.models import user_entry

if __name__ == '__main__':
    while(True):
        time.sleep(10)
        to_delete = []
        for entry in user_entry.objects.all():
            try: 
                resp = requests.get(f'http://{entry.ip}:{entry.port}/alive?filename={entry.file_id}', timeout=2).json()
                if resp['status'] != 'open':
                    to_delete.append(entry.id)
            except requests.exceptions.Timeout as e: 
                to_delete.append(entry.id)
        print("to delete: ", to_delete)
        for i in to_delete:
            entry = user_entry.objects.get(id=i)
            entry.delete()
