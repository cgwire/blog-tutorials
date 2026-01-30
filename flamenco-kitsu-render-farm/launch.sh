curl -X 'POST' \
  'http://172.17.0.1:8080/api/v3/jobs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "metadata": {
    "project": "kitsu",
    "user.email": "basunako@gmail.com",
    "user.name": "kitsu"
  },
  "name": "Kitsu Render",
  "priority": 50,
  "settings": {},
  "submitter_platform": "linux",
  "type": "kitsu-render"
}'
