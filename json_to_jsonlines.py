import jsonlines
import json

with open('source_dataset\data.json', 'r',encoding='utf-8') as f:
    json_data = json.load(f,strict=False)

# json_data=json.dumps(json_data,ensure_ascii=False)
 
with jsonlines.open('dataset\data.jsonl', 'w') as writer:
    writer.write_all(json_data)

