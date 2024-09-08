import redis
import json
import re



class SolicitudService:
    @staticmethod
    def get_all_solicitudes_queue():
        r = redis.Redis(host='localhost', port=6379, db=0)

        keys = r.keys('celery-task-meta-*')

        for key in keys:
            result_data = r.get(key)
            
            if result_data:
                result_data = result_data.decode('utf-8')
                result_json = json.loads(result_data)
                
                if result_json.get('status') == 'SUCCESS':
                    result = result_json.get('result', '')
                    
                    match = re.search(r':\s*(.*)', result)
                    if match:
                        result_after_colon = match.group(1)
                        print('Resultado después de los dos puntos:', result_after_colon)
                    else:
                        print('No se encontró el formato esperado en el resultado:', result)
