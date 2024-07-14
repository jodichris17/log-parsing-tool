# src/log_parser.py
import json

def parse_log(file_path):
    metrics = {
        'error_counts': 0,
        'total_response_time': 0,
        'total_transactions': 0,
        'entries': []
    }
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            timestamp, service_name, status_code, response_time, user_id, transaction_id, additional_info = parts[:7]
            status_code = int(status_code)
            response_time_ms = int(response_time.replace('ms', ''))
            
            # Calculate metrics
            if status_code >= 400:
                metrics['error_counts'] += 1
            metrics['total_response_time'] += response_time_ms
            metrics['total_transactions'] += 1
            
            metrics['entries'].append({
                'timestamp': timestamp,
                'service_name': service_name,
                'status_code': status_code,
                'response_time_ms': response_time_ms,
                'user_id': user_id,
                'transaction_id': transaction_id,
                'additional_info': ' '.join(parts[7:])
            })
    
    metrics['average_response_time'] = metrics['total_response_time'] / metrics['total_transactions']
    return metrics

def save_to_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
log_data = parse_log('sample.log')
save_to_json(log_data, 'parsed_logs.json')
